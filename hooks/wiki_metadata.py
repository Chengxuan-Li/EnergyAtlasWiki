from __future__ import annotations

from functools import lru_cache
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any


DATE_FORMAT = "%H:%M %b %d %Y"


def format_gmt_offset(timestamp: datetime) -> str:
    offset = timestamp.strftime("%z")
    if not offset:
        return "GMT"
    return f"GMT{offset[:3]}:{offset[3:]}"


def format_git_timestamp(timestamp: str) -> str:
    normalized = timestamp.strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(normalized)
    return f"{format_gmt_offset(parsed)} {parsed.strftime(DATE_FORMAT)}"


@lru_cache(maxsize=None)
def git_timestamp(repo_root: Path, page_path: Path | None = None) -> str | None:
    command = ["git", "log", "-1", "--format=%cI"]
    if page_path is not None:
        command.extend(["--", str(page_path)])

    try:
        result = subprocess.run(
            command,
            cwd=str(repo_root),
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None

    timestamp = result.stdout.strip()
    return timestamp or None


def repo_root_from_config(config: Any) -> Path:
    config_path = config.get("config_file_path") if hasattr(config, "get") else config["config_file_path"]
    return Path(config_path).resolve().parent if config_path else Path.cwd()


def ensure_extra(config: Any) -> dict[str, Any]:
    extra = config.get("extra") if hasattr(config, "get") else config["extra"]
    if extra is None:
        extra = {}
        config["extra"] = extra
    return extra


def on_config(config: Any) -> Any:
    repo_root = repo_root_from_config(config)
    extra = ensure_extra(config)
    website_timestamp = git_timestamp(repo_root)

    if website_timestamp:
        extra["website_updated_at"] = format_git_timestamp(website_timestamp)
    else:
        extra["website_updated_at"] = "Unknown"

    return config


def on_page_markdown(markdown: str, page: Any, config: Any, files: Any) -> str:
    repo_root = repo_root_from_config(config)
    extra = ensure_extra(config)
    page_path_value = getattr(page.file, "abs_src_path", None)
    page_timestamp = git_timestamp(repo_root, Path(page_path_value)) if page_path_value else None

    page.meta["page_updated_at"] = (
        format_git_timestamp(page_timestamp)
        if page_timestamp
        else extra.get("website_updated_at", "Unknown")
    )

    return markdown


def is_nav_page(item: Any) -> bool:
    return hasattr(item, "meta") and hasattr(item, "url") and hasattr(item, "title")


def flatten_nav_pages(items: Any) -> list[Any]:
    pages: list[Any] = []
    for item in items:
        children = getattr(item, "children", None)
        if children:
            pages.extend(flatten_nav_pages(children))
        elif is_nav_page(item):
            pages.append(item)
    return pages


def article_summary(page: Any) -> dict[str, str]:
    return {
        "title": page.title,
        "url": page.url,
    }


def page_key(page: Any) -> str | None:
    file = getattr(page, "file", None)
    return (
        getattr(file, "src_uri", None)
        or getattr(file, "src_path", None)
        or getattr(file, "abs_src_path", None)
        or getattr(page, "url", None)
    )


def apply_article_nav_metadata(page: Any, pages: list[Any]) -> None:
    current_key = page_key(page)
    for index, nav_page in enumerate(pages):
        if nav_page is page or (current_key and page_key(nav_page) == current_key):
            page.meta["previous_article"] = article_summary(pages[index - 1]) if index > 0 else None
            page.meta["next_article"] = article_summary(pages[index + 1]) if index < len(pages) - 1 else None
            return

    page.meta["previous_article"] = None
    page.meta["next_article"] = None


def on_nav(nav: Any, config: Any, files: Any) -> Any:
    pages = flatten_nav_pages(getattr(nav, "items", []))

    for index, page in enumerate(pages):
        page.meta["previous_article"] = article_summary(pages[index - 1]) if index > 0 else None
        page.meta["next_article"] = article_summary(pages[index + 1]) if index < len(pages) - 1 else None

    return nav


def on_page_context(context: dict[str, Any], page: Any, config: Any, nav: Any) -> dict[str, Any]:
    apply_article_nav_metadata(page, flatten_nav_pages(getattr(nav, "items", [])))
    return context
