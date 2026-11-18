# praxis digest — 2026-11-18

_Since 7d · generated 2026-11-18T15:42:20Z_

## TL;DR for this week

- Release praxis-proxy/grid@v0.3.1
- Release praxis-proxy/ai@v0.11.0
- praxis-proxy/ai/apis: 20 PRs merged
- praxis-proxy/ai/filters: 6 PRs merged
- praxis-proxy/ai/server: 1 PRs merged

## praxis-proxy/ai (core)

### Releases
- [v0.11.0](https://github.com/praxis-proxy/ai/releases/tag/v0.11.0) — 2026-11-13
### apis

Summary unavailable (null LLM). Source items:
- #2013 refactor(translation): exchange state in `filter_state` (+1164/-939) by @alexsnaps files: apis/src/azure/to_openai/mod.rs, apis/src/bedrock/converse/mod.rs, apis/src/openai/responses/responses_to_chat_completions/mod.rs, apis/src/openai/responses/responses_to_chat_completions/tests.rs, apis/src/vertex/anthropic/mod.rs, apis/src/vertex/anthropic/request.rs, apis/src/vertex/anthropic/response.rs, apis/src/vertex/gemini/mod.rs
- all five: the response transform mode and upstream status
- vertex_gemini: the model, `include_usage` and candidate count
- bedrock_converse: the model, response ID and `include_usage`
- vertex_anthropic: the model and an operation marker
- openai_responses_to_chat_complet...
- #2028 feat(anthropic): reject the MCP connector on backends that cannot run it (+565/-26) by @leseb files: apis/src/anthropic/messages_request/mod.rs, apis/src/anthropic/messages_request/tests.rs, apis/src/anthropic/messages_to_chat_completions/request.rs, apis/src/anthropic/protocol/mod.rs, apis/src/anthropic/protocol/tests.rs, docs/anthropic-messages.md, docs/filters/anthropic_messages_protocol.md, examples/configs/anthropic/messages-native-vllm.yaml, tests/integration/sdk/anthropic/test_anthropic_sdk_compat.py, tests/integration/tests/suite/examples/anthropic_messages_native_vllm.rs
- #1996 fix(openai): accept blank namespace descriptions per schema (+239/-40) by @henschwartz files: apis/src/openai/responses/openai_client_tool_compat/mod.rs, apis/src/openai/responses/openai_client_tool_compat/tests.rs, tests/integration/sdk/openai/test_openai_responses_vllm.py, tests/integration/tests/suite/examples/openai_client_tool_compat.rs
- Accept schema-valid empty/whitespace `namespace.description` in `openai_client_tool_compat` (still reject missing/non-string).
- Fold blank namespace blurbs without an empty `: ` suffix; keep blank vs missing distinct in discovery conflict identity.
- [x] Unit: blank lowers; missing still 400; blank≡whitespace hoist; blank vs missing conflicts
- [x] IT: `...

### filters

Summary unavailable (null LLM). Source items:
- #1981 feat(metering): resolve tenant identity from verified AuthenticatedIdentity (+721/-29) by @guicassolato files: docs/filters/external_metering.md, examples/configs/external-metering.yaml, filters/src/identity.rs, filters/src/metering/config.rs, filters/src/metering/mod.rs, filters/src/metering/tests.rs, tests/integration/tests/suite/examples/external_metering.rs
**This enables using the Praxis Policy Engine (PPE) for identity resol...
- #2006 `token_rate_limit` state to `filter_state` (+595/-310) by @alexsnaps files: filters/src/token_rate_limit/hierarchy_tests.rs, filters/src/token_rate_limit/mod.rs, filters/src/token_rate_limit/tests.rs
- #1969 feat(ai_guardrails): Support NeMo guardrail redaction for OpenAI Responses and Anthropic Messages (+2252/-215) by @liavweiss files: apis/src/guardrail_messages/mod.rs, apis/src/guardrail_messages/redaction.rs, docs/filters/ai_guardrails.md, examples/configs/nemo-guardrails-response.yaml, examples/configs/nemo-guardrails.yaml, filters/src/guardrails/filter.rs, filters/src/guardrails/providers/nemo.rs, filters/src/guardrails/tests.rs, tests/integration/sdk/anthropic/test_anthropic_sdk_compat.py, tests/integration/tests/suite/examples/guardrails.rs, tests/integration/tests/suite/examples/guardrails_response.rs, tests/integration/tests/suite/examples/openai_agentic_loop.rs
- Apply replacements to the original message or text block while preserving the protocol structure and unaffected fields.
- Preserve message identity across concurrent checks, including when th...
- #1924 fix(filters): require explicit token rate limit backend (+216/-112) by @tsisodia10 files: docs/filters/token_rate_limit.md, examples/configs/token-rate-limit-header-keys.yaml, examples/configs/token-rate-limit-hierarchy.yaml, examples/configs/token-rate-limit-ip-keys.yaml, examples/configs/token-rate-limit-mixed-algorithms.yaml, examples/configs/token-rate-limit-model-keys.yaml, examples/configs/token-rate-limit-soft-enforcement.yaml, examples/configs/token-rate-limit-soft-tiers.yaml, examples/configs/token-rate-limit.yaml, filters/src/token_rate_limit/config.rs, filters/src/token_rate_limit/mod.rs, filters/src/token_rate_limit/tests.rs
- require `backend` and `backend.kind` for the token-rate-limit filter instead of silently selecting the in-memory backend
- reject network-only settings when `kind: memory` is selected
- update all token-rate-limit examples, generated filter documentation, unit coverage, and functional example coverage
- [x] Unit tests — `CARGO_TARGET...
- #1968 refactor(a2a): task-route capture state in `filter_state` (+676/-1176) by @alexsnaps files: filters/src/agentic/a2a/mod.rs, filters/src/agentic/a2a/sse.rs, filters/src/agentic/a2a/tests.rs, filters/src/token_usage/count.rs, filters/src/token_usage/count/tests.rs

**First-time contributors:** guicassolato
### server

Summary unavailable (null LLM). Source items:
- #1960 Include the Conversations API in the FIPS compliance profile (+48/-18) by @rhdedgar files: .github/scripts/release_qualification.py, Makefile, docs/fips.md, docs/release.md, server/src/server.rs, tests/integration/tests/suite/examples/mod.rs, xtask/src/fips/graph.rs

### store

Summary unavailable (null LLM). Source items:
- #1950 fix(conversations): complete exact API contract conformance (+1475/-605) by @leseb files: apis/src/openai/conversations/error.rs, apis/src/openai/conversations/filter.rs, apis/src/openai/conversations/handlers.rs, apis/src/openai/conversations/mod.rs, apis/src/openai/conversations/rate_limit.rs, apis/src/openai/conversations/routes.rs, apis/src/openai/conversations/tests.rs, docs/conformance/README.md, docs/conformance/openai-conformance-report.json, docs/filters/openai_conversations.md, examples/configs/openai/conversations/conversations.yaml, store-backends/src/postgres.rs
-> trusted owner check
-> op...

### store-backends

Summary unavailable (null LLM). Source items:
- #1950 fix(conversations): complete exact API contract conformance (+1475/-605) by @leseb files: apis/src/openai/conversations/error.rs, apis/src/openai/conversations/filter.rs, apis/src/openai/conversations/handlers.rs, apis/src/openai/conversations/mod.rs, apis/src/openai/conversations/rate_limit.rs, apis/src/openai/conversations/routes.rs, apis/src/openai/conversations/tests.rs, docs/conformance/README.md, docs/conformance/openai-conformance-report.json, docs/filters/openai_conversations.md, examples/configs/openai/conversations/conversations.yaml, store-backends/src/postgres.rs
-> trusted owner check
-> op...

### vllm

Summary unavailable (null LLM). Source items:
- #1977 test(openresponses): add full acceptance and live vision coverage (+824/-21) by @leseb files: .github/workflows/anthropic-vllm-vision.yaml, .github/workflows/openresponses-conformance.yaml, Makefile, docs/conformance/README.md, docs/conformance/openresponses-acceptance.md, docs/conformance/openresponses-translation.md, docs/developing/gpu-nightly-suite.md, tests/conformance/openresponses/managed.yaml, tests/conformance/openresponses/manifest.yaml, tests/conformance/openresponses/passthrough.yaml, tests/conformance/openresponses/run-cpu.ts, tests/integration/sdk/openai/run_responses_acceptance.py
-> serial C...

### xtask

Summary unavailable (null LLM). Source items:
- #1960 Include the Conversations API in the FIPS compliance profile (+48/-18) by @rhdedgar files: .github/scripts/release_qualification.py, Makefile, docs/fips.md, docs/release.md, server/src/server.rs, tests/integration/tests/suite/examples/mod.rs, xtask/src/fips/graph.rs
- #1955 feat(openai-files): pin the API contract and route/schema source of truth (+2633/-435) by @r-papso files: apis/Cargo.toml, apis/src/openai/chat_completions/routes/mod.rs, apis/src/openai/conversations/handlers.rs, apis/src/openai/conversations/mod.rs, apis/src/openai/conversations/openapi.rs, apis/src/openai/conversations/rate_limit.rs, apis/src/openai/conversations/routes.rs, apis/src/openai/conversations/tests.rs, apis/src/openai/error.rs, apis/src/openai/files/contracts.rs, apis/src/openai/files/mod.rs, apis/src/openai/files/openapi.rs
- **DTOs:** new experimental `openai-files` feature (in `openai-all`). `files/contracts.rs` holds the wire types.
- **Registry:** each `files_operations!` entry declares its contract...
- #1941 feat(release): publish a per-release support report (+3049/-27) by @nathan-weinberg files: .github/scripts/support_report.py, .github/scripts/vllm_qualification.py, .github/workflows/release.yaml, Makefile, docs/conformance/openresponses-coverage.json, docs/conformance/translation-matrix.json, docs/release.md, tests/qualification/test_support_report.py, tests/qualification/test_vllm_qualification.py, xtask/src/openresponses_coverage.rs, xtask/src/translation_matrix.rs
- `docs/conformance/translation-matrix.json` — declared native and translation behavior, generated from...
- #1979 feat(conformance): add OpenAI verification badges (+687/-48) by @leseb files: .github/workflows/openai-conformance.yaml, README.md, apis/src/openai/responses/rehydrate/tests.rs, apis/src/openai/responses/store/tests.rs, docs/README.md, docs/conformance/README.md, docs/conformance/badges/responses-lifecycle.svg, docs/conformance/badges/responses-persistence.svg, docs/conformance/badges/responses-rehydration.svg, docs/conformance/openai-conformance-report.json, tests/integration/sdk/openai/test_openai_responses_vllm.py, xtask/src/openai_conformance.rs
- #1950 fix(conversations): complete exact API contract conformance (+1475/-605) by @leseb files: apis/src/openai/conversations/error.rs, apis/src/openai/conversations/filter.rs, apis/src/openai/conversations/handlers.rs, apis/src/openai/conversations/mod.rs, apis/src/openai/conversations/rate_limit.rs, apis/src/openai/conversations/routes.rs, apis/src/openai/conversations/tests.rs, docs/conformance/README.md, docs/conformance/openai-conformance-report.json, docs/filters/openai_conversations.md, examples/configs/openai/conversations/conversations.yaml, store-backends/src/postgres.rs
-> trusted owner check
-> op...
- #1870 fix(anthropic): configure translated Messages API version (+892/-43) by @EleanorWho files: apis/src/anthropic/mod.rs, apis/src/anthropic/openai_chat_completions_to_anthropic/config.rs, apis/src/anthropic/openai_chat_completions_to_anthropic/mod.rs, apis/src/anthropic/openai_chat_completions_to_anthropic/tests.rs, apis/src/anthropic/protocol/config.rs, apis/src/anthropic/protocol/mod.rs, apis/src/anthropic/protocol/tests.rs, docs/anthropic-messages.md, docs/developing/openai-anthropic-compatibility.md, docs/filters/openai_chat_completions_to_anthropic.md, examples/README.md, examples/configs/openai-selected-provider-legacy-translation.yaml


### Highlights
- New release **v0.11.0**

## praxis-proxy/praxis (core)


### crates

Summary unavailable (null LLM). Source items:
- #1552 fix(policy): compose metadata response context (+25/-0) by @mkoushni files: crates/filter/src/builtins/http/security/policy/context.rs
- `cargo ...
- #1424 feat(policy): add a config surface for the host-supplied context slots2 (+326/-66) by @aviavissar files: CHANGELOG.md, crates/filter/src/builtins/http/security/policy/filter.rs, crates/filter/src/builtins/http/security/policy/tests.rs, tests/integration/fixtures/context-policy.yaml, tests/integration/tests/suite/examples/policy_context.rs
- [ ] Signed off all commits (`git commit -s`)
- [ ] Tests added or updated
- [ ] Documentation updated (if applicable)
- [ ] CHANGELOG.md updated (if the change is user-visible)
- [ ] `make lint && make test && make test-integration` passes locally
- #1535 refactor(filter): make filter_metadata a bounded FilterMetadata type (+1017/-380) by @alexsnaps files: CHANGELOG.md, crates/filter/src/builtins/http/observability/access_log/mod.rs, crates/filter/src/builtins/http/observability/access_log/tests.rs, crates/filter/src/builtins/http/observability/cloud_events.rs, crates/filter/src/builtins/http/payload_processing/grpc_web/mod.rs, crates/filter/src/builtins/http/payload_processing/grpc_web/tests.rs, crates/filter/src/builtins/http/payload_processing/json_body/tests.rs, crates/filter/src/builtins/http/security/policy/filter.rs, crates/filter/src/builtins/http/security/policy/mod.rs, crates/filter/src/builtins/http/security/policy/rate_limit_tests.rs, crates/filter/src/builtins/http/security/policy/request_input_tests.rs, crates/filter/src/builtins/http/security/policy/tests.rs
- #1517 fix(tls): poll certificate files for missed reloads (+1186/-46) by @cooktheryan files: CHANGELOG.md, crates/protocol/src/tls_setup.rs, crates/tls/Cargo.toml, crates/tls/src/setup.rs, crates/tls/src/watcher.rs, crates/tls/tests/reload_resumption.rs, docs/operating/tls.md, tests/integration/tests/suite/body_filter_failures.rs
- Fingerprint the watched certificate, key, CA, and CRL files on a 10-second
- Keep the watcher alive when `notify` cannot be constructed for the watched

**First-time contributors:** alexsnaps, averevki
### crates-core

Summary unavailable (null LLM). Source items:
- #1499 feat(shutdown): add readiness-first delayed handoff (+3058/-216) by @cooktheryan files: CHANGELOG.md, Cargo.lock, crates/core/Cargo.toml, crates/core/src/config.rs, crates/core/src/config/admin.rs, crates/core/src/config/validate/rules.rs, crates/core/src/server.rs, crates/core/src/server/contract.rs, crates/core/src/server/hyper.rs, crates/core/src/server/lifecycle.rs, crates/core/src/server/pingora.rs, crates/core/src/server/unavailable.rs

### xtask

Summary unavailable (null LLM). Source items:
- #1427 Catch dead doc links and run lint-extra in CI#1391 (+1768/-46) by @aviavissar files: .github/workflows/tests.yaml, .markdownlint.yaml, Makefile, examples/configs/branching/README.md, examples/configs/observability/README.md, examples/configs/payload-processing/README.md, examples/configs/pipeline/README.md, examples/configs/protocols/README.md, examples/configs/traffic-management/README.md, examples/configs/transformation/README.md, xtask/src/lint_doc_links.rs, xtask/src/main.rs
- #1499 feat(shutdown): add readiness-first delayed handoff (+3058/-216) by @cooktheryan files: CHANGELOG.md, Cargo.lock, crates/core/Cargo.toml, crates/core/src/config.rs, crates/core/src/config/admin.rs, crates/core/src/config/validate/rules.rs, crates/core/src/server.rs, crates/core/src/server/contract.rs, crates/core/src/server/hyper.rs, crates/core/src/server/lifecycle.rs, crates/core/src/server/pingora.rs, crates/core/src/server/unavailable.rs



## praxis-proxy/conventions (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #46 docs(maintainers): add Twinkll Sisodia as AI reviewer (+2/-0) by @tsisodia10 files: MAINTAINERS.md
- `make lint` (via the repository pre-commit hook)
- `git diff --check`


## praxis-proxy/enhancements (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #26 build(deps): Bump actions/create-github-app-token from 3.2.0 to 3.3.0 in the actions group across 1 directory [dependencies, github_actions] (+3/-3) by @dependabot files: .github/workflows/proposal-validation.yaml, .github/workflows/stale-proposals.yaml, .github/workflows/status-tracking.yaml
- #36 docs: add background jobs proposal (+155/-0) by @cdoern files: proposals/00807_background-jobs.md


## praxis-proxy/experimental (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #67 build(deps): bump docker/login-action from 4.6.0 to 4.8.0 [dependencies, github_actions] (+2/-2) by @dependabot files: .github/workflows/publish.yaml
- #72 build(deps): bump ubi9/ubi-minimal from 9.8 to 9.9 [dependencies, docker] (+1/-1) by @dependabot files: Containerfile
- #74 ci: repair audit and Markdown checks (+14/-13) by @nerdalert files: Cargo.lock, GOVERNANCE.md, MAINTAINERS.md
- Update only the affected lockfile packages: `rmcp` 3.4.1 → 3.9.0, `rustix` 1.1.4 → 1.1.6, and the yanked `chacha20` 0.10.1 → 0.10.2. The pinned Praxis AI revision is unchanged, and no advisory ignores were add...


## praxis-proxy/gateway-controller (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #76 chore: consolidate test targets into comprehensive make test (+16/-13) by @mikenairn files: .github/pull_request_template.md, .github/workflows/tests.yaml, AGENTS.md, CONTRIBUTING.md, Makefile, README.md
- [x] I have read every l...
- #74 Fix joinValidationErrors truncation and improve integration tests (+86/-2) by @philbrookes files: internal/controller/proxy_validation.go, internal/controller/proxy_validation_test.go, test/integration/proxy_controller_test.go
- Fix `joinValidationErrors` truncation to preserve first error content alongside the `(and N more)` suffix
- Count fully omitted errors in the remainder suffix and recalculate the byte budget
- Truncate to UTF-8 rune boundaries to avoid splitting multi-byte characters
- Add regression test for three-error truncation with separator handling
- #73 fix(test): stop e2e runs reporting false success (+13/-4) by @mikenairn files: Makefile, hack/setup-kind.sh, test/e2e/e2e_suite_test.go
* Fail e2e test suite if it can't connect to a cluster.
* Update controller deployment in kind-up to roll out the deployment and wait on the new ReplicaSet.
- #69 add guard rails and limits as v1alpha1 scope. (+70/-10) by @maleck13 files: docs/design/api-v1alpha1.md
- #29 Implement Proxy spec validation (+615/-7) by @philbrookes files: internal/controller/proxy_controller.go, internal/controller/proxy_validation.go, internal/controller/proxy_validation_test.go, test/integration/crd_test.go, test/integration/integration_suite_test.go, test/integration/policy_controller_test.go, test/integration/proxy_controller_test.go


## praxis-proxy/grid (watch)

### Releases
- [v0.3.1](https://github.com/praxis-proxy/grid/releases/tag/v0.3.1) — 2026-11-13: Grid v0.3.1
### Changes

Summary unavailable (null LLM). Source items:
- #603 fix(ci): restore reliable dependency checks on Rust 1.96 (+180/-13) by @nerdalert files: .github/workflows/gateway.yaml, .github/workflows/release.yaml, .github/workflows/tests.yaml, Makefile, crates/gateway/Cargo.toml, crates/gateway/deny.toml, deny.toml, scripts/check-unused-dependencies.py, scripts/test-gateway-dependencies.py
- Pin cargo-machete to the published 0.9.2 release. The newer 0.10.1 release fails to compile on Rust 1.96; Praxis AI uses the same pin.
- Fix the Gateway manifest declarations so cargo-machete checks the package instead of silently skipping it. Dependency versions, features, and lockfiles ...
- #366 feat(api): publish AgentToAgentProvider contract and install artifacts (+2055/-96) by @liavweiss files: .github/workflows/tests.yaml, Makefile, charts/grid-operator/README.md, charts/grid-operator/templates/clusterrole-crd.yaml, charts/grid-operator/templates/crds/agenttoagentprovider.yaml, charts/grid-operator/tests/clusterrole-crd_test.yaml, charts/grid-operator/tests/crds_test.yaml, charts/grid-operator/values.schema.json, charts/grid-operator/values.yaml, config/samples/agent-to-agent-provider.yaml, crates/operator/Cargo.toml, crates/operator/src/bin/generate_crds.rs
- Replaced the placeholder `AgentToAgentProvider` type with a bounded `v1al...
- #575 ci: make FIPS optional for combined-site qualification (+1208/-73) by @nerdalert files: .github/workflows/triggered-integration-test.yaml, crates/xtask/src/env/combined_site_demo.rs, docs/release.md, scripts/combined-site-cleanup-ownership.sh, scripts/test-combined-site-cleanup-ownership.sh, tests/e2e/topologies/grid-combined-site/README.md
- Make the FIPS operator image optional so full combined-site/SWIM qualification runs by default with the standard image on GitHub-hosted Ubuntu runners. Keep FIPS as an explicit option for a FIPS-enabled self-hosted runner.
- Guard FIPS mode with a host kernel check and reject PR merge sources on the self-hosted runner. Record the selected image mode in the image manifest, artifact...
- #592 test(e2e): add and remove models and a site under Local membership (+312/-78) by @hexfusion files: scripts/e2e-acm-path.sh
- A site declares a provider with two models. Then it gains a model, loses a model, gains a second provider, and loses that provider. ...
- #594 chore(release): prepare v0.3.1 (+120/-120) by @hexfusion files: Cargo.lock, Cargo.toml, charts/grid-enrollment/Chart.yaml, charts/grid-mock-providers/Chart.yaml, charts/grid-operator/Chart.yaml, charts/grid-site/Chart.yaml, charts/praxis-gateway/Chart.yaml, charts/praxis-gateway/README.md, charts/praxis-gateway/values.yaml, crates/fleet-dashboard/charts/grid-fleet-dashboard/Chart.yaml, crates/fleet-dashboard/charts/grid-fleet-dashboard/tests/golden/central-monitor-demo.yaml, crates/fleet-dashboard/charts/grid-fleet-dashboard/tests/golden/default.yaml
* **Release**

### Highlights
- New release **v0.3.1** — Grid v0.3.1

## praxis-proxy/operator (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #24 feat(k8s): add operator rollout acceptance (+2394/-313) by @cooktheryan files: .github/workflows/conformance.yaml, .github/workflows/integration.yaml, .github/workflows/rollout.yaml, CHANGELOG.md, deploy/rollout-test/backend.yaml, deploy/rollout-test/gateway.yaml, deploy/rollout-test/httproute.yaml, deploy/rollout-test/kustomization.yaml, deploy/rollout-test/namespace.yaml, deploy/rollout-test/service.yaml, docs/architecture.md, docs/configuration.md
- Add the operator-owned rollout reference resources consumed by praxis-proxy/praxis#1494.
- Preserve one replica by default; support the `praxis.sh/replicas` annotation, zero-unavailable rolling updates, a PodDisruptionBudget, hostname/zone spread, and a five-second preStop delay within the existing grace period.
- Generate Praxis `0.7.5`-compatible listener-scoped configuration with ...
- #20 Add license scan report and status (+5/-0) by @fossabot files: README.md
- [CircleCI](https://docs.fossa.com/docs/circleci)
- [TravisCI](https://docs.fossa.com/docs/travisci)
- [Jenkins](https://github.com/fossas/fossa-jenkins-plugin)
- [Other](https://github.com/fossas/fossa...
- #18 chore(deps): bump the patch-and-minor group across 1 directory with 2 updates [dependencies, rust] (+4/-4) by @dependabot files: Cargo.lock


## praxis-proxy/policy (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #287 feat(apl): execute fetch before policy decisions [enhancement, area/security] (+1779/-88) by @mkoushni files: CHANGELOG.md, crates/ppe-apl-core/src/attributes.rs, crates/ppe-apl-core/src/evaluator.rs, crates/ppe-apl-core/src/parser.rs, crates/ppe-apl-core/src/rules.rs, crates/ppe-apl-core/src/step.rs, crates/ppe-apl-runtime/src/cmf_invoker.rs, crates/ppe-apl-runtime/src/dispatch_plan.rs, crates/ppe-apl-runtime/src/route_handler.rs, crates/ppe-apl-runtime/src/visitor.rs, crates/ppe-apl-runtime/tests/cmf_invoker_dispatch.rs, crates/ppe-apl-runtime/tests/fetch_metadata_e2e.rs
- #284 docs(brainstorms): revocation and transaction tokens requirements. (+1062/-0) by @terylt files: docs/brainstorms/2026-10-26-revocation-transaction-tokens-requirements.md


## praxis-proxy/praxis-proxy.github.io (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #47 feat(website): publish enhancement proposals from the enhancements repo [approved, needs-kind] (+931/-4) by @leseb files: .gitmodules, Makefile, README.md, assets/scss/_styles_project.scss, content/enhancements/_index.md, data/enhancements.json, layouts/_partials/enhancements/criteria-heading.html, layouts/_partials/enhancements/lifecycle.html, layouts/_partials/navbar.html, layouts/enhancements/baseof.html, layouts/enhancements/list.html, layouts/enhancements/single.html
- #44 chore(website): update docs versions to latest releases [needs-kind] (+15/-8) by @github-actions files: data/docs_versions.json, packages/hugoautogen/hugo_packagemeta.json, sources/ai
- Promotes each project's docs default to the latest release eligible under each project’s configured policy and moves the matching submodule pointer.
- Refreshes the development channel SHAs (`development` in
- #46 feat(ci): auto-merge docs update pull requests [approved, needs-kind] (+10/-0) by @leseb files: .github/workflows/update-docs.yml
- **Before:** The docs updater opens a PR and dispatches checks, but leaves merge action to a person.
- **After:** The updater requests squash auto-merge for its generated PR. The repository auto-merge setting is enabled; the main ruleset r...
- #45 fix(ci): sign off automated docs update commits [approved, needs-kind] (+2/-1) by @leseb files: .github/workflows/update-docs.yml
- automated commits omit DCO sign-off
- **Before:** Release update PR #44 failed DCO on the workflow-generated snapshot commit.
- **After:** The workflow now signs off both the validation snapshot commit and the commit created by `create-pull-request`. CI will verify the updated automation...
- #34 chore: update contributing links to go directly to document [approved, kind/cleanup] (+4/-4) by @nathan-weinberg files: content/community/_index.md


