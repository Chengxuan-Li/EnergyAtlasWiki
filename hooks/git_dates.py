from __future__ import annotations

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
