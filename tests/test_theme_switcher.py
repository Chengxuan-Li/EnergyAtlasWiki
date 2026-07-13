import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_base_template_bootstraps_dark_first_theme_and_renders_toggle():
    base = read("theme/base.html")

    assert "energyatlas-wiki-theme" in base
    assert "document.documentElement.dataset.theme = theme" in base
    assert "theme = 'dark'" in base
    assert 'id="wiki-theme-toggle"' in base
    assert 'aria-pressed="false"' in base
    assert '<span class="wiki-theme-toggle-text">' not in base
    assert "Edit on GitHub" not in base
    assert re.search(r">\s*Edit\s*<", base)
    assert base.index('class="wiki-topbar-left"') < base.index('id="wiki-theme-toggle"')
    assert base.index('id="wiki-theme-toggle"') < base.index('class="wiki-topbar-link"')


def test_main_template_renders_central_page_footer():
    main = read("theme/main.html")

    assert "wiki-page-footer" in main
    assert "Last page update {{ page.meta.page_updated_at or \"Unknown\" }}" in main
    assert "Last website update {{ config.extra.website_updated_at or \"Unknown\" }}" in main
    assert "Found an issue on this page?" in main


def test_theme_script_is_loaded_before_plotly_renderer():
    config = read("mkdocs.yml")

    theme_script = "assets/js/theme-toggle.js"
    plotly_renderer = "assets/js/plotly-render.js"

    assert theme_script in config
    assert config.index(theme_script) < config.index(plotly_renderer)


def test_theme_tokens_exist_in_both_asset_copies():
    for css_path in ("assets/css/main.css", "docs/assets/css/main.css"):
        css = read(css_path)

        assert ':root[data-theme="light"]' in css
        assert "--plotly-font-color" in css
        assert "--theme-toggle-bg" in css
        assert ".wiki-theme-toggle" in css
        assert "width: 32px;" in css
        assert "border-radius: 50%;" in css
        assert '[data-theme="light"] .code-block-body .n' in css


def test_theme_toggle_controller_persists_choice_and_announces_changes():
    script = read("docs/assets/js/theme-toggle.js")

    assert "energyatlas-wiki-theme" in script
    assert "localStorage.setItem" in script
    assert "aria-pressed" in script
    assert "energyatlas-theme-change" in script


def test_plotly_renderer_reads_css_theme_tokens_and_reacts_to_theme_change():
    script = read("docs/assets/js/plotly-render.js")

    assert "getThemePlotlyDefaults" in script
    assert "getComputedStyle(document.documentElement)" in script
    assert "energyatlas-theme-change" in script
    assert "Plotly.react" in script
