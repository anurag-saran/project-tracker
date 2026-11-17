"""GitHub API client and discovery helpers."""

from tracker.github.client import GitHubClient
from tracker.github.discover import (
    PROPOSAL_CANDIDATES,
    propose_modules,
    resolve_project_repos,
)

__all__ = [
    "GitHubClient",
    "PROPOSAL_CANDIDATES",
    "propose_modules",
    "resolve_project_repos",
]
