"""Structural tests for the live LikeC4 diagrams in the Architecture subspace.

These run without a generated viewer bundle, so they gate the source of truth: that every
embedded view exists in the LikeC4 project, that every view in the project is reachable, and
that the page and theme wiring needed to render a diagram is actually present.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
ARCHITECTURE_DOCS = ROOT / "docs" / "architecture"
LIKEC4 = ROOT / "architecture" / "likec4"

VIEW_DEFINITION = re.compile(r"^\s*view\s+([A-Za-z][A-Za-z0-9_]*)\b", re.MULTILINE)
NAVIGATE_TO = re.compile(r"\bnavigateTo\s+([A-Za-z][A-Za-z0-9_]*)")
EMBEDDED_VIEW = re.compile(r'<likec4-view\s+view-id="([^"]+)"([^>]*)>')
IMAGE_REFERENCE = re.compile(r"!\[[^\]]*\]\([^)]+\)|<img\b", re.IGNORECASE)

# Views published on their own page. Everything else is reached by drilldown.
PRIMARY_VIEWS = {
    "index": "index.md",
    "simulationDataFlow": "simulation-data-flow.md",
    "scenarioSimulationView": "scenario-simulation.md",
    "postHocScenarioMixerView": "post-hoc-scenario-mixer.md",
}


def likec4_source() -> str:
    return "\n".join(
        path.read_text(encoding="utf-8") for path in sorted(LIKEC4.rglob("*.c4"))
    )


def defined_views() -> set[str]:
    return set(VIEW_DEFINITION.findall(likec4_source()))


def architecture_pages() -> list[Path]:
    return sorted(ARCHITECTURE_DOCS.glob("*.md"))


def front_matter(page: Path) -> dict[str, object]:
    text = page.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    return yaml.safe_load(text.split("---\n", 2)[1]) or {}


def embedded_views(page: Path) -> list[tuple[str, str]]:
    return EMBEDDED_VIEW.findall(page.read_text(encoding="utf-8"))


def test_every_embedded_view_exists_in_the_likec4_project():
    available = defined_views()
    missing = [
        f"{page.name} -> {view_id}"
        for page in architecture_pages()
        for view_id, _ in embedded_views(page)
        if view_id not in available
    ]

    assert not missing, "\n".join(missing)


def test_each_primary_view_is_published_on_exactly_one_page():
    published = Counter(
        view_id for page in architecture_pages() for view_id, _ in embedded_views(page)
    )

    assert published == Counter(PRIMARY_VIEWS.keys())
    for view_id, page_name in PRIMARY_VIEWS.items():
        page = ARCHITECTURE_DOCS / page_name
        assert page.is_file()
        assert view_id in [embedded for embedded, _ in embedded_views(page)]


def test_every_view_in_the_project_is_reachable_from_a_published_page():
    """No unused architectural inventory: a view is either published or drilled into."""
    reachable = set(PRIMARY_VIEWS) | set(NAVIGATE_TO.findall(likec4_source()))

    assert defined_views() - reachable == set()


def test_diagram_pages_declare_the_flags_that_load_the_viewer():
    for page in architecture_pages():
        meta = front_matter(page)
        assert meta.get("likec4") is True, page.name
        assert meta.get("full_width") is True, page.name


def test_embedded_views_enable_the_interactive_browser():
    for page in architecture_pages():
        for view_id, attributes in embedded_views(page):
            assert 'browser="true"' in attributes, f"{page.name} -> {view_id}"


def test_theme_loads_the_viewer_only_for_flagged_pages():
    base = (ROOT / "theme" / "base.html").read_text(encoding="utf-8")

    assert "{% if page and page.meta and page.meta.likec4 %}" in base
    assert "'assets/js/likec4-views.js' | url" in base
    assert "'assets/js/likec4-embed.js' | url" in base


def test_embed_script_syncs_the_wiki_theme_into_the_diagrams():
    embed = (ROOT / "docs" / "assets" / "js" / "likec4-embed.js").read_text(encoding="utf-8")

    assert "energyatlas-theme-change" in embed
    assert "color-scheme" in embed
    assert "EnergyAtlasTheme" in embed


def test_architecture_pages_ship_no_diagram_images():
    """Diagrams are published live. A PNG export must never reappear."""
    offenders = [
        page.name
        for page in architecture_pages()
        if IMAGE_REFERENCE.search(page.read_text(encoding="utf-8"))
    ]

    assert not offenders
    assert not list(ARCHITECTURE_DOCS.rglob("*.png"))
    assert not list(ARCHITECTURE_DOCS.rglob("*.svg"))


def test_generated_viewer_artifacts_are_not_tracked_in_git():
    ignored = (ROOT / "architecture" / ".gitignore").read_text(encoding="utf-8")
    root_ignored = (ROOT / ".gitignore").read_text(encoding="utf-8")

    assert "node_modules/" in ignored
    assert "likec4/.likec4/" in ignored
    assert "docs/assets/js/likec4-views.js" in root_ignored
