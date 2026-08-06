# Architecture diagram style

## Scope and composition

- Each primary view answers one architectural question.
- Prefer 5–12 responsibility-level elements and no more than three meaningful boundaries.
- Combine classes that collectively implement one responsibility.
- Use short public-facing titles, brief descriptions, and verb-phrase relationship labels.
- Prefer top-to-bottom layout for hierarchical flows and left-to-right layout for compact
  processing flows.
- Compose on a grid of aligned ranks with whitespace reserved for relationship routing.
  Establish the primary reading order before adding secondary relationships.
- Separate primary simulation flow from secondary persistence, aggregation, export, and
  observability flows. Keep primary flow visually stronger and shorter than the rest.

## Containers, cards, and colour

- Draw containment as pale, solid-bordered structural frames with visible top-left labels.
  Parent frames are lighter than child frames and remain quieter than work cards. No
  container should become the most visually dominant object merely because it is large.
- Prefer compact rectangular cards. Keep explanatory descriptions in the model for
  interactive inspection, but use title-only cards when prose would enlarge the view.
- Use a restrained semantic palette: cool pale frames for structure, one accent family for
  processing, amber for external inputs, green for results, and neutral relationships. Do not
  rely on colour alone to communicate meaning; shape is the second cue.
- Use icons only when they are already available, public-safe, stylistically consistent, and
  meaningfully improve recognition. A labelled card is the safe default.
- LikeC4 does not allow a direct relationship between a container and its immediate child.
  Convey parent-to-child delegation through concise container labels and model descriptions.

## Connectors

- Relationship connectors travel only horizontally and vertically, joined by rounded
  90-degree elbows. They attach at cardinal points, carry short labels on straight portions,
  and cross rarely.
- This geometry comes from `tools/orthogonal-router`, not from LikeC4's own layout, which
  produces curved diagonal splines. Regenerate the snapshots after any model or view edit and
  before publishing; a stale snapshot silently keeps the old routing.
- Only describe routes as strictly orthogonal while the router's geometry check passes with
  zero violations. If it reports a fallback edge, that edge kept its original spline and must
  be described as such.

## Interaction

Published views are live, not images. Design for the interaction as well as the still frame:

- Keep a description on every element worth inspecting; the rendered card may be title-only,
  but the description is what a reader sees when they click it.
- Give a collapsed system a `navigateTo` target whenever a detail view exists, so drilldown
  is available from the diagram itself rather than only from the page text.
- Detail views should stand alone. A reader can arrive at one directly through drilldown
  without having read the page that hosts its parent.

## Review checklist

Compare a view at normal Wiki width against these checks:

1. The reading order is apparent before relationship labels are read.
2. The largest filled area is not the strongest visual element.
3. Nested boundaries remain distinguishable without saturated fills.
4. Cards and labels remain legible without excessive zoom.
5. Primary relationships are shorter and clearer than secondary relationships.
6. The router reported zero violations and zero fallback edges.
7. Every drilldown target resolves, and the back path returns to the hosting view.

## Public-content rules

- Do not include unused elements, unpublished and unreachable views, private provenance,
  source paths, repository names, or investigation notes.
- Use implementation class names only when a published page genuinely needs them and they are
  suitable for public documentation.
- Treat the complete LikeC4 project — not only what a given view renders — as public content.
  Every element, description, relationship, and comment ships in the viewer bundle.
- Never generate, reference, or commit a diagram image. Views are published live.
