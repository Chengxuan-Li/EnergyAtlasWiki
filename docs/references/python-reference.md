# EnergyAtlas Python Reference

- Generated on: `2026-07-13`
- Source commit: `565002b6bd4393f149b2cdf348d4401d848e3151`
- Source branch: `shading-api`
- Dirty state: Dirty source state present excluding generated skill/doc paths.
- Note: generated deterministically from current source; older hand-written docs are context only.

## Overview

The Python connector package is `energyatlas` version `0.1.0` with import name `energyatlas`.
It wraps EnergyAtlas web APIs with a synchronous client surface and helper orchestration classes.

## Related Guides

These companion guides explain the voxel-shading math and API workflows referenced by this source-derived API reference.

| Guide | What it explains |
| --- | --- |
| [Voxel shading guide index](guides/voxel-shading-guide-index.md) | Entry point for shading math and API workflow guides. |
| [Sky and horizon view factors](guides/sky-horizon-view-factors.md) | How SVF, HVF, and dome sky-bin visibility are ray-marched. |
| [Incident radiation from weather and shading](guides/incident-radiation.md) | How EPW DNI/DHI, Perez components, sunlit fraction, SVF, and HVF produce incident radiation. |
| [Sunlit fraction calculation](guides/sunlit-fraction.md) | How representative-day sun vectors and voxel ray marching produce sunlit fraction arrays. |
| [Voxelization, sensor generation, and shading pipeline](guides/voxelization-sensors-calculation.md) | How the voxelize, generateSensors, calculate, preview, job, and result API flow works. |

## Install and Runtime Requirements

| Item | Value |
| --- | --- |
| Python | >=3.10 |
| Build backend | setuptools.build_meta |
| Runtime dependencies | httpx>=0.27, pydantic>=2.6 |
| Discovery extra | psutil>=5.9 |
| Dev extra | pytest>=8.0, ruff>=0.5, mypy>=1.10 |

```powershell
cd Connectors/python
python -m pip install -e .
python -m pip install -e ".[dev,discovery]"
```

PyPI caution: the public package name `energyatlas` must be verified before recommending `pip install energyatlas`; use the repo-local editable install unless package publication ownership is confirmed.

## Backend Discovery and Startup

### `EnergyAtlasBackend`

| Method | Signature | Source |
| --- | --- | --- |
| start | start(*, repo_root: Optional[str \| os.PathLike[str]] = None, port: Optional[int] = None, host: str = '127.0.0.1', timeout_s: float = 90.0, dotnet_command: str = 'dotnet', logs: str = 'inherit') -> 'EnergyAtlasBackend' | Connectors/python/src/energyatlas/backend.py:41 |
| close | close(*, timeout_s: float = 10.0) -> None | Connectors/python/src/energyatlas/backend.py:168 |

### Discovery Functions

| Function | Signature | Source |
| --- | --- | --- |
| discover_base_url | discover_base_url(*, explicit_port: Optional[int] = None, explicit_host: str = '127.0.0.1', prefer_https: bool = False, extra_ports: Sequence[int] = (), timeout_s: float = 1.5, verify_ssl: bool = False) -> DiscoveredInstance | Connectors/python/src/energyatlas/discovery.py:61 |
| iter_default_ports | iter_default_ports() -> Iterable[int] | Connectors/python/src/energyatlas/discovery.py:267 |

### Discovery Constants

_None found._

## Client Construction

| Method | Signature | Source |
| --- | --- | --- |
| auto | auto(*, prefer_https: bool = False, timeout_s: float = 120.0, verify_ssl: bool = False, extra_ports: Iterable[int] = ()) -> 'EnergyAtlasClient' | Auto-discover a running EnergyAtlas backend and connect to it. | Connectors/python/src/energyatlas/client.py:1906 |
| ensure_backend | ensure_backend(*, base_url: Optional[str] = None, port: Optional[int] = None, host: str = '127.0.0.1', prefer_https: bool = False, timeout_s: float = 120.0, verify_ssl: bool = False, extra_ports: Iterable[int] = (), start_if_missing: bool = False, repo_root: Optional[str \| Path] = None, backend_timeout_s: float = 90.0, dotnet_command: str = 'dotnet', backend_logs: str = 'inherit') -> 'EnergyAtlasClient' | Connect to a backend, optionally launching EnergyAtlasWeb if discovery fails. | Connectors/python/src/energyatlas/client.py:1924 |
| from_port | from_port(port: int, *, host: str = '127.0.0.1', prefer_https: bool = False, timeout_s: float = 120.0, verify_ssl: bool = False) -> 'EnergyAtlasClient' | Connect to a specific local port (HTTP first, HTTPS fallback). | Connectors/python/src/energyatlas/client.py:1974 |
| base_url | base_url() -> str |  | Connectors/python/src/energyatlas/client.py:1996 |
| discovered | discovered() -> Optional[DiscoveredInstance] |  | Connectors/python/src/energyatlas/client.py:2000 |
| close | close() -> None |  | Connectors/python/src/energyatlas/client.py:2003 |

## Client Namespace APIs

| Namespace | Backing class | Method count | Methods |
| --- | --- | --- | --- |
| archetypes | _ArchetypesApi | 5 | load, filter_options, list, detail, delete |
| data_hub | _DataHubApi | 4 | fetch_feature_collection, fetch_weather_epw, fetch_geo_data_project_file, save_bytes |
| fusion | _FusionApi | 5 | preview_from_path, preview_upload, run, get_artifact, replace_artifact |
| geometry | _GeometryApi | 3 | run, get_artifact, replace_artifact |
| measures | _MeasuresApi | 6 | load, list, defaults, detail, save, delete |
| project | _ProjectApi | 5 | current, create, open, save, close |
| results | _ResultsApi | 3 | upload, get_uploaded, census_overlay |
| scenarios | _ScenarioApi | 13 | envelope, heating, cooling, hotwater, plugload, gas_equipment, pv, evaluate, save_library, load_library, save_scenario, export, import_rules |
| schema_match | _SchemaMatchApi | 9 | target_fields, upload_geojson, apply_mapping, save_rules, load_rules, save_to_data_hub, get_artifact, replace_artifact, complete |
| simulation | _SimulationApi | 6 | preflight, run, get_job_status, run_and_wait, get_baseline_artifact, replace_baseline_artifact |
| template_assignment | _TemplateAssignmentApi | 12 | list_constructions, list_systems, list_spaceloads, list_external_loads, default_rules, evaluate, complete, export_ruleset, import_ruleset, export_templated, get_sim_ready_artifact, replace_sim_ready_artifact |
| voxel_shading | _VoxelShadingApi | 11 | generate_sensors, calculate, voxelize, preview_voxels, preview_sensors, preview_shading, get_job_status, get_result, generate_sensors_and_wait, calculate_and_wait, voxelize_and_wait |
| weather | _WeatherApi | 7 | list_entries, list_sample, load_from_disk, resolve_entry_name, load_from_disk_and_get_entry, import_sample, upload |
| workflow | _WorkflowApi | 5 | get_states, get_item_state, set_data, set_status, persist_files |
| zone_schedules | _ZoneSchedulesApi | 4 | list, get, put, batch_update |
| zone_simulation | _ZoneSimulationApi | 13 | preflight, run, batch_run, run_from_definitions, run_standalone, run_standalone_from_definition_file, clone_definition, set_definition_value, collect_results, get_job, wait_for_job, parse_result, parse_job |
| zones | _ZonesApi | 10 | extract, list, list_definitions, export_definitions, get, get_definition, for_building, patch, batch_patch, import_definitions |

### `archetypes`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| load | load(folders: Iterable[str]) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:357 |
| filter_options | filter_options() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:364 |
| list | list(category: str) -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:367 |
| detail | detail(category: str, entry_name: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:373 |
| delete | delete(category: str, entry_name: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:385 |

### `data_hub`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| fetch_feature_collection | fetch_feature_collection(file_name: str) -> bytes |  | Connectors/python/src/energyatlas/client.py:1286 |
| fetch_weather_epw | fetch_weather_epw(file_name: str) -> bytes | Fetch cached weather EPW content by DataHub cached file name. | Connectors/python/src/energyatlas/client.py:1293 |
| fetch_geo_data_project_file | fetch_geo_data_project_file(relative_path: str) -> bytes | Project-relative file download (used by Stage 1 inspect/download). | Connectors/python/src/energyatlas/client.py:1302 |
| save_bytes | save_bytes(payload: bytes, *, destination: str \| Path) -> Path | Convenience helper to persist downloaded bytes to disk. | Connectors/python/src/energyatlas/client.py:1310 |

### `fusion`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| preview_from_path | preview_from_path(path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:216 |
| preview_upload | preview_upload(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:223 |
| run | run() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:231 |
| get_artifact | get_artifact() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:234 |
| replace_artifact | replace_artifact(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:237 |

### `geometry`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| run | run() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:334 |
| get_artifact | get_artifact() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:337 |
| replace_artifact | replace_artifact(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:340 |

### `measures`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| load | load(folders: Iterable[str]) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1098 |
| list | list(category: str) -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:1105 |
| defaults | defaults(category: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1111 |
| detail | detail(category: str, entry_name: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1123 |
| save | save(*, category_id: str, entry_name: str, is_new: bool, measure_json: str \| dict[str, Any]) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1135 |
| delete | delete(category: str, entry_name: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1155 |

### `project`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| current | current() -> dict[str, Any] | ``GET /api/project`` — returns ``{loaded, project?}``. | Connectors/python/src/energyatlas/client.py:115 |
| create | create(folder: str, *, name: Optional[str] = None) -> dict[str, Any] | Create a project at ``folder`` (the server creates the folder structure). | Connectors/python/src/energyatlas/client.py:120 |
| open | open(*, folder: Optional[str] = None, project_json_path: Optional[str] = None) -> dict[str, Any] | Open an existing project, either by folder or by ``Project.json`` path. | Connectors/python/src/energyatlas/client.py:131 |
| save | save() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:144 |
| close | close() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:147 |

### `results`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| upload | upload(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1231 |
| get_uploaded | get_uploaded(upload_id: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1239 |
| census_overlay | census_overlay(*, min_lon: float, min_lat: float, max_lon: float, max_lat: float, layer: Optional[str] = None, feature_collection: Optional[dict[str, Any]] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1248 |

### `scenarios`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| envelope | envelope() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:1168 |
| heating | heating() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:1171 |
| cooling | cooling() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:1174 |
| hotwater | hotwater() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:1177 |
| plugload | plugload() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:1180 |
| gas_equipment | gas_equipment() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:1183 |
| pv | pv() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:1186 |
| evaluate | evaluate(request: dict[str, Any]) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1189 |
| save_library | save_library(request: dict[str, Any]) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1195 |
| load_library | load_library() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1201 |
| save_scenario | save_scenario(request: dict[str, Any]) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1204 |
| export | export(request: dict[str, Any]) -> bytes |  | Connectors/python/src/energyatlas/client.py:1210 |
| import_rules | import_rules(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1216 |

### `schema_match`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| target_fields | target_fields() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:252 |
| upload_geojson | upload_geojson(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:255 |
| apply_mapping | apply_mapping(entry_name: str, mappings: Iterable[SchemaMappingRule \| dict[str, Any]]) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:263 |
| save_rules | save_rules(mappings: Iterable[SchemaMappingRule \| dict[str, Any]]) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:275 |
| load_rules | load_rules() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:286 |
| save_to_data_hub | save_to_data_hub(*, entry_name: str, output_entry_name: str, mappings: Iterable[SchemaMappingRule \| dict[str, Any]]) -> bytes |  | Connectors/python/src/energyatlas/client.py:289 |
| get_artifact | get_artifact() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:307 |
| replace_artifact | replace_artifact(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:310 |
| complete | complete() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:318 |

### `simulation`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| preflight | preflight(*, entry_name: Optional[str] = None, feature_collection: Optional[dict[str, Any]] = None, defaults: Optional[dict[str, Any]] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:529 |
| run | run(*, weather_entry_name: str, entry_name: Optional[str] = None, feature_collection: Optional[dict[str, Any]] = None, defaults: Optional[dict[str, Any]] = None, scenario_entry_name: Optional[str] = None, scenario_json: Optional[str] = None, options: Optional[SimulationOptions \| dict[str, Any]] = None, dashboard_name: Optional[str] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:546 |
| get_job_status | get_job_status(job_id: str, *, max_signals: int = 50) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:577 |
| run_and_wait | run_and_wait(*, weather_entry_name: str, entry_name: Optional[str] = None, feature_collection: Optional[dict[str, Any]] = None, defaults: Optional[dict[str, Any]] = None, scenario_entry_name: Optional[str] = None, scenario_json: Optional[str] = None, options: Optional[SimulationOptions \| dict[str, Any]] = None, dashboard_name: Optional[str] = None, poll_interval_s: float = 2.0, timeout_s: float = 60 * 60, idle_timeout_s: Optional[float] = None, project_folder: Optional[str] = None, scenario_name: str = 'Baseline', result_basename: Optional[str] = None, progress_callback: Optional[Callable[[dict[str, Any]], None]] = None, progress_interval_s: float = 10.0, expected_total: Optional[int] = None) -> dict[str, Any] | Run a baseline simulation and block until the workflow item completes. | Connectors/python/src/energyatlas/client.py:585 |
| get_baseline_artifact | get_baseline_artifact() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:965 |
| replace_baseline_artifact | replace_baseline_artifact(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:968 |

### `template_assignment`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| list_constructions | list_constructions() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:398 |
| list_systems | list_systems() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:401 |
| list_spaceloads | list_spaceloads() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:404 |
| list_external_loads | list_external_loads() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:407 |
| default_rules | default_rules(*, climate_zone: Optional[str] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:410 |
| evaluate | evaluate(request: dict[str, Any]) -> dict[str, Any] | ``POST /api/templateAssignment/evaluate``. | Connectors/python/src/energyatlas/client.py:414 |
| complete | complete(request: dict[str, Any]) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:430 |
| export_ruleset | export_ruleset() -> bytes |  | Connectors/python/src/energyatlas/client.py:436 |
| import_ruleset | import_ruleset(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:439 |
| export_templated | export_templated() -> bytes |  | Connectors/python/src/energyatlas/client.py:447 |
| get_sim_ready_artifact | get_sim_ready_artifact() -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:450 |
| replace_sim_ready_artifact | replace_sim_ready_artifact(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:453 |

### `voxel_shading`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| generate_sensors | generate_sensors(**kwargs: Any) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:987 |
| calculate | calculate(**kwargs: Any) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:994 |
| voxelize | voxelize(**kwargs: Any) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1001 |
| preview_voxels | preview_voxels(**kwargs: Any) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1008 |
| preview_sensors | preview_sensors(**kwargs: Any) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1015 |
| preview_shading | preview_shading(**kwargs: Any) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1022 |
| get_job_status | get_job_status(job_id: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1029 |
| get_result | get_result(job_id: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1034 |
| generate_sensors_and_wait | generate_sensors_and_wait(*, poll_interval_s: float = 2.0, timeout_s: float = 3600, **kwargs: Any) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1060 |
| calculate_and_wait | calculate_and_wait(*, poll_interval_s: float = 2.0, timeout_s: float = 3600, **kwargs: Any) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1067 |
| voxelize_and_wait | voxelize_and_wait(*, poll_interval_s: float = 2.0, timeout_s: float = 3600, **kwargs: Any) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1074 |

### `weather`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| list_entries | list_entries() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:468 |
| list_sample | list_sample() -> list[dict[str, Any]] |  | Connectors/python/src/energyatlas/client.py:471 |
| load_from_disk | load_from_disk(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:474 |
| resolve_entry_name | resolve_entry_name(payload: dict[str, Any]) -> Optional[str] | Extract weather entry name from a weather API response payload. | Connectors/python/src/energyatlas/client.py:482 |
| load_from_disk_and_get_entry | load_from_disk_and_get_entry(file_path: str) -> str | Load an EPW file and return the registered weather entry name. | Connectors/python/src/energyatlas/client.py:497 |
| import_sample | import_sample(sample_entry_name: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:506 |
| upload | upload(file_path: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:513 |

### `workflow`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| get_states | get_states() -> dict[str, Any] | ``GET /api/project/workflow``. | Connectors/python/src/energyatlas/client.py:157 |
| get_item_state | get_item_state(item_id: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:162 |
| set_data | set_data(item_id: str, data: dict[str, Any]) -> dict[str, Any] | ``POST /api/project/workflow/{itemId}/data``. | Connectors/python/src/energyatlas/client.py:169 |
| set_status | set_status(item_id: str, status: WorkflowItemStatus \| str) -> dict[str, Any] | ``POST /api/project/workflow/{itemId}/status``. | Connectors/python/src/energyatlas/client.py:177 |
| persist_files | persist_files(item_id: str, *, footprint_source: Optional[str] = None, parcel_sources: Optional[Iterable[str]] = None) -> dict[str, Any] | ``POST /api/project/workflow/{itemId}/persist-files``. | Connectors/python/src/energyatlas/client.py:191 |

### `zone_schedules`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| list | list(zone_id: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1488 |
| get | get(zone_id: str, schedule_type: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1493 |
| put | put(zone_id: str, schedule_type: str, schedule: ZoneScheduleObject \| dict[str, Any], *, base_model_ref: Optional[ZoneModelRef] = None, project_id: Optional[str] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1498 |
| batch_update | batch_update(updates: Iterable[ZoneSchedulePatch \| dict[str, Any]], *, base_model_ref: Optional[ZoneModelRef] = None, project_id: Optional[str] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1522 |

### `zone_simulation`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| preflight | preflight(*, zone_ids: Iterable[str], weather_entry_name: Optional[str] = None, base_model_ref: Optional[ZoneModelRef] = None, project_id: Optional[str] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1554 |
| run | run(*, weather_entry_name: str, runs: Optional[Iterable[ZoneSimulationRun \| dict[str, Any]]] = None, execution_mode: str = 'sync', base_model_ref: Optional[ZoneModelRef] = None, project_id: Optional[str] = None, run_options: Optional[ZoneRunOptions \| dict[str, Any]] = None, source_entry_name: Optional[str] = None, zone_definitions: Optional[Iterable[ZoneDefinition \| ZoneFullDefinition \| dict[str, Any]]] = None, zone: Optional[ZoneDefinition \| ZoneFullDefinition \| dict[str, Any]] = None, zones: Optional[Iterable[ZoneDefinition \| ZoneFullDefinition \| dict[str, Any]]] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1573 |
| batch_run | batch_run(*, weather_entry_name: str, runs: Iterable[ZoneSimulationRun \| dict[str, Any]], batch_id: Optional[str] = None, base_model_ref: Optional[ZoneModelRef] = None, project_id: Optional[str] = None, run_options: Optional[ZoneRunOptions \| dict[str, Any]] = None, source_entry_name: Optional[str] = None, zone_definitions: Optional[Iterable[ZoneDefinition \| ZoneFullDefinition \| dict[str, Any]]] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1614 |
| run_from_definitions | run_from_definitions(*, weather_entry_name: str, runs: Iterable[ZoneSimulationRun \| dict[str, Any]], zone_definitions: Iterable[ZoneDefinition \| ZoneFullDefinition \| dict[str, Any]], source_entry_name: Optional[str] = None, execution_mode: str = 'sync', base_model_ref: Optional[ZoneModelRef] = None, project_id: Optional[str] = None, run_options: Optional[ZoneRunOptions \| dict[str, Any]] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1641 |
| run_standalone | run_standalone(*, weather_entry_name: str, zone: Optional[ZoneFullDefinition \| dict[str, Any]] = None, zones: Optional[Iterable[ZoneFullDefinition \| dict[str, Any]]] = None, execution_mode: str = 'sync', run_options: Optional[ZoneRunOptions \| dict[str, Any]] = None, source_entry_name: Optional[str] = None) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1658 |
| run_standalone_from_definition_file | run_standalone_from_definition_file(*, definition_path: str, weather_file: str, execution_mode: str = 'sync', run_options: Optional[ZoneRunOptions \| dict[str, Any]] = None, source_entry_name: Optional[str] = None) -> dict[str, Any] | Load a definition JSON file + weather EPW, then call definition-first ``run``. | Connectors/python/src/energyatlas/client.py:1672 |
| clone_definition | clone_definition(definition: ZoneDefinition \| ZoneFullDefinition \| dict[str, Any]) -> dict[str, Any] | Return a deep-copied zone definition payload for safe editing. | Connectors/python/src/energyatlas/client.py:1705 |
| set_definition_value | set_definition_value(definition: ZoneDefinition \| ZoneFullDefinition \| dict[str, Any], path: str \| Iterable[str], value: Any) -> dict[str, Any] | Deep-copy a definition and set one nested value by path. | Connectors/python/src/energyatlas/client.py:1719 |
| collect_results | collect_results(payload: dict[str, Any]) -> list[dict[str, Any]] | Extract a flat list of zone result payloads from sync or async responses. | Connectors/python/src/energyatlas/client.py:1739 |
| get_job | get_job(job_id: str, *, run_id: Optional[str] = None, include_results: bool = False) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1758 |
| wait_for_job | wait_for_job(job_id: str, *, poll_interval_s: float = 2.0, timeout_s: float = 60 * 30) -> dict[str, Any] | Poll ``get_job`` until ``status`` is terminal or ``timeout_s`` elapses. | Connectors/python/src/energyatlas/client.py:1772 |
| parse_result | parse_result(payload: dict[str, Any]) -> ZoneSimulationResult | Validate a single zone result payload into a typed model. | Connectors/python/src/energyatlas/client.py:1821 |
| parse_job | parse_job(payload: dict[str, Any]) -> ZoneSimulationJobResponse | Validate a ``GET /api/zoneSimulation/job/{jobId}`` payload. | Connectors/python/src/energyatlas/client.py:1827 |

### `zones`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| extract | extract(*, entry_name: str, source: str = 'projectArtifact', project_id: Optional[str] = None, force_regenerate: bool = False, overwrite_existing: bool = False) -> dict[str, Any] | ``POST /api/zones/extract`` — populate the server-side zone registry. | Connectors/python/src/energyatlas/client.py:1334 |
| list | list(*, building_id: Optional[str] = None, page: int = 0, page_size: int = 100) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1355 |
| list_definitions | list_definitions(*, page: int = 0, page_size: int = 100) -> dict[str, Any] | ``GET /api/zones/definitions`` — export full portable zone definitions. | Connectors/python/src/energyatlas/client.py:1367 |
| export_definitions | export_definitions(zone_ids: Optional[Iterable[str]] = None) -> dict[str, Any] | ``POST /api/zones/definitions/export``. | Connectors/python/src/energyatlas/client.py:1380 |
| get | get(zone_id: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1393 |
| get_definition | get_definition(zone_id: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1398 |
| for_building | for_building(building_id: str) -> dict[str, Any] |  | Connectors/python/src/energyatlas/client.py:1403 |
| patch | patch(zone_id: str, patch: dict[str, Any], *, base_model_ref: Optional[ZoneModelRef] = None, project_id: Optional[str] = None) -> dict[str, Any] | ``PATCH /api/zones/{zoneId}`` — single resource update (one JSON object). | Connectors/python/src/energyatlas/client.py:1408 |
| batch_patch | batch_patch(patches: Iterable[ZonePatch \| dict[str, Any]], *, base_model_ref: Optional[ZoneModelRef] = None, project_id: Optional[str] = None) -> dict[str, Any] | ``POST /api/zones/batchPatch`` — list-of-objects payload for bulk edits. | Connectors/python/src/energyatlas/client.py:1427 |
| import_definitions | import_definitions(definitions: Iterable[ZoneDefinition \| ZoneFullDefinition \| dict[str, Any]], *, source_entry_name: Optional[str] = None, base_model_ref: Optional[ZoneModelRef] = None, extract_if_missing: bool = True) -> dict[str, Any] | ``POST /api/zones/importDefinitions`` — load zone definitions into registry. | Connectors/python/src/energyatlas/client.py:1444 |

## Workflow Orchestration

### `SetupInputs`

_None found._

### `ModelInputs`

_None found._

### `SimulationInputs`

_None found._

### `ScenarioInputs`

_None found._

### `ResultsInputs`

_None found._

### `StageReport`

_None found._

### `WorkflowOrchestrator`

| Method | Signature | Doc | Source |
| --- | --- | --- | --- |
| setup_stage | setup_stage(inputs: SetupInputs) -> StageReport |  | Connectors/python/src/energyatlas/workflow.py:149 |
| model_stage | model_stage(inputs: ModelInputs) -> StageReport |  | Connectors/python/src/energyatlas/workflow.py:215 |
| simulation_stage | simulation_stage(inputs: SimulationInputs) -> StageReport |  | Connectors/python/src/energyatlas/workflow.py:260 |
| scenario_stage | scenario_stage(inputs: ScenarioInputs) -> StageReport |  | Connectors/python/src/energyatlas/workflow.py:330 |
| results_stage | results_stage(inputs: ResultsInputs) -> StageReport |  | Connectors/python/src/energyatlas/workflow.py:372 |
| run_full_lifecycle | run_full_lifecycle(*, setup: SetupInputs, model: ModelInputs, simulation: SimulationInputs, scenarios: ScenarioInputs, results: ResultsInputs) -> list[StageReport] | Run all five stages in order. | Connectors/python/src/energyatlas/workflow.py:400 |

## Models and Validation

Models are Pydantic v2 models where extracted from `models.py`; many permit extra fields for backend shape drift.

| Model | Bases | Fields | Source |
| --- | --- | --- | --- |
| WorkflowItemStatus | str, Enum | NOT_STARTED, COMPLETE, RUNNING, SKIPPED, FUTURE | Connectors/python/src/energyatlas/models.py:25 |
| BaseEnvelope | _Base | success: Optional[bool], error: Optional[str], message: Optional[str], raw: dict[str, Any] | Connectors/python/src/energyatlas/models.py:114 |
| CreateProjectRequest | _Base | name: Optional[str], folder: str | Connectors/python/src/energyatlas/models.py:132 |
| OpenProjectRequest | _Base | folder: Optional[str], project_json_path: Optional[str] | Connectors/python/src/energyatlas/models.py:139 |
| SetStatusRequest | _Base | status: WorkflowItemStatus | Connectors/python/src/energyatlas/models.py:146 |
| PersistFilesRequest | _Base | footprint_source: Optional[str], parcel_sources: Optional[list[str]] | Connectors/python/src/energyatlas/models.py:152 |
| PreviewFromPathRequest | _Base | path: str | Connectors/python/src/energyatlas/models.py:159 |
| SchemaMappingRule | _Base | source: str, target: str, transform: Optional[str], tier: Optional[str] | Connectors/python/src/energyatlas/models.py:169 |
| SaveSchemaRulesRequest | _Base | mappings: list[SchemaMappingRule] | Connectors/python/src/energyatlas/models.py:178 |
| SchemaApplyMappingRequest | _Base | entry_name: str, mappings: list[SchemaMappingRule] | Connectors/python/src/energyatlas/models.py:184 |
| SchemaSaveToDataHubRequest | SchemaApplyMappingRequest | output_entry_name: str | Connectors/python/src/energyatlas/models.py:191 |
| LoadArchetypesRequest | _Base | folders: list[str] | Connectors/python/src/energyatlas/models.py:201 |
| WeatherDiskRequest | _Base | file_path: str | Connectors/python/src/energyatlas/models.py:211 |
| WeatherImportRequest | _Base | sample_entry_name: str | Connectors/python/src/energyatlas/models.py:217 |
| SimulationOptions | _Base | deg_parallelism: Optional[int], iterations: Optional[int], chunk_size: Optional[int], write_csv: Optional[bool], report_hourly: Optional[bool], plot_graphs: Optional[bool], result_name: Optional[str] | Connectors/python/src/energyatlas/models.py:227 |
| SimulationRunRequest | _Base | weather_entry_name: str, entry_name: Optional[str], feature_collection: Optional[dict[str, Any]], defaults: Optional[dict[str, Any]], scenario_entry_name: Optional[str], scenario_json: Optional[str], options: Optional[SimulationOptions], dashboard_name: Optional[str] | Connectors/python/src/energyatlas/models.py:243 |
| SimulationPreflightRequest | _Base | entry_name: Optional[str], feature_collection: Optional[dict[str, Any]], defaults: Optional[dict[str, Any]] | Connectors/python/src/energyatlas/models.py:260 |
| LoadMeasuresRequest | _Base | folders: list[str] | Connectors/python/src/energyatlas/models.py:272 |
| MeasureSaveRequest | _Base | category_id: str, entry_name: str, is_new: bool, measure_json: str | Connectors/python/src/energyatlas/models.py:278 |
| WorkflowItemState | _Base | status: Optional[WorkflowItemStatus], user_data: dict[str, Any] | Connectors/python/src/energyatlas/models.py:295 |
| WorkflowStatesResponse | _Base | loaded: bool, states: dict[str, dict[str, Any]] | Connectors/python/src/energyatlas/models.py:302 |
| Schedule1Polymorphic | _Base | type_name: Literal['Schedule1'], name: Optional[str], value: float, active_value: Optional[float] | Connectors/python/src/energyatlas/models.py:332 |
| Schedule24Polymorphic | _Base | type_name: Literal['Schedule24'], values: list[float] | Connectors/python/src/energyatlas/models.py:341 |
| Schedule365Polymorphic | _Base | type_name: Literal['Schedule365'], name: Optional[str], active_value: Optional[float], dst: Optional[bool], dst_start: Optional[int], dst_end: Optional[int], day_schedules: list[Schedule24Polymorphic \| dict[str, Any]], day_schedule_indices: list[int], hourly: Optional[list[float]] | Connectors/python/src/energyatlas/models.py:348 |
| ScheduledValuePolymorphic | _Base | type_name: Literal['ScheduledValue'], value: float, schedule: SchedulePolymorphic \| dict[str, Any] | Connectors/python/src/energyatlas/models.py:365 |
| DomesticHotWaterPolymorphic | _Base | type_name: Literal['DomesticHotWater'], water_inlet_temperature: Optional[SchedulePolymorphic \| dict[str, Any]], water_supply_temperature: Optional[SchedulePolymorphic \| dict[str, Any]], hot_water_flow_rate_per_person: Optional[ScheduledValuePolymorphic \| dict[str, Any]], fuel_type: Optional[str], cop: Optional[float] | Connectors/python/src/energyatlas/models.py:373 |
| ZoneLoadsPolymorphic | _Base | type_name: Optional[str], name: Optional[str], building_type: Optional[str], area_weight: Optional[float], volumn_weight: Optional[float], vent_ach: Optional[float], vent_outdoor_air_per_person: Optional[float], vent_outdoor_air_per_area: Optional[float], heat_gain_per_person: Optional[float], moisture_gain_per_person: Optional[float], illuminance_target: Optional[float], lighting_utilisation_factor: Optional[float], ... +8 more | Connectors/python/src/energyatlas/models.py:390 |
| ZoneSimulationInputs | _Base | program: Optional[str], grouping: Optional[str], time_shift: Optional[int], construction: Optional[dict[str, Any]], systems: Optional[dict[str, Any]], loads: Optional[ZoneLoadsPolymorphic \| dict[str, Any]], source_feature: Optional[dict[str, Any]] | Connectors/python/src/energyatlas/models.py:421 |
| ZoneReferenceSummary | _Base | zone_id: str, building_id: Optional[str], model_version: Optional[str], floor_area: Optional[float], room_volume: Optional[float], program: Optional[str], grouping: Optional[str], has_patches: Optional[bool], has_schedule_overrides: Optional[bool], spaceload_name: Optional[str] | Connectors/python/src/energyatlas/models.py:433 |
| ZoneFullDefinition | _Base | zone_id: Optional[str], building_id: Optional[str], source_entry_name: Optional[str], source_feature: Optional[dict[str, Any]], simulation_inputs: Optional[ZoneSimulationInputs \| dict[str, Any]], patch: dict[str, Any], schedule_overrides: dict[str, SchedulePolymorphic \| ZoneScheduleObject \| dict[str, Any]] | Connectors/python/src/energyatlas/models.py:448 |
| ZoneModelRef | _Base | entry_name: str, source: str | Connectors/python/src/energyatlas/models.py:465 |
| ZoneExtractOptions | _Base | force_regenerate: bool, overwrite_existing: bool | Connectors/python/src/energyatlas/models.py:476 |
| ZoneExtractRequest | _Base | base_model_ref: ZoneModelRef, project_id: Optional[str], options: Optional[ZoneExtractOptions] | Connectors/python/src/energyatlas/models.py:481 |
| ZoneSelection | _Base | zone_ids: list[str] | Connectors/python/src/energyatlas/models.py:489 |
| ZonePatch | _Base | zone_id: str, patch: dict[str, Any] | Connectors/python/src/energyatlas/models.py:495 |
| ZoneDefinition | _Base | zone_id: str, building_id: Optional[str], source_entry_name: Optional[str], model_version: Optional[str], patch: dict[str, Any], schedule_overrides: dict[str, ZoneScheduleObject \| dict[str, Any]] | Connectors/python/src/energyatlas/models.py:506 |
| ZoneDefinitionExportRequest | _Base | zone_ids: list[str] | Connectors/python/src/energyatlas/models.py:528 |
| ZonePatchRequest | _Base | patch: dict[str, Any], base_model_ref: Optional[ZoneModelRef], project_id: Optional[str] | Connectors/python/src/energyatlas/models.py:534 |
| ZoneBatchPatchRequest | _Base | patches: list[ZonePatch], base_model_ref: Optional[ZoneModelRef], project_id: Optional[str] | Connectors/python/src/energyatlas/models.py:542 |
| ZoneDefinitionsImportOptions | _Base | extract_if_missing: bool | Connectors/python/src/energyatlas/models.py:550 |
| ZoneDefinitionsImportRequest | _Base | definitions: list[ZoneDefinition], source_entry_name: Optional[str], base_model_ref: Optional[ZoneModelRef], options: Optional[ZoneDefinitionsImportOptions] | Connectors/python/src/energyatlas/models.py:554 |
| ZoneScheduleObject | _Base | kind: ScheduleKind, name: Optional[str], value: Optional[float], values: Optional[list[float]], weekday: Optional[list[float]], weekend: Optional[list[float]], saturday: Optional[list[float]], sunday: Optional[list[float]], hourly: Optional[list[float]], timezone: Optional[str] | Connectors/python/src/energyatlas/models.py:566 |
| ZoneSchedulePutRequest | _Base | schedule: ZoneScheduleObject, base_model_ref: Optional[ZoneModelRef], project_id: Optional[str] | Connectors/python/src/energyatlas/models.py:594 |
| ZoneSchedulePatch | _Base | zone_id: str, schedule_type: ScheduleType, schedule: ZoneScheduleObject | Connectors/python/src/energyatlas/models.py:602 |
| ZoneScheduleBatchUpdateRequest | _Base | updates: list[ZoneSchedulePatch], base_model_ref: Optional[ZoneModelRef], project_id: Optional[str] | Connectors/python/src/energyatlas/models.py:610 |
| ZoneWeatherRef | _Base | weather_entry_name: str | Connectors/python/src/energyatlas/models.py:621 |
| ZoneRunOptions | _Base | deg_parallelism: Optional[int], iterations: Optional[int], chunk_size: Optional[int], report_hourly: Optional[bool], write_csv: Optional[bool] | Connectors/python/src/energyatlas/models.py:625 |
| ZoneSchedulePatchSpec | _Base | schedule_type: ScheduleType, schedule: ZoneScheduleObject | Connectors/python/src/energyatlas/models.py:640 |
| ZoneSimulationRun | _Base | run_id: str, zone_selection: ZoneSelection | Connectors/python/src/energyatlas/models.py:647 |
| ZoneSimulationRunRequest | _Base | runs: list[ZoneSimulationRun], weather: ZoneWeatherRef, base_model_ref: Optional[ZoneModelRef], project_id: Optional[str], run_options: Optional[ZoneRunOptions], execution_mode: Literal['sync', 'async'], source_entry_name: Optional[str], zone_definitions: list[ZoneDefinition \| ZoneFullDefinition] | Connectors/python/src/energyatlas/models.py:654 |
| ZoneBatchSimulationBatch | _Base | batch_id: Optional[str], runs: list[ZoneSimulationRun] | Connectors/python/src/energyatlas/models.py:667 |
| ZoneBatchSimulationRequest | _Base | batch: ZoneBatchSimulationBatch, weather: ZoneWeatherRef, base_model_ref: Optional[ZoneModelRef], project_id: Optional[str], run_options: Optional[ZoneRunOptions], source_entry_name: Optional[str], zone_definitions: list[ZoneDefinition \| ZoneFullDefinition] | Connectors/python/src/energyatlas/models.py:672 |
| StandaloneZoneSimulationRequest | _Base | zone: Optional[ZoneFullDefinition], zones: list[ZoneFullDefinition], weather: ZoneWeatherRef, run_options: Optional[ZoneRunOptions], execution_mode: Literal['sync', 'async'], source_entry_name: Optional[str] | Connectors/python/src/energyatlas/models.py:684 |
| StandaloneZoneSimulationResponse | _Base | success: bool, mode: Optional[str], job_id: Optional[str], generated_zone_ids: list[str], status_url: Optional[str], results: Optional[list[ZoneSimulationResult \| dict[str, Any]]] | Connectors/python/src/energyatlas/models.py:695 |
| ZoneSimulationResult | _Base | run_id: Optional[str], zone_id: Optional[str], heating_fuel: Optional[str], cooling_fuel: Optional[str], hot_water_fuel: Optional[str], gas_equipment_fuel: Optional[str], auxiliary_fuel: Optional[str], heating_load_wh: list[float], heating_energy_wh: list[float], cooling_load_wh: list[float], cooling_energy_wh: list[float], water_heating_load_wh: list[float], ... +18 more | Connectors/python/src/energyatlas/models.py:709 |
| ZoneRunSummary | _Base | run_id: str, zone_ids: list[str], status: str, error: Optional[str], warnings: list[str], results: Optional[list[ZoneSimulationResult]] | Connectors/python/src/energyatlas/models.py:751 |
| ZoneSimulationJobResponse | _Base | success: bool, job_id: str, batch_id: Optional[str], status: str, total_runs: int, completed_runs: int, failed_runs: int, runs: list[ZoneRunSummary] | Connectors/python/src/energyatlas/models.py:762 |
| ZoneBatchSimulationResult | _Base | job_id: str, batch_id: Optional[str], status: str, runs: list[ZoneRunSummary] | Connectors/python/src/energyatlas/models.py:775 |
| SensorGenOptions | _Base | spacing: float, vertical_spacing: float, vertical_offset: float, normal_offset: float, facade_normal_offset: float, generate_on_facade: bool | Connectors/python/src/energyatlas/models.py:788 |
| VoxelShadingCalcParams | _Base | calc_update_freq: int, time_step: int, calculation_radius: float, sky_dome_samples: int, horizon_samples: int, calculate_for_diffuse: bool, summarize_hourly: bool, time_zone: Optional[float] | Connectors/python/src/energyatlas/models.py:799 |
| GenerateSensorsRequest | _Base | voxel_cache_dir: str, sensor_out_dir: str, gen_opt: SensorGenOptions, resolution: float, padding_distance: float | Connectors/python/src/energyatlas/models.py:812 |
| CalculateShadingRequest | _Base | voxel_cache_dir: str, sensor_dir: str, shading_out_dir: str, latitude: Optional[float], longitude: Optional[float], calc_params: VoxelShadingCalcParams, resolution: float, padding_distance: float | Connectors/python/src/energyatlas/models.py:822 |
| VoxelizationSettingModel | _Base | resolution: float, padding_distance: float, k_neighbors: int, fill_hole_with_mean_edge_elevation: bool, resume_cache_exists_only: bool, absorb_building_buffer_steps: Optional[int] | Connectors/python/src/energyatlas/models.py:839 |
| TileSlicerSettingModel | _Base | tile_size_x: Optional[float], tile_size_y: Optional[float] | Connectors/python/src/energyatlas/models.py:854 |
| VoxelizeRequest | _Base | lidar_files: list[str], footprint_file: str, output_dir: str, setting: VoxelizationSettingModel, slicer_setting: TileSlicerSettingModel | Connectors/python/src/energyatlas/models.py:861 |
| VoxelPreviewRequest | _Base | voxel_cache_dir: str, max_points: int, tile_key: Optional[str], classes: Optional[list[str]] | Connectors/python/src/energyatlas/models.py:871 |
| SensorPreviewRequest | _Base | sensor_dir: str, max_points: int, tile_key: Optional[str], include_normals: bool | Connectors/python/src/energyatlas/models.py:880 |
| ShadingPreviewRequest | _Base | shading_dir: str, max_points: int, tile_key: Optional[str], sunlit_index: Optional[int] | Connectors/python/src/energyatlas/models.py:889 |

## Exceptions

| Exception | Bases | Source |
| --- | --- | --- |
| EnergyAtlasError | Exception | Connectors/python/src/energyatlas/errors.py:8 |
| InstanceNotFoundError | EnergyAtlasError | Connectors/python/src/energyatlas/errors.py:12 |
| ApiRequestError | EnergyAtlasError | Connectors/python/src/energyatlas/errors.py:16 |
| ProjectNotLoadedError | EnergyAtlasError | Connectors/python/src/energyatlas/errors.py:43 |
| JobFailedError | EnergyAtlasError | Connectors/python/src/energyatlas/errors.py:47 |
| JobTimeoutError | EnergyAtlasError | Connectors/python/src/energyatlas/errors.py:55 |
| ValidationFailedError | EnergyAtlasError | Connectors/python/src/energyatlas/errors.py:63 |

## Public Exports

`EnergyAtlasClient`, `EnergyAtlasBackend`, `WorkflowOrchestrator`, `discover_base_url`, `DiscoveredInstance`, `EnergyAtlasError`, `ProjectNotLoadedError`, `ApiRequestError`, `InstanceNotFoundError`, `JobFailedError`, `JobTimeoutError`, `WorkflowItemStatus`, `WORKFLOW_ITEM_IDS`, `STAGE_TO_ITEM_IDS`, `CreateProjectRequest`, `OpenProjectRequest`, `SetStatusRequest`, `PersistFilesRequest`, `LoadArchetypesRequest`, `LoadMeasuresRequest`, `MeasureSaveRequest`, `PreviewFromPathRequest`, `WeatherDiskRequest`, `WeatherImportRequest`, `SchemaMappingRule`, `SaveSchemaRulesRequest`, `SchemaApplyMappingRequest`, `SimulationRunRequest`, `SimulationOptions`, `BaseEnvelope`, `VoxelPreviewRequest`, `SensorPreviewRequest`, `ShadingPreviewRequest`, `ScheduleType`, `ScheduleKind`, `Schedule1Polymorphic`, `Schedule24Polymorphic`, `Schedule365Polymorphic`, `SchedulePolymorphic`, `ScheduledValuePolymorphic`, `DomesticHotWaterPolymorphic`, `ZoneLoadsPolymorphic`, `ZoneSimulationInputs`, `ZoneReferenceSummary`, `ZoneModelRef`, `ZoneExtractOptions`, `ZoneExtractRequest`, `ZoneSelection`, `ZonePatch`, `ZoneFullDefinition`, `ZoneDefinition`, `ZoneDefinitionExportRequest`, `ZonePatchRequest`, `ZoneBatchPatchRequest`, `ZoneDefinitionsImportOptions`, `ZoneDefinitionsImportRequest`, `ZoneScheduleObject`, `ZoneSchedulePutRequest`, `ZoneSchedulePatch`, `ZoneScheduleBatchUpdateRequest`, `ZoneWeatherRef`, `ZoneRunOptions`, `ZoneSchedulePatchSpec`, `ZoneSimulationRun`, `ZoneSimulationRunRequest`, `ZoneBatchSimulationBatch`, `ZoneBatchSimulationRequest`, `StandaloneZoneSimulationRequest`, `StandaloneZoneSimulationResponse`, `ZoneSimulationResult`, `ZoneRunSummary`, `ZoneSimulationJobResponse`, `ZoneBatchSimulationResult`

## Examples

| Path | Description |
| --- | --- |
| Connectors/python/examples/_example_defaults.py | Shared default paths/settings for example scripts. |
| Connectors/python/examples/_voxel_shading_example_common.py | Shared utilities for voxel-shading connector examples. |
| Connectors/python/examples/_voxel_shading_visualization.py | Plotly helpers for voxel-shading preview payloads. |
| Connectors/python/examples/load_archetypes_and_print_counts.py | Load archetypes from folder(s) and print per-archetype component counts. |
| Connectors/python/examples/load_weather_and_print.py | Load weather from a local EPW file, then print its content from the API. |
| Connectors/python/examples/run_export_zone_definitions.py | Build model inputs and export zone JSON definitions. |
| Connectors/python/examples/run_extract_zones_preview.py | Run setup+model workflow, extract zones, preview first definitions. |
| Connectors/python/examples/run_full_lifecycle.py | End-to-end sample script for the EnergyAtlas Python connector. |
| Connectors/python/examples/run_lidar_voxelization_nyc.py | Run LiDAR voxelization for the bundled NYC fixture. |
| Connectors/python/examples/run_shading_calculation_nyc.py | Calculate shading for generated NYC sensor tiles. |
| Connectors/python/examples/run_shading_sensor_generation_nyc.py | Generate shading sensors from an NYC voxel cache. |
| Connectors/python/examples/run_voxel_shading_nyc.py | Run the full NYC voxel-shading pipeline through the Python connector. |
| Connectors/python/examples/run_zone_sim_from_definitions.py | Run definition-first zone simulation from full definition JSON. |
| Connectors/python/examples/voxel_shading_nyc_workflow.ipynb | Notebook example |
| Connectors/python/examples/zone_sim_standalone_simple_demo.ipynb | Notebook example |

## Tests and Validation

| Kind | Path |
| --- | --- |
| test | Connectors/python/tests/test_backend.py |
| test | Connectors/python/tests/test_connection.py |
| test | Connectors/python/tests/test_http_transport.py |
| test | Connectors/python/tests/test_models.py |
| test | Connectors/python/tests/test_voxel_shading_client.py |
| test | Connectors/python/tests/test_voxel_shading_e2e.py |
| test | Connectors/python/tests/test_voxel_shading_e2e_config.py |
| test | Connectors/python/tests/test_voxel_shading_examples.py |
| test | Connectors/python/tests/test_voxel_shading_models.py |
| test | Connectors/python/tests/test_voxel_shading_voxelize_e2e.py |
| test | Connectors/python/tests/test_voxel_shading_voxelize_e2e_config.py |
| runner | TestRunners/run-py-connector-tests-invoke-backend.bat |
| runner | TestRunners/run-py-connector-tests-invoke-backend.sh |
| runner | TestRunners/run-py-connector-tests-no-backend.bat |
| runner | TestRunners/run-py-connector-tests-no-backend.sh |
| runner | TestRunners/run_py_connector_tests_invoke_backend.py |

```powershell
cd Connectors/python
python -m pytest -q -rs
```

## Known Limitations and Cautions

- The Python connector is synchronous; no async public client is extracted from source.
- The public PyPI name 'energyatlas' must be verified before recommending plain 'pip install energyatlas'.
- Discovery and TLS defaults are source-derived and should be rechecked after connector changes.
- Some backend endpoints may intentionally have no Python wrapper; compare this doc with `web-api-reference.md` when full route coverage matters.
