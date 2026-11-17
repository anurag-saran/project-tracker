# llm-d digest — 2026-11-17

_Since 7d · generated 2026-11-17T02:42:58Z_

## TL;DR for this week

- Release llm-d/llm-d-inference-sim@v1.2.0-rc1
- Release llm-d/llm-d-inference-sim@v1.2.0-rc.2
- Release llm-d/llm-d-inference-sim@v1.2.0
- Release llm-d/llm-d-batch-gateway@v1.1.0-rc1
- Release llm-d/llm-d-batch-gateway@v1.0.1-rc1

## llm-d/llm-d (core)


### guides

Summary unavailable (null LLM). Source items:
- #3041 feat(fma-keda): add GKE overlays and nightly E2E lane for Fast Model Actuation + KEDA (+719/-38) by @RyanRosario files: .github/slack-channels.yaml, .github/workflows/consolidate-status-fast-model-actuation-keda-gke-acc-gpu-vllm-x.yaml, .github/workflows/nightly-e2e-fast-model-actuation-keda-gke-acc-gpu-vllm-x.yaml, .github/workflows/nightly-e2e-fast-model-actuation-keda-ibm-acc-gpu-vllm-x.yaml, .github/workflows/notify-slack-nightly.yaml, guides/fast-model-actuation/components/gke/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/README.md, guides/fast-model-actuation/fast-model-actuation-keda/guide.yaml, guides/fast-model-actuation/fast-model-actuation-keda/keda/gke/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/modelserver/gpu/vllm/base/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/modelserver/gpu/vllm/gke/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/modelserver/gpu/vllm/ocp/kustomization.yaml
- **GKE Platform & Monitoring Overlays...
- #3040 feat(fma): add GKE platform overlay and nightly E2E lane for Fast Model Actuation (+550/-20) by @RyanRosario files: .github/slack-channels.yaml, .github/workflows/consolidate-status-fast-model-actuation-gke-acc-gpu-vllm-x.yaml, .github/workflows/nightly-e2e-fast-model-actuation-gke-acc-gpu-vllm-x.yaml, .github/workflows/nightly-e2e-fast-model-actuation-ibm-acc-gpu-vllm-x.yaml, .github/workflows/notify-slack-nightly.yaml, guides/fast-model-actuation/README.md, guides/fast-model-actuation/components/gke/kustomization.yaml, guides/fast-model-actuation/guide.yaml, guides/fast-model-actuation/modelserver/gpu/vllm/base/kustomization.yaml, guides/fast-model-actuation/modelserver/gpu/vllm/gke/kustomization.yaml, guides/fast-model-actuation/modelserver/gpu/vllm/ocp/kustomization.yaml, guides/fast-model-actuation/platform/gke/kustomization.yaml
- **GKE Kustomize Component (`guides/fast-model-actuation/components/gke/kustomization.yaml`)**:
- GKE Container-Optimized OS (COS) nodes do not have an `nvidia` `RuntimeClass` or NVIDIA GPU Feature Discovery labels (`nvidia.com/gpu.p...
- #3039 pd-disaggregation amd-ci: generate UCX kernel config for the running kernel (+21/-26) by @sheralskumar files: guides/pd-disaggregation/modelserver/amd/vllm/nixl/amd-ci/config-6.8.0-124-generic, guides/pd-disaggregation/modelserver/amd/vllm/nixl/amd-ci/kustomization.yaml, guides/pd-disaggregation/modelserver/amd/vllm/nixl/amd-ci/patch-amd-ci.yaml
- #3019 feat(fma): Update the WLPs to FMA v0.8.0 (+39/-39) by @dumb0002 files: .github/scripts/install-fma-crds.sh, guides/fast-model-actuation/README.md, guides/fast-model-actuation/fast-model-actuation-keda/README.md, guides/fast-model-actuation/fast-model-actuation-keda/guide.yaml, guides/fast-model-actuation/fast-model-actuation-keda/modelserver/gpu/vllm/base/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/modelserver/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/router/fast-model-actuation-keda.values.yaml, guides/fast-model-actuation/guide.yaml, guides/fast-model-actuation/modelserver/inferenceserverconfig.yaml, guides/fast-model-actuation/modelserver/launcherconfig.yaml, guides/fast-model-actuation/requester/deployment.yaml, guides/fast-model-actuation/router/fast-model-actuation.values.yaml
- #2901 guides(optimized-baseline): enable SGLang Rust server on NVIDIA GPU (+28/-0) by @andreyod files: docs/architecture/model-servers/sglang.md, guides/optimized-baseline/README.md, guides/optimized-baseline/modelserver/gpu/sglang/base/patch-sglang.yaml

**First-time contributors:** andreyod, sheralskumar
### release

Summary unavailable (null LLM). Source items:
- #3041 feat(fma-keda): add GKE overlays and nightly E2E lane for Fast Model Actuation + KEDA (+719/-38) by @RyanRosario files: .github/slack-channels.yaml, .github/workflows/consolidate-status-fast-model-actuation-keda-gke-acc-gpu-vllm-x.yaml, .github/workflows/nightly-e2e-fast-model-actuation-keda-gke-acc-gpu-vllm-x.yaml, .github/workflows/nightly-e2e-fast-model-actuation-keda-ibm-acc-gpu-vllm-x.yaml, .github/workflows/notify-slack-nightly.yaml, guides/fast-model-actuation/components/gke/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/README.md, guides/fast-model-actuation/fast-model-actuation-keda/guide.yaml, guides/fast-model-actuation/fast-model-actuation-keda/keda/gke/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/modelserver/gpu/vllm/base/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/modelserver/gpu/vllm/gke/kustomization.yaml, guides/fast-model-actuation/fast-model-actuation-keda/modelserver/gpu/vllm/ocp/kustomization.yaml
- **GKE Platform & Monitoring Overlays...
- #3040 feat(fma): add GKE platform overlay and nightly E2E lane for Fast Model Actuation (+550/-20) by @RyanRosario files: .github/slack-channels.yaml, .github/workflows/consolidate-status-fast-model-actuation-gke-acc-gpu-vllm-x.yaml, .github/workflows/nightly-e2e-fast-model-actuation-gke-acc-gpu-vllm-x.yaml, .github/workflows/nightly-e2e-fast-model-actuation-ibm-acc-gpu-vllm-x.yaml, .github/workflows/notify-slack-nightly.yaml, guides/fast-model-actuation/README.md, guides/fast-model-actuation/components/gke/kustomization.yaml, guides/fast-model-actuation/guide.yaml, guides/fast-model-actuation/modelserver/gpu/vllm/base/kustomization.yaml, guides/fast-model-actuation/modelserver/gpu/vllm/gke/kustomization.yaml, guides/fast-model-actuation/modelserver/gpu/vllm/ocp/kustomization.yaml, guides/fast-model-actuation/platform/gke/kustomization.yaml
- **GKE Kustomize Component (`guides/fast-model-actuation/components/gke/kustomization.yaml`)**:
- GKE Container-Optimized OS (COS) nodes do not have an `nvidia` `RuntimeClass` or NVIDIA GPU Feature Discovery labels (`nvidia.com/gpu.p...



## llm-d-incubation/llm-d-fast-model-actuation (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #835 Require launcher inference port pools [ready-for-ai-review] (+124/-279) by @waltforme files: api/fma/v1alpha1/inferenceserverconfig_types.go, api/fma/v1alpha1/launcherconfig_types.go, config/crd/fma.llm-d.ai_inferenceserverconfigs.yaml, config/crd/fma.llm-d.ai_launcherconfigs.yaml, config/crds.yaml, docs/dual-pods.md, pkg/controller/dual-pods/inference-server.go, pkg/generated/applyconfiguration/fma/v1alpha1/modelserverconfig.go, test/e2e/mkobjs-openshift.sh, test/e2e/mkobjs.sh, test/e2e/test-cases.sh
- #832 deps(go): bump github.com/spf13/pflag from 1.0.10 to 1.1.0 in the go-dependencies group across 1 directory [dependencies, ready-for-ai-review] (+3/-3) by @dependabot files: go.mod, go.sum
- #819 ci: add shellcheck pre-commit hook and fix findings [sentinel-alert, ready-for-human-review] (+44/-19) by @rubambiza files: .pre-commit-config.yaml, hack/verify-idl-consumption.sh, inference_server/benchmark/setup_kind_resources.sh, test/e2e/deploy-wva-stack.sh, test/e2e/run-launcher-based.sh, test/e2e/run.sh, test/e2e/test-cases.sh, test/e2e/validate.sh
- #837 Remove CI testing of release 0.7.1 [ready-for-ai-review] (+1/-1) by @MikeSpreitzer files: .github/workflows/launcher-based-e2e-test.yml
- #828 test(metrics): isolate launcher creation samples [ready-for-ai-review] (+41/-29) by @delavet files: pkg/controller/launcher-populator/helpers_test.go


## llm-d-incubation/llm-d-lens (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #128 Validate BLIS results and assess constraints (+869/-1) by @VincyZhang files: apps/backend/src/llm_d_lens/estimate_tools/blis/service.py, apps/backend/tests/unit/estimate_tools/test_blis.py
- Reject malformed, duplicate-key, trailing, nonfinite, incomplete-schema, or inconsistent result evidence explicitly.
- Verify compiled bundle integrity, request attribution, runtime revisions, workload controls, overrides, and metric definitions.
- Preserve native metric names, un...
- #124 Write kubeconfigs atomically and keep engine instances out of orphan cleanup (+336/-24) by @joshuayao files: apps/backend/src/llm_d_lens/cluster/registry.py, apps/backend/src/llm_d_lens/deploy/orphans.py, apps/backend/src/llm_d_lens/deploy/router.py, apps/backend/tests/unit/cluster/test_service.py, apps/backend/tests/unit/deploy/test_orphans.py, docs/site/i18n/en/docusaurus-plugin-content-docs/current/api-reference/modules/deployments.mdx, docs/site/i18n/zh-CN/docusaurus-plugin-content-docs/current/api-reference/modules/deployments.mdx
- `kubeconfig_path` writes the cluster kubeconfig to a temporary file and renames it into place.
- Orphan namespace scan and cleanup skip namespaces holding a `lens` engine instance (inventory ConfigMap) and refuse namespaces they cannot check.
- The kubeconfig was rewritten in place on every call, so concurrent kubectl calls could read ...
- #127 Add bounded BLIS subprocess execution (+394/-1) by @VincyZhang files: apps/backend/src/llm_d_lens/estimate_tools/blis/service.py, apps/backend/tests/unit/estimate_tools/test_blis.py
- Launch the managed binary through the shared process infrastructure with fixed arguments, closed stdin, an isolated environment and a caller-owned bundle directory.
- Bound execution with a default 120-second process timeout and an 8 MiB combined stdout/stderr retention limit...
- #122 Compile BLIS deployment bundles and workloads (+903/-2) by @VincyZhang files: apps/backend/src/llm_d_lens/estimate_tools/blis/service.py, apps/backend/tests/unit/estimate_tools/test_blis.py


## llm-d-incubation/llm-d-scaling-manager (watch)

### Releases
- [v0.11.1](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.1) — 2026-11-15: llm-d-scaling-manager v0.11.1- [v0.11.1-rc2](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.1-rc2) — 2026-11-14: llm-d-scaling-manager v0.11.1-rc2- [v0.11.0](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.0) — 2026-11-12: llm-d-scaling-manager v0.11.0
### Changes

Summary unavailable (null LLM). Source items:
- #148 chore(release): reset newTag to main after v0.11.2-rc2 (+1/-1) by @ev-shindin files: config/base/manager/kustomization.yaml
- :seedling: `config/base/manager/kustomization.yaml` pins `newTag: main` again.
- #147 chore(release): pin v0.11.2-rc2 (+1/-1) by @ev-shindin files: config/base/manager/kustomization.yaml
- :seedling: `config/base/manager/kustomization.yaml` pins `newTag: v0.11.2-rc2`, so the tag can be pushed on this PR's merge commit. The reset to `newTag: main` follows once the release run has succeeded.
- #143 chore(router): move to llm-d-router v1.0.0 (+1318/-213) by @ev-shindin files: .github/workflows/ci-e2e-openshift.yaml, .github/workflows/ci-pr-checks.yaml, Makefile, config/samples/analyzers/external-analyzers.yaml, deploy/grafana/operational-dashboard.json, deploy/inference-objective-e2e.yaml, deploy/install-epp.sh, deploy/lib/epp-base.values.yaml, deploy/lib/epp-flow-control.values.yaml, deploy/lib/epp-optimized-baseline.values.yaml, deploy/lib/infra_epp.sh, deploy/lib/infra_monitoring.sh
- :arrow_up: **Router v1.0.0 ...
- #141 fix(install): install against a plain HTTP Prometheus with --allow-http (+1283/-63) by @ev-shindin files: config/release/settings-configmap.yaml, deploy/lib/release_install.sh, deploy/scaling-manager-tools.sh, docs/guides/install-cluster-wide/README.md, docs/guides/install-in-namespace/README.md, docs/proposals/install-from-release.md, docs/reference/configuration-advanced.md, docs/reference/configuration.md, docs/reference/preflight.md, docs/reference/prometheus.md, docs/reference/tools-install.md, docs/reference/troubleshooting.md
- #144 fix(make): install setup-envtest by its tag, not a release branch (+7/-4) by @ev-shindin files: Makefile
- #140 chore(release): reset newTag to main after v0.11.2-rc1 (+1/-1) by @ev-shindin files: config/base/manager/kustomization.yaml
- :seedling: `config/base/manager/kustomization.yaml` pins `newTag: main` again.
- #139 chore(release): pin v0.11.2-rc1 (+1/-1) by @ev-shindin files: config/base/manager/kustomization.yaml
- :seedling: `config/base/manager/kustomization.yaml` pins `newTag: v0.11.2-rc1`, so the tag can be pushed on this PR's merge commit. The reset to `newTag: main` follows once the release run has succeeded.

### Highlights
- New release **v0.11.1** — llm-d-scaling-manager v0.11.1
- New release **v0.11.1-rc2** — llm-d-scaling-manager v0.11.1-rc2
- New release **v0.11.0** — llm-d-scaling-manager v0.11.0

## llm-d-incubation/llm-d-validate (watch)

### Releases
- [v0.1.0](https://github.com/llm-d-incubation/llm-d-validate/releases/tag/v0.1.0) — 2026-11-14: llm-d-validate v0.1.0
### Changes

Summary unavailable (null LLM). Source items:
- #46 Report a local connection lost mid-run as the environment [kind/bug] (+427/-22) by @Vezio files: AGENTS.md, docs/manual.md, src/llmdv/cli/exit_codes.py, src/llmdv/cli/verify_cmd.py, src/llmdv/evidence/outcome.py, src/llmdv/http/client.py, src/llmdv/plugin.py, src/llmdv/preflight.py, src/llmdv/profile/schema.py, src/llmdv/results/record.py, tests/fakes.py, tests/test_connection_lost.py
- the case that hit it is recorded as `error` naming the lost connection ("your environment, not the fleet");
- lat...
- #42 Derive the layer graph from ingress kinds and pair layers by one rule [kind/feature] (+528/-25) by @Vezio files: .agents/DECISIONS.md, docs/architecture.md, docs/compare.md, profiles/REFERENCE.md, src/llmdv/cli/verify_cmd.py, src/llmdv/evidence/alerts.py, src/llmdv/evidence/outcome.py, src/llmdv/profile/README.md, src/llmdv/profile/schema.py, src/llmdv/profile/topology.py, tests/test_outcome.py, tests/test_topology.py
**Stacked on #33**; the top commit is this PR's.
- Adds a layer graph derived from today's ingress kinds (`src/llmdv/profile/topology.py`): each ingress fronts the ingresses at the next deeper kind that is present; two ingresses of one kind are peers with no edge between them. `Profile.chain()` returns its order.
- The summary ladder and `alerts.attribute` now share o...
- #41 Add an engine-only example profile [kind/docs] (+91/-0) by @Vezio files: .agents/skills/writing-an-infra-profile/SKILL.md, profiles/README.md, profiles/examples/README.md, profiles/examples/example-engine-only.yaml, tests/test_plan.py
- #39 State that the core validates any serving stack, and test it [kind/feature] (+82/-3) by @Vezio files: AGENTS.md, src/llmdv/profile/schema.py, tests/test_stack_agnostic_core.py
- AGENTS.md gains a hard rule: the core validates any model-serving stack. Nothing in `src/` depends on an llm-d guide, a guide's name, `guide.yaml` or llm-d's `llm-d.ai/*` pod labels; pods are found through selectors the profile declares; guide support is data and optional conveniences on top.
- `tests/test_stack_agnostic_core.py` fails when a core module refers to an...
- #43 Judge statistical claims as one check over declared samples [kind/feature] (+974/-97) by @Vezio files: .agents/skills/extending-llmdv/SKILL.md, profiles/REFERENCE.md, src/llmdv/assertions/README.md, src/llmdv/assertions/samples.py, src/llmdv/evidence/bundle.py, src/llmdv/evidence/journal.py, src/llmdv/plugin.py, src/llmdv/profile/loader.py, src/llmdv/profile/schema.py, src/llmdv/suites/conftest.py, src/llmdv/suites/openai_chat/test_repeats.py, src/llmdv/suites/openai_chat/test_thinking.py

### Highlights
- New release **v0.1.0** — llm-d-validate v0.1.0

## llm-d-incubation/py-inference-scheduler (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #85 docs: add an overscheduling guide (+245/-0) by @aniketmohanty82 files: .agents/skills/overscheduling/SKILL.md, docs/guides/overscheduling.md, integration/verl/README.md
- Running overscheduling takes a scheduler profile, a Mooncake master and client config, four connector overrides and four env vars, and nothing documents them in one place.
- This adds an overscheduling guide that walks through each step and lists the metrics that show it works.
- It also adds an overscheduling skill so agents can diagnose a setup: where each part lives in the ...


## llm-d/llm-d-async (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #552 fix(sqlflow): report the broker backlog source as available (+24/-0) by @sohom-cs files: pkg/sqlflow/flow.go, pkg/sqlflow/flow_test.go
- #537 deps(go): bump the go-dependencies group with 5 updates [dependencies, release-note-none] (+21/-21) by @dependabot files: go.mod, go.sum
- #553 fix(server): warn when prometheus-ca-cert alone cannot authenticate GMP queries (+114/-7) by @mstandley-tempus files: docs/deployment.md, pkg/async/inference/flowcontrol/gate_factory.go, pkg/async/inference/flowcontrol/gate_factory_test.go, pkg/server/prometheus_gate_test.go, pkg/server/runner.go, release-notes.d/unreleased/553.md
- Adds a startup warning when `--prometheus-ca-cert` is set without `--prometheus-bearer-token-file` while `--prometheus-url` targets Google Managed Prometheus (`monitoring.googleapis.com...
- #554 refactor(flowcontrol): remove dead flag-driven GMP gate path (+0/-48) by @mstandley-tempus files: pkg/async/inference/flowcontrol/binary_metric_dispatch_gate.go, pkg/async/inference/flowcontrol/metric_source.go
- Deletes the four package-level flags `gate.pmetric.is-gmp`, `gate.prometheus.url`, `gate.pmetric.gmp.project-id`, and `gate.prometheus.model-name` from [binary_metric_dispatch_gate.go](pkg/async/inference/flowcontrol/binary_...
- #547 fix(flowcontrol): authenticate prometheus gates to Google Managed Prometheus (+431/-8) by @mstandley-tempus files: docs/deployment.md, pkg/async/inference/flowcontrol/gate_factory.go, pkg/async/inference/flowcontrol/gate_factory_test.go, pkg/async/inference/flowcontrol/metric_source.go, release-notes.d/unreleased/547.md
- #539 feat(gates): authenticate Prometheus gate queries with a bearer token and CA (+406/-7) by @aneeshkp files: charts/llm-d-async/templates/ap-deployments.yaml, charts/llm-d-async/tests/deployment_test.yaml, charts/llm-d-async/values.yaml, docs/deployment.md, go.mod, pkg/async/inference/flowcontrol/gate_factory.go, pkg/async/inference/flowcontrol/prometheus_client.go, pkg/async/inference/flowcontrol/prometheus_client_test.go, pkg/server/options.go, pkg/server/prometheus_gate_test.go, pkg/server/runner.go, release-notes.d/unreleased/539.md
-  promapi.Config{Address: prometheusURL}


## llm-d/llm-d-autoscaling (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #1613 benchmark/protocol: add the keda-epp inflight verdict (+200/-0) by @mamy-CS files: benchmark/protocol/verdicts/keda-epp/inflight.md
- :gift: Add `benchmark/protocol/verdicts/keda-epp/inflight.md`: the static signal analysis of the keda-epp guide's `inflight` ScaledObject (`sum(llm_d_epp_inflight_requests)`, `AverageValue`, threshold 16), read a...
- #1614 static analysis: change load definition (+117/-45) by @lionelvillard files: .claude/skills/static-signal-analysis/SKILL.md, benchmark/protocol/1-per-trigger-how-to.md, benchmark/protocol/1-static-signal-analysis.md, benchmark/protocol/verdicts/pd-disaggregation/kv-early.md
- #1615 Allow lgtm write (+1/-0) by @lionelvillard files: .github/workflows/prow-github.yml
- Add `statuses: write` to the top-level `permissions` block in `.github/workflows/prow-github.yml`.
- #1610 Work rate based KEDA config (staging) [approved] (+2306/-10) by @lionelvillard files: .claude/skills/run-benchmark/SKILL.md, Makefile, benchmark/README.md, benchmark/config/cluster-configs/k8s/model-sim-qwen3-8b-npd.yaml, benchmark/config/cluster-configs/ocp/vllm-npd.yaml, benchmark/config/scenarios/staging/optimized-baseline/baseline.yaml, benchmark/config/scenarios/staging/optimized-baseline/npd-fcoff.yaml, benchmark/config/specification/staging/optimized-baseline/baseline.yaml.j2, benchmark/config/specification/staging/optimized-baseline/npd-fcoff.yaml.j2, benchmark/config/workloads/npd-fcoff/README.md, benchmark/config/workloads/npd-fcoff/agentic.yaml.in, benchmark/config/workloads/npd-fcoff/bootstrap.yaml.in
- #1612 Add evaluation protocol (+1148/-0) by @lionelvillard files: .claude/skills/static-signal-analysis/SKILL.md, benchmark/README.md, benchmark/protocol/1-per-trigger-how-to.md, benchmark/protocol/1-static-signal-analysis.md, benchmark/protocol/README.md, benchmark/protocol/traps.md, benchmark/protocol/verdicts/pd-disaggregation/kv-early.md
- **Protocol overview** (`benchmark/protocol/README.md`): a step table, linked from `benchmark/READ...
- #1611 benchmark: run vLLM v0.31.0 in the ocp backend overlays (+9/-4) by @lionelvillard files: benchmark/config/cluster-configs/ocp/model-sim-qwen3-32b.yaml, benchmark/config/cluster-configs/ocp/vllm.yaml
- `ocp/model-sim-qwen3-32b.yaml`: CPU image moved from `vllm/vllm-openai-cpu:v0.2...


## llm-d/llm-d-batch-gateway (watch)

### Releases
- [v1.0.1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.1) — 2026-11-16: v1.0.1- [v1.0.1-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.1-rc1) — 2026-11-16: v1.0.1-rc1- [v1.1.0-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.1.0-rc1) — 2026-11-12: v1.1.0-rc1 (deprecated, use v1.0.1)
### Changes

Summary unavailable (null LLM). Source items:
- #785 fix(s3): publish large stream outputs with a server-side multipart copy [bug] (+499/-35) by @dundysm files: internal/files_store/s3/client.go, internal/files_store/s3/client_test.go
- #778 feat(processor): carry the job tenant in async request metadata [feature] (+307/-10) by @aneeshkp files: charts/batch-gateway/README.md, charts/batch-gateway/templates/processor-configmap.yaml, charts/batch-gateway/tests/processor-configmap_test.yaml, charts/batch-gateway/values.yaml, cmd/batch-processor/config.yaml, internal/processor/config/config.go, internal/processor/config/config_test.go, internal/processor/pipeline/async_test.go, internal/processor/pipeline/dispatcher_async.go, internal/processor/pipeline/request_item.go, internal/processor/worker/source_planfile.go, internal/processor/worker/source_planfile_test.go
- #720 fix: check job ownership on every progress interval [bug, lifecycle/stale] (+572/-16) by @jia-gao files: internal/processor/pipeline/progress_tracker.go, internal/processor/pipeline/progress_tracker_test.go, internal/processor/worker/execute_pipeline.go, internal/processor/worker/execute_pipeline_test.go, internal/processor/worker/progress_check_pg_test.go, internal/processor/worker/status_updater.go
- #745 feat(files_store): add native GCS file backend [feature] (+3380/-49) by @mstandley-tempus files: .github/workflows/ci-integration-tests.yml, Makefile, charts/batch-gateway/templates/_helpers.tpl, charts/batch-gateway/templates/apiserver-configmap.yaml, charts/batch-gateway/templates/gc-configmap.yaml, charts/batch-gateway/templates/processor-configmap.yaml, charts/batch-gateway/tests/apiserver-configmap_test.yaml, charts/batch-gateway/tests/gc-configmap_test.yaml, charts/batch-gateway/tests/processor-configmap_test.yaml, charts/batch-gateway/values.yaml, cmd/apiserver/config.yaml, cmd/batch-gc/config.yaml
- #780 test(e2e): let BatchAPIHardKillRecovery run against any Async deployment [release-note-none] (+42/-12) by @aneeshkp files: test/e2e/README.md, test/e2e/dispatcher_hard_kill_test.go
-  --selector app.kubernetes.io/instance=$TEST_DISPATCHER_RELEASE,app.kubernetes.io/name=llm-d-async
-  pod.Image == "ghcr.i...
- #773 deps: bump llm-d-async producer-sql to versioned sql migrations [dependencies] (+25/-9) by @aneeshkp files: go.mod, go.sum, pkg/clients/inference/async_inference_client_integration_test.go, pkg/clients/inference/async_inference_client_resolver_test.go
- The llm-d-async processor now applies migrations at startup. Its migration `0001` drops the old `async_schema` table and records the version in `async_schema_migrations`.
- The `producer-sql` we pin (`3c134ef6d2ce`, llm-d/llm-d-async#...

### Highlights
- New release **v1.0.1** — v1.0.1
- New release **v1.0.1-rc1** — v1.0.1-rc1
- New release **v1.1.0-rc1** — v1.1.0-rc1 (deprecated, use v1.0.1)

## llm-d/llm-d-benchmark (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #2160 Keep a treatment's dotted keys out of shared setup constants (+37/-1) by @RaphaelFakhri files: llmdbenchmark/experiment/parser.py, tests/test_experiment.py
- #2156 Persist vllm compile cache (+1135/-29) by @ruocco files: config/README.md, config/templates/jinja/13_ms-values.yaml.j2, config/templates/jinja/14_standalone-deployment_yaml.j2, config/templates/jinja/24_fma-deployment.yaml.j2, config/templates/jinja/_macros.j2, config/templates/values/defaults.yaml, docs/developer-guide.md, docs/openshift-setup.md, docs/upstream-versions.md, llmdbenchmark/cli.py, llmdbenchmark/executor/README.md, llmdbenchmark/executor/context.py
- #2152 Add a client-side speculative prefill recipe to the inference-perf mu… (+398/-27) by @sywangyi files: tests/test_inference_perf_chat_multiturn.py, tests/test_inference_perf_lifecycle.py, workload/README.md, workload/harnesses/inference-perf-llm-d-benchmark.sh, workload/harnesses/inference_perf_chat_multiturn.py, workload/profiles/inference-perf/speculative_prefill_multi_turn.yaml.in
- #2135 fix(ci): let the unstale workflow remove labels from PRs (+1/-0) by @sugix files: .github/workflows/unstale.yaml
- #2125 Pin the HuggingFace revision of the step 04 model download with model.revision (+116/-2) by @NopeCharon files: config/README.md, config/templates/jinja/03_download_daemonset.yaml.j2, config/templates/jinja/04_download_job.yaml.j2, config/templates/values/defaults.yaml, llmdbenchmark/parser/config_schema.py, tests/test_config_schema.py, tests/test_model_download_revision.py
- #2130 deps(actions): bump pypa/gh-action-pypi-publish from 1.14.2 to 1.14.3 (+1/-1) by @dependabot files: .github/workflows/br-release.yaml
- #2126 Fix "unparseable" typos reported by the nightly scan (+3/-3) by @NopeCharon files: config/README.md, llmdbenchmark/utilities/standup_parameters.py, tests/test_update_invocation.py
- `llmdbenchmark/utilities/standup_parameters.py`: the warning logged when a persisted `--set` pair from the invocation Secret no longer parses
- `tests/test_update_invocation.py`: the name of the test that covers that warning
- `config/README.md`: the routing-table settle del...
- #2128 Add the artifact base class and kind registry (+2942/-2252) by @Bslabe123 files: benchmark-report/README.md, benchmark-report/llmd_benchmark_report/__init__.py, benchmark-report/llmd_benchmark_report/artifacts/__init__.py, benchmark-report/llmd_benchmark_report/artifacts/base.py, benchmark-report/llmd_benchmark_report/artifacts/benchmark_report/__init__.py, benchmark-report/llmd_benchmark_report/artifacts/benchmark_report/base.py, benchmark-report/llmd_benchmark_report/artifacts/benchmark_report/v0_1/__init__.py, benchmark-report/llmd_benchmark_report/artifacts/benchmark_report/v0_1/schema.py, benchmark-report/llmd_benchmark_report/artifacts/benchmark_report/v0_2/__init__.py, benchmark-report/llmd_benchmark_report/artifacts/benchmark_report/v0_2/components.py, benchmark-report/llmd_benchmark_report/artifacts/benchmark_report/v0_2/schema.py, benchmark-report/llmd_benchmark_report/artifacts/registry.py
- #2141 Wait for the pool to drain before the serving-capacity ladder (+257/-5) by @asm582 files: Makefile, docs/serving-capacity.md, llmdbenchmark/run/pool_drain.py, tests/test_pool_drain.py


## llm-d/llm-d-inference-sim (watch)

### Releases
- [v1.2.0](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.2.0) — 2026-11-10: v1.2.0- [v1.2.0-rc.2](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.2.0-rc.2) — 2026-11-10: v1.2.0-rc.2- [v1.2.0-rc1](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.2.0-rc1) — 2026-11-10: v1.2.0-rc1
### Changes

Summary unavailable (null LLM). Source items:
- #921 fix: draw seeded tool-call arguments in a stable parameter order (+35/-2) by @wguo7 files: pkg/endpoint/tools_arg_generator_test.go, pkg/endpoint/tools_utils.go
- #899 fix: end each streamed tool-call choice with its own finish_reason (+46/-6) by @wguo7 files: pkg/communication/http.go, pkg/communication/send_response_test.go
- #910 Reuse render connections safely across vLLM's keep-alive timeout (+125/-1) by @sunilmehta-si files: pkg/tokenizer/render_client.go, pkg/tokenizer/render_client_test.go
- #911 deps(go): bump go.opentelemetry.io/otel/sdk from 1.45.0 to 1.47.0 [dependencies, release-note-none] (+17/-14) by @dependabot files: go.mod, go.sum
- #905 fix: report one response id for all prompts of a text completion (+26/-4) by @JaynouOliver files: pkg/api/request.go, pkg/communication/response_builder.go, pkg/endpoint/text_completion.go, pkg/tests/http_server_test.go, pkg/tests/text_completions_test.go
- #777 Add --stream-interval to batch streamed tokens per chunk  (+285/-33) by @YashmitVaish files: docs/configuration.md, pkg/common/config.go, pkg/common/parser.go, pkg/communication/http.go, pkg/communication/response_builder.go, pkg/engine/vllm/flags_test.go, pkg/simulator/simulator.go, pkg/tests/chat_completions_test.go, pkg/tests/grpc_test.go, pkg/tests/text_completions_test.go, pkg/tests/tools_test.go
- Batching happens only in the producer (`simulateResponseProcessing`), so every streaming transport (chat, text, ...
- #882 chore(typos): allow thw and fix ressponse typo (+10/-5) by @dbdefault files: _typos.toml, pkg/dataset/dataset.go, pkg/tokenizer/tokenizer_test.go
- Allows only `image_grid_thw` and `video_grid_thw` under `[default.extend-identifiers]` in `_typos.toml`. Plain `thw` is not globally allowed.
- Renames the local `thw` test variable to `gridDims` in `pkg/tokenizer/tokenizer_test.go`.
- Corrects `ressponse` to `response` in a comment in `pkg/dataset/dataset.go`.
- #898 fix(render): return a 400 from the render service to the client as a 400 (+91/-1) by @bhargavchintam files: pkg/endpoint/request.go, pkg/endpoint/request_test.go, pkg/tokenizer/render_client.go

### Highlights
- New release **v1.2.0** — v1.2.0
- New release **v1.2.0-rc.2** — v1.2.0-rc.2
- New release **v1.2.0-rc1** — v1.2.0-rc1

## llm-d/llm-d-prism (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #197 fix(agent): point BR v0.2 hint to llmd-benchmark-report and add subcommand help & init flags (+727/-45) by @jjk-g files: cli/prism.ts, skills/prism-results/SKILL.md, skills/prism-results/scripts/prism.mjs, src/tests/prismCli.test.js, src/utils/bundleAssembler.js, src/utils/piiScrubber.js
- Upstream `llm-d/llm-d-benchmark` extracted the Benchmark Report converter into a lightweight standalone package (`llmd-benchmark-report` on PyPI / `./benchmark-report`, entrypoint `bench...
- #196 feat(agent): add llms.txt & .well-known autodiscovery and fail clearly on unconverted harness files (+247/-12) by @jjk-g files: cli/prism.ts, index.html, server/results/index.ts, server/results/routes/agent.ts, server/server.js, skills/prism-results/SKILL.md, skills/prism-results/scripts/prism.mjs, src/tests/agentToolingBackend.test.jsx, src/tests/prismCli.test.js, src/utils/bundleAssembler.js
- **Agent Autodiscovery (`/llms.txt`, `/.well-known/*`, `<link>` & HTTP `Link` headers, `/api/config`)**:
- Adds `GET /llms.txt` (`getLlmsTxtHandler`) serving a standard `llms.txt` index pointing to `/SKILL.md`, `/api/results/agent`, `/api/results/agent/prism.mjs`, `/api/results/agent/install.sh`, and `/api/results/agent/experiment.yaml`.
- Registers `/.well-known/agent.json`, `/...
- #194 fix(results): preserve dynamically hydrated runs across loadAllData and auto-hydrate own/unlisted submissions (+135/-28) by @jjk-g files: skills/prism-results/scripts/prism.mjs, src/components/ManageBenchmarks/UnifiedDataTable.jsx, src/components/ResultsStore.jsx, src/hooks/useDashboardData.jsx, src/utils/manifestMetadataExtractor.js
- **Mount Race Condition**: `processShareLink` fetches `/api/results/:runId` and calls `injectDynamicEntries` on init...


## llm-d/llm-d-router (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #4057 Mix multimodal content hashes into approximate prefix block hashes [kind/bug, size/XL, area/epp, area/scheduling] (+533/-18) by @RishabhSaini files: pkg/epp/framework/plugins/requesthandling/dataproducer/approximateprefix/plugin_test.go, pkg/epp/framework/plugins/requesthandling/dataproducer/burstprefix/plugin_test.go, pkg/epp/framework/plugins/requesthandling/dataproducer/prefixhash/hashing.go, pkg/epp/framework/plugins/requesthandling/dataproducer/prefixhash/hashing_reference_test.go, pkg/epp/framework/plugins/requesthandling/dataproducer/prefixhash/hashing_test.go, test/integration/epp/endpoint_scores_test.go
**What type of PR is this?**
**What this PR does / why we need it:**
- #3733 refactor: parse TLS version and cipher flags with k8s component-base helpers [area/sidecar, size/L, area/epp, kind/cleanup, area/coordinator, area/docs] (+316/-157) by @chethanuk files: docs/tls.md, internal/tls/tls.go, internal/tls/tls_test.go, pkg/coordinator/server/tls.go, pkg/coordinator/server/tls_test.go, pkg/epp/server/options.go, pkg/epp/server/options_test.go, pkg/sidecar/proxy/options.go, pkg/sidecar/proxy/options_test.go
**What type of PR is this?**
**What this PR does / why we need it**:
- #3964 Claim audio transcriptions endpoints in the OpenAI parser [kind/feature, size/L, area/epp, area/scheduling, re-approve] (+425/-36) by @RishabhSaini files: pkg/epp/framework/common/request/conversation_prefix_test.go, pkg/epp/framework/common/request/types.go, pkg/epp/framework/plugins/requesthandling/dataproducer/tokenizer/estimate.go, pkg/epp/framework/plugins/requesthandling/dataproducer/tokenizer/estimate_test.go, pkg/epp/framework/plugins/requesthandling/dataproducer/tokenizer/mm_estimate.go, pkg/epp/framework/plugins/requesthandling/parsers/openai/openai.go, pkg/epp/framework/plugins/requesthandling/parsers/openai/openai_test.go, pkg/epp/handlers/parsers_test.go
**What type of PR is this?**
**What this PR does / why we need it:**
- #4273 sidecar: exit non-zero on startup failure and drain on SIGTERM [kind/bug, area/sidecar, size/L] (+144/-3) by @satyamg1620 files: cmd/pd-sidecar/main.go, cmd/pd-sidecar/main_test.go, pkg/sidecar/proxy/proxy_helpers.go, pkg/sidecar/proxy/proxy_test.go
**What type of PR is this?**
**What this PR does / why we need it**:


## llm-d/llm-d.github.io (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #496 [Blog]: Multi-Tenant and Multi-Priority Model Serving with llm-d [Blog Post, approved] (+424/-0) by @shimib files: blog/2026-11-16_multi-tenant-multi-priority-model-serving-llm-d.md, blog/authors.yml, blog/tags.yml, static/img/blogs/multitenant-async/architecture.jpg, static/img/blogs/multitenant-async/ttft-chart.svg
- #507 [Blog]: add agent trace formats comparison (+501/-1) by @lenadankin files: blog/2026-10-06_from-agent-traces-to-replay.mdx, blog/authors.yml, static/img/blogs/lenadankin.webp, static/img/blogs/michaljacovi.webp, static/img/blogs/michalshmu.webp, static/img/blogs/trace-formats-comparison/schema-comparison.html
- An interactive comparison of agent trace schemas
- Author profiles and images
- Tables comparing trace datasets and replay mechanisms
- Guidance for selecting trace and replay combinations at different deployment stages


