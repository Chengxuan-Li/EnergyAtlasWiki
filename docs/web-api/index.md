# EnergyAtlas Web API Reference

- Generated on: `2026-07-13`
- Source commit: `565002b6bd4393f149b2cdf348d4401d848e3151`
- Source branch: `shading-api`
- Dirty state: Dirty source state present excluding generated skill/doc paths.
- Note: generated deterministically from current source; older hand-written docs are context only.

## Overview

This reference is generated from the current ASP.NET controller source and startup configuration.
Use it as the source-derived endpoint inventory for agents; hand-written API docs may lag behind source changes.

## Related Guides

These companion guides explain the voxel-shading math and API workflows referenced by this source-derived API reference.

| Guide | What it explains |
| --- | --- |
| [Voxel shading guide index](../workflows/shading/index.md) | Entry point for shading math and API workflow guides. |
| [Sky and horizon view factors](../workflows/shading/sky-horizon-view-factors.md) | How SVF, HVF, and dome sky-bin visibility are ray-marched. |
| [Incident radiation from weather and shading](../workflows/shading/incident-radiation.md) | How EPW DNI/DHI, Perez components, sunlit fraction, SVF, and HVF produce incident radiation. |
| [Sunlit fraction calculation](../workflows/shading/sunlit-fraction.md) | How representative-day sun vectors and voxel ray marching produce sunlit fraction arrays. |
| [Voxelization, sensor generation, and shading pipeline](../workflows/shading/voxelization-sensors-calculation.md) | How the voxelize, generateSensors, calculate, preview, job, and result API flow works. |

## Running the Backend

| Item | Value |
| --- | --- |
| Project | EnergyAtlasWeb/EnergyAtlasWeb.csproj |
| Target frameworks | net8.0 |
| Project references | ../EnergyAtlasCore/EnergyAtlasCore.csproj, ../EnergyAtlasLib/EnergyAtlasLib.csproj |
| Preferred HTTP port | 5094 |
| Preferred HTTPS port | 7200 |
| Port search window |  |

```powershell
dotnet restore EnergyAtlasWeb/EnergyAtlasWeb.csproj
dotnet run --project EnergyAtlasWeb/EnergyAtlasWeb.csproj
```

The Python connector's invoked backend path uses `dotnet run --project EnergyAtlasWeb/EnergyAtlasWeb.csproj --no-launch-profile` and may set `ASPNETCORE_URLS`.

## Ports, Swagger, and Hubs

| Surface | Path or value |
| --- | --- |
| Swagger JSON | /swagger/v1/swagger.json |
| Swagger UI | /api-docs |
| SignalR hub `JobHub` | /jobHub |
| SignalR hub `WorkflowProgressHub` | /workflowProgressHub |

Launch profiles:

| Profile | Application URL | Environment |
| --- | --- | --- |
| http | http://localhost:5094 | Development |
| https | https://localhost:7200;http://localhost:5094 | Development |

## API Conventions

| Convention | Source-derived note |
| --- | --- |
| Authentication | No AddAuthentication/UseAuthentication/[Authorize] patterns found |
| CORS | No AddCors/UseCors/[EnableCors] patterns found |
| Large uploads | Configured |
| Secret-like config keys | Mapbox:Token = <masked> |

## Controller Endpoint Inventory

| Metric | Value |
| --- | --- |
| Existing docs source | docs/api/api-reference.md |
| Existing docs controller count | 16 |
| Existing docs endpoint count | 201 |
| Current source controller count | 17 |
| Current source endpoint count | 209 |

| Controller | Endpoint count | Source |
| --- | --- | --- |
| BuildingDownloaderController | 4 | EnergyAtlasWeb/Controllers/BuildingDownloaderController.cs |
| DataHubController | 83 | EnergyAtlasWeb/Controllers/DataHubController.cs |
| FusionController | 7 | EnergyAtlasWeb/Controllers/FusionController.cs |
| GUIJobRunnerController | 11 | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs |
| GeoDataPreviewController | 4 | EnergyAtlasWeb/Controllers/GeoDataPreviewController.cs |
| GeometricPreprocessingController | 3 | EnergyAtlasWeb/Controllers/GeometricPreprocessingController.cs |
| JobListController | 1 | EnergyAtlasWeb/Controllers/JobListController.cs |
| JobRouterController | 1 | EnergyAtlasWeb/Controllers/JobRouterController.cs |
| ProjectController | 20 | EnergyAtlasWeb/Controllers/ProjectController.cs |
| ResultViewerController | 3 | EnergyAtlasWeb/Controllers/ResultViewerController.cs |
| ScenarioDesignerController | 13 | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs |
| SchemaMatchingController | 8 | EnergyAtlasWeb/Controllers/SchemaMatchingController.cs |
| SimulationController | 5 | EnergyAtlasWeb/Controllers/SimulationController.cs |
| TemplateAssignmentController | 13 | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs |
| VoxelShadingController | 8 | EnergyAtlasWeb/Controllers/VoxelShadingController.cs |
| WeatherController | 5 | EnergyAtlasWeb/Controllers/WeatherController.cs |
| ZoneCalibrationController | 20 | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs |

| Method | Route | Controller | Action | Request DTOs | Responses | Source |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /api/buildingDownloader/listOvertureLayers | BuildingDownloaderController | ListOvertureLayers |  |  | EnergyAtlasWeb/Controllers/BuildingDownloaderController.cs:43 |
| POST | /api/buildingDownloader/fetchRegion | BuildingDownloaderController | FetchRegion | FetchRegionRequest |  | EnergyAtlasWeb/Controllers/BuildingDownloaderController.cs:153 |
| POST | /api/buildingDownloader/getTileMetadata | BuildingDownloaderController | GetTileMetadata | GetTileMetadataRequest |  | EnergyAtlasWeb/Controllers/BuildingDownloaderController.cs:399 |
| POST | /api/buildingDownloader/saveToDataHub | BuildingDownloaderController | SaveToDataHub | SaveToDataHubRequest |  | EnergyAtlasWeb/Controllers/BuildingDownloaderController.cs:621 |
| POST | /api/dataHub/fetchFeatureCollection | DataHubController | FetchFeatureCollection |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:25 |
| POST | /api/dataHub/fetchBuildingTemplate | DataHubController | FetchBuildingTemplate |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:47 |
| POST | /api/dataHub/fetchConstruction | DataHubController | FetchConstruction |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:67 |
| POST | /api/dataHub/fetchSystems | DataHubController | FetchSystems |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:87 |
| POST | /api/dataHub/fetchSpaceloads | DataHubController | FetchSpaceloads |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:107 |
| POST | /api/dataHub/fetchExternalLoads | DataHubController | FetchExternalLoads |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:127 |
| POST | /api/dataHub/fetchEnvelopeMeasure | DataHubController | FetchEnvelopeMeasure |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:142 |
| POST | /api/dataHub/fetchHeatingSystemMeasure | DataHubController | FetchHeatingSystemMeasure |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:156 |
| POST | /api/dataHub/fetchCoolingSystemMeasure | DataHubController | FetchCoolingSystemMeasure |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:170 |
| POST | /api/dataHub/fetchHotWaterMeasure | DataHubController | FetchHotWaterMeasure |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:184 |
| POST | /api/dataHub/fetchPlugLoadMeasure | DataHubController | FetchPlugLoadMeasure |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:198 |
| POST | /api/dataHub/fetchGasEquipmentMeasure | DataHubController | FetchGasEquipmentMeasure |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:212 |
| POST | /api/dataHub/fetchPVMeasure | DataHubController | FetchPVMeasure |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:226 |
| POST | /api/dataHub/fetchCsv | DataHubController | FetchCsv |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:245 |
| POST | /api/dataHub/fetchJsonString | DataHubController | FetchJsonString |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:301 |
| POST | /api/dataHub/fetchWeatherEpw | DataHubController | FetchWeatherEpw |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:319 |
| GET | /api/dataHub/listGeoJsonEntries | DataHubController | ListGeoJsonEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:333 |
| GET | /api/dataHub/listScenarioEntries | DataHubController | ListScenarioEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:350 |
| GET | /api/dataHub/listCsvEntries | DataHubController | ListCsvEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:369 |
| GET | /api/dataHub/listJsonStringEntries | DataHubController | ListJsonStringEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:386 |
| GET | /api/dataHub/listBuildingTemplateEntries | DataHubController | ListBuildingTemplateEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:403 |
| GET | /api/dataHub/listConstructionEntries | DataHubController | ListConstructionEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:420 |
| GET | /api/dataHub/listSystemsEntries | DataHubController | ListSystemsEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:437 |
| GET | /api/dataHub/listSpaceloadsEntries | DataHubController | ListSpaceloadsEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:454 |
| GET | /api/dataHub/listExternalLoadsEntries | DataHubController | ListExternalLoadsEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:471 |
| GET | /api/dataHub/listWeatherEntries | DataHubController | ListWeatherEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:488 |
| GET | /api/dataHub/listEnvelopeMeasureEntries | DataHubController | ListEnvelopeMeasureEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:505 |
| GET | /api/dataHub/listHeatingSystemMeasureEntries | DataHubController | ListHeatingSystemMeasureEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:522 |
| GET | /api/dataHub/listCoolingSystemMeasureEntries | DataHubController | ListCoolingSystemMeasureEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:539 |
| GET | /api/dataHub/listHotWaterMeasureEntries | DataHubController | ListHotWaterMeasureEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:556 |
| GET | /api/dataHub/listPlugLoadMeasureEntries | DataHubController | ListPlugLoadMeasureEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:573 |
| GET | /api/dataHub/listGasEquipmentMeasureEntries | DataHubController | ListGasEquipmentMeasureEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:590 |
| GET | /api/dataHub/listPVMeasureEntries | DataHubController | ListPVMeasureEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:607 |
| GET | /api/dataHub/listSampleGeoJsonEntries | DataHubController | ListSampleGeoJsonEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:625 |
| GET | /api/dataHub/listSampleCsvEntries | DataHubController | ListSampleCsvEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:642 |
| GET | /api/dataHub/listSampleJsonStringEntries | DataHubController | ListSampleJsonStringEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:659 |
| GET | /api/dataHub/listSampleBuildingTemplateEntries | DataHubController | ListSampleBuildingTemplateEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:676 |
| GET | /api/dataHub/listSampleMeasureEntries | DataHubController | ListSampleMeasureEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:693 |
| GET | /api/dataHub/listSampleWeatherEntries | DataHubController | ListSampleWeatherEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:710 |
| GET | /api/dataHub/listSampleConstructionEntries | DataHubController | ListSampleConstructionEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:727 |
| GET | /api/dataHub/listSampleSystemsEntries | DataHubController | ListSampleSystemsEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:742 |
| GET | /api/dataHub/listSampleSpaceloadsEntries | DataHubController | ListSampleSpaceloadsEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:756 |
| GET | /api/dataHub/listSampleExternalLoadsEntries | DataHubController | ListSampleExternalLoadsEntries |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:770 |
| POST | /api/dataHub/importGeoJsonEntry | DataHubController | ImportGeoJsonEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:785 |
| POST | /api/dataHub/importCsvEntry | DataHubController | ImportCsvEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:805 |
| POST | /api/dataHub/importJsonStringEntry | DataHubController | ImportJsonStringEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:825 |
| POST | /api/dataHub/importMeasureEntry | DataHubController | ImportMeasureEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:845 |
| POST | /api/dataHub/uploadGeoJsonEntry | DataHubController | UploadGeoJsonEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:873 |
| POST | /api/dataHub/uploadCsvEntry | DataHubController | UploadCsvEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:948 |
| POST | /api/dataHub/uploadJsonStringEntry | DataHubController | UploadJsonStringEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1009 |
| POST | /api/dataHub/uploadWeatherEntry | DataHubController | UploadWeatherEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1066 |
| POST | /api/dataHub/uploadBuildingTemplateEntry | DataHubController | UploadBuildingTemplateEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1134 |
| POST | /api/dataHub/uploadConstructionEntry | DataHubController | UploadConstructionEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1207 |
| POST | /api/dataHub/uploadSystemsEntry | DataHubController | UploadSystemsEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1232 |
| POST | /api/dataHub/uploadSpaceloadsEntry | DataHubController | UploadSpaceloadsEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1257 |
| POST | /api/dataHub/uploadExternalLoadsEntry | DataHubController | UploadExternalLoadsEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1282 |
| POST | /api/dataHub/uploadMeasureEntry | DataHubController | UploadMeasureEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1307 |
| POST | /api/dataHub/upsertMeasureEntry | DataHubController | UpsertMeasureEntry | UpsertMeasureRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1388 |
| POST | /api/dataHub/importBuildingTemplateEntry | DataHubController | ImportBuildingTemplateEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1504 |
| POST | /api/dataHub/importConstructionEntry | DataHubController | ImportConstructionEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1528 |
| POST | /api/dataHub/importSystemsEntry | DataHubController | ImportSystemsEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1557 |
| POST | /api/dataHub/importSpaceloadsEntry | DataHubController | ImportSpaceloadsEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1584 |
| POST | /api/dataHub/importExternalLoadsEntry | DataHubController | ImportExternalLoadsEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1611 |
| POST | /api/dataHub/importWeatherEntry | DataHubController | ImportWeatherEntry | ImportRequest |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1638 |
| DELETE | /api/dataHub/removeGeoJsonEntry | DataHubController | RemoveGeoJsonEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1659 |
| DELETE | /api/dataHub/removeScenarioEntry | DataHubController | RemoveScenarioEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1691 |
| DELETE | /api/dataHub/removeCsvEntry | DataHubController | RemoveCsvEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1720 |
| DELETE | /api/dataHub/removeJsonStringEntry | DataHubController | RemoveJsonStringEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1752 |
| DELETE | /api/dataHub/removeBuildingTemplateEntry | DataHubController | RemoveBuildingTemplateEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1784 |
| DELETE | /api/dataHub/removeConstructionEntry | DataHubController | RemoveConstructionEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1816 |
| DELETE | /api/dataHub/removeSystemsEntry | DataHubController | RemoveSystemsEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1845 |
| DELETE | /api/dataHub/removeSpaceloadsEntry | DataHubController | RemoveSpaceloadsEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1874 |
| DELETE | /api/dataHub/removeExternalLoadsEntry | DataHubController | RemoveExternalLoadsEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1903 |
| DELETE | /api/dataHub/removeWeatherEntry | DataHubController | RemoveWeatherEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1932 |
| DELETE | /api/dataHub/removeEnvelopeMeasureEntry | DataHubController | RemoveEnvelopeMeasureEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1962 |
| DELETE | /api/dataHub/removeHeatingSystemMeasureEntry | DataHubController | RemoveHeatingSystemMeasureEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:1991 |
| DELETE | /api/dataHub/removeCoolingSystemMeasureEntry | DataHubController | RemoveCoolingSystemMeasureEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:2020 |
| DELETE | /api/dataHub/removeHotWaterMeasureEntry | DataHubController | RemoveHotWaterMeasureEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:2049 |
| DELETE | /api/dataHub/removePlugLoadMeasureEntry | DataHubController | RemovePlugLoadMeasureEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:2078 |
| DELETE | /api/dataHub/removeGasEquipmentMeasureEntry | DataHubController | RemoveGasEquipmentMeasureEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:2107 |
| DELETE | /api/dataHub/removePVMeasureEntry | DataHubController | RemovePVMeasureEntry |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:2136 |
| GET | /api/dataHub/geoData | DataHubController | GetGeoData |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:2384 |
| GET | /api/dataHub/archetypes | DataHubController | GetArchetypes |  |  | EnergyAtlasWeb/Controllers/DataHubController.cs:2397 |
| POST | /api/project/fusion/run | FusionController | Run |  |  | EnergyAtlasWeb/Controllers/FusionController.cs:32 |
| POST | /api/project/fusion/replaceArtifact | FusionController | ReplaceArtifact |  |  | EnergyAtlasWeb/Controllers/FusionController.cs:281 |
| POST | /api/project/fusion/previewUpload | FusionController | PreviewUpload |  |  | EnergyAtlasWeb/Controllers/FusionController.cs:379 |
| POST | /api/project/fusion/previewFromPath | FusionController | PreviewFromPath | PreviewFromPathRequest |  | EnergyAtlasWeb/Controllers/FusionController.cs:443 |
| GET | /api/project/fusion/artifact | FusionController | GetArtifact |  |  | EnergyAtlasWeb/Controllers/FusionController.cs:496 |
| GET | /api/project/schemaMatch/artifact | FusionController | GetSchemaMatchedArtifact |  |  | EnergyAtlasWeb/Controllers/FusionController.cs:700 |
| POST | /api/project/schemaMatch/replaceArtifact | FusionController | ReplaceSchemaMatchedArtifact |  |  | EnergyAtlasWeb/Controllers/FusionController.cs:743 |
| GET | /api/config | GUIJobRunnerController | GetConfig |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:47 |
| GET | /api/guiJob | GUIJobRunnerController | ListJobs |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:63 |
| GET | /api/guiJob/{jobName}/schema | GUIJobRunnerController | GetSchema |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:77 |
| POST | /api/guiJob/{jobName}/validate | GUIJobRunnerController | Validate |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:101 |
| POST | /api/guiJob/{jobName}/run | GUIJobRunnerController | Run |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:145 |
| GET | /api/guiJob/{jobName}/result/{jobId} | GUIJobRunnerController | GetResult |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:253 |
| POST | /api/guiJob/upload | GUIJobRunnerController | Upload |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:271 |
| GET | /api/guiJob/DemoJob/presets | GUIJobRunnerController | DemoPresets |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:329 |
| GET | /api/guiJob/{jobId}/download/{artifactKey} | GUIJobRunnerController | DownloadArtifact |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:346 |
| GET | /api/guiJob/download | GUIJobRunnerController | DownloadFile |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:366 |
| POST | /api/guiJob/revealInFolder | GUIJobRunnerController | RevealInFolder |  |  | EnergyAtlasWeb/Controllers/GUIJobRunnerController.cs:388 |
| GET | /api/geoDataPreview/listGeoJsonEntries | GeoDataPreviewController | ListGeoJsonEntries |  |  | EnergyAtlasWeb/Controllers/GeoDataPreviewController.cs:28 |
| POST | /api/geoDataPreview/fetchGeoJson | GeoDataPreviewController | FetchGeoJson | FetchGeoJsonRequest |  | EnergyAtlasWeb/Controllers/GeoDataPreviewController.cs:55 |
| GET | /api/geoDataPreview/getFeatureAttributes | GeoDataPreviewController | GetFeatureAttributes |  |  | EnergyAtlasWeb/Controllers/GeoDataPreviewController.cs:199 |
| GET | /api/geoDataPreview/fetchProjectFile | GeoDataPreviewController | FetchProjectFile |  |  | EnergyAtlasWeb/Controllers/GeoDataPreviewController.cs:397 |
| POST | /api/project/geometricPreprocessing/run | GeometricPreprocessingController | Run |  |  | EnergyAtlasWeb/Controllers/GeometricPreprocessingController.cs:36 |
| GET | /api/project/geometricPreprocessing/artifact | GeometricPreprocessingController | GetArtifact |  |  | EnergyAtlasWeb/Controllers/GeometricPreprocessingController.cs:151 |
| POST | /api/project/geometricPreprocessing/replaceArtifact | GeometricPreprocessingController | ReplaceArtifact |  |  | EnergyAtlasWeb/Controllers/GeometricPreprocessingController.cs:191 |
| GET | /api/jobList | JobListController | ListJobs |  | 200 IEnumerable<JobDescriptor> | EnergyAtlasWeb/Controllers/JobListController.cs:23 |
| POST | /api/jobList/{jobName}/start | JobRouterController | StartJob |  | 200 object, 404 | EnergyAtlasWeb/Controllers/JobRouterController.cs:61 |
| GET | /api/project | ProjectController | GetCurrent |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:23 |
| GET | /api/project/workflow | ProjectController | GetWorkflowStates |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:33 |
| POST | /api/project/create | ProjectController | Create | CreateProjectRequest |  | EnergyAtlasWeb/Controllers/ProjectController.cs:45 |
| POST | /api/project/open | ProjectController | Open | OpenProjectRequest |  | EnergyAtlasWeb/Controllers/ProjectController.cs:72 |
| POST | /api/project/save | ProjectController | Save |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:141 |
| POST | /api/project/workflow/{itemId}/status | ProjectController | SetStatus | SetStatusRequest |  | EnergyAtlasWeb/Controllers/ProjectController.cs:154 |
| POST | /api/project/workflow/{itemId}/data | ProjectController | SetData | Dictionary<string, object> |  | EnergyAtlasWeb/Controllers/ProjectController.cs:166 |
| POST | /api/project/workflow/{itemId}/persist-files | ProjectController | PersistFiles | PersistFilesRequest |  | EnergyAtlasWeb/Controllers/ProjectController.cs:186 |
| POST | /api/project/close | ProjectController | Close |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:268 |
| POST | /api/project/archetypes/load | ProjectController | LoadArchetypes | LoadArchetypesRequest |  | EnergyAtlasWeb/Controllers/ProjectController.cs:701 |
| GET | /api/project/archetypes/filterOptions | ProjectController | GetArchetypeFilterOptions |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:987 |
| GET | /api/project/archetypes/list | ProjectController | ListArchetypesByCategory |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:998 |
| GET | /api/project/archetypes/detail | ProjectController | GetArchetypeDetail |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:1106 |
| DELETE | /api/project/archetypes/delete | ProjectController | DeleteArchetype |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:1173 |
| POST | /api/project/measures/load | ProjectController | LoadMeasures | LoadMeasuresRequest |  | EnergyAtlasWeb/Controllers/ProjectController.cs:1363 |
| GET | /api/project/measures/list | ProjectController | ListMeasures |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:1461 |
| GET | /api/project/measures/defaults | ProjectController | GetMeasureDefaults |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:1474 |
| GET | /api/project/measures/detail | ProjectController | GetMeasureDetail |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:1494 |
| POST | /api/project/measures/save | ProjectController | SaveMeasure | MeasureSaveRequest |  | EnergyAtlasWeb/Controllers/ProjectController.cs:1525 |
| DELETE | /api/project/measures/delete | ProjectController | DeleteMeasure |  |  | EnergyAtlasWeb/Controllers/ProjectController.cs:1580 |
| POST | /api/resultViewer/upload | ResultViewerController | Upload |  |  | EnergyAtlasWeb/Controllers/ResultViewerController.cs:28 |
| GET | /api/resultViewer/uploaded/{id} | ResultViewerController | GetUploaded |  |  | EnergyAtlasWeb/Controllers/ResultViewerController.cs:78 |
| POST | /api/resultViewer/censusOverlay | ResultViewerController | GetCensusOverlay |  |  | EnergyAtlasWeb/Controllers/ResultViewerController.cs:94 |
| GET | /api/scenarioDesigner/measures/envelope | ScenarioDesignerController | GetEnvelopeMeasures |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:25 |
| GET | /api/scenarioDesigner/measures/heating | ScenarioDesignerController | GetHeatingMeasures |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:34 |
| GET | /api/scenarioDesigner/measures/cooling | ScenarioDesignerController | GetCoolingMeasures |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:43 |
| GET | /api/scenarioDesigner/measures/hotwater | ScenarioDesignerController | GetHotWaterMeasures |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:52 |
| GET | /api/scenarioDesigner/measures/plugload | ScenarioDesignerController | GetPlugLoadMeasures |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:61 |
| GET | /api/scenarioDesigner/measures/gasequipment | ScenarioDesignerController | GetGasEquipmentMeasures |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:70 |
| GET | /api/scenarioDesigner/measures/pv | ScenarioDesignerController | GetPvMeasures |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:79 |
| POST | /api/scenarioDesigner/evaluate | ScenarioDesignerController | EvaluateRules |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:88 |
| POST | /api/scenarioDesigner/export | ScenarioDesignerController | ExportRules |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:305 |
| POST | /api/scenarioDesigner/import | ScenarioDesignerController | ImportRules |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:334 |
| POST | /api/scenarioDesigner/saveLibrary | ScenarioDesignerController | SaveLibrary |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:371 |
| GET | /api/scenarioDesigner/loadLibrary | ScenarioDesignerController | LoadLibrary |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:401 |
| POST | /api/scenarioDesigner/saveScenario | ScenarioDesignerController | SaveScenario |  |  | EnergyAtlasWeb/Controllers/ScenarioDesignerController.cs:428 |
| GET | /api/schemaMatching/targetFields | SchemaMatchingController | GetTargetFields |  |  | EnergyAtlasWeb/Controllers/SchemaMatchingController.cs:133 |
| POST | /api/schemaMatching/autoMatch | SchemaMatchingController | AutoMatch | SchemaAutoMatchRequest |  | EnergyAtlasWeb/Controllers/SchemaMatchingController.cs:207 |
| POST | /api/schemaMatching/applyMapping | SchemaMatchingController | ApplyMapping | SchemaApplyMappingRequest |  | EnergyAtlasWeb/Controllers/SchemaMatchingController.cs:264 |
| POST | /api/schemaMatching/saveToDataHub | SchemaMatchingController | SaveToDataHub | SchemaSaveToDataHubRequest |  | EnergyAtlasWeb/Controllers/SchemaMatchingController.cs:293 |
| POST | /api/schemaMatching/uploadGeoJson | SchemaMatchingController | UploadGeoJson |  |  | EnergyAtlasWeb/Controllers/SchemaMatchingController.cs:349 |
| GET | /api/schemaMatching/loadRules | SchemaMatchingController | LoadRules |  |  | EnergyAtlasWeb/Controllers/SchemaMatchingController.cs:430 |
| POST | /api/schemaMatching/saveRules | SchemaMatchingController | SaveRules | SaveSchemaRulesRequest |  | EnergyAtlasWeb/Controllers/SchemaMatchingController.cs:464 |
| POST | /api/project/schemaMatch/complete | SchemaMatchingController | CompleteSchemaMatch |  |  | EnergyAtlasWeb/Controllers/SchemaMatchingController.cs:504 |
| POST | /api/simulation/preflight | SimulationController | Preflight |  |  | EnergyAtlasWeb/Controllers/SimulationController.cs:44 |
| POST | /api/simulation/run | SimulationController | RunSimulation |  |  | EnergyAtlasWeb/Controllers/SimulationController.cs:76 |
| GET | /api/simulation/job/{jobId} | SimulationController | GetSimulationJob |  |  | EnergyAtlasWeb/Controllers/SimulationController.cs:178 |
| GET | /api/project/simulation/baselineArtifact | SimulationController | GetBaselineArtifact |  |  | EnergyAtlasWeb/Controllers/SimulationController.cs:407 |
| POST | /api/project/simulation/replaceBaselineArtifact | SimulationController | ReplaceBaselineArtifact |  |  | EnergyAtlasWeb/Controllers/SimulationController.cs:468 |
| GET | /api/samples/ithacaBuildings | TemplateAssignmentController | GetIthacaBuildings |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:52 |
| GET | /api/templateAssignment/archetypes/constructions | TemplateAssignmentController | GetConstructionArchetypes |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:63 |
| GET | /api/templateAssignment/archetypes/systems | TemplateAssignmentController | GetSystemsArchetypes |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:82 |
| GET | /api/templateAssignment/archetypes/spaceloads | TemplateAssignmentController | GetSpaceloadsArchetypes |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:101 |
| GET | /api/templateAssignment/archetypes/externalloads | TemplateAssignmentController | GetExternalLoadsArchetypes |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:120 |
| POST | /api/templateAssignment/evaluate | TemplateAssignmentController | EvaluateRules |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:140 |
| POST | /api/templateAssignment/templated | TemplateAssignmentController | ExportTemplatedGeoJson |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:427 |
| POST | /api/templateAssignment/complete | TemplateAssignmentController | Complete |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:675 |
| GET | /api/project/archetypeAssignment/artifact | TemplateAssignmentController | GetSimReadyArtifact |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:959 |
| POST | /api/project/archetypeAssignment/replaceArtifact | TemplateAssignmentController | ReplaceSimReadyArtifact |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:994 |
| POST | /api/templateAssignment/export | TemplateAssignmentController | ExportRuleset |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:1100 |
| POST | /api/templateAssignment/import | TemplateAssignmentController | ImportRuleset |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:1198 |
| GET | /api/templateAssignment/defaultRules | TemplateAssignmentController | GetDefaultRules |  |  | EnergyAtlasWeb/Controllers/TemplateAssignmentController.cs:1456 |
| POST | /api/voxelShading/generateSensors | VoxelShadingController | GenerateSensors | GenerateSensorsRequest |  | EnergyAtlasWeb/Controllers/VoxelShadingController.cs:150 |
| POST | /api/voxelShading/calculate | VoxelShadingController | Calculate | CalculateShadingRequest |  | EnergyAtlasWeb/Controllers/VoxelShadingController.cs:177 |
| POST | /api/voxelShading/voxelize | VoxelShadingController | Voxelize | VoxelizeRequest |  | EnergyAtlasWeb/Controllers/VoxelShadingController.cs:206 |
| POST | /api/voxelShading/preview/voxels | VoxelShadingController | PreviewVoxels | VoxelPreviewRequest |  | EnergyAtlasWeb/Controllers/VoxelShadingController.cs:239 |
| POST | /api/voxelShading/preview/sensors | VoxelShadingController | PreviewSensors | SensorPreviewRequest |  | EnergyAtlasWeb/Controllers/VoxelShadingController.cs:249 |
| POST | /api/voxelShading/preview/shading | VoxelShadingController | PreviewShading | ShadingPreviewRequest |  | EnergyAtlasWeb/Controllers/VoxelShadingController.cs:259 |
| GET | /api/voxelShading/job/{jobId} | VoxelShadingController | GetJob |  |  | EnergyAtlasWeb/Controllers/VoxelShadingController.cs:269 |
| GET | /api/voxelShading/result/{jobId} | VoxelShadingController | GetResult |  |  | EnergyAtlasWeb/Controllers/VoxelShadingController.cs:277 |
| GET | /api/weather/listSample | WeatherController | ListSampleWeatherEntries |  |  | EnergyAtlasWeb/Controllers/WeatherController.cs:14 |
| POST | /api/weather/importSample | WeatherController | ImportSampleWeatherEntry | WeatherImportRequest |  | EnergyAtlasWeb/Controllers/WeatherController.cs:32 |
| GET | /api/weather/listEntries | WeatherController | ListWeatherEntries |  |  | EnergyAtlasWeb/Controllers/WeatherController.cs:52 |
| POST | /api/weather/upload | WeatherController | UploadWeatherFile |  |  | EnergyAtlasWeb/Controllers/WeatherController.cs:70 |
| POST | /api/weather/loadFromDisk | WeatherController | LoadWeatherFromDisk | WeatherDiskRequest |  | EnergyAtlasWeb/Controllers/WeatherController.cs:110 |
| POST | /api/zones/extract | ZoneCalibrationController | ExtractZones |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:46 |
| GET | /api/zones | ZoneCalibrationController | ListZones |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:92 |
| GET | /api/zones/{zoneId} | ZoneCalibrationController | GetZone |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:126 |
| GET | /api/zones/{zoneId}/definition | ZoneCalibrationController | GetZoneDefinition |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:136 |
| GET | /api/buildings/{buildingId}/zones | ZoneCalibrationController | ZonesForBuilding |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:150 |
| GET | /api/zones/definitions | ZoneCalibrationController | ListZoneDefinitions |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:164 |
| POST | /api/zones/importDefinitions | ZoneCalibrationController | ImportZoneDefinitions |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:196 |
| POST | /api/zones/definitions/export | ZoneCalibrationController | ExportZoneDefinitions |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:279 |
| PATCH | /api/zones/{zoneId} | ZoneCalibrationController | PatchZone |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:320 |
| POST | /api/zones/batchPatch | ZoneCalibrationController | BatchPatchZones |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:350 |
| GET | /api/zones/{zoneId}/schedules | ZoneCalibrationController | ListZoneSchedules |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:400 |
| GET | /api/zones/{zoneId}/schedules/{scheduleType} | ZoneCalibrationController | GetZoneSchedule |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:424 |
| PUT | /api/zones/{zoneId}/schedules/{scheduleType} | ZoneCalibrationController | PutZoneSchedule |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:441 |
| POST | /api/zones/schedules/batchUpdate | ZoneCalibrationController | BatchUpdateSchedules |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:475 |
| POST | /api/zoneSimulation/preflight | ZoneCalibrationController | Preflight |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:523 |
| POST | /api/zoneSimulation/run | ZoneCalibrationController | Run |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:557 |
| POST | /api/zoneSimulation/runFromDefinitions | ZoneCalibrationController | RunFromDefinitions |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:655 |
| POST | /api/zoneSimulation/runStandalone | ZoneCalibrationController | RunStandalone |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:665 |
| POST | /api/zoneSimulation/batchRun | ZoneCalibrationController | BatchRun |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:675 |
| GET | /api/zoneSimulation/job/{jobId} | ZoneCalibrationController | GetJob |  |  | EnergyAtlasWeb/Controllers/ZoneCalibrationController.cs:706 |

## Workflow and Connector Relationship

- The Python connector covers project lifecycle, workflow state, fusion, schema matching, geometry preprocessing, archetypes, template assignment, weather, simulation, measures, scenarios, results, data hub, zones, zone schedules, zone simulation, and voxel shading namespaces.
- Compare connector namespace methods with this endpoint inventory before assuming a backend route has a Python wrapper.
- `POST /api/schemaMatching/autoMatch` is present in the web source inventory; connector coverage should be checked explicitly when needed.

## Jobs and Long-Running Operations

- Simulation jobs expose polling through `/api/simulation/job/{jobId}`.
- Zone simulation jobs expose polling through `/api/zoneSimulation/job/{jobId}`.
- Voxel shading jobs expose polling through `/api/voxelShading/job/{jobId}` and result retrieval through `/api/voxelShading/result/{jobId}`.
- SignalR hubs are listed above for progress-aware clients.

## Tests and Validation

| Kind | Path |
| --- | --- |
| test | EnergyAtlasWeb.ApiTests/ApiTestInfra.cs |
| test | EnergyAtlasWeb.ApiTests/ArchetypesLoadEndpointTests.cs |
| test | EnergyAtlasWeb.ApiTests/ConfigEndpointTests.cs |
| test | EnergyAtlasWeb.ApiTests/DataHubEndpointTests.cs |
| test | EnergyAtlasWeb.ApiTests/ProjectLifecycleEndpointTests.cs |
| test | EnergyAtlasWeb.ApiTests/ProjectReadsEndpointTests.cs |
| test | EnergyAtlasWeb.ApiTests/ProjectWorkflowEndpointTests.cs |
| test | EnergyAtlasWeb.ApiTests/SchemaMatchEndpointTests.cs |
| test | EnergyAtlasWeb.ApiTests/SignalRJobReporterTests.cs |
| test | EnergyAtlasWeb.ApiTests/SimulationEndpointTests.cs |
| test | EnergyAtlasWeb.ApiTests/SimulationWorkflowSequenceTests.cs |
| test | EnergyAtlasWeb.ApiTests/TemplateAssignmentEngineTests.cs |
| test | EnergyAtlasWeb.ApiTests/WeatherEndpointTests.cs |
| test | EnergyAtlasWeb.ApiTests/WorkflowPipeline.cs |
| test | EnergyAtlasWeb.ApiTests/ZoneCalibrationEndpointTests.cs |
| test | EnergyAtlasWeb.MethodTests/ArchetypeDedupHashTests.cs |
| test | EnergyAtlasWeb.MethodTests/JobExecutionTests.cs |
| test | EnergyAtlasWeb.MethodTests/JobRuntimeStateLogsConcurrencyTests.cs |
| test | EnergyAtlasWeb.MethodTests/JobSignalReplayOrderTests.cs |
| test | EnergyAtlasWeb.MethodTests/ProjectDataUserDataRoundTripTests.cs |
| test | EnergyAtlasWeb.MethodTests/SchemaMatchAutoMatcherTests.cs |
| test | EnergyAtlasWeb.MethodTests/SchemaMatchOverrideTests.cs |
| test | EnergyAtlasWeb.MethodTests/SerializeResultDriftTests.cs |
| test | EnergyAtlasWeb.MethodTests/SimulationValidationTests.cs |
| test | EnergyAtlasWeb.MethodTests/TestPaths.cs |
| test | EnergyAtlasWeb.MethodTests/VoxelizationInputPrepTests.cs |
| test | EnergyAtlasWeb.MethodTests/VoxelShadingControllerNycTests.cs |
| test | EnergyAtlasWeb.MethodTests/VoxelShadingControllerTests.cs |
| test | EnergyAtlasWeb.MethodTests/VoxelShadingPreviewServiceTests.cs |
| test | EnergyAtlasWeb.MethodTests/ZoneDefinitionUtilTests.cs |
| test | EnergyAtlasWeb.MethodTests/ZoneFixtures.cs |
| test | EnergyAtlasWeb.MethodTests/ZoneRunnerNativeTests.cs |
| runner | TestRunners/run-cs-tests-all.bat |
| runner | TestRunners/run-cs-tests-all.sh |
| runner | TestRunners/run-cs-tests-fast.bat |
| runner | TestRunners/run-cs-tests-fast.sh |

```powershell
dotnet build EnergyAtlasWeb/EnergyAtlasWeb.csproj
dotnet test EnergyAtlasWeb.ApiTests/EnergyAtlasWeb.ApiTests.csproj --filter "TestCategory=Compulsory&TestCategory!=Expensive"
dotnet test EnergyAtlasWeb.MethodTests/EnergyAtlasWeb.MethodTests.csproj --filter "TestCategory=Compulsory&TestCategory!=Expensive"
```

## Known Limitations and Cautions

- Controller source is authoritative for endpoint counts.
- Swagger is enabled, but response metadata may be sparse.
- No authentication or CORS behavior should be claimed unless source patterns are found.
- Existing hand-written docs may lag behind current controllers.
- Swagger output is useful for runtime cross-checks, but this generated document does not require starting the backend.
- Secret-like config values are masked and must not be copied into docs.
