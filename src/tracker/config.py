"""Pydantic models and loaders for projects.yaml / modules.generated.yaml."""

from __future__ import annotations

import fnmatch
import re
from enum import Enum
from pathlib import Path
from typing import Annotated

import yaml
from pydantic import BaseModel, Field, field_validator, model_validator


class Tier(str, Enum):
    CORE = "core"
    WATCH = "watch"
    OVERFLOW = "overflow"


class ModuleConfig(BaseModel):
    name: str
    paths: list[str]
    description: str | None = None


class SignificantPR(BaseModel):
    labels: list[str] = Field(default_factory=list)
    min_files: int | None = None
    min_additions: int | None = None


class PipelineSignals(BaseModel):
    issue_title_prefixes: list[str] = Field(default_factory=list)
    labels: list[str] = Field(default_factory=list)
    proposals_dirs: list[str] = Field(default_factory=list)
    significant_pr: SignificantPR = Field(default_factory=SignificantPR)


class PeopleSignals(BaseModel):
    codeowners: list[str] = Field(
        default_factory=lambda: [".github/CODEOWNERS", "CODEOWNERS"]
    )
    owners_files: list[str] = Field(default_factory=list)
    governance_urls: list[str] = Field(default_factory=list)


class OrgSource(BaseModel):
    org: str
    include: list[str] = Field(default_factory=lambda: ["*"])
    exclude: list[str] = Field(default_factory=list)
    skip_archived: bool = True
    tier: Tier | None = None

    def matches(self, repo_name: str) -> bool:
        """Match short repo name against include/exclude globs."""
        if any(fnmatch.fnmatch(repo_name, pat) for pat in self.exclude):
            return False
        return any(fnmatch.fnmatch(repo_name, pat) for pat in self.include)


class RepoSource(BaseModel):
    repo: str
    tier: Tier | None = None
    modules: list[ModuleConfig] = Field(default_factory=list)

    @field_validator("repo")
    @classmethod
    def validate_repo(cls, v: str) -> str:
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", v):
            raise ValueError(f"repo must be owner/name, got {v!r}")
        return v


Source = Annotated[OrgSource | RepoSource, Field(discriminator=None)]


class ProjectConfig(BaseModel):
    name: str
    description: str | None = None
    docs_urls: list[str] = Field(default_factory=list)
    blog_urls: list[str] = Field(
        default_factory=list,
        description="Blog index URLs; RSS is resolved as <url>/rss.xml when needed",
    )
    tier: Tier | None = None
    sources: list[OrgSource | RepoSource]
    pipeline_signals: PipelineSignals = Field(default_factory=PipelineSignals)
    people_signals: PeopleSignals = Field(default_factory=PeopleSignals)

    def resolved_blog_urls(self) -> list[str]:
        """blog_urls, plus any docs_urls that look like blogs."""
        seen: list[str] = []
        for u in [*self.blog_urls, *self.docs_urls]:
            if "/blog" in u.rstrip("/").lower() and u not in seen:
                seen.append(u.rstrip("/"))
        return seen

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", v):
            raise ValueError(
                f"project name must be a lowercase slug, got {v!r}"
            )
        return v

    @model_validator(mode="after")
    def require_sources(self) -> ProjectConfig:
        if not self.sources:
            raise ValueError(f"project {self.name!r} needs at least one source")
        return self

    def org_sources(self) -> list[OrgSource]:
        return [s for s in self.sources if isinstance(s, OrgSource)]

    def repo_sources(self) -> list[RepoSource]:
        return [s for s in self.sources if isinstance(s, RepoSource)]


class Settings(BaseModel):
    max_repos_per_org: int = 25
    default_since: str = "30d"


class RootConfig(BaseModel):
    settings: Settings = Field(default_factory=Settings)
    projects: list[ProjectConfig]

    def get_project(self, name: str) -> ProjectConfig:
        for p in self.projects:
            if p.name == name:
                return p
        raise KeyError(f"unknown project: {name}")

    def project_names(self) -> list[str]:
        return [p.name for p in self.projects]


class GeneratedModule(BaseModel):
    name: str
    paths: list[str]
    description: str | None = None


class GeneratedRepos(BaseModel):
    projects: dict[str, dict[str, list[GeneratedModule]]] = Field(
        default_factory=dict
    )
    """projects[project_name][owner/repo] -> modules"""

    @classmethod
    def from_nested(cls, data: dict) -> GeneratedRepos:
        """Parse {projects: {name: {repos: {full_name: [...]}}}}."""
        out: dict[str, dict[str, list[GeneratedModule]]] = {}
        raw_projects = (data or {}).get("projects") or {}
        for pname, pdata in raw_projects.items():
            repos = pdata.get("repos") if isinstance(pdata, dict) else pdata
            out[pname] = {}
            if not isinstance(repos, dict):
                continue
            for full_name, mods in repos.items():
                out[pname][full_name] = [
                    GeneratedModule.model_validate(m) for m in (mods or [])
                ]
        return cls(projects=out)

    def to_yaml_dict(self) -> dict:
        return {
            "projects": {
                pname: {
                    "repos": {
                        full: [m.model_dump(exclude_none=True) for m in mods]
                        for full, mods in repos.items()
                    }
                }
                for pname, repos in self.projects.items()
            }
        }


class OverrideEntry(BaseModel):
    description: str | None = None
    purpose: str | None = None
    entry_points: list[str] | None = None
    relations: str | None = None


class ProjectOverrides(BaseModel):
    """overrides/<project>.yaml — keyed by repo or repo/module."""

    modules: dict[str, OverrideEntry] = Field(default_factory=dict)
    repos: dict[str, OverrideEntry] = Field(default_factory=dict)


def _parse_source(raw: dict) -> OrgSource | RepoSource:
    if "org" in raw and "repo" in raw:
        raise ValueError(f"source cannot have both org and repo: {raw}")
    if "org" in raw:
        return OrgSource.model_validate(raw)
    if "repo" in raw:
        return RepoSource.model_validate(raw)
    raise ValueError(f"source needs org or repo: {raw}")


def load_config(path: Path) -> RootConfig:
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Run `tracker init` first."
        )
    data = yaml.safe_load(path.read_text()) or {}
    projects_raw = data.get("projects") or []
    projects: list[ProjectConfig] = []
    for pr in projects_raw:
        sources = [_parse_source(s) for s in pr.get("sources") or []]
        payload = {**pr, "sources": sources}
        # Rebuild without raw source dicts for pydantic
        cleaned = {k: v for k, v in pr.items() if k != "sources"}
        projects.append(
            ProjectConfig.model_validate({**cleaned, "sources": sources})
        )
    settings = Settings.model_validate(data.get("settings") or {})
    return RootConfig(settings=settings, projects=projects)


def load_generated_modules(path: Path) -> GeneratedRepos:
    if not path.exists():
        return GeneratedRepos()
    data = yaml.safe_load(path.read_text()) or {}
    return GeneratedRepos.from_nested(data)


def save_generated_modules(path: Path, generated: GeneratedRepos) -> None:
    path.write_text(
        yaml.safe_dump(
            generated.to_yaml_dict(),
            sort_keys=False,
            default_flow_style=False,
        )
    )


def load_overrides(path: Path) -> ProjectOverrides:
    if not path.exists():
        return ProjectOverrides()
    data = yaml.safe_load(path.read_text()) or {}
    return ProjectOverrides.model_validate(data)


def effective_tier(
    *,
    repo_tier: Tier | None,
    org_tier: Tier | None,
    project_tier: Tier | None,
) -> Tier:
    for t in (repo_tier, org_tier, project_tier):
        if t is not None and t != Tier.OVERFLOW:
            return t
    return Tier.WATCH


def parse_proposals_dir(entry: str) -> tuple[str | None, str]:
    """Parse 'owner/repo:path' or 'owner/repo:<discover>' or bare path.

    Returns (full_name_or_None, path_or_discover_token).
    """
    if ":" in entry and "/" in entry.split(":")[0]:
        full, path = entry.split(":", 1)
        return full, path
    return None, entry


SEED_PROJECTS_YAML = """\
settings:
  max_repos_per_org: 25
  default_since: 30d

# Focus: vLLM + llm-d only. Add other projects later by appending here.
projects:
  - name: vllm
    description: High-throughput and memory-efficient inference engine for LLMs
    sources:
      - org: vllm-project
        skip_archived: true
      - repo: vllm-project/vllm
        tier: core
    pipeline_signals:
      issue_title_prefixes: ["[RFC]", "[Roadmap]"]
      labels: ["RFC"]
      significant_pr:
        labels: ["RFC", "breaking-change"]
        min_files: 25
        min_additions: 500
    people_signals:
      codeowners: [".github/CODEOWNERS"]
    docs_urls:
      - "https://docs.vllm.ai"
      - "https://vllm.ai/blog"
    blog_urls:
      - "https://vllm.ai/blog"

  - name: llm-d
    description: Kubernetes-native distributed LLM inference (built around vLLM)
    sources:
      - org: llm-d
        skip_archived: true
      - repo: llm-d/llm-d
        tier: core
      - org: llm-d-incubation
        skip_archived: true
        tier: watch
    pipeline_signals:
      issue_title_prefixes: ["[RFC]", "[Proposal]"]
      labels: ["RFC", "proposal"]
      proposals_dirs: ["llm-d/llm-d:docs/proposals"]
      significant_pr:
        labels: ["RFC", "proposal"]
        min_files: 20
        min_additions: 400
    people_signals:
      codeowners: [".github/CODEOWNERS", "CODEOWNERS"]
      governance_urls: ["https://llm-d.ai/community/sigs"]
    docs_urls:
      - "https://llm-d.ai"
      - "https://github.com/llm-d/llm-d/tree/main/docs/proposals"
    blog_urls:
      - "https://llm-d.ai/blog"
"""
