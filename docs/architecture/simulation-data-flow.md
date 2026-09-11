---
full_width: true
likec4: true
---

# Simulation Stages and Data Flow

The baseline path through EnergyAtlas: from GeoJSON ingestion, through domain construction
and thermal simulation, to aggregation, persistence, and GIS export.

<figure class="likec4-figure">
  <div class="likec4-figure-canvas">
    <likec4-view view-id="simulationDataFlow" browser="true"></likec4-view>
  </div>
  <noscript><p class="likec4-figure-fallback">This diagram requires JavaScript. The sections
  below describe the same flow in text.</p></noscript>
  <figcaption>The UBEM boundary holds the processing stages. Inputs enter from the left;
  persistence and GIS export sit on the right. Drill into Inputs, Feature2Building, Precompute
  Boundary Conditions, Results Aggregation, or any table group.</figcaption>
  <p class="likec4-figure-hint">Tap the diagram to open it full screen.</p>
</figure>

## Ingestion and preprocessing

Input GeoJSON supplies the source geospatial features. **Preprocessing** performs schema
matching, geometric preprocessing, and archetype assignment, then emits preprocessed features
to Feature2Building and processed collection data to the GIS Properties Table.

## Feature2Building

**Feature2Building (F2B)** constructs the simulation domain from a preprocessed feature.

The Feature emits three archetype assignments — construction, systems, and energy loads — and
supplies geometric information to the Building. The Building owns Zones, and Zones own Faces.

Each archetype then flows to the component it characterises. The Construction Archetype
supplies thermal mass and infiltration rate to ZoneConstruction, and U-value and
window-to-wall ratio to Face material info. The Systems Archetype supplies conditioning
systems, and the Energy Loads Archetype supplies schedules.

Building and Zone definitions are written to the Definition Tables, with zone definitions
carrying their energy-load time series.

Drill into Feature2Building to see this structure, and from there into Zones or Faces.

## Simulation

**Precompute Boundary Conditions** resolves zone-local weather from site weather and zone
context, computes face radiation, and assembles the boundary conditions Zone5R1C consumes. It
also writes boundary results to the Zone Result Table.

**Zone5R1C Simulation** runs the prepared zone objects against weather input and emits a
ZoneResult.

**Results Aggregation** rolls zone results into building results and building results into a
site energy result.

## Persistence and export

Result Tables persist zone, building, and site energy results. GIS Tables hold processed
feature properties from preprocessing and a selective GIS projection of site energy results.
Both GIS tables export to Results GeoJSON.

## Related views

- [Scenario Simulation](scenario-simulation.md) shows how this same pipeline is replicated
  per scenario alongside a baseline.
- [Post-hoc Scenario Mixer](post-hoc-scenario-mixer.md) shows what happens to the persisted
  site energy results afterwards.
