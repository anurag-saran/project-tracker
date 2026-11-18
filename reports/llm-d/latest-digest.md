# llm-d digest — 2026-11-18

_Since 7d · generated 2026-11-18T17:46:16Z_

## TL;DR for this week

- Release llm-d/llm-d-batch-gateway@v1.1.0-rc1
- Release llm-d/llm-d-batch-gateway@v1.0.1-rc1
- Release llm-d/llm-d-batch-gateway@v1.0.1
- Release llm-d-incubation/llm-d-validate@v0.1.0
- Release llm-d-incubation/llm-d-scaling-manager@v0.11.0

## llm-d/llm-d (core)


### docker

## Features

- Added initial support for Intel XPU in the `omni-serving` text-to-video task using vLLM-Omni and the `Wan-AI/Wan2.1-T2V-1.3B-Diffusers` model (#2970).

## Infra

- Updated Dockerfile and CI workflows to include configurations for the new Intel XPU vLLM-Omni setup (#2970).

**First-time contributors:** sihancx
### guides

## Features

- Added GKE platform support and a nightly GKE E2E lane for the **Fast Model Actuation + KEDA** guide (#3041).
- Introduced a nightly GKE E2E lane for the **Workload Autoscaling: KEDA + EPP** path (#3042).
- Added GKE platform support and a nightly GKE E2E lane for the **Fast Model Actuation (FMA)** guide (#3040).
- Added initial aggregated Intel XPU support for the `omni-serving` text-to-video task with vLLM-Omni (#2970).

## Infra

- Generated UCX kernel config for the running kernel in AMD CI to address crashes due to missing ROCm dmabuf support (#3039).

**First-time contributors:** sheralskumar, sihancx
### release

# Summary of Recent Changes in `llm-d/llm-d` (Module: release)

## Features
- Added GKE platform support and a nightly GKE E2E lane for the **Fast Model Actuation + KEDA** guide (#3041).
- Added a nightly GKE E2E lane for the **Workload Autoscaling: KEDA + EPP** path (#3042).
- Added GKE platform support and a nightly GKE E2E lane for the **Fast Model Actuation (FMA)** guide (#3040).

## Infra
- Introduced new GitHub Actions workflows for GKE E2E testing across multiple lanes (#3040, #3041, #3042).
- Updated Slack notification configurations to include new workflows and lanes (#3040, #3041, #3042).



## llm-d-incubation/llm-d-fast-model-actuation (watch)


### Changes

## Features

- Require launcher inference port pools to standardize port allocation and remove legacy configurations (#835).
- Document the deletion of unbound launchers to align API comments and documentation (#838).

## Performance

- Add `shellcheck` pre-commit hook and fix all warnings to improve code quality and maintainability (#819).

## Fixes

- Update `docker/login-action` to version 4.8.0 for improved security and compatibility (#839).
- Bump `github.com/spf13/pflag` to version 1.1.0 for bug fixes and improved functionality (#832).


## llm-d-incubation/llm-d-lens (watch)


### Changes

## Features

- Enable DisaggregatedSet and Slice deployment and evaluation, allowing more flexible configuration across deployment and evaluation workflows (#133).
- Add bounded BLIS topology search over explicit tensor-parallel and replica grids, preserving pipeline/data parallelism (#131).

## Performance

- Add bounded BLIS subprocess execution to launch managed binaries through shared process infrastructure, improving execution control (#127).
- Compile BLIS deployment bundles and workloads for efficient deployment (#122).

## Fixes

- Preserve AIC hardware identity and prediction availability by resolving systems through hardware profiles and ignoring conflicting device models (#121).

## Infra

- Write kubeconfigs atomically and prevent engine instances from being orphaned during cleanup, improving cluster management safety (#124).


## llm-d-incubation/llm-d-planner (watch)


### Changes

## Fixes

- Fixed a typing mistake in `getattr()` invocations that caused zero reported stats when using the local library Planner (#357).


## llm-d-incubation/llm-d-resiliency-operator (watch)


### Changes

## Fixes

- Allows the unstale workflow to remove stale labels from PRs by granting `pull-requests: write` permissions (#84).


## llm-d-incubation/llm-d-scaling-manager (watch)

### Releases
- [v0.11.2](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.2) — 2026-11-17: llm-d-scaling-manager v0.11.2- [v0.11.1](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.1) — 2026-11-15: llm-d-scaling-manager v0.11.1- [v0.11.1-rc2](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.1-rc2) — 2026-11-14: llm-d-scaling-manager v0.11.1-rc2- [v0.11.0](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.0) — 2026-11-12: llm-d-scaling-manager v0.11.0
### Changes

## Features

- Added support for scaling DisaggregatedSet roles, enabling more flexible management of prefill/decode objects (#154).
- Introduced a capacity planner API and whatif serve functionality to help operators evaluate fleet sizing (#93).
- Implemented the ability to determine how many prefill and decode replicas are needed over a day, enabling better fleet planning (#166).

## Fixes

- Fixed an issue with the preflight check job, ensuring it reads settings with the controller parser and avoids issues during re-installation (#86).
- Addressed a bug where a cold plan at specific replica counts took too long to execute, reducing the runtime significantly (#128).
- Fixed installation against Prometheus instances serving plain HTTP by allowing `--allow-http` (#141).

## Performance

- Improved the performance of cold capacity planning requests, reducing execution time from over an hour to under 15 seconds (#128).

## Infra

- Added a read-only preflight check job for installation from release files, improving the reliability of deployment checks (#76).
- Enhanced the install process with two commands (`admin-setup` and `admin-finish`) for easier deployment (#137).

### Highlights
- New release **v0.11.2** — llm-d-scaling-manager v0.11.2
- New release **v0.11.1** — llm-d-scaling-manager v0.11.1
- New release **v0.11.1-rc2** — llm-d-scaling-manager v0.11.1-rc2
- New release **v0.11.0** — llm-d-scaling-manager v0.11.0

## llm-d-incubation/llm-d-validate (watch)

### Releases
- [v0.1.0](https://github.com/llm-d-incubation/llm-d-validate/releases/tag/v0.1.0) — 2026-11-14: llm-d-validate v0.1.0
### Changes

## Features

- Added `llm-d-validate`, an end-to-end validation tool for model serving stacks, with support for statistical checks over declared samples (#5, #43).
- Introduced profile `extends` functionality, allowing profiles to inherit from other profiles or lists of profiles (#17, #35).
- Added `llmdv plan` command, listing what verification would run or skip based on selectors (#34).

## Performance

- Improved profile parsing with a strict module, reducing errors and improving consistency (#15).
- Optimized results reading with a strict check, enhancing reliability and documentation of optional fields (#32).

## Fixes

- Fixed error reporting in profile loading, naming the file and path of every load error (#16).
- Ensured exit codes are consistent and documented, with clear class and meaning (#19, #21).
- Corrected out-of-date documentation and removed repeated content (#68).

## Breaking or deprecations

- Exit codes for certain errors have changed, such as `llmdv compare` exiting with code `3` instead of `4` for unusable results stores (#20).
- Refused loading profiles with unknown top-level keys or malformed ingress IDs (#63).

## Infra

- Added governance files, GitHub templates, and shared CI workflows for the repository (#1).
- Restructured the repository to align with conventions of other llm-d projects (#3).

### Highlights
- New release **v0.1.0** — llm-d-validate v0.1.0

## llm-d/.project (watch)


### Changes

## Infra

- Updated the `artwork` field in `project.yaml` to point to the CNCF's official artwork repository for consistent project branding (#4).


## llm-d/llm-d-async (watch)


### Changes

## Fixes

- Added authentication for Prometheus gates when querying Google Managed Prometheus, ensuring secure access (#547, #539).
- Made the enqueue script idempotent to handle retries with go-redis, preventing duplicate entries (#522).
- Introduced warnings and fail-closed behavior for misconfigured GMP CA certificates to improve operator visibility and reliability (#553, #559).

## Features

- Enabled Prometheus gates to authenticate with a bearer token and CA certificate, supporting secure Prometheus API queries (#539).

## Refactor

- Removed a dead flag-driven GMP gate path from the flow control module, cleaning up unused code (#554).

## Performance

- Improved the visibility and reliability of the SQLFlow broker backlog source by marking it as available on successful reads (#552).

## Infra

- Updated Go dependencies with 5 critical security and performance improvements (#537).


## llm-d/llm-d-autoscaling (watch)


### Changes

## Features

- Added a new evaluation protocol with step 1, "Static signal analysis," for checking KEDA autoscaling configurations (#1612).
- Introduced a `scenario-sanity-check` skill to validate KEDA scaling scenarios end-to-end against real clusters (#1618).

## Performance

- Updated staging benchmark scenarios to be compatible with llm-d-router v1.0.0 and vLLM v0.31.0, fixing broken EPP plugin configurations (#1620).
- Updated vLLM-backed benchmark overlays to use vLLM v0.31.0 for more accurate performance evaluation (#1611).

## Fixes

- Fixed the `run-benchmark` skill to support git worktree checkouts, resolving path assumptions that broke in such environments (#1617).
- Enabled `/lgtm` comments to write commit statuses by granting the Prow Commands workflow the necessary permissions (#1615).

## Infra

- Added a verdict for the default KEDA-EPP inflight configuration using step 1 of the evaluation protocol (#1613).
- Added a verdict for the `npd-fcoff` work-rate law scenario in the staging environment (#1619).


## llm-d/llm-d-batch-gateway (watch)

### Releases
- [v1.0.1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.1) — 2026-11-16: v1.0.1- [v1.0.1-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.1-rc1) — 2026-11-16: v1.0.1-rc1- [v1.1.0-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.1.0-rc1) — 2026-11-12: v1.1.0-rc1 (deprecated, use v1.0.1)
### Changes

## Fixes

- Ensured job ownership is checked on every progress interval to prevent stale or unauthorized job modifications (#720).
- Fixed S3 large stream output publishing by using server-side multipart copy to avoid memory issues (#785).

## Features

- Added support for carrying the job tenant in async request metadata to enable proper quota enforcement based on tenant information (#778).

### Highlights
- New release **v1.0.1** — v1.0.1
- New release **v1.0.1-rc1** — v1.0.1-rc1
- New release **v1.1.0-rc1** — v1.1.0-rc1 (deprecated, use v1.0.1)

## llm-d/llm-d-benchmark (watch)


### Changes

# Summary of Recent Changes in `_ungrouped` Module

## Features
- Added a base class and kind registry for artifacts, enabling new types of benchmark reports to be plugged into the system (#2128).
- Introduced a client-side speculative prefill recipe for multi-turn chat workloads, improving the efficiency of inference performance testing (#2152).

## Performance
- Enhanced the `calibrate-serving-capacity` process by waiting for the pool to drain before proceeding, ensuring accurate R measurements (#2141).
- Improved the autoscaling sizing report by adding demand p95 and an optional demand series for better capacity planning (#2149).

## Fixes
- Ensured the harness ServiceAccount exists before ephemeral smoketest pods are created, preventing health check failures (#2181).
- Fixed an issue where the HuggingFace model access check used `model_info` instead of `auth_check`, improving reliability (#2137).
- Addressed a problem where scaled-to-zero stacks failed to wake up before verifying model endpoints, preventing false negatives in health checks (#2188).

## Breaking or deprecations
- No major breaking changes reported in the provided PRs.

## Infra
- Updated the FMA chart version and launcher/requester image tags to v0.8.0, improving compatibility and performance (#2157).
- Rendered KEDA ScaledObject templates with additional parameters like `fallback`, `ignoreNullValues`, and `scalingModifiers`, enhancing flexibility (#2180).
- Bumped the `pypa/gh-action-pypi-publish` dependency to version 1.14.3, improving CI/CD reliability (#2130).
- Enabled the unstale workflow to remove labels from PRs, improving repository maintenance (#2135).


## llm-d/llm-d-inference-sim (watch)


### Changes

## Fixes

- Exit with non-zero status when the simulator or dataset tool fails to start, ensuring errors are properly signaled to the caller (#920).
- Count only started requests in latency histograms and running gauge to avoid including failed or invalid requests (#915).
- Fix streamed `/v1/responses` events to end correctly at `max_output_tokens`, aligning with vLLM behavior (#924).

## Performance

- Reuse render connections safely across vLLM's keep-alive timeout to reduce overhead and improve performance (#910).
- Include queue time in the vLLM time to first token metric for more accurate latency tracking (#878).

## Features

- Add `--stream-interval N` flag to control how tokens are grouped in streamed responses, aligning with vLLM behavior (#777).
- Make the dataset conversion examples in the documentation runnable with the new `ds_tool` command (#929).

## Infra

- Bump go dependencies including `go.opentelemetry.io/otel/sdk` to 1.47.0 and others for security and compatibility (#911, #884, #928).

## Other

- Fix rendering errors to return proper 400 status codes from the render service (#898).
- Send empty arguments, text, and annotations in `/v1/responses` items to align with expected output (#926).


## llm-d/llm-d-latency-predictor (watch)


### Changes

## Fixes

- Pins configuration settings in unit tests to ensure consistent test behavior and removes conditional assertions for ensemble mode, improving test reliability (#109).


## llm-d/llm-d-prism (watch)


### Changes

## Features

- Added support for S3-compatible storage backend for the Prism Results Store, enabling seamless integration with various object storage solutions (#198).


## llm-d/llm-d-router (watch)


### Changes

## Features

- Added support for upstream vLLM gRPC P/D and EC disaggregation in both the coordinator and sidecar, enabling more flexible and efficient model inference (#4013, #4011).
- Introduced an opt-in `explorationBudget` parameter for the `weighted-random-picker` scheduling plugin to allow for more dynamic exploration in scheduling (#3972).
- Enhanced the OpenAI parser to claim audio transcription endpoints, ensuring correct handling of `/v1/audio/transcriptions` and `/v1/audio/translations` (#3964).

## Performance

- Optimized multimodal prefix hashing to avoid repeated scans of media features, improving performance in token block processing (#4315).

## Fixes

- Fixed the issue where the `approx-prefix-cache-producer` was indexing prompt block hashes for failed requests, which could lead to incorrect cache state (#3938).
- Corrected the handling of `cache_salt` in the vLLM KV cache to ensure it's preserved after later multimodal items in the many:1 realignment (#4138).
- Ensured that the `precise-prefix-cache-producer` registers the endpoint-notification source correctly in pull mode, avoiding missed updates (#4258).

## Breaking or deprecations

- No breaking changes or deprecations identified in the provided PRs.

## Infra

- Improved the `thunder-agent` plugin by simplifying its configuration and parameter handling, making it more maintainable and easier to configure (#4174).
- Refactored the TLS version and cipher parsing logic across EPP, sidecar, and coordinator to use k8s component-base helpers, ensuring consistency and reliability (#3733).


## llm-d/llm-d.github.io (watch)


### Changes

## Features

- Introduces a detailed blog post on implementing multi-tenant and multi-priority model serving architecture using llm-d (#496).  
- Provides visual aids and technical insights into efficiently sharing GPU resources across multiple teams (#496).  
- Enhances the blog section with new metadata entries for authors and tags (#496).


