# OSS Project Tracker

CLI to track multi-repo open-source projects (starting with **vLLM** and **llm-d**): module maps, change digests, pipeline (RFCs / big PRs), and people/ownership.

Adding a project means editing [`projects.yaml`](projects.yaml) only — no code changes.

## Setup

Requirements: Python 3.12+, [uv](https://docs.astral.sh/uv/), a GitHub token.

```bash
uv sync --all-extras
export GITHUB_TOKEN=ghp_...          # required for fetch/validate/discover
export ANTHROPIC_API_KEY=sk-ant-...  # optional; digests/maps use null LLM without it
uv run tracker init
```

Optional LLM providers:

| Env | Purpose |
|-----|---------|
| `TRACKER_LLM_PROVIDER` | `anthropic` (default), `openai`, or `null` |
| `ANTHROPIC_API_KEY` | Anthropic |
| `OPENAI_API_KEY` / `OPENAI_BASE_URL` | OpenAI or OpenAI-compatible (e.g. local vLLM) |
| `TRACKER_OPENAI_MODEL` / `TRACKER_ANTHROPIC_MODEL` | Model overrides |

## CLI

```bash
tracker init                         # projects.yaml, .tracker/db, folders
tracker validate                     # resolve orgs/repos/paths against GitHub
tracker discover <project>           # rank repos, propose modules → modules.generated.yaml
tracker fetch <project|all> [--since 7d]
tracker digest <project|all> [--since 7d] [--dry-run] [--skip-fetch]
tracker pipeline <project|all> [--since 7d] [--dry-run]
tracker blogs <project|all> [--since 7d] [--dry-run]   # RSS → summaries + links
tracker people <project>
tracker map <project> [--dry-run]
tracker site                         # static HTML under site/
tracker rollup                       # reports/WEEKLY.md + ensure latest-* copies
tracker notify <project> --channel slack   # optional; off by default
```

Reports land in `reports/<project>/`:

- `YYYY-MM-DD-digest.md` (archive) and `latest-digest.md` (stable, for diffs)
- `YYYY-MM-DD-pipeline.md` / `latest-pipeline.md`
- `YYYY-MM-DD-blogs.md` / `latest-blogs.md` — new posts with summaries + **Read full post** links
- `YYYY-MM-DD-people.md` / `latest-people.md`
- `module-map.md`
- `reports/WEEKLY.md` — cross-project TL;DR rollup (includes blogs)

## Adding a project

Edit `projects.yaml`:

```yaml
projects:
  - name: my-project
    description: Short blurb
    docs_urls: ["https://example.com"]
    sources:
      - org: my-org
        skip_archived: true
      - repo: my-org/core-repo
        tier: core
    pipeline_signals:
      issue_title_prefixes: ["[RFC]"]
      labels: ["RFC"]
      proposals_dirs: ["my-org/core-repo:docs/proposals"]
    people_signals:
      codeowners: [".github/CODEOWNERS"]
```

Then:

```bash
uv run tracker validate
uv run tracker discover my-project
uv run tracker digest my-project --since 7d
```

**Tiers:** `core` gets per-module detail; `watch` is a short section; org repos beyond `settings.max_repos_per_org` become `overflow` one-liners. Effective tier: explicit repo → org source → project → `watch`.

**Modules:** configure under a `repo:` source, or run `discover` and edit `modules.generated.yaml`. Description overrides go in `overrides/<project>.yaml`.

## Tuning prompts

LLM prompts live in [`prompts/`](prompts/) (`digest.md`, `module_map.md`, `pipeline.md`). Edit them and re-run with `--skip-fetch` to re-summarize from SQLite without hitting GitHub.

Fetch (deterministic) and summarize (LLM) are separate stages. Raw data is stored in `.tracker/tracker.db` first.

## Notifiers

Off by default. Enable with:

```bash
export SLACK_WEBHOOK_URL=https://hooks.slack.com/...
uv run tracker notify vllm --channel slack
# or SMTP_HOST / SMTP_FROM / SMTP_TO / SMTP_USER / SMTP_PASSWORD
```

## Automation (read updates + diff sections)

[`.github/workflows/weekly.yml`](.github/workflows/weekly.yml) runs Mondays ~7am ET and on `workflow_dispatch`:

1. Fetches GitHub data and builds digests / pipelines / **blog summaries** (module map on the first Monday or manual runs)
2. Writes `reports/WEEKLY.md` plus stable `latest-*.md` files per project
3. Opens (or updates) a PR: **Weekly tracker — YYYY-MM-DD**

Configure blogs with `blog_urls` in `projects.yaml` (vLLM → `https://vllm.ai/blog`, llm-d → `https://llm-d.ai/blog`). Feeds are read from `/rss.xml`.

**How to read it**

| Where | What you get |
|-------|----------------|
| PR description | TL;DRs for every project (code + **new blogs**) |
| PR **Files changed** | Week-over-week diff of each project section (`latest-digest.md`, `latest-blogs.md`, …) |
| `latest-blogs.md` | Short summary per new post + link to the full article |
| Dated `YYYY-MM-DD-*.md` files | Full history archive |
| GitHub Pages `weekly.html` | Same rollup on the static site |

Merge the PR when you’ve reviewed the week (or leave it open as the reading surface).

Set repository secret `ANTHROPIC_API_KEY` (optional) and enable GitHub Pages (source: GitHub Actions).

## Development

```bash
uv sync --all-extras
uv run pytest
```

Tests use recorded fixtures under `tests/fixtures/github/` — no live network.
