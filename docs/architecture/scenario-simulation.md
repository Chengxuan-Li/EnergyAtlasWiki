---
full_width: true
likec4: true
---

# Scenario Simulation

How scenario definitions become parallel simulation runs: from processed features and scenario
mappings, through building upgrades and copied simulation instances, to persistence and GIS
export.

<figure class="likec4-figure">
  <div class="likec4-figure-canvas">
    <likec4-view view-id="scenarioSimulationView" browser="true"></likec4-view>
  </div>
  <noscript><p class="likec4-figure-fallback">This diagram requires JavaScript. The sections
  below describe the same flow in text.</p></noscript>
  <figcaption>Simulation is drawn as a stacked card because one instance exists per scenario.
  Drill into it to see the stages inside, or into Feature2Building and the table groups.
  </figcaption>
  <p class="likec4-figure-hint">Tap the diagram to open it full screen.</p>
</figure>

## Scenario mappings

Preprocessing feeds **Scenario Mappings**, which applies measure packages according to
selection criteria, once per scenario. It is drawn as a stacked card for that reason.

## Building upgrade scenarios

**Building Upgrade Scenarios** are copies of the Building produced by Feature2Building, with
scenario selections and measures applied. Feature2Building supplies the copy; Scenario
Mappings supplies the applied selections and scenario measures.

Like Scenario Mappings, this is a stacked card: one set of upgraded buildings exists per
scenario. The upgraded buildings write their definitions to the Definition Tables, so a
scenario's building and zone definitions are persisted alongside the baseline's.

## Parallel simulation instances

Each set of upgraded buildings produces a copy of the simulation instance. The **Baseline**
runs the reference case without scenario upgrades, taking zone geometry and location directly
from Feature2Building.

Baseline and scenario instances are ranked side by side in the diagram to make the parallel
explicit. Drill into Simulation to see the stages each instance runs: precompute boundary
conditions, Zone5R1C, and results aggregation. These are the same stages described in
[Simulation Stages and Data Flow](simulation-data-flow.md).

## Persistence and export

All instances write into the same Result Tables, and site energy results reach GIS Tables as a
selective projection. Results GeoJSON is exported from GIS properties and GIS results, exactly
as in the baseline flow.

Because every scenario's results are persisted rather than held in memory, they remain
available for the [Post-hoc Scenario Mixer](post-hoc-scenario-mixer.md) after the run
finishes.
