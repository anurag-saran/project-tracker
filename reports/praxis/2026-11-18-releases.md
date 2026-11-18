# praxis releases — 2026-11-18

_Generated 2026-11-18T18:16:54Z_

**Docs:** [https://praxis.fast](https://praxis.fast) · [https://praxis.fast/ai/](https://praxis.fast/ai/)
## TL;DR

- praxis-proxy/ai v0.11.0: 8 feature(s)
- praxis-proxy/praxis v0.8.0: 7 feature(s)
- praxis-proxy/grid v0.3.1: 3 feature(s)
- praxis-proxy/grid next RC/train: v0.3.0-rc.4
- praxis-proxy/policy v0.6.0: 11 feature(s)

## praxis-proxy/ai (core)

Release page: [https://github.com/praxis-proxy/ai/releases](https://github.com/praxis-proxy/ai/releases)

### Shipped (what went in)

#### [v0.11.0](https://github.com/praxis-proxy/ai/releases/tag/v0.11.0) — 2026-11-13
- Policy crypto backend support — Bumped Praxis to 0.8.0 and selected the Policy crypto backend for enhanced security.
- GPU nightly guardrails — Repaired setup and qualification for GPU nightly builds to ensure stability.
- OpenAPI reference refresh — Updated the pinned OpenAPI reference for better API compatibility and clarity.
- Rate-limit error conformity — Ensured rate-limit errors returned are conformant with expected standards.
- Pre-1.0 release labeling — Marked pre-1.0 builds as GitHub pre-releases for clearer version tracking.
- Message API version configuration — Configured translated Messages API version for Anthropic compatibility.
- Onboarding guide — Added a guide for first requests and provider setup to improve user onboarding.
- Experimental image and PostgreSQL store documentation — Covered experimental features for image and PostgreSQL store in CLI-VLLM documentation.

#### [v0.10.0](https://github.com/praxis-proxy/ai/releases/tag/v0.10.0) — 2026-11-06
- Cross-provider failover — Add support for API translation and failover across different inference providers.
- Cargo xtask bump-pins — Introduce a command and workflow to automate version pin updates.
- NeMo message slices — Evaluate message slices from NeMo concurrently for improved performance.
- Multi-format message extraction — Support extracting messages in multiple formats for guardrails.
- Skip unchanged cache updates — Improve performance by skipping cache updates for unchanged conversations.
- Reject unsupported Code Interpreter tools — Prevent responses from using unsupported Code Interpreter tools.
- Codex apply_patch grammar support — Enable compatibility with Codex's apply_patch grammar via client tools.
- Filtered execution for callouts — Require filtered execution for filter callouts in documentation.
- Weekly bump workflow — Add a scheduled workflow to regularly update dependencies.

#### [v0.9.0](https://github.com/praxis-proxy/ai/releases/tag/v0.9.0) — 2026-10-30
- Pi coding harness support — Add support for the Pi coding harness alongside Claude Code, Codex, and OpenCode.
- Response-store TTL and background reaper — Introduce time-to-live for stored responses and a background process to clean expired entries.
- Runtime cryptographic readiness checks — Add checks to ensure cryptographic operations are ready at runtime.
- Validate web-search queries before dispatch — Ensure web-search queries are validated before being sent for processing.
- Compact reasoning and validate web-search events — Improve compact reasoning and add validation for web-search events.
- Accept schema-valid empty conversations — Allow empty conversations that conform to the expected schema in explicit compact mode.

#### [v0.8.0](https://github.com/praxis-proxy/ai/releases/tag/v0.8.0) — 2026-10-22
- Preserve Multi-Query Web Search Calls — Preserves multi-query web search calls in OpenAI interactions.
- Enforce Operator Minimum Approval Policy — Enforces a minimum approval policy for Responses tool dispatch in MCP.
- Make Tool Metadata Trust Explicit — Makes tool metadata trust explicit and enforces read-only settings in MCP.
- Enforce Connector-Only Routing — Enforces connector-only routing for MCP tools.
- Translate OpenAI Chat for Anthropic — Translates OpenAI chat formats for Anthropic providers.
- Model/Cluster-Labeled LLM Gateway Metrics — Adds model/cluster-labeled LLM gateway metrics and fixes TTFT model issues.
- Publish Exact-Commit CI Evidence — Publishes exact-commit CI evidence for release transparency.
- Hide Server Configuration Details — Hides server configuration details from client-facing errors.
- Ai Guardrails Ne Mo Mask / Redact Action — Implements AI guardrails for masking/redacting actions.
- Experimental Responses and Agentic Loops — Marks Responses and agentic loops as experimental features.

#### [v0.7.0](https://github.com/praxis-proxy/ai/releases/tag/v0.7.0) — 2026-10-16
- Token Rate Limit Enforcement — Enforce organization, team, and user budgets independently for token usage.
- Custom-Tool Added Events — Restored custom-tool added events to include required input parameters.
- Model-to-Header Filter — Skip the filter when headers are already present in the request.
- GPU Image Reuse — Publish and reuse GPU images from nightlies to improve efficiency.
- Performance Optimization — Avoid re-parsing outbound body for stream boolean to enhance response performance.

#### [v0.6.0](https://github.com/praxis-proxy/ai/releases/tag/v0.6.0) — 2026-10-09
- Intelligent Route — Serve authoritative no-route overlays for improved routing decisions.
- Guardrails — Screen IRR tool results to enhance safety and compliance.
- Responses Opt-Out — Allow chains to opt out of initializing Responses state for flexibility.
- OpenAI SDK 3.x Support — Add dual-lane test support for OpenAI SDK 3.x.
- Qwen3 Serving — Serve Qwen3 models without thinking, guarded by a nightly test.
- Provider-Neutral Classifier — Expose a classifier for use across different AI providers.
- Responses State Handling — Improve handling of ambiguous namespace names in Responses.
- Responses Conformance Docs — Add documentation for Responses stateful-loop conformance with drift guard.
- Vertex Streaming — Constrain streaming candidate and tool-slot admission for better control.
- Client Tool Compatibility — Improve performance by moving owned JSON values for better tool compatibility.


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [#2027 feat(anthropic): execute Messages MCP connector toolsets in Praxis](https://github.com/praxis-proxy/ai/issues/2027) _(rfc · open RFC/proposal)_ — ## Parent

Part of #148. Follow-up to #638.

## Context

Anthropic's Messages API MCP connector (`mcp-client-2025-11-20` beta) lets direct Anthropic SDK users declare remote MCP servers (`mcp_serve...- [#2023 openai_file_resolve: Files API targets a cluster instead of files_api_url (breaking)](https://github.com/praxis-proxy/ai/issues/2023) _(rfc · open RFC/proposal)_ — ## Summary

`openai_file_resolve` sends Files API calls (`file_id` resolution) to `files_api_url`, a URL staged through `FilteredSubrequestExecutor`. Replace it with a cluster reference. The `file_...- [#2024 web search: optional cluster override instead of base_url; api_key optional with user_credential](https://github.com/praxis-proxy/ai/issues/2024) _(rfc · open RFC/proposal)_ — ## Summary

`openai_web_search_dispatch` and `anthropic_web_search` call a built-in provider endpoint, or an optional `base_url` override. Keep the built-in default, so `provider: brave` alone stil...- [#2022 openai_file_search_dispatch: target a cluster instead of vector_store_url (breaking)](https://github.com/praxis-proxy/ai/issues/2022) _(rfc · open RFC/proposal)_ — ## Summary

`openai_file_search_dispatch` sends vector-store calls to `vector_store_url`, a URL staged through `FilteredSubrequestExecutor`. Replace it with a cluster reference.

Part of epic #2015...- [#2020 openai_responses_compact: target a cluster instead of inference_url (breaking)](https://github.com/praxis-proxy/ai/issues/2020) _(rfc · open RFC/proposal)_ — ## Summary

`openai_responses_compact` sends its anonymous summarization call to `inference_url` through raw `SubRequestClient::execute_url`, with its own `allow_private_inference_url` opt-in. Repl...- [#2021 ai_guardrails NeMo: target a cluster instead of provider.endpoint (breaking)](https://github.com/praxis-proxy/ai/issues/2021) _(rfc · open RFC/proposal)_ — ## Summary

`ai_guardrails` with the NeMo provider sends its checks to `provider.endpoint`, a URL staged through `FilteredSubrequestExecutor`. Replace it with a cluster reference.

Part of epic #20...- [#2019 external_metering: target a cluster instead of metering_url (breaking)](https://github.com/praxis-proxy/ai/issues/2019) _(rfc · open RFC/proposal)_ — ## Summary

`external_metering` sends its balance check and usage report to `metering_url` through raw `SubRequestClient::execute_url`, with its own `allow_private_endpoint` opt-in. Replace the URL...- [#2018 http_callout: target a cluster instead of target.url (breaking)](https://github.com/praxis-proxy/ai/issues/2018) _(rfc · open RFC/proposal)_ — ## Summary

`http_callout` sends its request to `target.url` through raw `SubRequestClient::execute_url`, so it skips the outbound filter chain, and `target.allow_private_addresses` is its own priv...
## praxis-proxy/praxis (core)

Release page: [https://github.com/praxis-proxy/praxis/releases](https://github.com/praxis-proxy/praxis/releases)

### Shipped (what went in)

#### [v0.8.0](https://github.com/praxis-proxy/praxis/releases/tag/v0.8.0) — 2026-11-07
- TLS and HTTPS health probes — Adds support for secure health checks using TLS and HTTPS.
- Experimental Hyper Backend — Introduces an experimental backend using Hyper for improved performance or features.
- Inline clusters inherit top-level endpoints — Allows configuration of inline clusters to inherit endpoints from the top-level configuration.
- Support diagnostics reference — Adds documentation reference for support diagnostics, aiding in troubleshooting.
- Make kv store backend creation explicit — Enhances clarity and control in the creation of key-value store backends.
- Add fossa action — Integrates Fossa for dependency analysis and security checks in the CI pipeline.
- Gate Linux-only test helpers to macOS builds — Ensures Linux-specific test helpers are not used on macOS, improving build reliability.

#### [v0.7.5](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.5) — 2026-10-21
- Request-Head Filter Lifecycle — Adds a new phase for classifying request headers.
- Endpoint Slow Start — Gradually ramps up traffic to new or recovered endpoints.
- Hedged Attempts & Timeouts — Core logic for managing parallel requests and cancellations.
- Protocol Backend Seam — Enables plugging in different protocol backends.
- FIPS Crypto Readiness — Configurable settings and tests for FIPS compliance.
- Slow-Start Endpoint Weights — Applies dynamic weights during endpoint selection.
- Policy Context Headers/Meta — Exposes headers and metadata configuration in policies.

#### [v0.7.4](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.4) — 2026-10-12
- Access Log Sinks — Add stdout, file, and syslog sinks for access_log filtering.
- Headers Present Condition — Introduce `headers_present` predicate for conditional filtering.
- Inherit Filter Chain Conditions — Allow conditions to be inherited from named filter chains.
- Admin/Metrics Port Separation — Separate admin and metrics ports, removing `allow_public_admin` requirement for metrics.
- Preserve Query Params Only — Add `preserve_query_params_only` operation for URL rewrite filtering.
- OpenTelemetry Span Linking — Link HTTP spans across proxy hops for improved observability.
- Per-Route Hedge Policy — Configure hedge policies on a per-route basis in the router.
- Policy-Aware Subrequests — Execute URL subrequests with policy-aware execution in core.
- Per-Cluster Base Path — Define a base path for upstreams per cluster for routing flexibility.

#### [v0.7.3](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.3) — 2026-10-03
- Cluster trust — Trust a named private upstream per cluster.
- Rate-limit shadow mode — Observe rate limits without enforcing them.
- Host and SNI derivation — Derive upstream Host and SNI from selected endpoint.
- Branch-chains matching — Match on_result with contains, not, and any_of.
- Env var credential injection — Example for injecting credentials via environment variables.
- Gateway example — Added example for env_var credential injection gateway.
- Resilience test coverage — Fill gaps in resilience and failure-mode tests.

#### [v0.7.2](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.2) — 2026-09-30
- Centralized IP Address Classification — Centralizes logic for classifying IP addresses within praxis-core.
- File Descriptor Handling — Enhances management of file descriptors for improved resource control.
- Subrequest Stream Deadline Recap — Ensures absolute stream deadlines are properly applied to live bodies in subrequests.

#### [v0.7.1](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.1) — 2026-09-26
- Policy Egress — Permit a pinned private endpoint for policy egress.
- Filter Scheduling — Infer bound-body scheduling from filter conditions.
- SNI Matching — Introduce consolidated `SniMatcher` for improved SNI handling.
- FIPS Compliance — Expand testing and prove runtime behaviors for FIPS compliance.


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [#1474 refactor(filter): move shared AI credential helpers into Core](https://github.com/praxis-proxy/praxis/issues/1474) _(rfc · open RFC/proposal)_ — ### What?

Move AI's generic credential helpers into a shared Core module:

- `apis/src/credential_source/`: bounded value/env/file loading, file rotation, secret handles, and bearer-header formatt...- [#1218 A support-bundle command for collecting diagnostics](https://github.com/praxis-proxy/praxis/issues/1218) _(rfc · open RFC/proposal)_ — When someone hits a problem there is no single way to capture the state we would need to help. Add a command that gathers one sanitized archive: the effective config (reusing the redaction we alrea...- [#1408 v1: capacity signals and stress tests for safe autoscaling](https://github.com/praxis-proxy/praxis/issues/1408) _(rfc · open RFC/proposal)_ — For v1, we need to know a replica is running out of room while there's still time to add capacity. Part of #1285; use the operational work in #1067.

- Expose generic capacity/autoscaling signals t...- [#1384 policy: warn when an authenticated credential is forwarded upstream](https://github.com/praxis-proxy/praxis/issues/1384) _(rfc · open RFC/proposal)_ — ### What?

A load-time warning when a `policy` filter authenticates callers with an `identity/*` plugin but
the header it reads the credential from is still forwarded upstream: the header isn't gov...- [#1375 `Service` which outlive filters](https://github.com/praxis-proxy/praxis/issues/1375) _(rfc · open RFC/proposal)_ — ### What?

Add a `Service` abstraction and `ServiceRegistry` so filters can hold long-lived shared resources (connection pools, SDK clients, circuit breakers) that survive filter-chain hot-reload a...- [#1300 Reference Kubernetes deployment for multi-replica Praxis](https://github.com/praxis-proxy/praxis/issues/1300) _(rfc · open RFC/proposal)_ — > **Note**: May need to be moved to https://github.com/praxis-proxy/operator

There is no supported way to run Praxis as a replica set. The repo ships a `Containerfile` (exposing 8080 and 9902) and...- [#1299 Valkey KvStore backend for multi-replica state](https://github.com/praxis-proxy/praxis/issues/1299) _(rfc · open RFC/proposal)_ — Every piece of runtime state in Praxis is per-process, so replicas cannot share anything. The only Valkey client in praxis's dependency graph today is the policy engine's session store (`praxis-pol...- [#1298 State interface: KvStore trait, StateRegistry, and state.kv config with an in-memory default](https://github.com/praxis-proxy/praxis/issues/1298) _(rfc · open RFC/proposal)_ — The Valkey driver in this epic has nothing to plug into yet. Core state today is the synchronous `KvBackend` trait and a `KvStoreRegistry` whose `get_or_create` always builds an in-memory store (`c...
## praxis-proxy/experimental (watch)

Release page: [https://github.com/praxis-proxy/experimental/releases](https://github.com/praxis-proxy/experimental/releases)

### Shipped (what went in)

_No stable releases stored yet. Run fetch / releases with a GitHub token._

### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [#2 epic: switchyard_route — Mixture-of-Models routing POC around NeMo Switchyard](https://github.com/praxis-proxy/experimental/issues/2) _(rfc · open RFC/proposal)_ — Originating discussion: https://github.com/orgs/praxis-proxy/discussions/976
(maintainer +1: https://github.com/orgs/praxis-proxy/discussions/976#discussioncomment-18019663)
Parent epic: https://gi...
## praxis-proxy/grid (watch)

Release page: [https://github.com/praxis-proxy/grid/releases](https://github.com/praxis-proxy/grid/releases)

### Shipped (what went in)

#### [v0.3.1](https://github.com/praxis-proxy/grid/releases/tag/v0.3.1) — 2026-11-13
- Distributed Token Quota Support — Requires Praxis AI image with `token-rate-limit-filter` for quota example deployments.
- Local TLS Dial with Grid Certificate — Gateway now presents the grid certificate on local TLS connections.
- Improved Operator Metrics — Metrics cache is invalidated when providers change for accurate monitoring.

#### [v0.3.0](https://github.com/praxis-proxy/grid/releases/tag/v0.3.0) — 2026-11-10
- Distributed Token Quota Support — Requires Praxis AI image with `token-rate-limit-filter` for quota-based deployments.
- HA Support with Leader Elections — Enables high availability through leader elections in the operator.
- Route Generated Consumer Config — Operator now routes generated consumer configuration using `grid_site_route`.
- Updated Praxis AI Image — Praxis AI version 0.8.0 is now supported for enhanced functionality.
- Improved Provider Model Discovery — Refactored provider model discovery and selection for better performance.
- Immutable Image References — All container image references are now immutable for consistency and security.

#### [v0.2.2](https://github.com/praxis-proxy/grid/releases/tag/v0.2.2) — 2026-10-22
- Distributed token quota support — Requires Praxis AI image with `token-rate-limit-filter` for quota example deployments.
- Publish discovered models — Operator now publishes discovered models in provider status.
- Go Kubernetes API types — Added Go types for Grid Custom Resource Definitions (CRDs).
- Helm chart updates — Updated Helm charts for grid-operator, praxis-gateway, grid-site, grid-mock-providers, and grid-enrollment to version 0.2.2.
- Hardened grid-gateway values — Improved security and configuration options for grid-gateway Helm chart.
- Immutable container image references — All container image references are now immutable for consistency and reliability.

#### [v0.2.1](https://github.com/praxis-proxy/grid/releases/tag/v0.2.1) — 2026-10-19
- Distributed Token Quota Support — Grid now publishes routing topology and qualification for distributed token quotas, requiring a custom Praxis AI image with the token-rate-limit-filter feature.
- No-Route Revisions — Grid can now publish and serve no-route revisions for flexible routing configurations.
- Local Operator Load Reading — Gateway reads every site's load from the local operator only, improving performance and accuracy.
- Consumer Endpoint Topology — Operator derives consumer endpoint topology from allowlisted providers, enhancing routing and management capabilities.
- Grid Metrics Documentation — Added documentation for Grid metrics to aid in monitoring and analysis.
- Helm Chart Updates — Updated Helm charts for Grid components to version 0.2.1 for easier deployment and management.

#### [v0.2.0](https://github.com/praxis-proxy/grid/releases/tag/v0.2.0) — 2026-10-08
- Distributed token quota support — Requires Praxis AI image with `token-rate-limit-filter` for quota example deployments.
- Administrative provider drain — Allows manual draining of providers via the operator.
- Static weighted provider selection — Enables routing with predefined weights for provider selection.
- DNS endpoint hostname resolution — Resolves DNS hostnames for endpoints in the SWIM protocol.
- Helm chart updates — Updated Helm charts for grid-operator, praxis-gateway, grid-site, grid-mock-providers, and grid-enrollment.
- Container image versioning — Updated container images with specific SHA256 hashes for immutability.
- Immutable image references — All image references are now immutable for consistency and reliability.

#### [v0.1.4](https://github.com/praxis-proxy/grid/releases/tag/v0.1.4) — 2026-09-04
- Provider Selection Groups — Enable stable provider candidate selection and round-robin routing for load balancing.
- Distributed Token Quotas — Allow identity-scoped budget sharing across gateways with Valkey-backed sliding-window state.
- Basic Auth Integration — Support for authentication before quota reservation in distributed token-quota setup.
- Pressure-Aware Admission — Improve routing decisions based on system pressure and provider availability.
- Provider Recovery — Enhance resilience with automatic recovery mechanisms for failed providers.
- Secure SWIM State Validation — Ensure secure and consistent state validation for cluster membership.
- AgentToolProvider Support — Enable integration with AgentToolProvider for extended functionality.
- Quota Persistence — Maintain quota state across consumer restarts for continuity.
- Fail-Closed Admission — Safeguard against quota failures during Valkey outages.
- NetworkPolicy Isolation — Enforce isolation for quota-client access with Kubernetes NetworkPolicy.
- Experimental Features — Include token-rate-limiting and basic-auth filters for advanced use cases.
- Routing State Publication — Expose routing state for consumer configuration and integration.


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.3.0-rc.4](https://github.com/praxis-proxy/grid/releases/tag/v0.3.0-rc.4) (2026-11-04)  - Expose Unavailable Score Reasons — Gateway now provides detailed reasons for unavailable scores.
  - Publish and Route Model Inventories — Operator now publishes and routes discovered model inventories.
  - Distributed Token Quota Support — Grid now publishes routing topology and qualification for distributed token quotas, requiring a custom Praxis AI image with the token-rate-limit-filter feature.
- [v0.3.0-rc.3](https://github.com/praxis-proxy/grid/releases/tag/v0.3.0-rc.3) (2026-10-30)  - Distributed Token Quota Support — Requires Praxis AI image with `token-rate-limit-filter` for quota-based deployments.
  - Model Expiry in CRDs — Adds model expiry support and enables receiving gossiped models in the operator.
  - Local Provider Topology Derivation — Operator now derives topology for every local provider.
  - Site Certificate-Based Gossip Signing — Enhances security by signing state gossip with site certificates.
  - Helm Chart Improvements — Ensures operator config is rendered only when it has a site section.
  - Grid Operator Condition Status Enum — Refactors Condition.status to use an enum for clarity and consistency.
- [v0.3.0-rc.2](https://github.com/praxis-proxy/grid/releases/tag/v0.3.0-rc.2) (2026-10-29)  - Distributed Token Quota Requirement — Praxis AI deployments using distributed token quotas must use an image built with the `token-rate-limit-filter` feature.
  - Helm Chart Updates — Updated Helm charts for Grid components to version `0.3.0-rc.2` for easier deployment and management.
  - Memory Sizing Documentation — Added memory sizing guidance and capacity cross-links for the Gateway component.
  - Fleet Dashboard Release Integration — Brought the Fleet Dashboard onto the main release line for consistent updates.
  - Improved CI/CD Configurations — Bumped dependencies and tuned linting guidelines for better CI performance and code quality.

**Milestones, roadmaps & open RFCs feeding the next drop**
- [#13 feat(observability): emit structured intelligent routing decisions](https://github.com/praxis-proxy/grid/issues/13) _(rfc · open RFC/proposal)_ — ## Summary

Add bounded, structured routing-decision logs to the Praxis AI `intelligent_route` filter so operators can understand how Grid-produced routing state was applied by each Praxis gateway....- [#359 Add the GridGateway CRD](https://github.com/praxis-proxy/grid/issues/359) _(rfc · open RFC/proposal)_ — # THIS DESIGN IS CURRENTLY IN REVIEW SEE DESIGN DOC

## Summary

The gateway is a Helm release, and the operator only patches mounts on a Deployment the chart created. A platform install has no Hel...- [#169 feat(routing): dynamic weighted routing from live metrics](https://github.com/praxis-proxy/grid/issues/169) _(rfc · open RFC/proposal)_ — STRETCH for the Red Hat AI 3.6 technical preview (see `TODO.md`).

Add metrics-based dynamic weighting: automatically and continuously
re-distribute traffic weight across eligible providers from li...- [#136 feat(routing): share session affinity across gateway replicas](https://github.com/praxis-proxy/grid/issues/136) _(rfc · open RFC/proposal)_ — ## Problem

A gateway can keep a session on a selected routing destination by reading a configured request header or cookie and retaining a binding with a TTL. When that binding exists only in one ...- [#168 Publish the Grid to a software catalog (Red Hat certified or community)](https://github.com/praxis-proxy/grid/issues/168) _(rfc · open RFC/proposal)_ — STRETCH for the Red Hat AI 3.6 technical preview (see `TODO.md`).

Investigate and, if feasible, publish the Grid to a software catalog
so it is discoverable and installable through a supported cha...- [#19 Add secure structured logging and observable routing reload failures](https://github.com/praxis-proxy/grid/issues/19) _(rfc · open RFC/proposal)_ — ## Summary

Add a minimal structured-logging baseline for Grid that satisfies the routing-state, governance, security, and privacy contracts without introducing a logging backend or broader telemet...- [#167 test: dogfooding, expanded coverage, and a written manual test plan](https://github.com/praxis-proxy/grid/issues/167) _(rfc · open RFC/proposal)_ — Part of the Red Hat AI 3.6 technical preview MUST list (see `TODO.md`).

Raise confidence for the technical preview through:

- Dogfooding the Grid on representative topologies.
- More unit and int...- [#18 Epic: add optional observability to Grid demos](https://github.com/praxis-proxy/grid/issues/18) _(rfc · open RFC/proposal)_ — ## Goal

Provide an optional, turnkey Prometheus and Grafana experience for the upstream Grid demos while keeping production monitoring-stack ownership outside Grid.

The demo stack should make rou...
## praxis-proxy/policy (watch)

Release page: [https://github.com/praxis-proxy/policy/releases](https://github.com/praxis-proxy/policy/releases)

### Shipped (what went in)

#### [v0.6.0](https://github.com/praxis-proxy/policy/releases/tag/v0.6.0) — 2026-11-06
- Selectable crypto backends — Added support for RustCrypto (default) and OpenSSL FIPS SHA-256 with startup checks and capability reporting.
- FIPS JWT and DPoP verification — Added FIPS-compliant verification for JWTs and DPoP proofs using `jwt-openssl-fips`.
- HTTP query access — Exposed raw HTTP query strings to policy with capability-gated plugin access and redacted diagnostics.
- Audit exporters — Added stdout, stderr, and append-only file audit exporters for OCSF sink compatibility.
- Rate-limit hooks — Added pre- and post-identity rate-limit hooks with scoped configuration and normalized client address.
- In-process rate-limit plugin — Added opt-in `ratelimit/limitador` plugin with client-safe denials and fail-closed handling.
- Valkey CIBA store — Added Valkey-backed CIBA approval store with atomic poll claims and replica-safe redemption.
- Per-issuer DPoP verification — Added per-issuer DPoP proof verification with key-binding attributes and replay guards.
- LLM request access — Added typed LLM request and history access with canonical `llm.*` policy attributes.
- Immutable metadata — Added immutable acquired metadata under `metadata.<instance>.*` for policy and plugins.
- Credential locations for JWT — Added support for header, cookie, and query-parameter credential locations for `identity/jwt`.

#### [v0.5.0](https://github.com/praxis-proxy/policy/releases/tag/v0.5.0) — 2026-10-13
- Vault Credential Delegation — Opt-in `delegator/vault` builtin to read downstream credentials from Vault KV v2 for a user, client, or workload.
- Secret-Backed Header Assertions — Request header assertions can use declared `secret.<name>` values for static upstream credentials, with rotation taking effect on next request after refresh.
- OCSF Audit Sink — Added an OCSF audit sink plugin emitting decision records with optional chained attestations and DSSE signatures for offline verification.
- MCP Annotations Exposure — Exposed MCP tool, resource, and prompt annotations to policy, including `readOnlyHint` and `destructiveHint`, with workload attestation timestamps available for comparison.
- Secret Provider Health Monitoring — Added secret-provider health details via `secrets_health` and atomic value/generation reads through `SecretRef::snapshot`.
- Breaking: Secret Reload Failures — Secret configuration reloads that change `secrets:` now fail; restart required to apply changes, with `secrets_health` for outage detection.
- Breaking: Rust Secret Assertion Changes — Secret assertions add `HttpExtension::secret_headers`; exhaustive struct literals must initialize it, and hosts must preserve it between hooks.
- Breaking: CEL Function Registration — `CelResolver::with_functions` now returns `Result`, with conflicts failing construction and requiring CEL `Env` overloads for custom functions.
- Breaking: CEL String Handling — CEL 0.15 counts Unicode code points instead of UTF-8 bytes in string `size()`, affecting byte limit policies and list-predicate errors.
- Breaking: Removed Constants — Removed eight `CAP_READ_*` and seven `BAG_*_PREFIX` constants for Rust callers, though policy attributes remain available.

#### [v0.4.1](https://github.com/praxis-proxy/policy/releases/tag/v0.4.1) — 2026-10-06
- Optional PDP Decision Cache — Stores Allow/Deny decisions with TTL and entry cap for improved performance without retaining request data.
- Host-Supplied LLM Request Evaluation — PDPs can now evaluate JSON and native tool arguments from host-supplied LLM requests.
- Verdict Audit Sinks and Provenance Logging — Adds durable effect logs and keyed content provenance for enhanced auditing.
- Breaking: Native JSON for Tool Route Args — OPA and CEL now use native JSON for `tool:` route `args`; `RoutePayload` requires `structured`.
- Breaking: Cloned Extensions Limitations — Cloned extensions drop HTTP transport and are limited to `sequential` and `transform` modes.
- Structured Input Validation — Missing or overly deep structured input now results in a deny decision.
- Enhanced Error Handling — PDP-generated errors hide input values for security, and Cedar schemas require `structured_context: true`.
- Audit Logger Default Mode — The reference audit logger uses sink mode when `hooks:` is absent.
- Plugin Panic Containment — Serial and transform plugin panics are now contained and report `plugin_panic`.

#### [v0.4.0](https://github.com/praxis-proxy/policy/releases/tag/v0.4.0) — 2026-09-29
- Named secrets providers — Support for local and Kubernetes-mounted credentials with built-in `file` and `env` providers.
- Vault KV v2 secret provider — Integration with Vault using Kubernetes or AppRole authentication.
- Quota plugin — Opt-in per-principal LLM token budgeting using Limitador.
- `ibmverify` JWT claim mapper — Preset for scalar or array collection claims in JWTs.
- API key resolver — Configure with `provider:` and use through the `api-key` feature with file and HTTP directories.
- JWT claim mapper presets — Documentation on adding and testing provider-specific JWT claim mappers.
- Consolidated extensions — Moved to `praxis-policy-builtins` with one feature per extension.
- Identity claim mapper update — Moved to `praxis_policy_core::identity::mapping` with new configuration requirements.
- Secret provider retry — Exposed `execute_with_retry` for secret providers using the host transport.
- Dependency updates — Replaced `serde_yaml` with `yaml_serde` and updated `regorus` to 0.12.0.

#### [v0.3.1](https://github.com/praxis-proxy/policy/releases/tag/v0.3.1) — 2026-09-22
- Test improvements — Pinned specific test configurations to avoid conflicts in CEL evaluations.

#### [v0.3.0](https://github.com/praxis-proxy/policy/releases/tag/v0.3.0) — 2026-09-18
- Comprehensive PPE documentation — Added tested examples and detailed documentation for PPE.
- CMF extension bag contract — Documented the contract and expanded cross-PDP conformance tests.
- Fail-closed safety invariants — Added a catalog with fault-injection tests for safety.
- Criterion benchmarks — Added performance benchmarks for key operations and throughput.
- Security improvements — Redacted sensitive keys from debug output and updated `rustls` for security.
- Dependency updates — Updated key dependencies including `base64`, CEL, Redis, and others.


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [#325 Replace duplicate Limitador expression checks with a safe upstream error contract](https://github.com/praxis-proxy/policy/issues/325) _(rfc · open RFC/proposal)_ — The embedded limiter pre-evaluates conditions and computed counter keys, then asks Limitador to evaluate them again. It also handles CEL macro locals and catches panics around dependency calls. See...- [#76 feat(apl): address one content part of a message instead of the whole thing](https://github.com/praxis-proxy/policy/issues/76) _(rfc · open RFC/proposal)_ — ## Description

A CMF `Message` is a list of typed `ContentPart`s. An assistant turn is thinking plus text plus two tool calls; a rendered prompt is a list of messages; an A2A artifact is a list of...- [#127 feat(host): inject host-managed backend stores into PPE plugins](https://github.com/praxis-proxy/policy/issues/127) _(rfc · open RFC/proposal)_ — ## Description

PPE already lets an embedding host install one `HttpTransport` and expose its operations to plugins through `HostServices`, `InitExtensions`, and request-scoped `Extensions`. The `p...- [#205 Epic(identity): a shared revocation store, checked by the framework, fed by SSF signals and local quarantine](https://github.com/praxis-proxy/policy/issues/205) _(rfc · open RFC/proposal)_ — ## Description

PPE has no way to stop trusting a credential before it expires. `identity/jwt` verifies tokens offline, the API key directory picks up a revoked key only on its next reload or cache...- [#206 feat(delegation): PPE as a Transaction Token issuer for downstream services that trust it](https://github.com/praxis-proxy/policy/issues/206) _(rfc · open RFC/proposal)_ — ## Description

When PPE obtains a downstream credential today, it exchanges a token at an identity provider, and the provider decides what the new token says. With Keycloak 26.8 that limits what a...- [#10 Epic: PPE ODIS / AIMS Compliance](https://github.com/praxis-proxy/policy/issues/10) _(rfc · open RFC/proposal)_ — ## Summary

Close the remaining gaps between PPE and two agent identity standards: NVIDIA ODIS (Open Delegation & Identity Standard, v0.1) and IETF AIMS (`draft-klrc-aiagent-auth-03`). The goal is ...- [#153 feat(apl): authorize effective tool arguments after pipelines](https://github.com/praxis-proxy/policy/issues/153) _(rfc · open RFC/proposal)_ — ## Problem

Structured `args` currently captures the tool call before an `args:` pipeline runs. A PDP
therefore authorizes the received arguments while the pipeline can redact, omit, or
replace fie...- [#147 feat(pdps): avoid reconverting structured input on every PDP step](https://github.com/praxis-proxy/policy/issues/147) _(rfc · open RFC/proposal)_ — ## Problem

Each PDP step converts the full structured request again:
- Cedar sanitizes `llm.request` and `args` on every step, even when no policy reads `context.llm` or `context.args` (`crates/bu...
