from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import hooks.wiki_metadata as wiki_metadata


def test_format_git_timestamp_uses_requested_footer_format():
    formatted = wiki_metadata.format_git_timestamp("2026-01-22T14:07:33-05:00")

    assert formatted == "GMT-05:00 14:07 Jan 22 2026"


def test_git_timestamp_passes_page_path_after_separator(monkeypatch):
    calls = []

    def fake_run(command, cwd, check, capture_output, text):
        calls.append((command, cwd, check, capture_output, text))
        return SimpleNamespace(stdout="2026-01-22T14:07:33-05:00\n")

    monkeypatch.setattr(wiki_metadata.subprocess, "run", fake_run)

    result = wiki_metadata.git_timestamp(Path("C:/repo"), Path("C:/repo/docs/index.md"))

    assert result == "2026-01-22T14:07:33-05:00"
    assert calls[0][0] == ["git", "log", "-1", "--format=%cI", "--", str(Path("C:/repo/docs/index.md"))]


def test_on_config_sets_website_updated_at(monkeypatch):
    monkeypatch.setattr(wiki_metadata, "git_timestamp", Mock(return_value="2026-01-22T14:07:33-05:00"))
    config = {"config_file_path": "C:/repo/mkdocs.yml", "extra": {}}

    result = wiki_metadata.on_config(config)

    assert result["extra"]["website_updated_at"] == "GMT-05:00 14:07 Jan 22 2026"


def test_on_page_markdown_sets_page_specific_updated_at(monkeypatch):
    monkeypatch.setattr(wiki_metadata, "git_timestamp", Mock(return_value="2026-02-03T09:30:00-05:00"))
    page = SimpleNamespace(
        file=SimpleNamespace(abs_src_path="C:/repo/docs/index.md"),
        meta={},
    )
    config = {"config_file_path": "C:/repo/mkdocs.yml", "extra": {"website_updated_at": "GMT-05:00 14:07 Jan 22 2026"}}

    markdown = wiki_metadata.on_page_markdown("body", page=page, config=config, files=[])

    assert markdown == "body"
    assert page.meta["page_updated_at"] == "GMT-05:00 09:30 Feb 03 2026"
