---
full_width: true
likec4: true
---

# Post-hoc Scenario Mixer

How persisted annual results and modeling parameters produce a real-time scenario mixture and
a WebUI style update, without re-running a simulation.

<figure class="likec4-figure">
  <div class="likec4-figure-canvas">
    <likec4-view view-id="postHocScenarioMixerView" browser="true"></likec4-view>
  </div>
  <noscript><p class="likec4-figure-fallback">This diagram requires JavaScript. The sections
  below describe the same flow in text.</p></noscript>
  <figcaption>Result Tables appear as a single collapsed card here; drill into it to see the
  underlying tables. Input and WebUI sit outside the Scenario Mixer boundary.</figcaption>
  <p class="likec4-figure-hint">Tap the diagram to open it full screen.</p>
</figure>

## Why post-hoc

Scenario simulation persists annual results for every building in every scenario. The mixer
works from that persisted data, so exploring a different mixture of scenarios is a query and
an aggregation rather than a new simulation run. That is what makes the interaction
real-time.

## Inputs

Two things enter the mixer.

The **Site Energy Result Table** supplies building identifiers and annual results. Inside the
mixer these become **SiteEnergyResult**, drawn as a stacked card because one exists per
building.

**Input** supplies modeling parameters, and the **WebUI** issues API calls carrying mixer
parameters.

## Choice model and mixture selection

The **Choice Model** converts modeling parameters and API requests into mixer parameters.
**Modeled Mixture Selection** applies those parameters to the modeled scenario mixture,
drawing on the annual per-building results.

## Response

Modeled Mixture Selection produces **Scenario Results** by real-time aggregation. The API
response returns to the WebUI and triggers a style update, so the map reflects the selected
mixture immediately.

## Related views

- [Scenario Simulation](scenario-simulation.md) produces and persists the annual results this
  view consumes.
- [Simulation Stages and Data Flow](simulation-data-flow.md) shows the aggregation that
  produces a site energy result in the first place.
