# Working with Local Files

This page covers how file picking, file upload, and output artefacts work across
execution modes. For the modes themselves, see [Execution Modes](exec-modes.md).


## 1. File input: how files reach the job

A GUI job declares file inputs with `[JobInput]` and a file-related `InputFieldType`:

| InputFieldType | Description |
|---------------|-------------|
| `LocalFile` | Single file picker |
| `LocalFiles` | Multi-file picker (or folder scan) |
| `FolderPath` | Directory picker (path only) |
| `DataHubFile` | Single file from DataHub catalog |
| `DataHubFiles` | Multiple files from DataHub catalog |

The **execution mode** determines how the user selects files and how those files reach the
server. See [Execution Modes](exec-modes.md) for how the mode is configured.

### Browser mode (`executionMode = "browser"`)

```
User clicks <input type="file">
    → File blob stored in JS (fileInputs)
    → On Run: POST /api/guiJob/upload (multipart/form-data)
    → Server saves to {TempPath}/guijob/{guid}/{filename}
    → Server returns { originalName, tempPath }
    → Frontend substitutes tempPath into the input JSON payload
    → Job receives the server-side temp path in TInput
```

- The `<input type="file">` HTML element is used.
- Files are uploaded **before** the job starts.
- The job sees a **server-local temp path** (e.g. `C:\Users\...\AppData\Local\Temp\guijob\abc\data.csv`).
- Allowed extensions are validated server-side during upload.

### Local mode (`executionMode = "local"`, MAUI)

```
User clicks [File...] button
    → window.MauiFilePicker.pickFile({ extensions: ".csv" })
    → Native OS file dialog opens
    → Absolute path returned to JS (e.g. "C:\Data\input.csv")
    → Path stored directly in inputValues
    → On Run: path sent in JSON payload (no upload)
    → Job receives the native absolute path in TInput
```

- The **MAUI file picker bridge** is used (`window.MauiFilePicker`).
- No upload step — the path is sent directly.
- The job sees a **user-selected native path** (e.g. `C:\Data\input.csv`).
- Multi-file inputs also support a **Folder...** button that calls `pickFolder()`
  (returns all matching files inside the chosen directory).

### MAUI bridge contract

When `executionMode === "local"`, the frontend installs (or expects) `window.MauiFilePicker`
with the following async methods:

| Method | Returns | Description |
|--------|---------|-------------|
| `pickFile({ extensions })` | `string` or `null` | Single file absolute path |
| `pickFiles({ extensions })` | `string[]` or `null` | Multiple file absolute paths |
| `pickFolder({ extensions })` | `string[]` or `null` | Files matching extensions in chosen folder |
| `pickDirectory()` | `string` or `null` | Directory absolute path |

The bridge communicates via `maui://` URL navigation: the frontend navigates to
`maui://{operation}?id={callbackId}&ext={extensions}`, the native MAUI side intercepts the
navigation, runs the native dialog, and calls back via
`window.__mauiResolve(id, result)` / `window.__mauiReject(id, error)`.


## 2. File output: on-disk vs download artefacts

A GUI job produces file outputs via `OutputFileReference` properties in `TOutput`
(with `[JobOutput]` attribute and `OutputFieldType.File`).

There are **two kinds** of output file references:

### On-disk (`IsOnDisk = true`)

The file physically exists on disk. The frontend shows a **folder icon** and a
**reveal-in-folder** link.

```csharp
// In Run():
var outDir = Path.Combine(Path.GetTempPath(), "guijob_output", Guid.NewGuid().ToString());
Directory.CreateDirectory(outDir);
var outPath = Path.Combine(outDir, "result.csv");
File.WriteAllText(outPath, csvContent);

// In TOutput:
new OutputFileReference
{
    DisplayName = "result.csv",
    Reference   = outPath,        // absolute path to the file
    IsOnDisk    = true
}
```

When the user clicks, the frontend calls `POST /api/guiJob/revealInFolder?path={path}`.
The server opens the containing folder in the system file explorer
(`explorer /select,"path"` on Windows, `open -R "path"` on macOS).

**Path safety:** The server validates the path against allowed roots
(`{TempPath}/guijob/` and `{TempPath}/guijob_output/`). In local mode, any rooted path
is accepted (the user chose it).

### Download (`IsOnDisk = false`)

The file **does not exist on disk**. The job generates bytes in memory and registers them
in the **artifact sink**. The frontend shows a **download icon** and a download link.

```csharp
// In Run():
var reportBytes = Encoding.UTF8.GetBytes(reportContent);
GUIJobRunContext.Current?.ArtifactSink?.Register(
    artifactKey:  "report",
    displayName:  "analysis_report.txt",
    contentType:  "text/plain",
    data:         reportBytes
);

// In TOutput:
new OutputFileReference
{
    DisplayName  = "analysis_report.txt",
    ArtifactKey  = "report",
    ContentType  = "text/plain",
    IsOnDisk     = false
}
```

When the user clicks, the browser navigates to
`GET /api/guiJob/{jobId}/download/{artifactKey}`, which streams the in-memory blob
with the correct content type and display name. **No file is ever written to disk.**


## 3. Artifact sink design

The artifact sink is the mechanism that lets jobs register download blobs during execution
without touching the file system.

### Components

| Component | File | Role |
|-----------|------|------|
| `IArtifactSink` | `Runtime/ArtifactSink.cs` | Interface: `Register(key, displayName, contentType, bytes)` |
| `ArtifactCollector` | `Runtime/ArtifactSink.cs` | Implementation: collects blobs in a dictionary |
| `ArtifactBlob` | `Runtime/ArtifactSink.cs` | Data class: `DisplayName`, `ContentType`, `byte[] Data` |
| `GUIJobRunContext` | `Runtime/GUIJobRunContext.cs` | Per-run context (AsyncLocal) holding `JobId` + `IArtifactSink` |
| `JobRuntimeState.Artifacts` | `Runtime/JobRuntimeState.cs` | `Dictionary<string, ArtifactBlob>` on the job state |

### Flow

```
Controller (before Execute)                Job (during Run)                  Controller (after Execute)
─────────────────────────                  ────────────────                  ──────────────────────────
1. Create ArtifactCollector                                                 
2. Set GUIJobRunContext.Current            3. GUIJobRunContext.Current       5. Copy collector.Artifacts
   = new(jobId, collector)                    ?.ArtifactSink                   → jobState.Artifacts
                                              ?.Register(key, name,         
                                                contentType, bytes)         6. Clear GUIJobRunContext.Current
                                           4. Return TOutput with           
                                              ArtifactKey set               
```

### Artifact lifetime

- Artifacts live in `JobRuntimeState.Artifacts` (in-memory, keyed by `jobId`).
- They persist as long as the `JobStore` entry exists (server process lifetime).
- The download API (`GET /api/guiJob/{jobId}/download/{artifactKey}`) looks them up and
  returns `File(blob.Data, blob.ContentType, blob.DisplayName)`.

### Usage in a job

```csharp
public TOutput Run(TInput input, IJobReporter reporter)
{
    var sink = GUIJobRunContext.Current?.ArtifactSink;

    var csvBytes = Encoding.UTF8.GetBytes("col1,col2\n1,2\n3,4\n");
    sink?.Register("csv-export", "export.csv", "text/csv", csvBytes);

    return new TOutput
    {
        ExportFile = new OutputFileReference
        {
            DisplayName = "export.csv",
            ArtifactKey = "csv-export",
            ContentType = "text/csv",
            IsOnDisk    = false
        }
    };
}
```


## 4. Summary: file access by execution mode

| Aspect | Browser mode | Local mode (MAUI) |
|--------|-------------|-------------------|
| **File picker UI** | `<input type="file">` | Native OS dialog via MauiFilePicker bridge |
| **How files reach server** | Uploaded via `POST /api/guiJob/upload` | Path sent directly in JSON |
| **What the job receives** | Server temp path | User's native absolute path |
| **On-disk outputs** | Reveal-in-folder (temp dir only) | Reveal-in-folder (any rooted path) |
| **Download outputs** | In-memory artifact → download link | Same (artifact sink is mode-agnostic) |
| **Folder picking** | Not available (browser limitation) | `pickFolder()` / `pickDirectory()` |


## See also

- [Execution Modes](exec-modes.md) — how execution modes are configured and detected
- [GUI Job](gui-job.md) — auto-generated job pages with inputs and outputs
- [SignalR Logging](report-logs.md) — reporter, signal types, progress bars
