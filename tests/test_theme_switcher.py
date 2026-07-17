import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_base_template_bootstraps_dark_first_theme_and_renders_toggle():
    base = read("theme/base.html")

    assert "energyatlas-wiki-theme" in base
    assert "document.documentElement.dataset.theme = theme" in base
    assert "prefers-color-scheme: light" in base
    assert 'id="wiki-theme-toggle"' in base
    assert 'aria-pressed="false"' in base
    assert '<span class="wiki-theme-toggle-track" aria-hidden="true">' in base
    assert "Edit on GitHub" not in base
    assert not re.search(r">\s*Edit\s*<", base)
    assert not re.search(r">\s*View on GitHub\s*<", base)
    assert 'aria-label="Edit this page"' in base
    assert 'aria-label="View GitHub repository"' in base
    assert 'class="wiki-topbar-link wiki-topbar-icon-button wiki-topbar-edit-button"' in base
    assert 'class="wiki-topbar-link wiki-topbar-icon-button wiki-topbar-github-button"' in base
    assert 'href="{{ page.edit_url }}"' in base
    assert 'href="{{ config.repo_url }}"' in base
    assert "wiki-topbar-pen-icon" in base
    assert "wiki-topbar-github-icon" in base
    assert base.index('class="wiki-topbar-left"') < base.index('id="wiki-theme-toggle"')
    assert base.index('id="wiki-theme-toggle"') < base.index('class="wiki-topbar-link wiki-topbar-icon-button')


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
        assert "--theme-toggle-track-bg" in css
        assert ".wiki-theme-toggle" in css
        assert "--wiki-theme-toggle-width: 64px;" in css
        assert ".wiki-theme-toggle-thumb" in css
        assert "z-index: 1;" in css
        assert "z-index: 2;" in css
        assert ".wiki-topbar-icon-button" in css
        assert "border-radius: 50%;" in css
        assert '[data-theme="light"] .code-block-body .n' in css


def test_theme_toggle_controller_persists_choice_and_announces_changes():
    script = read("docs/assets/js/theme-toggle.js")

    assert "energyatlas-wiki-theme" in script
    assert "localStorage.setItem" in script
    assert "prefers-color-scheme: dark" in script
    assert "aria-pressed" in script
    assert "energyatlas-theme-change" in script


def test_plotly_renderer_reads_css_theme_tokens_and_reacts_to_theme_change():
    script = read("docs/assets/js/plotly-render.js")

    assert "getThemePlotlyDefaults" in script
    assert "getComputedStyle(document.documentElement)" in script
    assert "energyatlas-theme-change" in script
    assert "Plotly.react" in script
