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
        "  - Python:",
        "  - WebAPI:",
        "  - Library:",
        "  - User Stories:",
        "  - Wiki Guide:",
    ]

    positions = [config.index(heading) for heading in headings]
    assert positions == sorted(positions)
    assert "EnergyAtlas References" not in config


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
