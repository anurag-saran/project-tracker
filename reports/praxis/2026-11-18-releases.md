# praxis releases — 2026-11-18

_Generated 2026-11-18T15:56:24Z_

**Docs:** [https://praxis.fast](https://praxis.fast) · [https://praxis.fast/ai/](https://praxis.fast/ai/)
## TL;DR

- praxis-proxy/ai v0.11.0: 3 feature(s)
- praxis-proxy/ai next milestone: v0.12.0
- praxis-proxy/praxis v0.8.0: 9 feature(s)
- praxis-proxy/praxis next milestone: v0.9.0
- praxis-proxy/forge next milestone: v0.1.0
- praxis-proxy/gateway-controller next milestone: v1.0.0
- praxis-proxy/grid v0.3.1: 1 feature(s)
- praxis-proxy/grid next RC/train: v0.3.0-rc.4

## praxis-proxy/ai (core)

Release page: [https://github.com/praxis-proxy/ai/releases](https://github.com/praxis-proxy/ai/releases)

### Shipped (what went in)

#### [v0.11.0](https://github.com/praxis-proxy/ai/releases/tag/v0.11.0) — 2026-11-13
- feat(conformance): add OpenAI verification badges by @leseb in https://github.com/praxis-proxy/ai/pull/1979
- feat(release): publish a per-release support report by @nathan-weinberg in https://github.com/praxis-proxy/ai/pull/1941
- feat(openai-files): pin the API contract and route/schema source of truth by @r-papso in https://github.com/praxis-proxy/ai/pull/1955

#### [v0.10.0](https://github.com/praxis-proxy/ai/releases/tag/v0.10.0) — 2026-11-06
- feat(xtask): add cargo xtask bump-pins and a weekly bump workflow by @nathan-weinberg in https://github.com/praxis-proxy/ai/pull/1829
- feat(inference): add cross-provider failover with API translation by @noalimoy in https://github.com/praxis-proxy/ai/pull/1808
- Support Codex apply_patch grammar through client-tool compatibility by @leseb in https://github.com/praxis-proxy/ai/pull/1854
- feat(guardrails): evaluate NeMo message slices concurrently by @liavweiss in https://github.com/praxis-proxy/ai/pull/1818
- feat(guardrails): add multi-format message extraction by @liavweiss in https://github.com/praxis-proxy/ai/pull/1773
- Reject unsupported Code Interpreter tools in Responses by @leseb in https://github.com/praxis-proxy/ai/pull/1913

#### [v0.9.0](https://github.com/praxis-proxy/ai/releases/tag/v0.9.0) — 2026-10-30
- feat(pi): support the pi coding harness alongside Claude Code, Codex, and OpenCode by @nathan-weinberg in https://github.com/praxis-proxy/ai/pull/1810
- feat(store): response-store TTL and background reaper (#630) by @leseb in https://github.com/praxis-proxy/ai/pull/1811
- feat(crypto): add runtime cryptographic readiness checks by @rhdedgar in https://github.com/praxis-proxy/ai/pull/1588
- feat(xtask): port the pins job to cargo xtask check-pins by @nathan-weinberg in https://github.com/praxis-proxy/ai/pull/1828
- feat(store): add atomic response-object compare-and-swap by @cdoern in https://github.com/praxis-proxy/ai/pull/1741

#### [v0.8.0](https://github.com/praxis-proxy/ai/releases/tag/v0.8.0) — 2026-10-22
- feat(openai)!: preserve multi-query web search calls by @Artemon-line in https://github.com/praxis-proxy/ai/pull/1693
- Bound MCP approval correlation ids before persistence by @Artemon-line in https://github.com/praxis-proxy/ai/pull/1651
- Ai guardrails ne mo mask / redact action #49 by @rkaplan-hub in https://github.com/praxis-proxy/ai/pull/1286
- feat(mcp): enforce an operator minimum approval policy for Responses tool dispatch by @leseb in https://github.com/praxis-proxy/ai/pull/1728
- feat(mcp): make tool metadata trust explicit and enforce read-only (#1724) by @leseb in https://github.com/praxis-proxy/ai/pull/1730
- Add license scan report and status by @fossabot in https://github.com/praxis-proxy/ai/pull/1743
- feat(translation): translate OpenAI chat for Anthropic providers by @nerdalert in https://github.com/praxis-proxy/ai/pull/1736
- feat(mcp): enforce connector-only routing for MCP tools (#1672) by @noalimoy in https://github.com/praxis-proxy/ai/pull/1739
- feat(release): publish exact-commit CI evidence by @leseb in https://github.com/praxis-proxy/ai/pull/1775
- Hide server configuration details from client-facing errors by @leseb in https://github.com/praxis-proxy/ai/pull/1779
- feat(filters): model/cluster-labeled LLM gateway metrics + TTFT model fix by @mrodden in https://github.com/praxis-proxy/ai/pull/1689
- feat: file-backed credentials for web_search and external_metering by @leseb in https://github.com/praxis-proxy/ai/pull/1737
- feat(metering): add organization_id and cost_center to CloudEvents by @jenniferubah in https://github.com/praxis-proxy/ai/pull/1734
- feat(token-rate-limit): add Redis/Valkey Sentinel HA by @jordigilh in https://github.com/praxis-proxy/ai/pull/1735
- Feat/anthropic drift gate and functional coverage by @rhdedgar in https://github.com/praxis-proxy/ai/pull/1661

#### [v0.7.0](https://github.com/praxis-proxy/ai/releases/tag/v0.7.0) — 2026-10-16
- Restored custom-tool added events include required input by @Artemon-line in https://github.com/praxis-proxy/ai/pull/1658
- feat(token_rate_limit): enforce org, team, and user budgets independently by @asaadbalum in https://github.com/praxis-proxy/ai/pull/1581
- feat(model_to_header): skip the filter with a headers_present condition by @shaneutt in https://github.com/praxis-proxy/ai/pull/1510
- Ai guardrails failure mode open not caught by security filter config validation no caching for growing conversation history 753 by @rkaplan-hub in https://github.com/praxis-proxy/ai/pull/1555
- feat(gcp): mint scoped tokens from service account key files by @shaneutt in https://github.com/praxis-proxy/ai/pull/1696
- feat(vertex): translate Anthropic messages for Vertex by @shaneutt in https://github.com/praxis-proxy/ai/pull/1695
- feat(intelligent_route): record decisions and validate overlay clusters by @szedan-rh in https://github.com/praxis-proxy/ai/pull/1662
- feat(inflight): in-flight per-model tracking filter (#374) by @crstrn13 in https://github.com/praxis-proxy/ai/pull/1630
- feat(mcp): validate tool-call arguments against advertised input schema by @leseb in https://github.com/praxis-proxy/ai/pull/1725

#### [v0.6.0](https://github.com/praxis-proxy/ai/releases/tag/v0.6.0) — 2026-10-09
- feat(responses): let a chain opt out of initializing Responses state by @cdoern in https://github.com/praxis-proxy/ai/pull/1487
- feat(intelligent_route): serve authoritative no-route overlays by @nerdalert in https://github.com/praxis-proxy/ai/pull/1539
- feat(guardrails): screen IRR tool results (#752) by @leseb in https://github.com/praxis-proxy/ai/pull/1599
- feat(anthropic): operator-approved degradation for Messages→Chat by @leseb in https://github.com/praxis-proxy/ai/pull/1643
- feat(intelligent_route): complete weighted overlay support by @nerdalert in https://github.com/praxis-proxy/ai/pull/1494
- feat(fips): enable certificate-only PostgreSQL Responses store by @leseb in https://github.com/praxis-proxy/ai/pull/1335
- feat(openai): Support streaming reasoning in responses-to-chat-completions translation by @s-akhtar-baig in https://github.com/praxis-proxy/ai/pull/1379
- feat(openai): classify Files and Vector Stores operations by @cdoern in https://github.com/praxis-proxy/ai/pull/1506
- feat(examples): add Tavily web-search scoped-credentials example by @leseb in https://github.com/praxis-proxy/ai/pull/1654
- feat(conversations): process conversation history incrementally by @skamenan7 in https://github.com/praxis-proxy/ai/pull/1509


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [v0.12.0](https://github.com/praxis-proxy/ai/milestone/13) _(milestone · due 2026-11-20 · 6/27 issues closed · 0 open PRs)_- [v0.13.0](https://github.com/praxis-proxy/ai/milestone/14) _(milestone · due 2026-11-27 · 0/0 issues closed · 0 open PRs)_- [v0.14.0](https://github.com/praxis-proxy/ai/milestone/15) _(milestone · due 2026-12-04 · 0/0 issues closed · 0 open PRs)_- [v0.15.0](https://github.com/praxis-proxy/ai/milestone/16) _(milestone · due 2026-12-11 · 0/0 issues closed · 0 open PRs)_- [v0.16.0](https://github.com/praxis-proxy/ai/milestone/17) _(milestone · due 2026-12-18 · 0/0 issues closed · 0 open PRs)_- [#2027 feat(anthropic): execute Messages MCP connector toolsets in Praxis](https://github.com/praxis-proxy/ai/issues/2027) _(rfc · open RFC/proposal)_ — ## Parent

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
- feat(health): add TLS and HTTPS health probes by @shaneutt in https://github.com/praxis-proxy/praxis/pull/1422
- Experimental Hyper Backend by @shaneutt in https://github.com/praxis-proxy/praxis/pull/1423
- Require-useful-detail-in-bug-reports--#1225-Open-Task by @aviavissar in https://github.com/praxis-proxy/praxis/pull/1475
- Point-questions,-bugs,-and-security-reports-to-the-right-place--#1227 by @aviavissar in https://github.com/praxis-proxy/praxis/pull/1454
- Give-the-mutation-testing-job-a-pass/fail-policy-#1390 by @aviavissar in https://github.com/praxis-proxy/praxis/pull/1453
- feat(config): inline clusters inherit top-level endpoints by @dgn in https://github.com/praxis-proxy/praxis/pull/1460
- feat(overload): publish smoothed pressure gauges by @abdallahsamabd in https://github.com/praxis-proxy/praxis/pull/1455
- feat(config): add forward_proxy block for HTTP listeners by @esnible in https://github.com/praxis-proxy/praxis/pull/1477
- feat(policy): upgrade to PPE 0.6.0 by @araujof in https://github.com/praxis-proxy/praxis/pull/1516

#### [v0.7.5](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.5) — 2026-10-21
- feat: add request-head filter lifecycle phase with head_classifier by @leseb in https://github.com/praxis-proxy/praxis/pull/1380
- feat: ramp new and recovered endpoints with slow start by @abdallahsamabd in https://github.com/praxis-proxy/praxis/pull/1364
- feat(core): decide hedged attempts, timeouts, and cancellation by @abdallahsamabd in https://github.com/praxis-proxy/praxis/pull/1372
- Feature: Protocol Backend Seam by @shaneutt in https://github.com/praxis-proxy/praxis/pull/1407
- feat: FIPS crypto readiness settings and tests by @rhdedgar in https://github.com/praxis-proxy/praxis/pull/1365
- feat: apply slow-start weights while selecting endpoints by @abdallahsamabd in https://github.com/praxis-proxy/praxis/pull/1406
- Add license scan report and status by @fossabot in https://github.com/praxis-proxy/praxis/pull/1417
- feat(policy): add context_headers and context_meta config surface by @aviavissar in https://github.com/praxis-proxy/praxis/pull/1388

#### [v0.7.4](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.4) — 2026-10-12
- feat(filter): add stdout and file sinks to access_log by @crstrn13 in https://github.com/praxis-proxy/praxis/pull/1324
- feat(conditions): add a headers_present predicate by @shaneutt in https://github.com/praxis-proxy/praxis/pull/1348
- feat(config): inherit conditions from named filter chains by @leseb in https://github.com/praxis-proxy/praxis/pull/1286
- feat(filter): add text template output to access_log by @crstrn13 in https://github.com/praxis-proxy/praxis/pull/1323
- feat: separate admin port from metrics, do not require allow_public_admin on metrics by @rikatz in https://github.com/praxis-proxy/praxis/pull/1342
- feat: Add preserve_query_params_only operation to url_rewrite filter by @valeriiashapoval in https://github.com/praxis-proxy/praxis/pull/1339
- feat(opentelemetry): link exported HTTP spans across proxy hops by @nerdalert in https://github.com/praxis-proxy/praxis/pull/1347
- feat(router): add per-route hedge policy configuration by @abdallahsamabd in https://github.com/praxis-proxy/praxis/pull/1361
- feat(filter): add syslog sink to access_log filter by @crstrn13 in https://github.com/praxis-proxy/praxis/pull/1360
- feat(policy): authorize on the parsed inference request; bump to PPE 0.4.1 by @araujof in https://github.com/praxis-proxy/praxis/pull/1297
- feat(core): add policy-aware URL subrequest execution by @leseb in https://github.com/praxis-proxy/praxis/pull/1337
- feat(core): per-cluster upstream base path by @hexfusion in https://github.com/praxis-proxy/praxis/pull/1377

#### [v0.7.3](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.3) — 2026-10-03
- feat(cluster): trust a named private upstream per cluster by @hexfusion in https://github.com/praxis-proxy/praxis/pull/1308
- feat(rate-limit): add shadow mode that observes a limit without enforcing it by @szedan-rh in https://github.com/praxis-proxy/praxis/pull/1322
- feat(cluster): derive the upstream Host and SNI from the selected endpoint by @shaneutt in https://github.com/praxis-proxy/praxis/pull/1334
- feat(branch-chains): match on_result with contains, not, and any_of by @shaneutt in https://github.com/praxis-proxy/praxis/pull/1335

#### [v0.7.2](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.2) — 2026-09-30
- feat(core): centralize IP address classification in praxis-core by @leseb in https://github.com/praxis-proxy/praxis/pull/1282
- Feat: File Descriptor Handling by @shaneutt in https://github.com/praxis-proxy/praxis/pull/1303

#### [v0.7.1](https://github.com/praxis-proxy/praxis/releases/tag/v0.7.1) — 2026-09-26
- FIPS: expand testing + prove runtime behaviors by @shaneutt in https://github.com/praxis-proxy/praxis/pull/1263
- feat(policy): permit a pinned private endpoint for policy egress by @hexfusion in https://github.com/praxis-proxy/praxis/pull/1260
- feat(filter): infer bound-body scheduling from filter conditions by @leseb in https://github.com/praxis-proxy/praxis/pull/1268


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [v0.9.0](https://github.com/praxis-proxy/praxis/milestone/23) _(milestone · due 2026-12-07 · 22/133 issues closed · 19 open PRs)_- [v0.12.0](https://github.com/praxis-proxy/praxis/milestone/24) _(milestone · due 2026-12-28 · 0/21 issues closed · 1 open PRs)_- [v1.0.0](https://github.com/praxis-proxy/praxis/milestone/25) _(milestone · due 2027-01-18 · 8/25 issues closed · 0 open PRs)_- [#1474 refactor(filter): move shared AI credential helpers into Core](https://github.com/praxis-proxy/praxis/issues/1474) _(rfc · open RFC/proposal)_ — ### What?

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
## praxis-proxy/forge (watch)

Release page: [https://github.com/praxis-proxy/forge/releases](https://github.com/praxis-proxy/forge/releases)

### Shipped (what went in)

_No stable releases stored yet. Run fetch / releases with a GitHub token._

### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [v0.1.0](https://github.com/praxis-proxy/forge/milestone/1) _(milestone · due TBD · 0/0 issues closed · 0 open PRs)_
## praxis-proxy/gateway-controller (watch)

Release page: [https://github.com/praxis-proxy/gateway-controller/releases](https://github.com/praxis-proxy/gateway-controller/releases)

### Shipped (what went in)

_No stable releases stored yet. Run fetch / releases with a GitHub token._

### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [v1.0.0](https://github.com/praxis-proxy/gateway-controller/milestone/1) _(milestone · due 2027-01-20 · 0/3 issues closed · 0 open PRs)_
## praxis-proxy/grid (watch)

Release page: [https://github.com/praxis-proxy/grid/releases](https://github.com/praxis-proxy/grid/releases)

### Shipped (what went in)

#### [v0.3.1](https://github.com/praxis-proxy/grid/releases/tag/v0.3.1) — 2026-11-13
- feat(gateway): present the grid certificate on a local TLS dial by @hexfusion in https://github.com/praxis-proxy/grid/pull/593

#### [v0.3.0](https://github.com/praxis-proxy/grid/releases/tag/v0.3.0) — 2026-11-10
- feat(operator): route generated consumer config with grid_site_route by @hexfusion in https://github.com/praxis-proxy/grid/pull/427
- feat(operator): support HA with leader elections by @hexfusion in https://github.com/praxis-proxy/grid/pull/437
- feat(operator): operator config driven enrollment and cert rotation by @hexfusion in https://github.com/praxis-proxy/grid/pull/429
- feat(operator): add opt-in local membership over HTTPS by @hexfusion in https://github.com/praxis-proxy/grid/pull/435
- feat(enrollment): bootstrap grids and distribute declared membership by @hexfusion in https://github.com/praxis-proxy/grid/pull/474
- feat: sign state gossip with site certificates by @evacchi in https://github.com/praxis-proxy/grid/pull/430
- feat(operator): add model expiry to CRDs + add support to receive gossiped models by @evacchi in https://github.com/praxis-proxy/grid/pull/426
- feat(operator): derive topology for every local provider by @hexfusion in https://github.com/praxis-proxy/grid/pull/494
- feat(gateway,operator): dial derived upstreams by @hexfusion in https://github.com/praxis-proxy/grid/pull/497
- feat(gateway): expose unavailable score reasons by @tsisodia10 in https://github.com/praxis-proxy/grid/pull/500
- feat(operator): publish and route discovered model inventories by @evacchi in https://github.com/praxis-proxy/grid/pull/487
- feat(praxis-gateway): make more than one replica safe to roll and drain by @hexfusion in https://github.com/praxis-proxy/grid/pull/441
- feat(chart): select the enrollment hub by label by @hexfusion in https://github.com/praxis-proxy/grid/pull/522
- feat(chart): forward /v1/messages and /v1/responses through the provider gateway by @hexfusion in https://github.com/praxis-proxy/grid/pull/519
- feat(route): fence grid_site_route to a request's sovereignty zones by @hexfusion in https://github.com/praxis-proxy/grid/pull/530

#### [v0.2.2](https://github.com/praxis-proxy/grid/releases/tag/v0.2.2) — 2026-10-22
- feat(operator): publish discovered models in provider status by @evacchi in https://github.com/praxis-proxy/grid/pull/389
- feat: Go Kubernetes API types for Grid CRDs by @valeriiashapoval in https://github.com/praxis-proxy/grid/pull/388

#### [v0.2.1](https://github.com/praxis-proxy/grid/releases/tag/v0.2.1) — 2026-10-19
- feat(routing): publish and serve no-route revisions by @nerdalert in https://github.com/praxis-proxy/grid/pull/270
- feat(gateway): read every site's load from the local operator only by @hexfusion in https://github.com/praxis-proxy/grid/pull/336
- feat(operator): derive consumer endpoint topology from allowlisted providers by @hexfusion in https://github.com/praxis-proxy/grid/pull/341
- chart(operator): render gatewayRefs[].consumerConfig from gateway.consumerConfig by @hexfusion in https://github.com/praxis-proxy/grid/pull/353
- feat: install the operator from a generated platform base and start a gateway on the generated config by @hexfusion in https://github.com/praxis-proxy/grid/pull/354
- feat(enrollment): record each enrollment as a CertificateSigningRequest by @hexfusion in https://github.com/praxis-proxy/grid/pull/360
- feat(gateway): kv cache saturation with ceiling by @hexfusion in https://github.com/praxis-proxy/grid/pull/375
- feat(client): unified HTTP client logic by @hexfusion in https://github.com/praxis-proxy/grid/pull/349
- feat(enrollment): reconcile SiteInvite resources by @hexfusion in https://github.com/praxis-proxy/grid/pull/382
- deps(gateway): pin Praxis AI with Praxis 0.7.4 support by @hexfusion in https://github.com/praxis-proxy/grid/pull/392
- feat(gateway): expose prefix affinity cache limits by @hexfusion in https://github.com/praxis-proxy/grid/pull/391
- feat(operator): name the site from its identity and create its records by @hexfusion in https://github.com/praxis-proxy/grid/pull/402

#### [v0.2.0](https://github.com/praxis-proxy/grid/releases/tag/v0.2.0) — 2026-10-08
- feat(swim): resolve DNS endpoint hostnames by @nerdalert in https://github.com/praxis-proxy/grid/pull/138
- feat(operator): add administrative provider drain by @nerdalert in https://github.com/praxis-proxy/grid/pull/126
- feat(routing): add static weighted provider selection by @nerdalert in https://github.com/praxis-proxy/grid/pull/142
- feat(operator): cross-site provider signals via a grid-wide signalTransport by @hexfusion in https://github.com/praxis-proxy/grid/pull/147
- feat(enrollment): standalone single-use site-token enrollment service by @hexfusion in https://github.com/praxis-proxy/grid/pull/153
- feat(operator): opt-in FIPS OpenSSL TLS backend by @hexfusion in https://github.com/praxis-proxy/grid/pull/148
- feat(gateway): stub the praxis-grid-gateway operand by @hexfusion in https://github.com/praxis-proxy/grid/pull/159
- Split the grid-gateway into its own workspace and bump praxis-proxy to 0.7 by @hexfusion in https://github.com/praxis-proxy/grid/pull/194
- feat(enrollment): grid enrollment, issuance, SPIFFE verifier, chart, and e2e by @hexfusion in https://github.com/praxis-proxy/grid/pull/201
- feat(grid): cross-site load routing over verified mTLS by @hexfusion in https://github.com/praxis-proxy/grid/pull/203
- feat(deploy): add a kustomization for the CRDs by @hexfusion in https://github.com/praxis-proxy/grid/pull/215
- render the gateway config from the chart with secure defaults by @hexfusion in https://github.com/praxis-proxy/grid/pull/210
- feat(grid-enrollment): pin images by digest by @hexfusion in https://github.com/praxis-proxy/grid/pull/225
- feat: operator auto-enroll from hub site invites by @hexfusion in https://github.com/praxis-proxy/grid/pull/234
- feat(operator): SWIM across clusters and signals peer trust by @hexfusion in https://github.com/praxis-proxy/grid/pull/237

#### [v0.1.4](https://github.com/praxis-proxy/grid/releases/tag/v0.1.4) — 2026-09-04
- Basic Auth before quota reservation
- One identity-scoped Alice budget shared across consumer gateways
- Valkey-backed sliding-window state
- Atomic concurrent reservation safety
- Natural window expiry and recovery
- Quota persistence across consumer restarts
- Fail-closed admission during Valkey outage
- NetworkPolicy isolation for quota-client access
- feat(operator,crdt,swim): tenant-budget plumbing via SWIM-gossiped GCounter (grid#40) by @jordigilh in https://github.com/praxis-proxy/grid/pull/47
- feat(demo): add --kv-cache flag to llm-d pool-metrics demo by @jordigilh in https://github.com/praxis-proxy/grid/pull/46
- feat(operator): stabilized provider admission with scrape-generation identity by @nerdalert in https://github.com/praxis-proxy/grid/pull/71
- feat(routing): publish provider selection modes by @nerdalert in https://github.com/praxis-proxy/grid/pull/65
- feat(token-quota): add distributed quota topology by @nerdalert in https://github.com/praxis-proxy/grid/pull/84


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.3.0-rc.4](https://github.com/praxis-proxy/grid/releases/tag/v0.3.0-rc.4) (2026-11-04)  - feat(gateway): expose unavailable score reasons by @tsisodia10 in https://github.com/praxis-proxy/grid/pull/500
  - feat(operator): publish and route discovered model inventories by @evacchi in https://github.com/praxis-proxy/grid/pull/487
  - feat(praxis-gateway): make more than one replica safe to roll and drain by @hexfusion in https://github.com/praxis-proxy/grid/pull/441
  - feat(chart): select the enrollment hub by label by @hexfusion in https://github.com/praxis-proxy/grid/pull/522
  - feat(chart): forward /v1/messages and /v1/responses through the provider gateway by @hexfusion in https://github.com/praxis-proxy/grid/pull/519
  - feat(route): fence grid_site_route to a request's sovereignty zones by @hexfusion in https://github.com/praxis-proxy/grid/pull/530
- [v0.3.0-rc.3](https://github.com/praxis-proxy/grid/releases/tag/v0.3.0-rc.3) (2026-10-30)  - feat: sign state gossip with site certificates by @evacchi in https://github.com/praxis-proxy/grid/pull/430
  - feat(operator): add model expiry to CRDs + add support to receive gossiped models by @evacchi in https://github.com/praxis-proxy/grid/pull/426
  - feat(operator): derive topology for every local provider by @hexfusion in https://github.com/praxis-proxy/grid/pull/494
  - feat(gateway,operator): dial derived upstreams by @hexfusion in https://github.com/praxis-proxy/grid/pull/497
- [v0.3.0-rc.2](https://github.com/praxis-proxy/grid/releases/tag/v0.3.0-rc.2) (2026-10-29)  - feat(enrollment): bootstrap grids and distribute declared membership by @hexfusion in https://github.com/praxis-proxy/grid/pull/474

**Milestones, roadmaps & open RFCs feeding the next drop**
- [v1.0.0](https://github.com/praxis-proxy/grid/milestone/3) _(milestone · due TBD · 0/1 issues closed · 0 open PRs)_- [v0.4.0](https://github.com/praxis-proxy/grid/milestone/5) _(milestone · due TBD · 4/31 issues closed · 2 open PRs)_- [v0.3.0](https://github.com/praxis-proxy/grid/milestone/4) _(milestone · due 2026-11-05 · 54/54 issues closed · 0 open PRs)_ — AI Grid Network - Inference Fundamentals- [#13 feat(observability): emit structured intelligent routing decisions](https://github.com/praxis-proxy/grid/issues/13) _(rfc · open RFC/proposal)_ — ## Summary

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
- Added selectable RustCrypto (default) and OpenSSL FIPS SHA-256 backends, startup checks, capability reporting, and backend-selected randomness. ([#306](https://github.com/praxis-proxy/policy/pull/306))
- Added FIPS verification for JWTs and DPoP proofs through `jwt-openssl-fips`. ([#315](https://github.com/praxis-proxy/policy/pull/315))
- Exposed raw HTTP query strings to policy as `http.query`, with capability-gated plugin access and redacted diagnostics. ([#223](https://github.com/praxis-proxy/policy/pull/223))
- Added stdout, stderr, and append-only file audit exporters, plus multiple destinations for the reference OCSF sink. ([#226](https://github.com/praxis-proxy/policy/pull/226))
- Added pre- and post-identity rate-limit hooks, scoped `rate_limits:` configuration, and a host-supplied normalized client address. ([#178](https://github.com/praxis-proxy/policy/pull/178))
- Added an opt-in in-process `ratelimit/limitador` plugin with client-safe denials and fail-closed counter-key handling. ([#178](https://github.com/praxis-proxy/policy/pull/178))
- Added a Valkey-backed CIBA approval store with atomic poll claims and redemption across replicas. ([#239](https://github.com/praxis-proxy/policy/pull/239))
- CIBA store failures now deny with `elicitation.store_unavailable` and JSON-RPC `-32122`. ([#239](https://github.com/praxis-proxy/policy/pull/239))
- Added per-issuer DPoP proof verification, key-binding attributes, and optional shared replay guards for JWT identity. ([#224](https://github.com/praxis-proxy/policy/pull/224))
- Added typed LLM request and history access, canonical `llm.*` policy attributes, and a reference transcript scanner. ([#95](https://github.com/praxis-proxy/policy/pull/95))
- Added immutable acquired metadata under `metadata.<instance>.*` for policy and explicitly granted plugins. ([#231](https://github.com/praxis-proxy/policy/pull/231))
- Added header, cookie, and query-parameter credential locations for `identity/jwt`. ([#96](https://github.com/praxis-proxy/policy/pull/96))
- **Breaking for builds without default features:** select exactly one crypto backend, `crypto-rustcrypto` or `fips`. ([#306](https://github.com/praxis-proxy/policy/pull/306))
- **Breaking Rust API:** hashing and crypto startup can now fail; handle `CryptoError`, `PluginError::Crypto`, and fallible digest helpers. ([#306](https://github.com/praxis-proxy/policy/pull/306))
- **Breaking FIPS configuration:** `jwt-openssl-fips` requires the FIPS provider, excludes `jwt`, and rejects HMAC, EdDSA, and unsupported keys. ([#315](https://github.com/praxis-proxy/policy/pull/315))

#### [v0.5.0](https://github.com/praxis-proxy/policy/releases/tag/v0.5.0) — 2026-10-13
- Added the opt-in `delegator/vault` builtin to read downstream credentials from Vault KV v2 for a user, client, or workload. Routes using it must authorize before delegation. ([#168](https://github.com/praxis-proxy/policy/pull/168))
- Request header assertions can use a declared `secret.<name>` value for static upstream credentials. Values are resolved at startup and read from the secret store at the point of use, so rotation takes effect on the next request after refresh without fetching on the request path. Unknown names and response assertions using secrets are rejected. ([#174](https://github.com/praxis-proxy/policy/pull/174))
- Added an OCSF audit sink as an unpublished reference plugin. It emits decision records with optional chained attestations and DSSE signatures for offline verification. ([#171](https://github.com/praxis-proxy/policy/pull/171))
- Exposed MCP tool, resource, and prompt annotations to policy, including `readOnlyHint` and `destructiveHint`. Workload attestation timestamps are available as RFC3339 strings and Unix seconds; APL can compare `attested_at_epoch` against a fixed threshold. ([#175](https://github.com/praxis-proxy/policy/pull/175))
- Added secret-provider health details through `secrets_health` and atomic value/generation reads through `SecretRef::snapshot`. ([#191](https://github.com/praxis-proxy/policy/pull/191))
- **Breaking:** Secret configuration reloads that change `secrets:` now fail; restart to apply those changes. The `env` provider rejects unused settings. `secrets_last_success` retains its last successful timestamp after a failure, so use `secrets_health` to detect outages. ([#191](https://github.com/praxis-proxy/policy/pull/191))
- **Breaking for Rust callers:** Secret assertions add `HttpExtension::secret_headers`; exhaustive struct literals must initialize it, and hosts must preserve it between hooks. `SourcePath::resolve` and `assertions::render` now take a secret store, `AssertionsConfig::validate` takes secret configuration, `SourcePath::capability` returns `Option<Capability>`, and `SourcePath` gains a `Secret(String)` variant and is non-exhaustive. ([#174](https://github.com/praxis-proxy/policy/pull/174))
- **Breaking for custom CEL functions:** `CelResolver::with_functions` and its registration callback now return `Result`. Conflicts with standard-library overloads fail construction; later registration failures deny even with `on_error: allow`. Hosts that need such overloads must use a CEL `Env` overload. ([#185](https://github.com/praxis-proxy/policy/pull/185))
- CEL 0.15 counts Unicode code points instead of UTF-8 bytes in string `size()`. `exists()` returns `true` if an element matches even when another element errors. Review policies that depend on byte limits or list-predicate errors, since previously denied requests may now allow. ([#185](https://github.com/praxis-proxy/policy/pull/185))
- JSON floats now parse with `serde_json`'s `float_roundtrip` feature. Exact numeric boundaries and re-serialized audit records can change. ([#171](https://github.com/praxis-proxy/policy/pull/171))
- **Breaking for Rust callers:** Removed eight `CAP_READ_*` names for unrestricted CMF slots and seven `BAG_*_PREFIX` constants. The policy attributes remain available. ([#175](https://github.com/praxis-proxy/policy/pull/175))

#### [v0.4.1](https://github.com/praxis-proxy/policy/releases/tag/v0.4.1) — 2026-10-06
- **Optional bounded PDP decision cache.** A `cache:` block on a `global.pdp[]` entry stores Allow and Deny for a positive TTL and a positive entry cap. Omission leaves evaluation unchanged. Keys are a digest of dialect, call arguments, the full attribute bag, and structured request input, so request data is not retained. Dispatch errors are never stored, expired entries are never returned, FIFO eviction stays inside the cap, and a PPE configuration generation change drops the map. External PDP policy can still go stale until the TTL expires; [`docs/pdp-decision-cache.md`](https://github.com/praxis-proxy/policy/blob/v0.4.1/docs/pdp-decision-cache.md) states that. ([#67](https://github.com/praxis-proxy/policy/issues/67))
- PDPs can evaluate host-supplied LLM request JSON and native tool arguments. ([#144](https://github.com/praxis-proxy/policy/pull/144))
- Added verdict audit sinks, durable effect logs, and keyed content provenance. ([#84](https://github.com/praxis-proxy/policy/pull/84))
- **Breaking:** OPA and CEL now use native JSON for `tool:` route `args`; `RoutePayload` struct literals require `structured`.
- **Breaking:** cloned extensions drop HTTP transport, and effects are limited to `sequential` and `transform` modes. ([#84](https://github.com/praxis-proxy/policy/pull/84))
- Missing required LLM requests and overly deep structured input now deny. ([#144](https://github.com/praxis-proxy/policy/pull/144))
- PDP-generated errors hide input values; Cedar schemas require `structured_context: true` for structured input. ([#144](https://github.com/praxis-proxy/policy/pull/144))
- The reference audit logger uses sink mode when `hooks:` is absent. ([#84](https://github.com/praxis-proxy/policy/pull/84))
- Serial and transform plugin panics are contained and report `plugin_panic`. ([#84](https://github.com/praxis-proxy/policy/pull/84))

#### [v0.4.0](https://github.com/praxis-proxy/policy/releases/tag/v0.4.0) — 2026-09-29
- Added named `secrets:` providers and values, startup resolution, and host-driven refresh. Built-in `file` and `env` providers support local and Kubernetes-mounted credentials. ([#97](https://github.com/praxis-proxy/policy/pull/97))
- Added a Vault KV v2 secret provider behind `secrets-vault`, with Kubernetes and AppRole authentication through the host HTTP transport. ([#103](https://github.com/praxis-proxy/policy/pull/103))
- Added an opt-in `quota` plugin backed by Limitador for per-principal LLM token budgets. ([#116](https://github.com/praxis-proxy/policy/pull/116))
- Added the `ibmverify` JWT claim mapper preset for scalar or array collection claims. ([#134](https://github.com/praxis-proxy/policy/pull/134))
- Added an `identity/api-key` resolver with file and HTTP directories, shared identity mapping, and bounded caching. Configure the backend with `provider:`; the facade exposes the resolver through the `api-key` feature. ([#125](https://github.com/praxis-proxy/policy/pull/125), [#135](https://github.com/praxis-proxy/policy/pull/135), [#136](https://github.com/praxis-proxy/policy/pull/136))
- Documented how to add and test provider-specific JWT claim mapper presets. ([#128](https://github.com/praxis-proxy/policy/pull/128))
- Consolidated the nine bundled extensions into `praxis-policy-builtins`, with one feature per extension. The facade's features, re-exports, and policy `kind` strings remain the same. **Direct users of a retired extension crate must switch to `praxis-policy-builtins` with the matching feature** to avoid duplicate registration. See the [crate mapping](https://github.com/praxis-proxy/policy/blob/v0.4.0/docs/content/crates.md). ([#140](https://github.com/praxis-proxy/policy/pull/140))
- JWT, OAuth, and CIBA configuration errors now name the plugin kind instead of the former crate name; update log or alert patterns that match this text. ([#140](https://github.com/praxis-proxy/policy/pull/140))
- Moved the configurable identity claim mapper to `praxis_policy_core::identity::mapping`. **Rust callers using the JWT plugin's module paths must update their imports**; `ConfiguredClaimMap::new` now takes a `MappingProfile`. The operator's `claim_map:` configuration is unchanged. ([#119](https://github.com/praxis-proxy/policy/pull/119))
- Exposed `execute_with_retry` for secret providers using the host transport. ([#103](https://github.com/praxis-proxy/policy/pull/103))
- Replaced `serde_yaml` with `yaml_serde` and updated `regorus` to 0.12.0. ([#121](https://github.com/praxis-proxy/policy/pull/121), [#114](https://github.com/praxis-proxy/policy/pull/114))

#### [v0.3.1](https://github.com/praxis-proxy/policy/releases/tag/v0.3.1) — 2026-09-22
- _No feature bullets extracted — see [full notes](https://github.com/praxis-proxy/policy/releases/tag/v0.3.1)._

#### [v0.3.0](https://github.com/praxis-proxy/policy/releases/tag/v0.3.0) — 2026-09-18
- Added comprehensive PPE documentation and tested examples. ([#82](https://github.com/praxis-proxy/policy/pull/82))
- Documented the CMF extension bag contract and expanded cross-PDP conformance tests. ([#59](https://github.com/praxis-proxy/policy/pull/59))
- Added a catalog of fail-closed safety invariants with fault-injection tests. ([#71](https://github.com/praxis-proxy/policy/pull/71))
- Added Criterion benchmarks for hook dispatch, full decisions, throughput, PDP evaluation, and session memory. ([#35](https://github.com/praxis-proxy/policy/pull/35))
- Updated `base64`, CEL, Redis, deadpool-redis, UUID, and related dependencies.([#111](https://github.com/praxis-proxy/policy/pull/111))
- Removed the unused public `BAG_WORKLOAD_PREFIX` constant. ([#59](https://github.com/praxis-proxy/policy/pull/59))
- Added multithreaded engine stress tests, a Loom memory-ordering model, and a nightly ThreadSanitizer job. ([#60](https://github.com/praxis-proxy/policy/pull/60))


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [0.7.0](https://github.com/praxis-proxy/policy/milestone/7) _(milestone · due 2026-11-20 · 5/26 issues closed · 3 open PRs)_- [0.8.0](https://github.com/praxis-proxy/policy/milestone/8) _(milestone · due 2026-12-18 · 0/1 issues closed · 0 open PRs)_- [1.0.0](https://github.com/praxis-proxy/policy/milestone/4) _(milestone · due 2027-01-08 · 5/26 issues closed · 0 open PRs)_- [#325 Replace duplicate Limitador expression checks with a safe upstream error contract](https://github.com/praxis-proxy/policy/issues/325) _(rfc · open RFC/proposal)_ — The embedded limiter pre-evaluates conditions and computed counter keys, then asks Limitador to evaluate them again. It also handles CEL macro locals and catches panics around dependency calls. See...- [#76 feat(apl): address one content part of a message instead of the whole thing](https://github.com/praxis-proxy/policy/issues/76) _(rfc · open RFC/proposal)_ — ## Description

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
