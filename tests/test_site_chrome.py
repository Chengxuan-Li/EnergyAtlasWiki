from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_base_template_uses_topbar_icon_as_svg_favicon():
    base = read("theme/base.html")

    favicon = '<link rel="icon" type="image/svg+xml" href="{{ \'assets/images/icon.svg\' | url }}" />'
    topbar_icon = '<img class="wiki-topbar-icon" src="{{ \'assets/images/icon.svg\' | url }}"'

    assert favicon in base
    assert topbar_icon in base
    assert base.index(favicon) < base.index("{% for path in config.extra_css %}")
