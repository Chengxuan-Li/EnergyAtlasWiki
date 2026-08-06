"""Public-safety scan for the published architecture surface.

The LikeC4 project and its Wiki pages are authored from a separate private workspace. Every
element, description, relationship, and comment in this repository ships to readers, including
parts of the model no rendered view happens to show. This scan fails the build if private
provenance reaches the public repository.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SCANNED_ROOTS = (ROOT / "architecture", ROOT / "docs" / "architecture")
SKIPPED_DIRECTORIES = {"node_modules", ".likec4", "__pycache__"}
TEXT_SUFFIXES = {".c4", ".md", ".json", ".mjs", ".js", ".yml", ".yaml", ".css", ".html"}

FORBIDDEN_PATTERNS = {
    "windows absolute path": re.compile(r"[A-Za-z]:\\\\?(?:github|Users)", re.IGNORECASE),
    "posix checkout path": re.compile(r"/(?:c|mnt/c)/github/", re.IGNORECASE),
    "private authoring repository": re.compile(r"likec4[-_]testground", re.IGNORECASE),
    "private implementation repository": re.compile(r"RCEnergySimulator", re.IGNORECASE),
    "private prompt directory": re.compile(r"\bprompts/(?:shelved/)?\d{4}-\d{2}-\d{2}"),
    "private design records": re.compile(r"docs/superpowers"),
    "private request id": re.compile(r"\brequest[-_ ]?id\b", re.IGNORECASE),
    "local approval renders": re.compile(r"\breview/[a-z0-9-]+\.png"),
    "home directory": re.compile(r"/home/[a-z]|/Users/[a-z]", re.IGNORECASE),
}

# The router's own CLI prints the workspace it was given; that is a runtime value, not a
# checked-in path, so only literal paths in source are forbidden.
PNG_REFERENCE = re.compile(r"\.png\b", re.IGNORECASE)


def scanned_files() -> list[Path]:
    files: list[Path] = []
    for root in SCANNED_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if SKIPPED_DIRECTORIES & set(path.relative_to(root).parts):
                continue
            if path.suffix.lower() in TEXT_SUFFIXES:
                files.append(path)
    return sorted(files)


def test_scan_covers_the_published_architecture_surface():
    files = scanned_files()

    assert files
    assert any(path.suffix == ".c4" for path in files)
    assert any(path.suffix == ".md" for path in files)


def test_no_private_provenance_reaches_the_public_repository():
    findings: list[str] = []

    for path in scanned_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in FORBIDDEN_PATTERNS.items():
                if pattern.search(line):
                    location = path.relative_to(ROOT).as_posix()
                    findings.append(f"{location}:{line_number} {label}: {line.strip()}")

    assert not findings, "\n".join(findings)


def test_no_diagram_image_is_referenced_anywhere_in_the_architecture_surface():
    findings = [
        f"{path.relative_to(ROOT).as_posix()}: {line.strip()}"
        for path in scanned_files()
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
        if PNG_REFERENCE.search(line)
    ]

    assert not findings, "\n".join(findings)


def test_no_binary_assets_are_checked_in_under_the_architecture_surface():
    binaries = [
        path.relative_to(ROOT).as_posix()
        for root in SCANNED_ROOTS
        if root.exists()
        for path in root.rglob("*")
        if path.is_file()
        and not SKIPPED_DIRECTORIES & set(path.relative_to(root).parts)
        and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}
    ]

    assert not binaries, "\n".join(binaries)
