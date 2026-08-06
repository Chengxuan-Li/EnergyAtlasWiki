from __future__ import annotations

from collections import Counter
from pathlib import Path
import posixpath
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONTENT_ROOTS = {
    "quick-start": "Quick Start",
    "workflows": "Workflows",
    "architecture": "Architecture",
    "python": "Python",
    "web-api": "WebAPI",
    "library": "Library",
    "user-stories": "User Stories",
    "wiki-guide": "Wiki Guide",
}
LINK_PATTERN = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
INLINE_CODE_PATTERN = re.compile(r"`+[^`\n]*`+")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")


def markdown_paths() -> set[str]:
    return {path.relative_to(DOCS).as_posix() for path in DOCS.rglob("*.md")}


def mkdocs_text() -> str:
    return (ROOT / "mkdocs.yml").read_text(encoding="utf-8")


def navigation() -> list[dict[str, object]]:
    text = mkdocs_text()
    nav_block = "nav:\n" + text.split("nav:\n", 1)[1].split("\nplugins:", 1)[0]
    return yaml.safe_load(nav_block)["nav"]


def page_paths(node: object) -> list[str]:
    if isinstance(node, str):
        return [node] if node.endswith(".md") else []
    if isinstance(node, list):
        return [path for item in node for path in page_paths(item)]
    if isinstance(node, dict):
        return [path for value in node.values() for path in page_paths(value)]
    return []


def redirect_map() -> dict[str, str]:
    block = mkdocs_text().split("redirect_maps:\n", 1)[1].split("\nmarkdown_extensions:", 1)[0]
    pairs = re.findall(r"^\s{8}([^:\n]+\.md):\s+(\S+\.md)\s*$", block, re.MULTILINE)
    return dict(pairs)


def markdown_link_targets(source: Path) -> list[Path]:
    targets: list[Path] = []
    in_fence = False
    fence_marker: str | None = None

    for line in source.read_text(encoding="utf-8").splitlines():
        fence = re.match(r"^\s*(```+|~~~+)", line)
        if fence:
            marker = fence.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = None
            continue
        if in_fence:
            continue

        code_spans = [match.span() for match in INLINE_CODE_PATTERN.finditer(line)]
        for match in LINK_PATTERN.finditer(line):
            if any(start <= match.start() < end for start, end in code_spans):
                continue
            destination = match.group(1).strip()
            if destination.startswith("<") and ">" in destination:
                target = destination[1:destination.index(">")]
            else:
                target = destination.split(None, 1)[0]
            if not target or target.startswith("#") or target.lower().startswith(EXTERNAL_PREFIXES):
                continue
            path_part = re.match(r"^[^#?]*", target).group(0)
            if path_part:
                targets.append((source.parent / Path(path_part)).resolve())

    return targets


def test_all_markdown_pages_live_in_exactly_one_subspace():
    paths = markdown_paths()

    assert len(paths) == 59
    assert all(path.split("/", 1)[0] in CONTENT_ROOTS for path in paths)
    assert not any((DOCS / legacy).exists() for legacy in (
        "getting-started",
        "ubem-wiki",
        "references",
        "dev-guide",
        "technical-references",
        "resources",
    ))


def test_navigation_matches_physical_subspace_folders_and_covers_every_page():
    nav = navigation()
    nav_paths: list[str] = []

    assert [next(iter(item)) for item in nav] == list(CONTENT_ROOTS.values())
    for item, (folder, label) in zip(nav, CONTENT_ROOTS.items()):
        assert next(iter(item)) == label
        subspace_paths = page_paths(item[label])
        assert subspace_paths
        assert all(path.startswith(f"{folder}/") for path in subspace_paths)
        nav_paths.extend(subspace_paths)

    assert len(nav_paths) == 59
    assert set(nav_paths) == markdown_paths()


def test_every_moved_page_has_a_unique_redirect_to_an_existing_target():
    redirects = redirect_map()

    assert len(redirects) == 52
    assert len(set(redirects.values())) == 52
    assert all(not (DOCS / source).exists() for source in redirects)
    assert all((DOCS / target).is_file() for target in redirects.values())
    assert redirects["index.md"] == "quick-start/index.md"


def test_all_relative_markdown_links_and_images_resolve():
    broken: list[str] = []
    for source in sorted(DOCS.rglob("*.md")):
        for target in markdown_link_targets(source):
            if not target.exists():
                broken.append(f"{source.relative_to(DOCS).as_posix()} -> {target}")

    assert not broken, "\n".join(broken)


def test_site_map_contains_every_markdown_page_exactly_once():
    site_map = DOCS / "wiki-guide" / "site-map.md"
    linked_pages = [
        target.relative_to(DOCS).as_posix()
        for target in markdown_link_targets(site_map)
        if target.suffix == ".md"
    ]

    assert Counter(linked_pages) == Counter(markdown_paths())
    assert not re.search(r"^- \[[^]]+\]\([^)]+\.md\)$", site_map.read_text(encoding="utf-8"), re.MULTILINE)
