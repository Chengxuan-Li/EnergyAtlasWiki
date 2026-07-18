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
