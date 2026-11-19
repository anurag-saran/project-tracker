# Build: OSS Project Tracker

I want a tool that helps me closely track open-source projects that span many
GitHub repos. It should (1) explain what each sub-project/module does, (2)
summarize what changed recently, (3) show what's in the pipeline (RFCs,
proposals, big open PRs), and (4) show who owns/leads each area.

I'm starting with **vLLM** and **llm-d**, but I'll add more projects later
(e.g. KServe, Envoy AI Gateway, Kubernetes Gateway API Inference Extension).
Adding a project must only mean editing a config file, with no code changes.

## Tech stack
- Python 3.12, managed with `uv`
- `typer` (CLI), `httpx` (GitHub GraphQL + REST), `pydantic` (config/models),
  `jinja2` (rendering), SQLite (state + cache), `pytest`
- LLM summarization behind a small provider interface; default to Anthropic
  (`ANTHROPIC_API_KEY`), and make it easy to swap in OpenAI or a local
  OpenAI-compatible endpoint (e.g. a vLLM server)
- Secrets via env vars: `GITHUB_TOKEN`, `ANTHROPIC_API_KEY`

## Config: `projects.yaml` (the only thing I edit to add projects)
Each project defines:
- `name`, `description`, `docs_urls` (website, blog, roadmap pages)
- `sources`: either whole GitHub orgs (with `include`/`exclude` globs and
  `skip_archived: true`) or explicit `owner/repo` entries
- `modules` (optional, for monorepos): named path globs inside a repo,
  e.g. `vllm/v1/core/**` → "v1 scheduler/core". If omitted, auto-discover
  (see below)
- `pipeline_signals`: how to find upcoming work, e.g.
  - issue title prefixes / labels (`[RFC]`, `RFC`, `roadmap`)
  - a proposals directory path in a repo (new/changed files = new proposals)
  - PR labels or size thresholds that mark a PR as "significant"
- `people_signals`: CODEOWNERS paths, OWNERS files, a SIG/governance page URL
- `tier`: `core` | `watch` (core repos get per-module detail; watch repos get
  a short section)

Seed it with:
```yaml
projects:
  - name: vllm
    sources:
      - org: vllm-project          # auto-discover all repos, rank by activity
        skip_archived: true
      - repo: vllm-project/vllm
        tier: core
        # auto-discover modules from top-level packages under vllm/ and vllm/v1/
    pipeline_signals:
      issue_title_prefixes: ["[RFC]", "[Roadmap]"]
      labels: ["RFC"]
    people_signals:
      codeowners: [".github/CODEOWNERS"]
    docs_urls: ["https://docs.vllm.ai", "https://vllm.ai/blog"]

  - name: llm-d
    sources:
      - org: llm-d
        skip_archived: true
      - org: llm-d-incubation
        skip_archived: true
        tier: watch
    pipeline_signals:
      # llm-d needs approved project proposals for public APIs / new components.
      # Find where proposals live in llm-d/llm-d and configure it here.
      proposals_dirs: ["llm-d/llm-d:<discover>"]
    people_signals:
      governance_urls: ["https://llm-d.ai/community/sigs"]
    docs_urls: ["https://llm-d.ai"]
```
Verify every repo/path against the live GitHub API instead of trusting my
seed values; print what was found and what didn't resolve.

## Features

### 1. Module map (`tracker map <project>`)
- For every repo (and every module in core monorepos), produce: one-paragraph
  purpose, key entry points/dirs, how it relates to other modules/repos,
  owners (from CODEOWNERS/OWNERS/SIG page), activity level (PRs merged in the
  last 90 days), latest release.
- Auto-discovery: for monorepos without configured modules, propose modules
  from directory structure + CODEOWNERS groupings, and write them into a
  `modules.generated.yaml` that I can edit/override.
- Generate descriptions with the LLM from README, docs, package docstrings
  and directory listings. Cache them by content hash and regenerate only when
  sources change. Manual overrides in `overrides/<project>.yaml` always win.

### 2. Change digest (`tracker digest <project|all> --since 30d`)
- Pull, since the last run (incremental, stored in SQLite):
  releases, merged PRs (title, body, labels, author, files changed, +/-),
  closed RFCs/proposals.
- Map each PR to modules using changed-file paths vs module globs.
- Per module: an LLM-written summary of what changed and why it matters,
  grouped into Features / Performance / Fixes / Breaking or deprecations /
  Infra. Every claim must link the PR(s) it came from. No claims without a
  source PR or release; if a summary can't be grounded, list the PRs instead.
- Highlight: breaking changes, new modules/repos, new releases, first-time
  contributors to core modules.

### 3. Pipeline (`tracker pipeline <project>`)
- Open RFCs and proposals (new this period vs ongoing), with a one-line
  summary, status, and discussion heat (comments/reactions in the period).
- "Significant" open PRs: large, labeled, touching core modules, or with
  high review activity. Show age, author, reviewers, last activity.
- Roadmap issues: extract checklist items and show progress (done/total).

### 4. People (`tracker people <project>`)
- Per module: owners, most active authors and reviewers in the last 90 days,
  SIG leads where defined. Use only public GitHub/governance data.

### 5. Output
- Markdown files under `reports/<project>/<YYYY-MM-DD>-digest.md`, plus
  `reports/<project>/module-map.md`
- A static HTML site (`tracker site`) with a project index, module map
  pages and a digest archive, deployable to GitHub Pages
- Optional notifiers behind an interface: Slack webhook, email (SMTP).
  Off by default.
- Every report starts with a 5-bullet "TL;DR for this month" across all modules.

### 6. Automation
- GitHub Actions workflow: monthly cron (1st of month ~7am ET) runs
  `tracker digest all`, `tracker pipeline all`, blogs/releases/rollup,
  commits reports, and rebuilds the site. `workflow_dispatch` for manual runs.
- `tracker map` runs on each monthly run or when new repos/modules are detected.

## CLI summary
```
tracker init                      # create projects.yaml, db, folders
tracker validate                  # resolve orgs/repos/paths, report problems
tracker discover <project>        # list repos, propose modules
tracker map <project>
tracker digest <project|all> [--since 30d|DATE] [--dry-run]
tracker pipeline <project|all>
tracker people <project>
tracker site
```

## Engineering requirements
- Prefer GraphQL for bulk fetches. Handle pagination, rate limits (back off
  and resume), and ETags/caching so reruns are cheap.
- Keep fetching (deterministic) and summarizing (LLM) as separate stages.
  Raw data goes in SQLite first, then summaries are built from it, so I can
  re-summarize without refetching.
- Keep the LLM's input small: send PR titles, labels, trimmed bodies and file
  lists, not full diffs. Batch per module. Track token usage per run and
  print the cost estimate.
- Prompts for the LLM live in `prompts/*.md` so I can tune them.
- Org repos ranked by activity; add a config cap (e.g. top 25) so large orgs
  stay readable, with the rest listed as "other repos" with one line each.
- Tests with recorded GitHub fixtures (no live network in tests).
- README covering setup, adding a new project and tuning prompts.

## Build order
Work in phases and stop for me to review after each:
1. Config schema + `init`/`validate`/`discover` + GitHub fetch into SQLite
2. `digest` with module mapping and Markdown output
3. `pipeline` and `people`
4. `map` with LLM descriptions, caching and overrides
5. HTML site + GitHub Actions + notifiers

Before writing code, show me the config schema, the SQLite schema and the
module/file layout, and ask about anything ambiguous.