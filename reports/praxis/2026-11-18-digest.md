# praxis digest — 2026-11-18

_Since 7d · generated 2026-11-18T18:28:21Z_

## TL;DR for this month

- Release praxis-proxy/grid@v0.3.1
- Release praxis-proxy/ai@v0.11.0
- praxis-proxy/ai/apis: 20 PRs merged
- praxis-proxy/ai/filters: 6 PRs merged
- praxis-proxy/ai/server: 1 PRs merged

## praxis-proxy/ai (core)

### Releases
- [v0.11.0](https://github.com/praxis-proxy/ai/releases/tag/v0.11.0) — 2026-11-13
### apis

# apis Module PR Summary

## Features
- Pin the OpenAI Files API contract as groundwork for a local Files API implementation, ensuring no runtime behavior change (#1955).
- Extend NeMo redaction support to OpenAI Responses and Anthropic Messages, enabling text-changing redaction in guardrail filters (#1969).

## Performance
- Retain incremental stream state in Anthropic streaming translation to avoid rescanning unfinished prefixes, improving efficiency (#1986).
- Optimize document extraction serialization by counting bytes without retaining full JSON bodies, reducing memory usage (#2002).

## Fixes
- Preserve request field order and enforce body contracts to ensure accurate JSON handling in filters (#1980).
- Fix handling of named tool-use blocks in Anthropic Messages streaming to return correct `stop_reason` (#1954).
- Accept blank namespace descriptions in `openai_client_tool_compat` as per schema, while rejecting missing or invalid types (#1996).
- Prevent leaking of provider error text and request values in logs to avoid exposing sensitive user data (#2010).

## Breaking or deprecations
- Remove redundant `api_translation_enabled` flag for Anthropic translation, as it's now always enabled (#1958).

## Infra
- Add OpenAI verification badges to README and conformance pages for improved visibility of conformance status (#1979).
- Bump pinned Codex CLI compatibility to `0.167.0` to ensure acceptance tests validate the latest client behavior (#1926).

### filters

## Features

- Support NeMo guardrail redaction for OpenAI Responses and Anthropic Messages (#1969).
- Add verified-identity tier to `external_metering` filter for resolving tenant identity from `AuthenticatedIdentity` (#1981).

## Performance

- Move `token_rate_limit` state to `filter_state` for better performance and management (#2006).
- Move `token_count` state to `filter_state` for improved efficiency (#1959).

## Fixes

- Require explicit token rate limit backend configuration instead of defaulting to in-memory (#1924).

## Breaking or deprecations

- `a2a` task-route capture state is now stored in `filter_state` instead of `filter_metadata` (#1968).

## Infra

- No infrastructure-related changes in this set of PRs.

**First-time contributors:** guicassolato
### server

## Features

- Added support for the Conversations API in the FIPS compliance profile, enabling secure handling of conversation data (#1960).

## Infra

- Updated release qualification scripts and documentation to reflect the inclusion of the Conversations API in FIPS compliance (#1960).

### store

# Summary of Recent Changes in `store` Module (praxis-proxy/ai)

## Fixes

- Ensured complete conformance with the OpenAI API contract for all eight locally owned Conversations operations, addressing discrepancies and improving alignment with the pinned OpenAI reference (#1950).

### store-backends

## Fixes

- Ensured full API contract conformance for all eight locally owned Conversations operations against the current pinned OpenAI reference (#1950). This ensures accurate behavior and compatibility with expected OpenAI API responses.
- Reduced code complexity by removing redundant or outdated code as part of aligning with the OpenAI reference implementation (#1950).

### vllm

## Features

- Added full acceptance and live vision coverage for OpenResponses testing (#1977). This enhances the CI process by ensuring broader validation of response templates, including vision capabilities.

### xtask

## Features

- Add per-release support report generation to automate documentation of release compatibility and qualification status (#1941).
- Introduce OpenAI verification badges in README and conformance pages to highlight API conformance achievements (#1979).

## Fixes

- Achieve exact API contract conformance for all locally owned Conversations operations against the OpenAI reference (#1950).
- Make Anthropic API version configurable for translated OpenAI Chat Completions requests, with support for `2026-10-21` (#1870).

## Infra

- Include the Conversations API in the FIPS compliance profile to ensure alignment with security and compliance standards (#1960).


### Highlights
- New release **v0.11.0**

## praxis-proxy/praxis (core)


### crates

## Features

- Add readiness-first delayed handoff for shutdown lifecycle (#1499).
- Introduce `FilterMetadata` as a bounded type to improve filtering metadata handling (#1535).
- Enable explicit configuration for host-supplied context slots in policy filters (#1424).

## Fixes

- Improve certificate reload detection by fingerprinting files at 10-second intervals (#1517).
- Make rate limit filter configuration require an explicit `scope: local` to avoid ambiguity (#1539).
- Allow composing metadata response context in policy filters without overwriting existing data (#1552).

## Infra

- Clarify policy filter capabilities and diagnostics with updated documentation and configuration notes (#1549).

**First-time contributors:** alexsnaps, averevki
### crates-core

## Features

- Added readiness-first delayed handoff mechanism to improve shutdown reliability (#1499).

### xtask

## Features

- Added readiness-first delayed handoff mechanism for shutdown lifecycle (#1499)
- Enhanced documentation link checking and CI linting with `lint-extra` (#1427)

## Fixes

- Resolved 14 dead links in example configuration README files (#1427)



## praxis-proxy/conventions (watch)


### Changes

## Infra

- Added Twinkll Sisodia as an AI reviewer to the Praxis conventions repository to enhance documentation review processes (#46).


## praxis-proxy/enhancements (watch)


### Changes

## Features

- Propose adding a bounded job queue with worker pool and per-job timeout to enable background job processing in core (#36).

## Infra

- Update GitHub Actions dependency `actions/create-github-app-token` from 3.2.0 to 3.3.0 to ensure compatibility and security (#26).


## praxis-proxy/experimental (watch)


### Changes

## Infra

- Repaired supply-chain and Markdown checks in CI to ensure consistency across open PRs (#74).
- Updated `docker/login-action` dependency to version 4.8.0 for improved GitHub Actions integration (#67).
- Upgraded `ubi9/ubi-minimal` base image to version 9.9 for potential security and performance improvements (#72).


## praxis-proxy/gateway-controller (watch)


### Changes

## Features

- Add Tenant CRD with optional authorized identities/credentials and Ready condition in status (#58).
- Introduce guard rails and limits as part of v1alpha1 API scope for future implementation (#69).

## Performance

- Consolidate test targets into a comprehensive `make test` suite to streamline verification and testing processes (#76).

## Fixes

- Fix `joinValidationErrors` truncation to preserve first error content and improve error reporting (#74).
- Ensure e2e test suite fails if it cannot connect to a cluster and improve deployment reliability in kind-up (#73).

## Breaking or deprecations

- Move away from generic protocols to specific inference and MCP config definitions in API design (#31).

## Infra

- Add automated container image building and publishing to GHCR via GitHub Actions (#57).
- Enable ginkgo with race detection and test randomization for more robust testing (#47).


## praxis-proxy/grid (watch)

### Releases
- [v0.3.1](https://github.com/praxis-proxy/grid/releases/tag/v0.3.1) — 2026-11-13: Grid v0.3.1
### Changes

## Features

- Publish the `AgentToAgentProvider` CRD contract and installation artifacts for the first A2A control-plane integration (#366).
- Allow local TLS dial to present the grid certificate for mtls_only InferenceProviders (#593).

## Performance

- Invalidate metrics cache when InferenceProviders change to ensure accurate reporting (#578).

## Fixes

- Restore reliable dependency checks on Rust 1.96 to ensure nested Gateway workspace analysis (#603).
- Add model and site change coverage for Local membership in e2e tests (#592).

## Infra

- Prepare release v0.3.1 with fixes for Local membership states and legacy Service Endpoints (#594).
- Make FIPS optional for combined-site qualification to enable default testing with standard images (#575).

### Highlights
- New release **v0.3.1** — Grid v0.3.1

## praxis-proxy/operator (watch)


### Changes

## Features

- Added operator-owned rollout reference resources to support praxis-proxy/praxis#1494, including default replica preservation and support for `praxis.sh/replicas` annotation (#24).

## Infra

- Updated dependencies including `serde_json` and `tokio` via Dependabot (#18).
- Added FOSSA license scan report and status badge to README for improved compliance tracking (#20).


## praxis-proxy/policy (watch)


### Changes

## Features

- Added support to fetch request-time facts before making policy decisions, enabling more accurate authorization based on dynamic data like account state or risk results (#287).

## Docs/Brainstorming

- Documented requirements and design considerations for revocation and transaction tokens, serving as a foundation for future implementation (#284).


## praxis-proxy/praxis-proxy.github.io (watch)


### Changes

# Summary of Recent Changes in `_ungrouped` Module

## Features
- Added a guided setup path from first setup to configuration, improving user onboarding (#37).
- Published enhancement proposals from the enhancements repo, enabling centralized proposal tracking (#47).
- Introduced metadata-driven discovery cards for AI APIs, providers, and operator recipes, making them easier to find (#42).

## Fixes
- Aligned onboarding links and release context to ensure consistency in AI setup flows (#36).
- Enabled tracking of AI 0.10 and alpha releases in documentation, ensuring up-to-date content (#41).

## Infra
- Updated `sass-embedded` to version 1.107.1 for improved CSS processing (#40).
- Auto-merged documentation update pull requests once checks pass, streamlining the release process (#46).
- Validated refreshed documentation snapshots to ensure consistency in CI/CD workflows (#43).

## Dependencies
- Updated `cncf/prow-github-actions` to version 3.5.0 for improved CI/CD integration (#39).
- Updated `zizmorcore/zizmor-action` to version 0.8.1 for improved automation (#38).
- Updated `gohugoio/hugo` to version 0.169.0 for improved static site generation (#30).

## Other
- Updated contributing links to point directly to the dedicated `CONTRIBUTING.md` documents (#34).
- Ensured automated commits for documentation updates include DCO sign-off (#45).


