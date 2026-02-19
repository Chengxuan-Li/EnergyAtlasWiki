# SignalR Logging

All jobs — both [GUI](gui-job.md) and [GUI-less](guiless-job.md) — report progress through
the `IJobReporter` interface. Signals are delivered to the frontend in real time via **SignalR**
and rendered in the log/progress area of the job page.


## IJobReporter

> `EnergyAtlasCore/Job/Job.cs`

```csharp
public interface IJobReporter
{
    void Report(JobSignal signal);
}
```

Every job receives an `IJobReporter` (either as a constructor argument for
[GUI-less jobs](guiless-job.md), or as the second parameter of
`Run(TInput input, IJobReporter reporter)` for [GUI jobs](gui-job.md)).

### Implementations

| Class | Use |
|-------|-----|
| `SignalRJobReporter` | Production: sends signals via SignalR hub in-order |
| `NullJobReporter` | Unit testing, silent execution, console app |


## JobSignal

> `EnergyAtlasCore/Job/Job.cs`

A `record` with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `Id` | `string` | Unique signal ID (auto-generated with GUID suffix) |
| `Type` | `JobSignalType` | Signal category (see below) |
| `Done` | `bool?` | For Binary signals: `false` = working, `true` = done |
| `Percent` | `double?` | For Progress signals: 0–100 |
| `Message` | `string?` | Human-readable text |

### Signal types (`JobSignalType`)

| Value | Name | Purpose |
|-------|------|---------|
| 0 | `Binary` | Working/done indicator (spinner) |
| 1 | `Progress` | Percentage-based progress bar |
| 2 | `Log` | Free-form text message |
| 3 | `Warning` | Warning message |
| 4 | `Exception` | Error message |

### Factory methods

| Method | Type | Notes |
|--------|------|-------|
| `JobSignal.Log(message)` | Log | General log line |
| `JobSignal.Start(message)` | Log | Prefixes message with "STARTING: " |
| `JobSignal.Complete(id)` | Log | Message = "JOB COMPLETED." |
| `JobSignal.Warning(message)` | Warning | Yellow warning |
| `JobSignal.Error(message)` | Exception | Red error |
| `JobSignal.Binary(id, message, done)` | Binary | **Internal** — use `BinaryProgress` instead |
| `JobSignal.Progress(id, percent, message)` | Progress | **Internal** — use `TQDM` instead |


## BinaryProgress (working/done spinner)

> `EnergyAtlasCore/Job/Job.cs`

A disposable wrapper that emits `Binary` signals. Shows a spinner while work is in progress,
then a "completed in Xs" message when done.

### Usage

```csharp
using (var bp = new BinaryProgress(reporter, label: "Loading dataset"))
{
    // ... synchronous work ...
}
// BinaryProgress.Dispose() calls Complete() automatically
```

### Behaviour

1. **Constructor**: Emits `Binary(id, label, done: false)` → frontend shows spinning indicator.
2. **Dispose / Complete()**: Emits `Binary(id, "label completed in Xs", done: true)` → spinner stops.

### Frontend rendering

```
Loading dataset |       ← spinning:  | / - \ (120ms cycle)
Loading dataset completed in 1.2s ✓  ← done: static text, "done" CSS class
```

The frontend maintains a `Map<id, div>` of binary lines. When `done === false`, the line
gets a spinning character appended. When `done === true`, the final message replaces it and
the spinner stops.


## TQDM (percentage progress bar)

> `EnergyAtlasCore/Job/Job.cs`

Named after Python's famous [tqdm](https://tqdm.github.io/) library. A disposable wrapper that emits `Progress` signals with percentage, elapsed time, and ETA.

> `tqdm` means "progress" in Arabic (taqadum, تقدّم) and is an abbreviation for "I love you so much" in Spanish (te quiero demasiado).

### Usage

```csharp
using (var tq = new TQDM(reporter, total: items.Count, label: "Processing items"))
{
    foreach (var item in items)
    {
        ProcessItem(item);
        tq.Increment();   // thread-safe
    }
}
// TQDM.Dispose() ensures progress reaches 100%
```

### Behaviour

1. **Constructor**: Emits `Binary(id, label, done: false)` (initial spinner) + `Progress(id, 0%, ...)`.
2. **Increment()**: Emits `Progress(id, percent, "label (done/total) | elapsed Xs | ETA Ys")`.
   - Thread-safe (uses `Interlocked`).
   - Throttled to avoid UI spam.
3. **Dispose**: Forces progress to 100%, then emits `Binary(id, "label completed in Xs", done: true)`.

### Frontend rendering

```
[########----------------------] 27.5% Processing items (275/1000) | elapsed 3.2s | ETA 8.4s
```

The frontend maintains a `Map<id, div>` of progress lines. Each `Progress` signal updates
the same line with an ASCII bar `[###---]`, percentage, and the message text.


## Log, Warning, Error

These are simple text signals rendered as lines in the log container.

### Usage

```csharp
reporter.Report(JobSignal.Log(message: "Loaded 1000 records from database."));
reporter.Report(JobSignal.Warning(message: "Column 'area' has 12 null values."));
reporter.Report(JobSignal.Error(message: "Fatal: input file is corrupt."));
reporter.Report(JobSignal.Start(message: "MyJob starting"));
reporter.Report(JobSignal.Complete());  // emits "JOB COMPLETED."
```

### Frontend rendering

| Type | CSS class | Prefix | Appearance |
|------|-----------|--------|------------|
| Log (type 2) | `log-line` | (none) | Normal text |
| Warning (type 3) | `log-line warning` | `[WARNING]` | Yellow/amber text |
| Exception (type 4) | `log-line error` | `[ERROR]` | Red text |

### Special log messages

- `"OUTPUT_JSON:{...}"` — Not displayed as a log line. Parsed by the frontend to render
  the output section (text, charts, artefacts).
- `"JOB COMPLETED."` — Updates the status badge to "Completed".


## SignalR delivery

### SignalRJobReporter

The production reporter sends signals through SignalR in **creation order**:

```csharp
public void Report(JobSignal signal)
{
    // Store in JobRuntimeState for replay
    if (JobStore.Jobs.TryGetValue(_jobId, out var job))
        job.Signals[signal.Id] = signal;

    // Chain sends to preserve order
    lock (_sendLock)
    {
        _sendChain = _sendChain.ContinueWith(async _ =>
        {
            await _hub.Clients.Group(_jobId).SendAsync("jobEvent", signal);
        }, TaskScheduler.Default).Unwrap();
    }
}
```

Key properties:
- **Ordered**: Signals are chained sequentially (even from parallel threads).
- **Stored**: All signals are persisted in `JobRuntimeState.Signals` for replay.
- **Resilient**: If a send fails, the signal is still in the store.

### JobHub (client connection)

When a client calls `JoinJob(jobId)`:
1. The client joins the SignalR group for that job.
2. All stored signals are **replayed** to the caller (so late-joining clients see full history).

### Frontend connection

```javascript
connection = new signalR.HubConnectionBuilder().withUrl("/jobHub").build();
connection.on("jobEvent", renderSignal);
await connection.start();
await connection.invoke("JoinJob", jobId);
```


## Recommended patterns

### Phase-based work with BinaryProgress

```csharp
using (var load = new BinaryProgress(reporter, label: "Loading data"))
{
    data = LoadData(input.FilePath);
}

using (var process = new BinaryProgress(reporter, label: "Processing"))
{
    result = Process(data);
}

using (var save = new BinaryProgress(reporter, label: "Saving output"))
{
    SaveResult(result, outputPath);
}
```

### Counted iteration with TQDM

```csharp
var items = GetWorkItems();
using (var tq = new TQDM(reporter, total: items.Count, label: "Analyzing buildings"))
{
    Parallel.ForEach(items, item =>
    {
        AnalyzeBuilding(item);
        tq.Increment();  // thread-safe
    });
}
```

### Mixed progress and logging

```csharp
reporter.Report(JobSignal.Start(message: "VoxelizationJob"));

using (var load = new BinaryProgress(reporter, label: "Loading LAS files"))
{
    tiles = LoadTiles(input.InputFiles);
}

reporter.Report(JobSignal.Log(message: $"Loaded {tiles.Count} tiles, {totalPoints:N0} points."));

using (var vox = new TQDM(reporter, total: tiles.Count, label: "Voxelizing tiles"))
{
    foreach (var tile in tiles)
    {
        VoxelizeTile(tile);
        vox.Increment();

        if (tile.HasWarnings)
            reporter.Report(JobSignal.Warning(message: $"Tile {tile.Name}: {tile.WarningText}"));
    }
}

reporter.Report(JobSignal.Log(message: "All tiles processed successfully."));
```


## Summary

| What to use | When | Type emitted |
|-------------|------|-------------|
| `BinaryProgress` | Wrap a phase of work (no item count) | Binary (0) |
| `TQDM` | Iterate over counted items | Progress (1) + Binary (0) |
| `JobSignal.Log(...)` | Informational text | Log (2) |
| `JobSignal.Warning(...)` | Non-fatal issue | Warning (3) |
| `JobSignal.Error(...)` | Fatal failure | Exception (4) |
| `JobSignal.Start(...)` | Job start announcement | Log (2) |
| `JobSignal.Complete()` | Job completion marker | Log (2) |


## See also

- [GUI Job](gui-job.md) — auto-generated job pages with inputs, outputs, and logging examples
- [GUI-less Job](guiless-job.md) — one-click jobs with logging examples
- [Working with Local Files](file-sys-access.md) — file picking and artifact sink
- [Execution Modes](exec-modes.md) — browser vs local mode
