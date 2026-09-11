from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_base_template_uses_sidebar_icon_as_svg_favicon():
    base = read("theme/base.html")

    favicon = '<link rel="icon" type="image/svg+xml" href="{{ \'assets/images/icon.svg\' | url }}" />'
    sidebar_icon = '<img class="wiki-sidebar-logo" src="{{ \'assets/images/icon.svg\' | url }}"'

    assert favicon in base
    assert sidebar_icon in base
    assert base.index(favicon) < base.index("{% for path in config.extra_css %}")


def test_base_template_renders_subspace_sidebar_and_attached_toc():
    base = read("theme/base.html")

    assert 'id="wiki-sidebar"' in base
    assert 'id="wiki-sidebar-toggle"' in base
    assert 'id="wiki-space-switcher"' in base
    assert "current_space.item.children" in base
    assert 'class="menu-column menu-column-toc"' in base
    assert 'class="toc-heading">On this page' in base
    assert 'class="wiki-topbar"' not in base


def test_mkdocs_navigation_defines_confirmed_subspaces_in_order():
    config = read("mkdocs.yml")
    headings = [
        "  - Quick Start:",
        "  - Workflows:",
        "  - Architecture:",
        "  - Python:",
        "  - WebAPI:",
        "  - Library:",
        "  - User Stories:",
        "  - Wiki Guide:",
    ]

    positions = [config.index(heading) for heading in headings]
    assert positions == sorted(positions)
    assert "EnergyAtlas References" not in config


def test_subspace_switcher_uses_distinct_icons_without_an_eyebrow_label():
    base = read("theme/base.html")

    assert '<span class="wiki-space-switcher-label">Subspace</span>' not in base
    assert "render_space_icon(current_space.item.title)" in base
    assert "render_space_icon(nav_item.title)" in base
    assert 'class="wiki-space-switcher-option-main"' in base
    assert 'class="wiki-space-switcher-check"' in base
    for icon_name in (
        "quick-start",
        "workflows",
        "architecture",
        "python",
        "web-api",
        "library",
        "user-stories",
        "wiki-guide",
    ):
        assert f"wiki-space-icon-{icon_name}" in base

    for icon_name in (
        "compass",
        "monitor",
        "network",
        "code-xml",
        "library-big",
        "users-round",
        "book-open-text",
    ):
        assert f'data-icon-source="lucide" data-icon-name="{icon_name}"' in base
    assert 'data-icon-source="simple-icons" data-icon-name="python"' in base

    for css_path in ("assets/css/main.css", "docs/assets/css/main.css"):
        css = read(css_path)
        brand_block = css.split(".wiki-sidebar-brand-name,", 1)[1].split("}", 1)[0]
        value_block = css.split(".wiki-space-switcher-value {", 1)[1].split("}", 1)[0]
        assert ".wiki-space-icon {" in css
        assert "font-size: var(--font-size-lg);" in brand_block
        assert "font-size: var(--font-size-base);" in value_block
        assert "width: 24px;" in css
        assert "--wiki-space-switcher-row-height: 56px;" in css
        summary_block = css.split(".wiki-space-switcher-summary {", 1)[1].split("}", 1)[0]
        option_block = css.split(".wiki-space-switcher-option {", 1)[1].split("}", 1)[0]
        assert "font-size: var(--font-size-base);" in option_block
        for block in (summary_block, option_block):
            assert "height: var(--wiki-space-switcher-row-height);" in block
            assert "min-height: var(--wiki-space-switcher-row-height);" in block
        assert ".wiki-space-icon-python {" in css
        assert ".wiki-space-icon-architecture {" in css
        assert "fill: currentColor;" in css
        assert ".wiki-space-switcher-option-main {" in css
        assert ".wiki-space-switcher-check {" in css


def test_wide_tables_use_table_local_horizontal_scrollers():
    base = read("theme/base.html")

    assert "table-scroll-wrapper-wide" in base
    assert "columnCount >= 5" in base
    assert "wrapper.scrollWidth > wrapper.clientWidth" in base
    assert "wrapper.setAttribute('aria-label', 'Scrollable table')" in base

    for css_path in ("assets/css/main.css", "docs/assets/css/main.css"):
        css = read(css_path)
        assert ".table-scroll-wrapper-wide > table" in css
        assert "width: max-content;" in css
        assert "overscroll-behavior-inline: contain;" in css


def test_desktop_sidebar_has_persistent_animated_collapse_control():
    base = read("theme/base.html")
    shell = read("docs/assets/js/wiki-shell.js")

    assert 'id="wiki-sidebar-collapse"' in base
    assert 'aria-controls="wiki-sidebar"' in base
    assert "energyatlas-wiki-sidebar-collapsed" in base
    assert "setDesktopCollapsed" in shell
    assert "syncCollapsedAccessibility" in shell
    assert "energyatlas-wiki-sidebar-collapsed" in shell

    for css_path in ("assets/css/main.css", "docs/assets/css/main.css"):
        css = read(css_path)
        assert ':root[data-sidebar-collapsed="true"] .wiki-sidebar' in css
        assert ':root[data-sidebar-collapsed="true"] .wiki-sidebar-tools' in css
        assert "--wiki-sidebar-tools-collapsed-width: 216px;" in css


def test_scroll_progress_owns_a_separate_full_width_bottom_row():
    base = read("theme/base.html")

    assert 'id="scroll-progress-track"' in base
    assert 'role="progressbar"' in base
    assert 'aria-label="Page scroll progress"' in base
    assert "scrollableHeight > 0" in base
    assert "scrollProgressTrack.setAttribute('aria-valuenow'" in base

    for css_path in ("assets/css/main.css", "docs/assets/css/main.css"):
        css = read(css_path)
        assert "--wiki-scroll-progress-height: 4px;" in css
        assert "bottom: var(--wiki-scroll-progress-height);" in css
        progress_block = css.split(".scroll-progress-bar {", 1)[1].split("}", 1)[0]
        assert "height: var(--wiki-scroll-progress-height);" in progress_block
        assert "z-index: 3800;" in progress_block
