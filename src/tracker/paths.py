"""Workspace path helpers."""

from __future__ import annotations

from pathlib import Path

ROOT_MARKERS = ("projects.yaml", "pyproject.toml")


def find_workspace(start: Path | None = None) -> Path:
    """Walk up from *start* (or cwd) looking for projects.yaml / pyproject.toml."""
    cur = (start or Path.cwd()).resolve()
    for candidate in [cur, *cur.parents]:
        if any((candidate / m).exists() for m in ROOT_MARKERS):
            return candidate
    return cur


def projects_yaml(root: Path | None = None) -> Path:
    return (root or find_workspace()) / "projects.yaml"


def db_path(root: Path | None = None) -> Path:
    return (root or find_workspace()) / ".tracker" / "tracker.db"


def modules_generated(root: Path | None = None) -> Path:
    return (root or find_workspace()) / "modules.generated.yaml"


def overrides_dir(root: Path | None = None) -> Path:
    return (root or find_workspace()) / "overrides"


def reports_dir(root: Path | None = None) -> Path:
    return (root or find_workspace()) / "reports"


def prompts_dir(root: Path | None = None) -> Path:
    return (root or find_workspace()) / "prompts"


def site_dir(root: Path | None = None) -> Path:
    return (root or find_workspace()) / "site"
