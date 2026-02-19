# Execution Modes

The application supports two **execution modes** that control how the frontend interacts with
files and the host environment. The mode is set server-side and read by the frontend at startup.


## The two modes

| Mode | Value | Host | File strategy |
|------|-------|------|---------------|
| **Browser** | `"browser"` (default) | Standard web browser | Upload via API; temp paths |
| **Local** | `"local"` | MAUI desktop app (WebView) | Native file picker; direct paths |


## How the mode is set

### Server-side configuration

The mode is a standard ASP.NET configuration key: `"ExecutionMode"`.

**`appsettings.json`** (default):
```json
{
  "ExecutionMode": "browser"
}
```

**Launch profile** (`Properties/launchSettings.json`):
```json
{
  "profiles": {
    "maui": {
      "environmentVariables": {
        "ExecutionMode": "local"
      }
    }
  }
}
```

It can also be set via environment variable, command-line argument, or any other
`IConfiguration` source.

### The `/api/config` endpoint

The controller reads the value and exposes it to the frontend:

```csharp
[HttpGet("/api/config")]
public IActionResult GetConfig()
{
    var mode = _config["ExecutionMode"] ?? "browser";
    return Ok(new { executionMode = mode });
}
```

### Frontend detection

At page load, the frontend fetches the mode and stores it globally:

```javascript
const cfgRes = await fetch("/api/config");
if (cfgRes.ok) {
    const cfg = await cfgRes.json();
    executionMode = cfg.executionMode || "browser";
    if (executionMode === "local") {
        ensureMauiFilePickerBridge();
    }
}
```

All file-input rendering, payload construction, and artefact linking branch on this value.


## Why two modes exist

### Browser mode

The application was originally built as a **web app** served by ASP.NET and accessed in a
browser. In this context:

- The browser sandbox prevents direct file system access.
- Files must be **uploaded** to the server (via `POST /api/guiJob/upload`) before the job
  can read them.
- Output files are served back via download API (artifact sink) or stored in a temp directory.
- Folder picking is not possible (browser limitation).

### Local mode (MAUI)

When the same web frontend is hosted inside a **.NET MAUI** desktop app (via WebView):

- The app runs on the user's machine and has native file system access.
- A **MAUI file picker bridge** (`window.MauiFilePicker`) is injected into the WebView,
  enabling native OS file/folder dialogs.
- File paths are sent directly in the JSON payload — no upload step.
- On-disk outputs can reveal any user-selected path in the system file explorer.
- The same ASP.NET backend runs locally (self-hosted or in-process).

This avoids the overhead of uploading large files to a server that is already local, and
enables folder-based workflows that the browser sandbox cannot support.


## What changes between modes

### File input rendering

```javascript
function renderFileInput(field, multiple) {
    if (executionMode === "local") {
        return renderLocalFileInput(field, multiple);   // MauiFilePicker
    }
    return renderBrowserFileInput(field, multiple);     // <input type="file">
}
```

| Feature | Browser | Local |
|---------|---------|-------|
| Single file | `<input type="file">` | `MauiFilePicker.pickFile()` |
| Multiple files | `<input type="file" multiple>` | `MauiFilePicker.pickFiles()` |
| Folder scan | Not available | `MauiFilePicker.pickFolder()` |
| Directory path | Not available | `MauiFilePicker.pickDirectory()` |

### Payload construction

```javascript
async function buildRunPayload() {
    const payload = { ...inputValues };
    if (executionMode === "local") {
        return payload;                    // paths already in inputValues
    }
    // Browser: upload files, substitute temp paths
    // ...
    return payload;
}
```

### Path security

The `IsAllowedJobPath` server-side check adapts to the mode:

- **Browser**: Only paths under `{TempPath}/guijob/` and `{TempPath}/guijob_output/` are allowed.
- **Local**: For reveal-in-folder, any rooted path is accepted (the user explicitly chose it).

### Output artefacts

Download artefacts (artifact sink, `IsOnDisk = false`) work **identically** in both modes —
they are in-memory blobs served via `GET /api/guiJob/{jobId}/download/{artifactKey}`.

On-disk artefacts (`IsOnDisk = true`) use reveal-in-folder, which opens the native file
explorer. This is meaningful in both modes but more useful in local mode where the paths
are user-chosen locations.


## Configuration summary

| Setting | Where | Default |
|---------|-------|---------|
| `ExecutionMode` | `appsettings.json`, environment variable, launch profile | `"browser"` |
| `/api/config` | Served to frontend at page load | `{ executionMode: "browser" }` |
| `executionMode` (JS) | Global variable in `jobRunner.js` | `"browser"` |


## See also

- [Working with Local Files](file-sys-access.md) — file picking, upload, and artifact sink behaviour
- [GUI Job](gui-job.md) — auto-generated job pages with inputs and outputs
- [SignalR Logging](report-logs.md) — reporter, signal types, progress bars
