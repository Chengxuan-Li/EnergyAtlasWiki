# EnergyAtlasWeb Job (Single-Click, No GUI)

A **GUI-less job** is a pre-configured background task that the user triggers with a single click.
It has **no input form** — parameters are hard-coded in the factory or read from server-side configuration.
The only user-facing surface is a Start button, a real-time log stream, and (optionally) a completion status.


## Architecture overview

```
┌──────────────┐   POST /api/jobList/{name}/start   ┌─────────────────────┐
│   Frontend   │ ──────────────────────────────────► │ JobRouterController  │
│  (one-click) │                                     │  → IJobFactory       │
│              │ ◄── SignalR (jobEvent) ────────────  │  → IControllerJob    │
└──────────────┘                                     └─────────────────────┘
```

1. **Frontend** shows a list of registered jobs (from `GET /api/jobList`).
2. User clicks **Start** — `POST /api/jobList/{jobName}/start`.
3. The controller resolves the factory, creates the job, runs it on a background thread.
4. Progress is streamed to the client via **SignalR** (`JobHub`).


## Key interfaces

### `IJobFactory`

> `EnergyAtlasWeb/Jobs/Abstractions/IJobFactory.cs`

```csharp
public interface IJobFactory
{
    string JobName { get; }
    string JobDescription { get; }
    IControllerJob Create(ILogger logger, IJobReporter reporter);
}
```

The factory is a **singleton** registered in DI. It provides a name/description for the job list and
creates a fresh `IControllerJob` instance for each run.

### `IControllerJob`

> `EnergyAtlasWeb/Jobs/Abstractions/IControllerJob.cs`

```csharp
public interface IControllerJob
{
    void Run();
}
```

No inputs, no outputs. The job does its work and reports progress via the `IJobReporter` it
received at construction time.


## Factory registration

Factories are registered as **singletons** in `Program.cs`:

```csharp
builder.Services.AddSingleton<IJobFactory, TiledVoxelShadingJobFactory>();
builder.Services.AddSingleton<IJobFactory, TiledLidarVoxelizationJobFactory>();
builder.Services.AddSingleton<IJobFactory, TqdmStressTestJobFactory>();
builder.Services.AddSingleton<JobRegistry>();   // collects all IJobFactory
```

`JobRegistry` receives `IEnumerable<IJobFactory>` via constructor injection and builds a
lookup dictionary keyed by `JobName`.

### Adding a new one-click job

1. Create a class that implements `IJobFactory`.
2. In `Create(...)`, return a new instance of your job (implementing `IControllerJob`).
3. Register it in `Program.cs`: `builder.Services.AddSingleton<IJobFactory, MyJobFactory>();`.
4. It automatically appears in the job list.


## Minimal code template

```csharp
// ─── Factory ────────────────────────────────
public class MyJobFactory : IJobFactory
{
    public string JobName => "MyJob";
    public string JobDescription => "Does something useful with one click.";

    public IControllerJob Create(ILogger logger, IJobReporter reporter)
        => new MyJob(logger, reporter);
}

// ─── Job ────────────────────────────────────
public class MyJob : IControllerJob
{
    private readonly ILogger _log;
    private readonly IJobReporter _reporter;

    public MyJob(ILogger log, IJobReporter reporter)
    {
        _log = log;
        _reporter = reporter;
    }

    public void Run()
    {
        _reporter.Report(JobSignal.Start(message: "MyJob starting"));

        using (var bp = new BinaryProgress(_reporter, label: "Loading data"))
        {
            // ... work ...
        }

        using (var tq = new TQDM(_reporter, total: 100, label: "Processing items"))
        {
            for (int i = 0; i < 100; i++)
            {
                // ... work per item ...
                tq.Increment();
            }
        }

        _reporter.Report(JobSignal.Log(message: "All done."));
    }
}
```

> See [SignalR Logging](report-logs.md) for the full reference on `BinaryProgress`, `TQDM`,
> `JobSignal`, and how each log type renders in the frontend.


## Execution flow (controller side)

`JobRouterController.StartJob` (`POST /api/jobList/{jobName}/start`):

1. Resolve factory from `JobRegistry`.
2. Generate a `jobId` (GUID).
3. Create `JobRuntimeState` via `JobStore.Create(jobId, jobName)`.
4. Spawn `Task.Run`:
   - Create `SignalRJobReporter(_hub, jobId)`.
   - Call `factory.Create(logger, reporter)` → `IControllerJob`.
   - Call `job.Run()`.
   - On success: `JobStore.Complete(jobId)`.
   - On failure: `JobStore.Fail(jobId, ex.Message)`.
5. Return `{ success: true, jobId }` immediately.

The frontend connects to SignalR (`JoinJob(jobId)`) and renders signals in real time.


## When to use this vs a GUI job

| Criterion | GUI-less job | GUI job |
|-----------|-------------|---------|
| User-provided parameters | None (or server config) | Yes — typed input form |
| Output artefacts | None (results are side effects) | Yes — text, charts, files |
| Use case | Batch processing, cron-like tasks, infrastructure | Analysis, reports, interactive tools |

If the job needs **any** user input or produces **downloadable output**, use a
[GUI Job](gui-job.md) instead.


## See also

- [GUI Job](gui-job.md) — auto-generated job pages with inputs and outputs
- [SignalR Logging](report-logs.md) — reporter, signal types, progress bars
- [Working with Local Files](file-sys-access.md) — file picking, artifact sink, execution mode differences
- [Execution Modes](exec-modes.md) — browser vs local mode
