# llm-d releases — 2026-11-18

_Generated 2026-11-18T15:56:57Z_

**Docs:** [https://llm-d.ai](https://llm-d.ai) · [https://github.com/llm-d/llm-d/tree/main/docs/proposals](https://github.com/llm-d/llm-d/tree/main/docs/proposals)
## TL;DR

- llm-d/llm-d v1.0.0: 15 feature(s)
- llm-d/llm-d next milestone: v1.0.0
- llm-d-incubation/hermes v0.3.1: 0 feature(s)
- llm-d-incubation/hermes next RC/train: v0.3.0-rc.3
- llm-d-incubation/llm-d-fast-model-actuation v0.8.0: 11 feature(s)
- llm-d-incubation/llm-d-fast-model-actuation next RC/train: v0.7.0-alpha.3
- llm-d-incubation/llm-d-lens v0.1.0: 15 feature(s)
- llm-d-incubation/llm-d-modelservice llm-d-modelservice-v0.5.2: 0 feature(s)

## llm-d/llm-d (core)

Release page: [https://github.com/llm-d/llm-d/releases](https://github.com/llm-d/llm-d/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d/releases/tag/v1.0.0) — 2026-10-20
- **Multi-tenant quality of service** — priority- and fairness-aware flow control with controlled load shedding (probabilistic admitter, program-aware fairness, turn-priority scoring), so latency-sensitive requests and bursty agent workloads share a fleet without starving one another under overload. Flow control config is consolidated under `flowControl`.
- **Zero-downtime operations** — router HA with hot standby and safe rolling updates. `DisaggregatedSet` manages prefill/decode replicas as one logical unit (coordinated rollouts, lockstep upgrades, readiness gated on Pod snapshot, native revision routing), making disaggregated serving practical in production.
- **A stable foundation to build on** — the router configuration API graduates to `v1`, the Responses API supports `previous_response_id`, and the EPP request path is hardened for reliability, performance and scalability. A DRA/DRANET topology-aware accelerator guide is included.
- **Agent-aware serving** — session-state-producer plugin and evolving session affinity keep multi-turn conversations close to their cached context; turn-priority scheduling and Responses API state help agents reuse context across turns.
- `ghcr.io/llm-d/llm-d-rocm` container image builds have been DEPRECATED. This was previously only kept around for RoCM PD dissagregation support. Eventually we will be moving to the upstream vLLM images. For this release we have cherry-picked the vllm `v0.32.0-rc.2` official rocm image into our registry to guard against image garbage collection: `ghcr.io/llm-d/vllm-openai-rocm:v0.32.0-rc.2` (see the [image component](https://github.com/llm-d/llm-d/blob/release-1.0/guides/recipes/modelserver/components/images/amd-vllm/beta/kustomization.yaml#L6))
- `ai-dynamo/modelexpress`: we have been very excited by the amazing work the dynamo team has been doing around p2p loading of model weights, and thus have chosen to integrate with `modelexpress. We are excited to see where this collaboration will take us!
- `llm-d/llm-d-api-extensions`: llm-d API Extensions exposes inference-server configuration, hardware, and KV-cache metadata through native extension points to support llm-d routing and scheduling.
- `llm-d/llm-d-pd-utils`: llm-d PD Utils provides preflight diagnostics, GPU topology discovery, and network benchmarks to validate and troubleshoot distributed inference deployments.
- Proposal: llm-d-perf-simulator by @jgchn in https://github.com/llm-d/llm-d/pull/2015
- Shorten the GLM-5.2 DisaggregatedSet name by @BenjaminBraunDev in https://github.com/llm-d/llm-d/pull/2610
- Move the GKE SGLang P/D nightly to llm-d-e2e-us-east5-2 by @kaushikmitr in https://github.com/llm-d/llm-d/pull/2631
- feat(workload-autoscaling): add AMD ROCm deploy script for the KEDA+EPP nightly by @PrateekKumar1709 in https://github.com/llm-d/llm-d/pull/2583
- guides/wide-ep: add AMD/ROCm MoRI wide-EP 2P2D DisaggregatedSet recipe for DeepSeek-V3 by @shikamd123 in https://github.com/llm-d/llm-d/pull/2493
- [ROCm] Pack CI nightly schedule by @vcave in https://github.com/llm-d/llm-d/pull/2673
- feat(keda-epp): add pending-aware overshoot guard for the queue signal by @mamy-CS in https://github.com/llm-d/llm-d/pull/2675

#### [v0.10.0](https://github.com/llm-d/llm-d/releases/tag/v0.10.0) — 2026-09-29
- Operational hardening — make the production path safe and boring: rollouts, HA, and failure behavior that operators can trust.
- Production readiness — graduate the flagship paths from "works" to "default."
- `llm-d/llm-d-kv-cache` repo has been migrated to `llm-d/llm-d-router` repo and deprecation of the old repo is in progress (although is not finished at the time of the `llm-d` `v0.10.0` release).
- `llm-d/llm-d-workload-variant-autoscaler` repo has been renamed to `llm-d/llm-d-autoscaling` to reflect the projects more hollistic approach to autoscaling beyond simply the WVA component. The WVA guides are marked as deprecated and will be removed in a future release.
- `ghcr.io/llm-d/llm-d-cuda` container image builds have been DEPRECATED in favor of `docker.io/vllm/vllm-openai`.
- `ghcr.io/llm-d/llm-d-aws` container image builds have been DEPRECATED in favor of `public.ecr.aws/deep-learning-containers/vllm`.
- `llm-d/llm-d-kv-cache/llmd-fs-connector` has been integrated upstream into vLLM under the `OffloadingConnector` and is thus DEPRECATED. This has the major benefit of existing in tree and out of the box with the container image - no independent installation required.
- revert artifact upload version bump by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2282
- Fixing WVA Namespace Overrides: Point the Controller's Watch Target at the Install Namespace - #2253 by @lionelvillard in https://github.com/llm-d/llm-d/pull/2283
- [Guides] Update dsv-4 guides by @ilmarkov in https://github.com/llm-d/llm-d/pull/2057
- reorganize the rollouts docs as a guide by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2266
- Add Grafana dashboard setup documentation for flow control by @alexagriffith in https://github.com/llm-d/llm-d/pull/1629
- Updating llm-d router metrics across guides by @ahg-g in https://github.com/llm-d/llm-d/pull/2288
- guides(wide-ep-lws): precise prefix-cache routing variant by @nilig in https://github.com/llm-d/llm-d/pull/2203
- Coordinator's guide by @roytman in https://github.com/llm-d/llm-d/pull/2119

#### [v0.9.0](https://github.com/llm-d/llm-d/releases/tag/v0.9.0) — 2026-08-17
- Add benchmark results for SGLang with tiered prefix cache by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1921
- pin inference-perf version by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1946
- Add Intel XPU vLLM support for multimodal optimized-baseline by @joshuayao in https://github.com/llm-d/llm-d/pull/1772
- Create skeleton for sig-llm-d-inference-payload-processor by @petecheslock in https://github.com/llm-d/llm-d/pull/1499
- Add cleanup parameter to slash command by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1961
- update-badge parameter by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1951
- Update links in kv-offloader documentation to point to the GitHub repo for deployment manifests by @petecheslock in https://github.com/llm-d/llm-d/pull/1962
- Add Snowflake as a user of llm-d by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1978
- [Docs] Update PD flow to include KV lease extension by @NickLucche in https://github.com/llm-d/llm-d/pull/1543
- Add sig-batch-inference to SIGS.md by @jtechapps in https://github.com/llm-d/llm-d/pull/1922
- proposal: Observability integration across the llm-d stack by @gyliu513 in https://github.com/llm-d/llm-d/pull/1685
- Add Novita as a user of llm-d by @UranusSeven in https://github.com/llm-d/llm-d/pull/1986
- [ROCm] Docker AMD ROCm image update by @vcave in https://github.com/llm-d/llm-d/pull/1977
- Support tiered prefix cache on Intel XPU with LMCache connector by @XinyuYe-Intel in https://github.com/llm-d/llm-d/pull/1731
- Update version badge to v0.8 by @chcost in https://github.com/llm-d/llm-d/pull/1989

#### [v0.8.1](https://github.com/llm-d/llm-d/releases/tag/v0.8.1) — 2026-06-26
- Point to patch v0.8.1 by @maugustosilva in commit d6ffb5c7cff80e3953c62f464c08984ccd6a6096
- Updated the branch to clone in the guides to release-0.8 branch by @ahg-g in https://github.com/llm-d/llm-d/pull/1958
- Pin inference-perf version by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1946

#### [v0.8.0](https://github.com/llm-d/llm-d/releases/tag/v0.8.0) — 2026-06-24
- Simplify WVA guide test by @lionelvillard in https://github.com/llm-d/llm-d/pull/1072
- Revise maturity status and TPU VM type details by @seanhorgan in https://github.com/llm-d/llm-d/pull/1085
- Updated maturity testing level on all guides by @maugustosilva in https://github.com/llm-d/llm-d/pull/1094
- Skip latest tag for release candidates by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1034
- [guides] Add a commented `priorityClassName` for use in nightly CI/CD by @maugustosilva in https://github.com/llm-d/llm-d/pull/1062
- Add shared drive for sig-rl by @petecheslock in https://github.com/llm-d/llm-d/pull/1109
- Add Moreh as a contributor to the adopters list by @hhk7734 in https://github.com/llm-d/llm-d/pull/1111
- Update guides with status badges. by @maugustosilva in https://github.com/llm-d/llm-d/pull/1110
- Add deployment health-check smoke test for llm-d clusters by @lisperz in https://github.com/llm-d/llm-d/pull/767
- [1/N] Documentation Revamp by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1100
- add OCI well-lit-path for P/D disaggregation by @hexfusion in https://github.com/llm-d/llm-d/pull/1123
- Update latency-predictor.md diagram by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1127
- [Docs][4/N] Update architecture/core/epp/scheduling.md docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1122
- [2/N] Proxy Doc by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1121
- [Docs][6/N]: add Istio gateway setup guide by @madhugoutham in https://github.com/llm-d/llm-d/pull/1146

#### [v0.7.0](https://github.com/llm-d/llm-d/releases/tag/v0.7.0) — 2026-05-12
- **⚠️ BREAKING CHANGE — CUDA 13.0.2 runtime:** All llm-d CUDA images now ship with CUDA 13.0.2 (upgraded from 12.x). This requires **NVIDIA driver 580 or later** on the host. Nodes running older drivers must be upgraded before deploying v0.7.0 images.
- UX Change - due to the difficulty configuring gateways for many adopters, we have made the default deployment of llm-d to use "standalone mode" where we use a generic proxy instead of the more feature full gateway. We still recomend a fully gateway for customers in production.
- Simplify WVA guide test by @lionelvillard in https://github.com/llm-d/llm-d/pull/1072
- Revise maturity status and TPU VM type details by @seanhorgan in https://github.com/llm-d/llm-d/pull/1085
- Updated maturity testing level on all guides by @maugustosilva in https://github.com/llm-d/llm-d/pull/1094
- Skip latest tag for release candidates by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1034
- [guides] Add a commented `priorityClassName` for use in nightly CI/CD by @maugustosilva in https://github.com/llm-d/llm-d/pull/1062
- Add shared drive for sig-rl by @petecheslock in https://github.com/llm-d/llm-d/pull/1109
- Add Moreh as a contributor to the adopters list by @hhk7734 in https://github.com/llm-d/llm-d/pull/1111
- Update guides with status badges. by @maugustosilva in https://github.com/llm-d/llm-d/pull/1110
- Add deployment health-check smoke test for llm-d clusters by @lisperz in https://github.com/llm-d/llm-d/pull/767
- [1/N] Documentation Revamp by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1100
- add OCI well-lit-path for P/D disaggregation by @hexfusion in https://github.com/llm-d/llm-d/pull/1123
- Update latency-predictor.md diagram by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1127
- [Docs][4/N] Update architecture/core/epp/scheduling.md docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1122


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [v1.0.0](https://github.com/llm-d/llm-d/milestone/14) _(milestone · due 2026-10-14 · 17/17 issues closed · 0 open PRs)_- [v1.1.0](https://github.com/llm-d/llm-d/milestone/17) _(milestone · due 2026-11-23 · 1/9 issues closed · 1 open PRs)_- [#3047 [Proposal] CPU Cache Sharing](https://github.com/llm-d/llm-d/issues/3047) _(rfc · open RFC/proposal)_ — # llm-d CPU Sharing: one CPU KV-cache pool per node
## Summary

Add `llm-d-cpu-sharing`: one CPU KV-cache pool per node, shared by every vLLM engine on it, so a prefix one engine offloaded is a hit...- [#2971 [Proposal] Native Compaction Support](https://github.com/llm-d/llm-d/issues/2971) _(rfc · open RFC/proposal)_ — **Reference Document:** [[[PUBLIC] llm-d Compaction Northstar]](https://docs.google.com/document/d/12w0d90ODvmkMtf4Z7LrViYCWTlUso4VWezhDRpJ5OS4/edit?usp=sharing))

### Summary
This project will pro...- [#2699 [RFC]: Dynamic runtime PD router infrastructure and strategy for llm-d](https://github.com/llm-d/llm-d/issues/2699) _(rfc · open RFC/proposal)_ — ### Feature Area

Routing strategy (e.g., llm-d-router, llm-d-autoscaling), telemetry components (e.g., Kubernetes, framework metrics), projection tools (inference-sim, AIConfigurator, heuristic lo...- [#2569 [Proposal] Upstream llm-d Unified Model Server Telemetry to OpenTelemetry GenAI Semantic Conventions (gen_ai.server.*)](https://github.com/llm-d/llm-d/issues/2569) _(rfc · open RFC/proposal)_ — ### Feature Area

Observability / Monitoring

### Problem Statement

# [Proposal] Upstream `llm-d` Unified Model Server Telemetry to OpenTelemetry GenAI Semantic Conventions (`gen_ai.server.*`)

##...
## llm-d-incubation/hermes (watch)

Release page: [https://github.com/llm-d-incubation/hermes/releases](https://github.com/llm-d-incubation/hermes/releases)

### Shipped (what went in)

#### [v0.3.1](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.1) — 2025-12-11
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.1)._

#### [v0.3.0](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.0) — 2025-12-11
- Sriov fixes by @wseaton in https://github.com/llm-d-incubation/hermes/pull/2
- Deepep fixes by @wseaton in https://github.com/llm-d-incubation/hermes/pull/3
- helmify by @wseaton in https://github.com/llm-d-incubation/hermes/pull/4

#### [v0.2.5](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.5) — 2025-10-15
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.5)._

#### [v0.2.4](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.4) — 2025-10-15
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.4)._

#### [v0.2.3](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.3) — 2025-10-15
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.3)._

#### [v0.2.2](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.2) — 2025-10-15
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.2)._


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.3.0-rc.3](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.0-rc.3) (2025-12-09)- [v0.3.0-rc.2](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.0-rc.2) (2025-12-08)- [v0.3.0-rc1](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.0-rc1) (2025-12-08)  - Sriov fixes by @wseaton in https://github.com/llm-d-incubation/hermes/pull/2
  - Deepep fixes by @wseaton in https://github.com/llm-d-incubation/hermes/pull/3


## llm-d-incubation/llm-d-fast-model-actuation (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases)

### Shipped (what went in)

#### [v0.8.0](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.8.0) — 2026-11-03
- Set `spec.inferencePorts` on each LauncherConfig, with at least `maxInstances`
- `InferenceServerConfig.spec.modelServerConfig.port` is deprecated. It is used
- Update set of releases tested for install-fma.sh to {0.7.1} by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/807
- Update builders to Go 1.27.3 due to Mudhra CA hack by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/808
- Update python version in code-quality by @diegocastanibm in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/817
- Stop blocking the launcher's event loop while stopping an instance by @diegocastanibm in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/751
- feat(grafana): add stacked launcher counts by LauncherConfig by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/811
- Use `LauncherConfigSpec.InferencePorts` by @waltforme in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/809
- Correct the Python version to what's in the runner by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/818
- feat(metrics): record launcher-populator Pod creation latency by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/815
- Remove obsolete demo scripts by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/826

#### [v0.7.1](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.1) — 2026-10-19
- Make `InferenceServerConfigSpec.ModelServerConfig.Port` optional by @waltforme in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/798

#### [v0.7.0](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.0) — 2026-10-16
- the introduction of a usable TCP proxy in the requester image. Clients, and requester Pods, are not required to use it. Port assignment responsibility has not changed yet;
- introducing an optional field to `LauncherConfig` to hold the pool of inference port numbers to use.
- Add clunky logging of tail of stopped vLLM instance log by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/744
- Use the requester's TCP proxy by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/721
- Add debugging for flakes by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/747
- Fixed minor nits found in review of PR 747 by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/752
- Improve launcher configuration by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/753
- Add script to find unwanted versions of images by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/754
- Quote newline-sensitive herestrings by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/757
- Add command line to logged process attributes by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/755
- Make launcher try to stop all procs in instance process group by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/756
- Add debugging for E2E test of direct providers by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/759
- Correct testing of releases wrt --debug-gpu-memory by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/761
- Tweak dependency bump review instructions by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/768
- Follow up #721 proxy test and documentation by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/766

#### [v0.6.5](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.6.5) — 2026-08-31
- Make E2E run on pok-prod instead of vllm-d by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/645
- dual-pods: return ordered entries from takeReadyItems by @Iceber in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/708
- Add 0.6.5 and its alpha.1 to release menu in bug template by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/713
- Introduce general-purpose installer script by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/703
- Address unresolved review threads from #635 and #673 by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/714
- Add overlooked launcher to list of images by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/717
- Don't upload coverage from failed tests by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/716
- Add document about FMA uninstall by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/715
- Add the requester's TCP proxy, without using it yet by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/719
- Make production of coverage data optional by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/718
- Remove config/examples by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/729
- Add options to test a release by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/724
- Retire global.local by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/727
- Quieten test by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/730
- Make go unit test workflow attach coverage by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/732

#### [v0.6.4](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.6.4) — 2026-08-11
- Switch order of dual-pods and launcher in docs/README.md by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/694
- Write general installation document by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/695
- launcher-populator: requeue LPPs on LC existence transitions by @Iceber in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/697
- Bring docs/upstream-versions.md up to date by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/693
- Note hands-off case in LPP meaning by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/698
- dual-pods: make nodeData.Add pull forward delayed queue items by @Iceber in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/696
- launcher-populator: report malformed LauncherConfig in LPP status by @Iceber in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/701
- Add 0.6.4 and 0.6.4-alpha.1 to releases in bug form by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/704
- Update vllm to version 0.26.0 to match llm-d by @aavarghese in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/710

#### [v0.6.3](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.6.3) — 2026-07-31
- Add 0.6.3 to release menu in bug template by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/656
- Independent item scheduling in DPC, 5-second polling of /is_sleeping by @omerap12 in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/626
- Establish design rules with automation and subjective tiers by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/634
- Add Prometheus metrics fma_launcher_pod_count to launcher-populator by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/635
- Publish an Event when unbinding on invalid routing metadata by @waltforme in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/661
- Update README.md by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/669
- Add reference to well-lit path PR of llm-d by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/671
- Start updating docs/dual-pods.md for milestone 3 by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/672
- Second round of updates to dual-pods doc by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/675
- Update Prometheus metrics documentation by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/684
- launcher-populator: report and retry stuck launchers by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/673
- Draft resource planning section of dual-pods doc by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/681
- Make DPC produce coverage data by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/687
- Add populator scrape dumping to E2E tests by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/685
- Document FMA's Event objects by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/690


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.7.0-alpha.3](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.0-alpha.3) (2026-10-07)  - Add clunky logging of tail of stopped vLLM instance log by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/744
  - Use the requester's TCP proxy by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/721
  - Add debugging for flakes by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/747
  - Fixed minor nits found in review of PR 747 by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/752
  - Improve launcher configuration by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/753
  - Add script to find unwanted versions of images by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/754
- [v0.7.0-alpha.2](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.0-alpha.2) (2026-10-07)  - Add clunky logging of tail of stopped vLLM instance log by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/744
  - Use the requester's TCP proxy by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/721
  - Add debugging for flakes by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/747
  - Fixed minor nits found in review of PR 747 by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/752
  - Improve launcher configuration by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/753
  - Add script to find unwanted versions of images by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/754
- [v0.7.0-alpha.1](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.0-alpha.1) (2026-10-01)  - Add clunky logging of tail of stopped vLLM instance log by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/744
  - Use the requester's TCP proxy by @delavet in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/721
  - Add debugging for flakes by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/747
  - Fixed minor nits found in review of PR 747 by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/752
  - Improve launcher configuration by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/753
  - Add script to find unwanted versions of images by @MikeSpreitzer in https://github.com/llm-d-incubation/llm-d-fast-model-actuation/pull/754

**Milestones, roadmaps & open RFCs feeding the next drop**
- [2 - System with sleep/wake only](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/milestone/2) _(milestone · due TBD · 7/7 issues closed · 0 open PRs)_ — Both sleep/wake and model swapping techniques can be enabled.- [3 (release 0.6.0) - System with model swapping and sleep/wake](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/milestone/3) _(milestone · due TBD · 59/59 issues closed · 0 open PRs)_- [release 0.7](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/milestone/7) _(milestone · due TBD · 3/6 issues closed · 0 open PRs)_- [release 0.8](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/milestone/8) _(milestone · due TBD · 1/1 issues closed · 0 open PRs)_ — Start providing and using optional port pool field of LauncherConfig.- [release 0.9](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/milestone/9) _(milestone · due TBD · 0/2 issues closed · 1 open PRs)_ — Make the new port pool field of LauncherConfig required.
## llm-d-incubation/llm-d-lens (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-lens/releases](https://github.com/llm-d-incubation/llm-d-lens/releases)

### Shipped (what went in)

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-lens/releases/tag/v0.1.0) — 2026-10-23
- **End-to-end inference workflow:** Prepare resources, deploy models, publish services, and validate performance in one console.
- **Unified accelerator management:** Manage deployment, resource allocation, and monitoring consistently across supported hardware platforms.
- **Performance evaluation:** Run controlled experiments across configurations and workloads to analyze performance trade-offs and SLO compliance.
- **Real-world traffic replay:** Replay captured real-world request traces to validate service behavior under realistic workloads.
- Register, bootstrap, and maintain clusters; manage storage and reusable model caches.
- Allocate accelerator resources for deployments using DRA or device plugins.
- Control resource access through role-based access control (RBAC), with user and group role assignments and cluster-scoped permissions.
- Configure Manual deployments or review and approve Agentic plans, with tensor parallelism, replicas, runtime settings, and placement policies.
- Integrate optimized baseline, precise prefix-cache routing, tiered prefix caching, and prefill/decode disaggregation Guides.
- Inspect YAML, Pods, logs, and endpoints; validate cache dependencies and manage deployment retries, stops, and cleanup.
- Publish OpenAI Chat Completions, Embeddings, and Anthropic Messages endpoints with access tokens, selection policies, and health-aware routing.
- Generate and score deployment candidates based on capacity, SLO targets, workload estimates, and user preferences, with human review and approval before deployment.
- An external AI provider is optional but recommended for AI-assisted scoring and explanations. Heuristic recommendations are available without an external AI provider.
- Run parameter sweeps and controlled comparisons across configurations, sequence lengths, concurrency, and request rates.
- Replay real-world request traces with configurable windows, time scaling, streaming, and rerun controls.


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [#15 [Roadmap] v0.1.0 - v0.2.0 (Oct - Dec '26)](https://github.com/llm-d-incubation/llm-d-lens/issues/15) _(roadmap · roadmap)_ — Hi everyone! 

As llm-d-lens takes its first steps, we’ve put together an initial plan for the next three months (Oct – Dec '26, v0.1.0 to v0.2.0).

This is our very first roadmap, but it is by no ...- [#132 [RFC] Enable DS and Slice](https://github.com/llm-d-incubation/llm-d-lens/issues/132) _(rfc · open RFC/proposal)_ — ## Summary

This RFC records the scope split for enabling DisaggregatedSet (DS) and Slice in Lens. **Step 2 will add items 3 and 4 below: UI-based node-label management for Slice placement, and sha...- [#125 [RFC] REST APIs for Lens engine](https://github.com/llm-d-incubation/llm-d-lens/issues/125) _(rfc · open RFC/proposal)_ — ## 0. Purpose
Add a REST API layer for the new Lens engine. 

## 1. API definition

### 1.1 Resource map

```mermaid
flowchart LR
    root["/api/v2"] --> sources["/sources<br/>GET"]
    sources -->...- [#104 [RFC]: Multi-Source Configuration-Driven Agentic Deploy - Stage 2](https://github.com/llm-d-incubation/llm-d-lens/issues/104) _(rfc · open RFC/proposal)_ — # RFC: Multi-Source Configuration-Driven Agentic Deploy

## Stage 2: AIC/BLIS Sweep When No Exact Historical Match Is Available

### 1. Purpose and Scope

When a user's requested model, hardware, r...- [#91 [RFC]: Multi-Source Configuration-Driven Agentic Deploy - Stage 1](https://github.com/llm-d-incubation/llm-d-lens/issues/91) _(rfc · open RFC/proposal)_ — # RFC: Multi-Source Configuration-Driven Agentic Deploy

## Stage 1: Exact Historical Data Matches

### 1. Problem Statement

Agentic Deploy needs to find relevant configurations based on the user'...- [#96 [RFC]: OS platform abstraction](https://github.com/llm-d-incubation/llm-d-lens/issues/96) _(rfc · open RFC/proposal)_ — ### Problem Statement

Lens runs only on Ubuntu 22.04+ x86_64 today. Planned targets are Fedora, CentOS Stream, macOS and Windows, with more later. 

This design adds one host OS layer that owns al...- [#90 [RFC] Document RAG Architecture for llm-d-lens](https://github.com/llm-d-incubation/llm-d-lens/issues/90) _(rfc · open RFC/proposal)_ — ## 1. Purpose and Scope

Design a document RAG engine for English and Chinese queries over approved Git documentation and technical blogs. It should combine exact-term and semantic retrieval, retur...
## llm-d-incubation/llm-d-modelservice (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-modelservice/releases](https://github.com/llm-d-incubation/llm-d-modelservice/releases)

### Shipped (what went in)

#### [llm-d-modelservice-v0.5.2](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.5.2) — 2026-10-30
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.5.2)._

#### [llm-d-modelservice-v0.5.1](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.5.1) — 2026-10-20
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.5.1)._

#### [llm-d-modelservice-v0.5.0](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.5.0) — 2026-09-14
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.5.0)._

#### [llm-d-modelservice-v0.4.16](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.4.16) — 2026-08-21
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.4.16)._

#### [llm-d-modelservice-v0.4.15](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.4.15) — 2026-06-22
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.4.15)._

#### [llm-d-modelservice-v0.4.14](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.4.14) — 2026-06-11
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.4.14)._


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d-incubation/llm-d-planner (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-planner/releases](https://github.com/llm-d-incubation/llm-d-planner/releases)

### Shipped (what went in)

#### [v0.3.3](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.3.3) — 2026-08-29
- feat: expand quality_scoring exports and preserve full API response fields by @anfredette in https://github.com/llm-d-incubation/llm-d-planner/pull/352

#### [v0.3.2](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.3.2) — 2026-08-28
- feat: migrate AA client to free V2 API by @anfredette in https://github.com/llm-d-incubation/llm-d-planner/pull/351

#### [v0.3.1](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.3.1) — 2026-08-24
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.3.1)._

#### [v0.3.0](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.3.0) — 2026-08-24
- feat: Composable programmatic API pipeline by @anfredette in https://github.com/llm-d-incubation/llm-d-planner/pull/328
- feat: Package as Python wheel with Planner library API by @anfredette in https://github.com/llm-d-incubation/llm-d-planner/pull/332
- feat: add PyPI publishing via trusted publisher and dynamic versioning by @anfredette in https://github.com/llm-d-incubation/llm-d-planner/pull/344

#### [v0.2.0](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.2.0) — 2026-08-18
- Update calibrated constants validated on real hardware by @jgchn in https://github.com/llm-d-incubation/llm-d-planner/pull/254
- Add minimal support for llm-d manifest generation by @jgchn in https://github.com/llm-d-incubation/llm-d-planner/pull/274
- Replace quality scoring with dual-source engine (Arena + AA) by @anfredette in https://github.com/llm-d-incubation/llm-d-planner/pull/282
- feat: expose benchmark_source in /api/v1/db/status by @tarilabs in https://github.com/llm-d-incubation/llm-d-planner/pull/275
- feat: Replace PostgreSQL with embedded SQLite database by @anfredette in https://github.com/llm-d-incubation/llm-d-planner/pull/318

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.1.0) — 2026-05-28
- _No feature bullets extracted — see [full notes](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.1.0)._


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d-incubation/llm-d-resiliency-operator (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-resiliency-operator/releases](https://github.com/llm-d-incubation/llm-d-resiliency-operator/releases)

### Shipped (what went in)

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-resiliency-operator/releases/tag/v0.1.0) — 2026-10-18
- **Engine fault recovery controller** - detects a failed rank, shrinks the group around it, resets the Pod, and records every step in a journal (#11, #34)
- **vLLM engine** - drives vLLM fault tolerance with `retry` and `scale_down`. On OpenShift it recovered in about 30s (#19)
- **`--ft-poll-interval`** - sets how often the controller polls (#41)


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [Recovery foundation](https://github.com/llm-d-incubation/llm-d-resiliency-operator/milestone/1) _(milestone · due TBD · 0/18 issues closed · 0 open PRs)_ — The engine action contract, component tests, Kubernetes tests, and repeatable vLLM GPU fault baseline pass.- [Backend v1 qualification](https://github.com/llm-d-incubation/llm-d-resiliency-operator/milestone/2) _(milestone · due TBD · 0/1 issues closed · 0 open PRs)_ — NIXL-EP v1 and DeepEP v1 have reproducible GLM 5.3 and DSv4.1F reports with acceptance decisions.- [Capacity restoration](https://github.com/llm-d-incubation/llm-d-resiliency-operator/milestone/3) _(milestone · due TBD · 0/9 issues closed · 0 open PRs)_ — Declared configurations pass repeated fault, replacement, admission, and stable full-capacity tests.- [Additional engine qualification](https://github.com/llm-d-incubation/llm-d-resiliency-operator/milestone/4) _(milestone · due TBD · 0/5 issues closed · 0 open PRs)_ — SGLang and TRT-LLM have support decisions and test evidence for each supported configuration.- [Next-generation backend qualification](https://github.com/llm-d-incubation/llm-d-resiliency-operator/milestone/5) _(milestone · due TBD · 0/1 issues closed · 0 open PRs)_ — The exact NIXL-EP v2 and DeepEP v2.5 integrations have reproducible comparison results and acceptance decisions.- [#87 IRO roadmap: production qualification and recovery](https://github.com/llm-d-incubation/llm-d-resiliency-operator/issues/87) _(roadmap · roadmap)_ — Track the work needed to qualify EP backends for production and extend IRO recovery.

The main model candidates are **GLM 5.3** and **DeepSeek V4.1 Flash (DSv4.1F)**. Smaller models support fast re...
## llm-d-incubation/llm-d-rl-time-slicing (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-rl-time-slicing/releases](https://github.com/llm-d-incubation/llm-d-rl-time-slicing/releases)

### Shipped (what went in)

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-rl-time-slicing/releases/tag/v0.1.0) — 2026-08-27
- Snapshot Agent: pluggable snapshot backends (cuda-checkpoint, vLLM sleep/wake, SGLang release/resume, direct-memory) to move workload state between VRAM and host
- TimeSlice Orchestrator: cooperative GPU time-slicing via group locks, including the cold-start acquire fix for pre-provisioned jobs (#152)
- llm-d-timeslice-slime: PhaseCallback package for Slime RL workloads with sync and async examples
- E2E validated on H100: sync (both pools checkpoint/restore) and async (trainer-only time-slicing) with two concurrent GRPO jobs


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d-incubation/llm-d-scaling-manager (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-scaling-manager/releases](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases)

### Shipped (what went in)

#### [v0.11.2](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.2) — 2026-11-17
- **A router you already run needs nothing.** The scaling manager reads the router's queue under both the old and the new metric names. To move the router to v1.0.0, follow the migration order in the router configuration reference: EPP configs use apiVersion `llm-d.ai/v1`, which v0.11.0 and older routers cannot read, so move the router and its config together.
- **Two commands from the tools image** (#137): `smt admin-setup` (cluster admin), `smt install` (namespace owner; runs the preflight and stops on a FAIL), then `smt admin-finish`. The release files are built into the tools image and signed once. Installing by hand from the release files still works.
- **Plain HTTP Prometheus** (#141): `smt install --allow-http` installs against a Prometheus that serves plain HTTP. The controller starts, and a re-run changes nothing. Without the flag, the install refuses an http URL with a clear message. The preflight now FAILs an http Prometheus URL while a bearer token or TLS setting is configured, instead of passing a configuration the controller refuses.
- **llm-d-router v1.0.0** (#143), was v0.9.0 for installs and e2e and v0.11.0 for benchmarks. The P/D routing sidecar is v1.0.0 with modelservice chart v0.4.16.
- **A slow plan no longer runs for an hour** (#128): a plan at some fleet sizes now prices in seconds with the same answer. A plan past `--plan-budget` (default 5m) is refused with 503.

#### [v0.11.1](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.1) — 2026-11-15
- **P/D prefill gets a floor below its knee** from the requests each prefill replica completes and how long each occupies it. Before, prefill could be sized on its resident KV alone and under-provisioned. Expect more prefill replicas at the same load. Rolling back to an earlier release is safe: it ignores the new learned-state field, and those windows age out. (#107)
- **A P/D prefill with no measured throughput counts the prompts waiting in the router** as demand, at most doubling the ready prefill fleet at a time. Before, a backlog held in the router under flow control never scaled prefill. (#100)
- **On vLLM v0.32.0 and later, a P/D decode's queue counts requests whose KV has landed** and that wait to be scheduled (`vllm:num_requests_kv_fetch_by_stage{stage="completed_waiting"}`), so a decode capped by `max_num_seqs` can scale up on that queue. Older vLLM is unchanged. (#95)
- **TTFT rates under EPP flow control are capped below the prefill flow-control onset**, in the what-if CLI, the planner API and the SLO analyzer. Past the onset the router holds requests. Answers may be lower than before, which errs toward more replicas. The CLI and the analyzer now share one TTFT verdict. (#104)
- **Tools image and tarball**, per release, for preparing, registering and sharing workloads without a clone. (#109)
- **Opt-in KEDA HPA repair** for KEDA 2.19 and older (`KEDA_HPA_REPAIR=true`, off by default): the controller finds HPAs KEDA left on the CPU default after a controller restart and has KEDA derive them again. Only with it on does the controller get access to HorizontalPodAutoscalers. Metrics `llmsm_keda_unwired_hpas`, `llmsm_keda_hpa_rewires_total`, `llmsm_keda_hpa_wiring_unread`; alerts `LLMSMKEDAHPAUnwired`, `LLMSMKEDAHPAWiringUnread`. The release files do not carry the grant; `keda.md` gives the commands. (#103)
- **`whatif serve`**: the capacity planner's API, locally (phase 0, no page). `POST /v1/inputs` resolves a recording or a Prometheus window; `POST /v1/plan` prices scenarios. Loopback by default; any other address needs `--auth=kubernetes` and TLS. (#93)
- **Recording for the capacity planner**: the metric list (`docs/reference/capacity-planner-metrics.md`) and a guide to record a Prometheus window with whatif or with only curl and jq. (#92, #108)
- **Joint prefill and decode TTFT inputs, in shadow**: `llmsm_slo_ttft_joint_input`, `llmsm_slo_ttft_joint_mean_seconds`, `llmsm_slo_ttft_joint_reason`, and `whatif joint-ttft`. Nothing scales from them yet. (#90)
- **Experimental, off by default**: `--price-router-wait` (CLI) and `slo-ttft-router-wait` (analyzer) price the router's flow-control wait, flagged `FlowControlWaitPriced`. Not validated on a cluster yet. (#104)

#### [v0.11.0](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.0) — 2026-11-12
- Tested end to end: the namespaced files on Kubernetes.
- **NOT YET TESTED end to end:** the cluster-wide files
- **Scale-to-zero is now OFF on a first install with `make deploy-scaling-manager`**,
- **New settings ConfigMap `scaling-manager-settings`.** A key it sets wins
- **`LOG_LEVEL` now takes effect.** If you set it on the controller Deployment
- **Tuned floor trust:** `analyzerTuning.floorTrust.lagFraction` and
- **`whatif --output json` is now schemaVersion 3** (`parts.kvPullWait` is
- The release attaches rendered, signed install manifests, a settings
- Passive, utilization share (`off`, `shadow`, `active`) and the limiter keys
- A Prometheus with a private CA: create Secret `scaling-manager-prometheus-ca`
- New preflight Job (`scaling-manager-preflight.yaml`) checks KEDA, the scaler
- On a release-file install the controller creates the external scaler's
- A re-install keeps the `default` policy entry's keys it does not render,
- A re-install into a namespace you uninstalled from no longer leaves KEDA
- When KEDA cannot reach the scaler, the controller reports `scalerUnreachable`


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.11.1-rc2](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.1-rc2) (2026-11-14)  - **P/D prefill gets a floor below its knee** from the requests each prefill replica completes and how long each occupies it. Before, prefill could be sized on its resident KV alone and under-provisioned. Expect more prefill replicas at the same load. Rolling back to an earlier release is safe: it ignores the new learned-state field, and those windows age out. (#107)
  - **A P/D prefill with no measured throughput counts the prompts waiting in the router** as demand, at most doubling the ready prefill fleet at a time. Before, a backlog held in the router under flow control never scaled prefill. (#100)
  - **On vLLM v0.32.0 and later, a P/D decode's queue counts requests whose KV has landed** and that wait to be scheduled (`vllm:num_requests_kv_fetch_by_stage{stage="completed_waiting"}`), so a decode capped by `max_num_seqs` can scale up on that queue. Older vLLM is unchanged. (#95)
  - **TTFT rates under EPP flow control are capped below the prefill flow-control onset**, in the what-if CLI, the planner API and the SLO analyzer. Past the onset the router holds requests. Answers may be lower than before, which errs toward more replicas. The CLI and the analyzer now share one TTFT verdict. (#104)
  - **Tools image and tarball**, per release, for preparing, registering and sharing workloads without a clone. (#109)
  - **Opt-in KEDA HPA repair** for KEDA 2.19 and older (`KEDA_HPA_REPAIR=true`, off by default): the controller finds HPAs KEDA left on the CPU default after a controller restart and has KEDA derive them again. Only with it on does the controller get access to HorizontalPodAutoscalers. Metrics `llmsm_keda_unwired_hpas`, `llmsm_keda_hpa_rewires_total`, `llmsm_keda_hpa_wiring_unread`; alerts `LLMSMKEDAHPAUnwired`, `LLMSMKEDAHPAWiringUnread`. The release files do not carry the grant; `keda.md` gives the commands. (#103)
- [v0.11.0-rc1](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.0-rc1) (2026-11-09)  - **Repository:** `github.com/llm-d-incubation/llm-d-scaling-manager` (was
  - **Image:** `ghcr.io/llm-d-incubation/llm-d-scaling-manager` (was
  - **Everything is renamed.** Kubernetes objects are named `scaling-manager`,
  - **The KEDA trigger is named `llmsm`**, so a `scalingModifiers` formula can
  - **Learned state and tuned policy are not carried over.** The controller keeps
  - Set `LLMSM_PASSIVE=true`, or `passive: true` on a scaling-policy entry, and


## llm-d-incubation/llm-d-validate (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-validate/releases](https://github.com/llm-d-incubation/llm-d-validate/releases)

### Shipped (what went in)

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-validate/releases/tag/v0.1.0) — 2026-11-14
- **API coverage:** OpenAI Chat Completions, Completions and Responses, and Anthropic Messages; streaming, tool calling, structured output, reasoning, images, long context, prefix caching, error handling, transport, change detection, client scenarios, a pinned Claude Code client, and fleet configuration, metrics and log rules. See [docs/coverage.md](https://github.com/llm-d-incubation/llm-d-validate/blob/main/docs/coverage.md).
- **Every layer, in one run:** engine, llm-d router (EPP) and ingresses, each tested as its own code path, with per-layer results.
- **Declarative profiles:** a YAML description of your stack and how a correct one behaves, validated offline before any request is sent. Three example profiles: gateway only, engine plus router, and a proxy in front of both.
- **Evidence for every verdict:** per-case results with the checks behind them, every request and response in redacted form, a `repro.sh` per failure, a `reproduce.sh` per run, and an optional self-contained HTML dashboard.
- **Known failures:** label failures already traced to an upstream fix. They still fail, but runs and comparisons show them as known rather than new.
- **`deploy/`:** a kustomize CronJob for scheduled runs, the `llmdv-trigger` Role, an example overlay with an in-cluster profile, `trigger.sh` for on-demand runs, an infrastructure smoke test, and a [deploy guide](https://github.com/llm-d-incubation/llm-d-validate/blob/main/deploy/README.md).
- **`Containerfile`:** a pinned runner image on UBI9 Python 3.11, with a hash-checked `requirements.lock` and a pinned Claude Code 2.1.289.
- **Publishing:** S3, S3-compatible storage, and IBM Cloud Object Storage (IAM).
- **Agent material:** eight agent skills under `.agents/skills/`, and the design notes and measured component behaviour under `.agents/`.
- **Contributing:** see [CONTRIBUTING.md](https://github.com/llm-d-incubation/llm-d-validate/blob/main/CONTRIBUTING.md). Every PR starts from an issue, stays small, and carries a DCO sign-off.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-api-extensions (watch)

Release page: [https://github.com/llm-d/llm-d-api-extensions/releases](https://github.com/llm-d/llm-d-api-extensions/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-api-extensions/releases/tag/v1.0.0) — 2026-10-20
- Add vLLM server intropsection endpoints by @hickeyma in https://github.com/llm-d/llm-d-api-extensions/pull/2
- [vLLM] Fix typo in server_introspection e2e test comment by @O1sumitkumar in https://github.com/llm-d/llm-d-api-extensions/pull/6
- [vLLM] [BugFix] Drop unused kv_transfer fields and rename group_id to group_idx by @hickeyma in https://github.com/llm-d/llm-d-api-extensions/pull/4
- [vLLM] Don't crash the server when vLLM internals change by @hickeyma in https://github.com/llm-d/llm-d-api-extensions/pull/7


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-async (watch)

Release page: [https://github.com/llm-d/llm-d-async/releases](https://github.com/llm-d/llm-d-async/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-async/releases/tag/v1.0.0) — 2026-10-15
- **Transports.** `redis-sortedset` durable claims with lease-based redelivery, durable result delivery, payloads stored apart from the envelope, and Redis Cluster and Sentinel support. `gcp-pubsub` routes results per topic or per message. `redis-pubsub` is marked deprecated.
- **Flow control.** Per-queue and per-pool gates: Prometheus budget and saturation sources on the llm-d-router `llm_d_epp_*` metrics, endpoint-scrape, Redis quota in blocking or classifying mode, tier-priority admission, and leased-rate. Gate decisions are labelled by the deciding gate's reason.
- **Lifecycle.** Cancellation reaches requests already executing; equal-deadline requests dispatch in submission order; the gate-waiting gauge supports metrics-driven scale-from-zero.
- **Operations.** Helm chart with transport secrets, PodMonitors with custom labels, the Async Processor Grafana dashboard shipped with the llm-d dashboard set, and the multitenant guide in llm-d at Tier 2.

#### [v0.11.0](https://github.com/llm-d/llm-d-async/releases/tag/v0.11.0) — 2026-10-12
- feat: cancel inference requests that are already executing by @jia-gao in https://github.com/llm-d/llm-d-async/pull/474
- feat(pubsub): per-topic and per-message result topic routing by @jia-gao in https://github.com/llm-d/llm-d-async/pull/466
- redis: order equal-deadline requests by a Redis sequence by @wseaton in https://github.com/llm-d/llm-d-async/pull/463
- Revise security reporting guidelines in SECURITY.md by @davidgs in https://github.com/llm-d/llm-d-async/pull/488
- Reference llm-d Code of Conduct in CODE_OF_CONDUCT.md by @davidgs in https://github.com/llm-d/llm-d-async/pull/490
- Store request payloads apart from the queued envelope by @wseaton in https://github.com/llm-d/llm-d-async/pull/458
- feat(redis): support Redis Cluster and Sentinel topologies by @shimib in https://github.com/llm-d/llm-d-async/pull/491
- feat(chart): allow custom labels on the model server PodMonitor by @madhugoutham in https://github.com/llm-d/llm-d-async/pull/498
- deps(go): bump golang.org/x/net to v0.61.0 (CVE-2026-78669) by @shimib in https://github.com/llm-d/llm-d-async/pull/499

#### [v0.10.0](https://github.com/llm-d/llm-d-async/releases/tag/v0.10.0) — 2026-09-16
- Align async trace attributes with GenAI semantic conventions by @JaredTan95 in https://github.com/llm-d/llm-d-async/pull/435
- feat(producer): add durable Redis result delivery by @hhzhang16 in https://github.com/llm-d/llm-d-async/pull/437
- Add charts for backlog size, in process size, token usage, deadline proximity by @jtechapps in https://github.com/llm-d/llm-d-async/pull/444
- feat: deprecate redis-pubsub transport by @804533125 in https://github.com/llm-d/llm-d-async/pull/442
- feat: expose planner dispatch contracts and telemetry by @sachalmalick in https://github.com/llm-d/llm-d-async/pull/425
- feat: bound pool gate wait lifecycle by @sachalmalick in https://github.com/llm-d/llm-d-async/pull/426
- feat: enforce leased Redis dispatch rates by @sachalmalick in https://github.com/llm-d/llm-d-async/pull/424
- feat(flowcontrol): support direct endpoint budgets by @hhzhang16 in https://github.com/llm-d/llm-d-async/pull/453

#### [v0.9.1](https://github.com/llm-d/llm-d-async/releases/tag/v0.9.1) — 2026-09-04
- Add async_gate_decisions_total metrics to worker pool gates by @jtechapps in https://github.com/llm-d/llm-d-async/pull/385
- feat(mergepolicy): stamp inference fairness ID from tenant metadata by @LukeAVanDrie in https://github.com/llm-d/llm-d-async/pull/380
- feat(worker): capture gateway drop reasons and honor Retry-After within the deadline by @LukeAVanDrie in https://github.com/llm-d/llm-d-async/pull/381
- feat(chart): support pod affinity (ap.affinity) for the llm-d-async chart by @todayim in https://github.com/llm-d/llm-d-async/pull/383
- feat(ap): result TTLs, per-lane objective stamping, and deadline classification by @BenjaminBraunDev in https://github.com/llm-d/llm-d-async/pull/394
- feat(metrics): add token throughput counter by @0xA8hinav in https://github.com/llm-d/llm-d-async/pull/401
- Add GCP PubSub e2e tests using emulator by @jtechapps in https://github.com/llm-d/llm-d-async/pull/395
- feat(metrics): deadline proximity histogram for backlog queues. by @0xA8hinav in https://github.com/llm-d/llm-d-async/pull/400
- Readme restructure by @shimib in https://github.com/llm-d/llm-d-async/pull/411
- feat(redis): hot reload sorted-set queue configuration by @todayim in https://github.com/llm-d/llm-d-async/pull/407
- feat(redis): durable dequeue via claims for the sorted-set transport by @0xA8hinav in https://github.com/llm-d/llm-d-async/pull/412

#### [v0.9.0](https://github.com/llm-d/llm-d-async/releases/tag/v0.9.0) — 2026-07-30
- deps(go): Bump the go-dependencies group with 5 updates in https://github.com/llm-d/llm-d-async/pull/352
- deps(go): Bump k8s.io/client-go from 0.34.9 to 0.34.10 in the kubernetes group in https://github.com/llm-d/llm-d-async/pull/351

#### [v0.8.0](https://github.com/llm-d/llm-d-async/releases/tag/v0.8.0) — 2026-07-27
- HTTP-error Payload now contains the raw upstream response body instead of a wrapped error string.
- Gate-drop Payload changed from {"status":"dropped"} to {"error":"Pool gating dropped request"} and is now unified across all transports
- Gate-drop results now include Metadata (from req.ReqMetadata()), which the previous inline construction omitted.
- InferenceClient.SendRequest now returns (*InferenceResponse, error), where InferenceResponse has StatusCode int and Body []byte fields


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [v1.1.0](https://github.com/llm-d/llm-d-async/milestone/5) _(milestone · due 2026-11-25 · 3/12 issues closed · 7 open PRs)_ — First minor after v1.0.0. Goals: sql transport (experimental), vllm-omni support, deadline-driven required-replicas gauge for KEDA. Tracking: #510- [#510 [Tracking] v1.1.0 Roadmap](https://github.com/llm-d/llm-d-async/issues/510) _(roadmap · roadmap)_ — Tracking issue for the **v1.1.0** milestone: the first minor after v1.0.0. It has three feature goals, plus work carried over from v0.11.0 / v1.0.0 and follow-ups from the v1.0.0 cut.

Milestone: [...
## llm-d/llm-d-autoscaling (watch)

Release page: [https://github.com/llm-d/llm-d-autoscaling/releases](https://github.com/llm-d/llm-d-autoscaling/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v1.0.0) — 2026-10-13
- **The repository is now KEDA-first.** The Workload-Variant-Autoscaler (WVA) controller is deprecated and has moved into `legacy/`, where it stays only until it is removed (#1563). KEDA is the autoscaling engine. This repository provides the KEDA manifest blueprints (`benchmark/config/scenarios/`) and the evaluation test bed (`benchmark/`).
- **Benchmark test bed:** a vLLM model simulator (#1545), a P/D-with-simulator scenario example (#1520), a token-aware scenario and an extended Grafana dashboard (#1555), and `benchmark/results` is now git-ignored (#1580).
- **Docs:** an autoscaling development workflow guide (#1571), and a proposal for async/batch autoscaling driven by llm-d-async metrics (#1573).
- **Validation:** an e2e test of the llm-d KEDA EPP guide on Kind (#1472).
- **Toolchain:** Go 1.26 and the builder image moved to golang 1.27 (#1512, #1540, #1549, #1541).
- **No controller image is published in this release.** The last supported WVA version is **v0.9.0** (`ghcr.io/llm-d/llm-d-workload-variant-autoscaler:v0.9.0`, branch `release-0.9`).

#### [v0.9.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.9.0) — 2026-08-13
- The VariantAutoscaling CRD is gone (a four-part removal series), leaving annotation mode as the only configuration path.
- KEDA is now the sole scaling backend — Prometheus Adapter is retired
- The WVA Helm chart is deleted, so deployment is kustomize-only. And the V2 token/capacity-based saturation analyzer is now the default, replacing V1.
- engine: add structured per-cycle log lines (analyzer-result, scaling-decision) by @deanlorenz in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1318
- checklists for analyzer in WVA by @asm582 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1127
- Add use case doc by @asm582 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1319
- bug-fix: observability - config info metrics by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1144
- Bumping llm-d release to latest version v0.8.1 by @dumb0002 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1337
- Create a dedicated component for Openshift patches and Openshift's cluster-scoped deployment by @aleskandro in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1354
- deploy: remove LLM_D_RELEASE dependency on llm-d/llm-d by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1357
- bug-fix: observability - available gpus metric by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1147
- feat: add wva_saturation_metrics_up freshness gauge by @jia-gao in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1190
- feat(benchmark): add post-processing script for tabular benchmark reports by @kahilam in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1315
- feat: add SGLang inference-engine backend support by @MohanKumar21 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1351
- bug: Observability - Dashboard: Limiter Impact Panel fix by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1381

#### [v0.8.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.8.0) — 2026-06-22
- **Observability suite** — new Prometheus metrics: collector health, configuration state, error tracking, pipeline-stage, and `wva_pod_mapping_miss_total` for unattributed pods. Plus Kubernetes events for scaling decisions and an operational Grafana dashboard with selectable data sources.
- **Saturation/throughput engine work** — P/D role-aware grouping in the V1 analyzer, V1 default thresholds with partial overrides, a multi-analyzer registry, a universal threshold post-step, and a new `ThroughputAnalyzer` (ITL model + scaling signal + engine wiring).
- **Kustomize-first install** — Kustomize is now the primary controller install path; added a namespace-scoped/Kubernetes overlay and OpenShift user-workload-monitoring metrics scraping.
- **Flexible variant discovery** — Phase 1 dual-mode annotation-based discovery; `llm-d.ai/variant` is now optional for Deployment/LWS via an ownerReference walk.
- **New Coordinator component** and an initial GPU **rebalancer** proof-of-concept.
- **Benchmarking** — new ShareGPT real-dataset profile, burst/bursty load scenarios, and extensive published results (Qwen3-0.6B / 32B, prefill/decode/symmetrical, HPA Sat V1).
- Role-aware scale-down for disaggregated models.
- Sentinel accelerator name used instead of silently halting scaling.
- V2 cost-aware optimizer fallback when GPU capacity is unknown.
- Include `gpuCount` in the V2 history key to prevent cross-variant contamination.
- Stop LWS group>1 from getting stuck in "model in transition" (V1).
- Emit replica scaling signal even when the accelerator is unresolved.
- Collector: drop `model_name` filter from `cache_config_info`; resolve/attribute VA via HPA `scaleTargetRef` for unmanaged scalers.
- **Env var rename:** `NAMESPACE` replaced by `WVA_NS`.
- **Multi-model surface removed** from the deploy config.

#### [v0.7.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.7.0) — 2026-04-30
- add new target for nightly by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/975
- Remove duplicate CKS nightly workflow by @clubanderson in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/974
- update new targets for nightly by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/977
- Set Metrics Fix: disable the metrics server in indexer testing by @Gregory-Pereira in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/976
- Using featureGates to enable EPP flowControl feature by @dumb0002 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/973
- feat: Phase 3a — CI benchmark for prefill-heavy workload (Saturation V1, OpenShift) by @kahilam in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/947
- Cleanup documentation structure and content by @lionelvillard in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/986
- update: trivy-action pinned SHA1 by @zdtsw in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/960
- Fixes for infra install by @asm582 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/998
- Restrict WVA controller ClusterRole to only WVA ConfigMaps by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/985
- Multi-model deploy and test with wrapper by @asm582 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1014
- Add multi-model benchmark guide by @kahilam in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1021
- Add decode hheavy mode for single model benchmark by @asm582 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1027
- tighten e2e fixture ensure correctness by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1032
- Add pr-review skill by @lionelvillard in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1039

#### [v0.6.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.6.0) — 2026-04-03
- Bug fix: fix zap-log-level flag by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/827
- Add scaling-decision logging and E2E failure/debug dumps by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/796
- Bug fix: Load Configmap in all namespaces during bootstrap by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/812
- update wva image after repo graduate by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/833
- 🐛 fix: checkout PR head SHA for issue_comment triggered workflows by @clubanderson in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/832
- attempt to fix full e2e ci trigger for fork by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/839
- 🐛 fix: report e2e commit status to fork PR head SHA by @clubanderson in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/840
- make full e2e tests required on pr ci run by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/842
- stop keda guard when kind cluster is deleted to avoid spamming the terminal by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/835
- document wva release process by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/845
- Bug: restart prometheus-adapter for stable e2e test by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/846
- add GIE queuing for scale from zero e2es by @mamy-CS in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/849
- cleanup: remove unused BENCHMARK_MODE var in install scripts by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/859
- e2e fix: limiter e2e "Accelerator-specific scaling" fix by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/862
- 🌱 Remove per-repo gh-aw typo/link/upstream workflows by @clubanderson in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/856


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.8.0-rc5](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.8.0-rc5) (2026-06-19)  - Enhancement: add panel showing wva_pod_mapping_miss_total metric in dashboard by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1301
- [v0.8.0-rc4](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.8.0-rc4) (2026-06-18)  - Observability Dashboard: support selectable data sources by @shuynh2017 in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1287
- [v0.8.0-rc3](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.8.0-rc3) (2026-06-17)  - Revert "feat(config): default to V2 token-based saturation analyzer (… by @lionelvillard in https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1286

**Milestones, roadmaps & open RFCs feeding the next drop**
- [v0.10.0 release](https://github.com/llm-d/llm-d-autoscaling/milestone/8) _(milestone · due TBD · 5/6 issues closed · 0 open PRs)_- [v0.9.0 release](https://github.com/llm-d/llm-d-autoscaling/milestone/7) _(milestone · due 2026-08-06 · 25/25 issues closed · 0 open PRs)_ — code freeze: July 30th- [v1.0.0 Release](https://github.com/llm-d/llm-d-autoscaling/milestone/9) _(milestone · due 2026-10-15 · 0/1 issues closed · 0 open PRs)_- [#1079 Roadmap ](https://github.com/llm-d/llm-d-autoscaling/issues/1079) _(roadmap · roadmap)_ — # Autoscaling Roadmap

This roadmap captures major initiatives for the Workload Variant Autoscaler.
Priorities may evolve based on community feedback and project needs.

### Core

- [ ] Unify WVA c...
## llm-d/llm-d-batch-gateway (watch)

Release page: [https://github.com/llm-d/llm-d-batch-gateway/releases](https://github.com/llm-d/llm-d-batch-gateway/releases)

### Shipped (what went in)

#### [v1.0.1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.1) — 2026-11-16
- feat: support PostgreSQL SQL async dispatch by @aneeshkp in https://github.com/llm-d/llm-d-batch-gateway/pull/754
- feat(files_store): add native GCS file backend by @mstandley-tempus in https://github.com/llm-d/llm-d-batch-gateway/pull/745
- feat(processor): carry the job tenant in async request metadata by @aneeshkp in https://github.com/llm-d/llm-d-batch-gateway/pull/778

#### [v1.0.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.0) — 2026-10-18
- ghcr.io/llm-d/batch-gateway-apiserver:v1.0.0
- ghcr.io/llm-d/batch-gateway-processor:v1.0.0
- ghcr.io/llm-d/batch-gateway-gc:v1.0.0
- enh: update helm charts to new llm-d-async config values by @evacchi in https://github.com/llm-d/llm-d-batch-gateway/pull/636
- feat: guard resumable batch takeover by @tryambak2019 in https://github.com/llm-d/llm-d-batch-gateway/pull/685
- feat: resumable batch foundation — entry schema, fenced store, stable request IDs by @acardace in https://github.com/llm-d/llm-d-batch-gateway/pull/735
- feat: run all jobs through the resumable pipeline by @acardace in https://github.com/llm-d/llm-d-batch-gateway/pull/736

#### [v0.7.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v0.7.0) — 2026-10-08
- ghcr.io/llm-d/batch-gateway-apiserver:v0.7.0
- ghcr.io/llm-d/batch-gateway-processor:v0.7.0
- ghcr.io/llm-d/batch-gateway-gc:v0.7.0
- Added PostgreSQL LISTEN/NOTIFY cancellation with durable batch events.
- Removed Redis/Valkey as a Batch Gateway control-plane dependency.
- Added configurable batch endpoints through global.extraEndpoints.
- Batch request totals are now visible immediately after processing starts.
- feat(gc): initialize OTel tracer and trace orphan triage by @wseaton in https://github.com/llm-d/llm-d-batch-gateway/pull/647
- feat: replace Redis queue with Postgres-native atomic job ownership by @acardace in https://github.com/llm-d/llm-d-batch-gateway/pull/582
- feat(processor): derive worker count from input disk budget by @lioraron in https://github.com/llm-d/llm-d-batch-gateway/pull/692
- feat: support configurable batch endpoints by @elizabetht in https://github.com/llm-d/llm-d-batch-gateway/pull/665
- feat: reimplement cancellation mechanism via Postgres LISTEN/NOTIFY and eliminate Redis by @acardace in https://github.com/llm-d/llm-d-batch-gateway/pull/676

#### [v0.6.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v0.6.0) — 2026-09-24
- ghcr.io/llm-d/batch-gateway-apiserver:v0.6.0
- ghcr.io/llm-d/batch-gateway-processor:v0.6.0
- ghcr.io/llm-d/batch-gateway-gc:v0.6.0
- feat(gc): initialize OTel tracer and trace orphan triage by @wseaton in https://github.com/llm-d/llm-d-batch-gateway/pull/647
- feat: replace Redis queue with Postgres-native atomic job ownership by @acardace in https://github.com/llm-d/llm-d-batch-gateway/pull/582
- feat(processor): derive worker count from input disk budget by @lioraron in https://github.com/llm-d/llm-d-batch-gateway/pull/692

#### [v0.5.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v0.5.0) — 2026-08-12
- enh: use single context with cancel cause in `Processor#runJob()` by @evacchi in https://github.com/llm-d/llm-d-batch-gateway/pull/625
- feat(processor): tenant-scoped model_gateways lookups (route_key_by_tenant) by @todayim in https://github.com/llm-d/llm-d-batch-gateway/pull/630

#### [v0.4.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v0.4.0) — 2026-08-07
- feat(demo): add llm-d-async dispatcher support to deploy-k8s.sh by @yizhaodev in https://github.com/llm-d/llm-d-batch-gateway/pull/607
- feat(benchmarks): implement scenario 5 async-processor deployment by @lioraron in https://github.com/llm-d/llm-d-batch-gateway/pull/600
- feat: add TLS CLI flags for external configuration by @ugiordan in https://github.com/llm-d/llm-d-batch-gateway/pull/618


### Next community release (planned)

**Release candidates / trains in flight**
- [v1.0.1-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.1-rc1) (2026-11-16)  - feat: support PostgreSQL SQL async dispatch by @aneeshkp in https://github.com/llm-d/llm-d-batch-gateway/pull/754
  - feat(files_store): add native GCS file backend by @mstandley-tempus in https://github.com/llm-d/llm-d-batch-gateway/pull/745
  - feat(processor): carry the job tenant in async request metadata by @aneeshkp in https://github.com/llm-d/llm-d-batch-gateway/pull/778
- [v1.1.0-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.1.0-rc1) (2026-11-12)  - feat: support PostgreSQL SQL async dispatch by @aneeshkp in https://github.com/llm-d/llm-d-batch-gateway/pull/754
  - feat(files_store): add native GCS file backend by @mstandley-tempus in https://github.com/llm-d/llm-d-batch-gateway/pull/745
- [v1.0.0-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.0-rc1) (2026-10-14)  - ghcr.io/llm-d/batch-gateway-apiserver:v1.0.0-rc1
  - ghcr.io/llm-d/batch-gateway-processor:v1.0.0-rc1
  - ghcr.io/llm-d/batch-gateway-gc:v1.0.0-rc1
  - enh: update helm charts to new llm-d-async config values by @evacchi in https://github.com/llm-d/llm-d-batch-gateway/pull/636
  - feat: guard resumable batch takeover by @tryambak2019 in https://github.com/llm-d/llm-d-batch-gateway/pull/685


## llm-d/llm-d-benchmark (watch)

Release page: [https://github.com/llm-d/llm-d-benchmark/releases](https://github.com/llm-d/llm-d-benchmark/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v1.0.0) — 2026-10-16
- feat: prefer inference-perf's native BR0.2 partial over hand-derived aggregate by @elinacse in https://github.com/llm-d/llm-d-benchmark/pull/1911
- Stop installing OS tools the driver never invokes by @ruocco in https://github.com/llm-d/llm-d-benchmark/pull/1970
- Consolidate Benchmark Report v0.2 and v0.2.1 into one implementation by @Bslabe123 in https://github.com/llm-d/llm-d-benchmark/pull/1923
- [Run] Fixes for `lm-eval` harness by @maugustosilva in https://github.com/llm-d/llm-d-benchmark/pull/1989
- run: keep the harness pod's treatment label a YAML string by @kaushikmitr in https://github.com/llm-d/llm-d-benchmark/pull/1995
- standup: filter amd router values by accelerator by @shikamd123 in https://github.com/llm-d/llm-d-benchmark/pull/1996
- Label KV-cache usage statistics as a fraction by @David-Wu1119 in https://github.com/llm-d/llm-d-benchmark/pull/1991
- Convert cross-treatment latency columns to seconds using each report's units by @David-Wu1119 in https://github.com/llm-d/llm-d-benchmark/pull/1990
- Count failed requests, not error types, in the aiperf import by @David-Wu1119 in https://github.com/llm-d/llm-d-benchmark/pull/1992
- teardown hangs forever on another tenant's PV by @ruocco in https://github.com/llm-d/llm-d-benchmark/pull/2001
- Do not multiply FMA comparison totals by num_workers by @David-Wu1119 in https://github.com/llm-d/llm-d-benchmark/pull/2003
- Report GuideLLM's TPOT as NTPOT, since it includes the first token by @David-Wu1119 in https://github.com/llm-d/llm-d-benchmark/pull/2007
- workload: add inference-perf profiles for the llm-d async multi-tenant nightly by @jtechapps in https://github.com/llm-d/llm-d-benchmark/pull/2004
- Report InferenceMAX lengths from totals and keep ITL/E2E p50 and p75 by @David-Wu1119 in https://github.com/llm-d/llm-d-benchmark/pull/2008
- Use std_dev in the token-shape inference-perf profiles by @asm582 in https://github.com/llm-d/llm-d-benchmark/pull/2009

#### [v0.8.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.8.0) — 2026-08-17
- Support for `standup` directly from the [guides](https://github.com/llm-d/llm-d/tree/main/guides)
- Initial implementation of `standup` for [no Kubernetes](https://github.com/llm-d/llm-d-benchmark/blob/main/docs/nok8s.md)
- Added [`lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) to evaluate accuracy/quality
- Added `eval-containers` harness, running agentic benchmarks against llm-d stacks.
- feat: add eval-containers agentic-benchmark harness (aider-polyglot, gaia) by @elronbandel in https://github.com/llm-d/llm-d-benchmark/pull/1565
- Add TPU optimized baseline workload profile by @rlakhtakia in https://github.com/llm-d/llm-d-benchmark/pull/1600
- Support inference-perf report conversion in run-only mode by @hubunt in https://github.com/llm-d/llm-d-benchmark/pull/1598
- Add license scan report and status by @fossabot in https://github.com/llm-d/llm-d-benchmark/pull/1608
- Add direct KEDA autoscaling (EPP+KEDA) without WVA controller by @asm582 in https://github.com/llm-d/llm-d-benchmark/pull/1611
- Add reset_caches option to clear vLLM caches between treatments by @ruocco in https://github.com/llm-d/llm-d-benchmark/pull/1616
- Add experiment per treatment retry by @ruocco in https://github.com/llm-d/llm-d-benchmark/pull/1635
- add no-k8s deployment by @mengmeiye in https://github.com/llm-d/llm-d-benchmark/pull/1631
- feat(keda): extend prometheus bearer token TTL from 60min to 24h by @asm582 in https://github.com/llm-d/llm-d-benchmark/pull/1664
- Add lm-eval accuracy harness by @WenjiaoYue in https://github.com/llm-d/llm-d-benchmark/pull/1606
- add sglang guides by @mengmeiye in https://github.com/llm-d/llm-d-benchmark/pull/1672

#### [v0.7.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.7.0) — 2026-06-25
- Support for AIPerf as a new harness
- Added all workloads used by "guides" in `llm-d` under `workload` directory (prefixed by `guide_<guide name>`
- Added Ruff as a linter and formatter to pre-commit.
- Significant overhaul of CI/CD, now shared with `llm-d` (for "nightly benchmarks")
- Add agentic code generation workload
- Improved integration with Fast Model Actuator
- Add nixl benchmark script (for "sanity check" on `pd-disaggregation` and `wide-ep-lws` scenarios)
- Increased compatibility for helm3 and helm4, s390x, and other miscellaneous installation bugs
- feat: implement queue-based async telemetry by @jjk-g in https://github.com/llm-d/llm-d-benchmark/pull/926
- feat: expose model_id_label as ${model.idLabel} for use in extraObjec… by @kalantar in https://github.com/llm-d/llm-d-benchmark/pull/1103
- feat(result store): Results Store CLI by @huaxig in https://github.com/llm-d/llm-d-benchmark/pull/914
- add max-concurrency treatment by @mengmeiye in https://github.com/llm-d/llm-d-benchmark/pull/1235
- feat: pin curl to 8.20.0 by @clubanderson with @Copilot in https://github.com/llm-d/llm-d-benchmark/pull/1256
- feat: Kustomize Integration for Optimized Baseline by @Vezio in https://github.com/llm-d/llm-d-benchmark/pull/1199
- Add nixl benchmark script by @praveingk in https://github.com/llm-d/llm-d-benchmark/pull/1367

#### [v0.6.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.6.0) — 2026-05-04
- Full conversion to `python`, with a new CLI and a new declarative specification language for experiment description
- Plugin architecture makes adding new stages to the life cycle fluent and scalable for future features.
- User experience was enhanced with a much more meaningful logging and message display
- Extensive health checking during and at the end of the deployment.
- New standup method available: "Fast Model Actuator" (FMA)
- Fast Model Actuation (FMA) is a Kubernetes-native system for efficiently managing LLM inference servers and reduces model startup latency from minutes to seconds. FMA uses two techniques: vLLM sleep/wake, where model instances move tensors from GPU to CPU memory — freeing accelerator resources while keeping the process alive for rapid wake-up and model swapping, where a persistent launcher process handles initialization upfront so instances can be swapped without full cold starts.
- Significant improvements for perfomance data collection, including relevant changes on benchmark report
- "Time-series" metrics on version 0.2 of the benchmark reports now include both statics summarization and link to raw collected data on csv format.
- Tighter integration with Workload Variant Autoscaler (WVA), including the ability to deploy multiple models on the same namespace as defined within a scenario. In the same vein - allowing one or more stacks in the scenario to be deployed and torn down based on user preference.
- Ability to provide different parameters for `vllm` process on different `pods` (by using `LeaderWorkerSet` (LWS) Kubernetes API).
- Allow filling in stack details from a YAML file from harness pod.
- Assorted corrections and robustness improvements.
- The "capacity planner" and "configuration explorer" are now part of a new project: https://github.com/llm-d-incubation/llm-d-planner
- Strongly enhanced development constructs including pre-commit and CICD that safe guard existing library patterns and functionality.
- Add memory and cache metrics #2 by @DolevAdas in https://github.com/llm-d/llm-d-benchmark/pull/742

#### [v0.5.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.5.0) — 2026-03-07
- All [well-lit paths](https://github.com/llm-d/llm-d/tree/main/guides) deployable via standup.sh
- This includes `wide-ep-lws` and `workload-autoscaling`
- Operational improvements
- Add a "benchmark runner" ([run_only.sh](https://github.com/llm-d/llm-d-benchmark/blob/main/existing_stack/run_only.sh)), for pre-existing stacks (key piece in integrating with [well-lit paths](https://github.com/llm-d/llm-d/tree/main/guides) on the main repository
- Additional improvements on automatic setup of `pods` (via "preprocess" utility [set_llmdbench_environment.py](https://github.com/llm-d/llm-d-benchmark/blob/main/setup/preprocess/set_llmdbench_environment.py) in clusters where RoCE/CDR/Infiniband (and LWS) are used.
- Expanded early detection of crashed `pods` to include both "gaie-epp" and "inference-gateway" ones.
- A new standup step, ["ensure admin prerequisites"](https://github.com/llm-d/llm-d-benchmark/blob/main/setup/steps/02_ensure_admin_prerequisites.py) (02), concentrates the installation of all cluster-wide prerequisites (e.g., `istio`, `gateway`, `lws`)
- `priorityClassName` support on `standalone` and `modelservice` methods for standup
- Fixes to allow spaces in directory paths
- Significant improvements for benchmark report
- Version 0.2 of the benchmark reports now support "time-series" metrics.
- Allow filling in stack details from a YAML file from harness pod.
- Assorted corrections and robustness improvements.
- Configuration Explorer:
- GPU recommender (using llm-optimizer's roofline analysis)

#### [v0.4.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.4.0) — 2025-12-19
- Support for all well-lit paths directly in standup
- Each well-lit path has now both a scenario and a experiment (the only exception is an experiment for`wide-ep-lws`)
- Examples scenarios for gpu, aiu (Spyre), cpu-only and simulated
- Deployable as both “standalone” (i.e., vanilla VLLM) and llm-d
- Ability deploy multiple load-generating pods
- Controlled via environment variable or command-line parameter
- Tight integration with WVA (Workload Variant Autoscaler)
- When enabled and deployed via standup, WVA configuration is done automatically
- Operational improvements
- Significant improvements on automatic setup of pods in cluster where RoCE/CDR/Infiniband (and LWS) are used.
- All PVCs are now read-only
- Better support for large model caching and sharing in a single cluster
- Early detection of crashed pods
- Whenever a deployment is attempted with wrong parameters, immediately detect and stop when pods crash
- Full support for (newer) istio and kgateway


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-inference-payload-processor (watch)

Release page: [https://github.com/llm-d/llm-d-inference-payload-processor/releases](https://github.com/llm-d/llm-d-inference-payload-processor/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-inference-payload-processor/releases/tag/v1.0.0) — 2026-10-20
- feat: echo selected model name as response header by @szedan-rh in https://github.com/llm-d/llm-d-inference-payload-processor/pull/199
- feat: model name Filter by @aradhalevy in https://github.com/llm-d/llm-d-inference-payload-processor/pull/172
- [Documentation] Extend data layer description by @ronenkat in https://github.com/llm-d/llm-d-inference-payload-processor/pull/198
- cleanup datastore interface by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/222
- [Feature] Adds shared pricing infrastructure for actual cost of inference scoring by @davidbreitgand in https://github.com/llm-d/llm-d-inference-payload-processor/pull/217
- [Feature] Adds cost t-digest accumulator by @davidbreitgand in https://github.com/llm-d/llm-d-inference-payload-processor/pull/228
- Datalayer: carry CycleState on request/response event payloads. by @Mohammad-nassar10 in https://github.com/llm-d/llm-d-inference-payload-processor/pull/203
- [Feature] Adds RequestCostMetadataExtractor plugin by @davidbreitgand in https://github.com/llm-d/llm-d-inference-payload-processor/pull/232
- [Feature] RequestCostMetadataExtractor registration and config by @davidbreitgand in https://github.com/llm-d/llm-d-inference-payload-processor/pull/238
- Add a group model filter by @ronenkat in https://github.com/llm-d/llm-d-inference-payload-processor/pull/227
- Emit datalayer response event on the streaming path by @aradhalevy in https://github.com/llm-d/llm-d-inference-payload-processor/pull/242
- [Feature] Add Anthropic and Google (Gemini) response format support to requestcostmetadata extractor by @abdallahsamabd in https://github.com/llm-d/llm-d-inference-payload-processor/pull/234
- Move group configuration Modelconfig collector group conf by @ronenkat in https://github.com/llm-d/llm-d-inference-payload-processor/pull/241
- [Feature] CostGuard scorer skeleton by @davidbreitgand in https://github.com/llm-d/llm-d-inference-payload-processor/pull/243
- [Documentation] Update filter documentation by @ronenkat in https://github.com/llm-d/llm-d-inference-payload-processor/pull/237

#### [v0.1.0](https://github.com/llm-d/llm-d-inference-payload-processor/releases/tag/v0.1.0) — 2026-07-12
- add nirrozenbaum to owners by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/8
- prepare for code migration by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/16
- migrate: sigs.k8s.io/gateway-api-inference-extension @ dc908434 by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/17
- continuation PR for migration. by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/20
- cleanup PR by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/29
- fixed label for pr size by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/40
- Add AttributeMap. by @Mohammad-nassar10 in https://github.com/llm-d/llm-d-inference-payload-processor/pull/30
- introduce minimal representation of a Model into framework datalayer by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/55
- add shmuelk to OWNERS by @nilig in https://github.com/llm-d/llm-d-inference-payload-processor/pull/57
- Add ModelSelector architecture proposal by @noyitz in https://github.com/llm-d/llm-d-inference-payload-processor/pull/43
- skeleton for model selector profile with plugins by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/58
- Datastore framework by @Mohammad-nassar10 in https://github.com/llm-d/llm-d-inference-payload-processor/pull/34
- Add data layer interfaces. by @Mohammad-nassar10 in https://github.com/llm-d/llm-d-inference-payload-processor/pull/60
- Add initial configuration structs with code generation machinery by @shmuelk in https://github.com/llm-d/llm-d-inference-payload-processor/pull/80
- feat: implement model selector pipeline by @noyitz in https://github.com/llm-d/llm-d-inference-payload-processor/pull/72


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.1.0-rc.4](https://github.com/llm-d/llm-d-inference-payload-processor/releases/tag/v0.1.0-rc.4) (2026-07-02)  - wire pre/post processors to the request handling pipeline by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/202
- [v0.1.0-rc.3](https://github.com/llm-d/llm-d-inference-payload-processor/releases/tag/v0.1.0-rc.3) (2026-06-30)  - add nirrozenbaum to owners by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/8
  - prepare for code migration by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/16
  - migrate: sigs.k8s.io/gateway-api-inference-extension @ dc908434 by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/17
  - continuation PR for migration. by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/20
  - cleanup PR by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/29
  - fixed label for pr size by @nirrozenbaum in https://github.com/llm-d/llm-d-inference-payload-processor/pull/40


## llm-d/llm-d-inference-sim (watch)

Release page: [https://github.com/llm-d/llm-d-inference-sim/releases](https://github.com/llm-d/llm-d-inference-sim/releases)

### Shipped (what went in)

#### [v1.2.0](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.2.0) — 2026-11-10
- Fixed tool call streaming to send id and type only in the initial delta.
- Emit a `cache_threshold` finish chunk for every streamed choice
- Reject a KV cache size of 0 when the KV cache is enabled
- Fixes in `mm_payload` support in `.../render`, in `--mm-encoder-only` mode, `ec_transfer_params` is keyed by each part's uuid
- Allow "caf" in typos config to fix false positive in unicode tests by @mayabar in https://github.com/llm-d/llm-d-inference-sim/pull/861
- Emit a cache_threshold finish chunk for every streamed choice by @Yaomeng1749 in https://github.com/llm-d/llm-d-inference-sim/pull/835
- Reject a KV cache size of 0 when the KV cache is enabled by @aliaa039 in https://github.com/llm-d/llm-d-inference-sim/pull/870
- kvcache: pick blocks to evict without scanning every unused block by @qwert123q in https://github.com/llm-d/llm-d-inference-sim/pull/863
- Support the coordinator's mm_payload none path on render and generate by @mayabar in https://github.com/llm-d/llm-d-inference-sim/pull/871

#### [v1.1.0](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.1.0) — 2026-11-03
- Accept the **model** as a positional command line argument
- Add support for `min_tokens` in `/v1/chat/completions`
- Generate JSON content when `response_format` is set to`json_object` or `json_schema` in `/v1/chat/completions`
- Add output message ID in non-streaming `/v1/responses`
- Add vLLM endpoints `/v1/systemone` and `/v1/decisions`
- Honor `min_token` on /v1/completions
- Honor `mm_payload` and `return_mm_kwargs` on the render endpoints
- Tokenization
- Prevent Unicode text loss during simulated tokenization
- Allow enabling fake metrics via POST `/admin/config` at runtime
- Export `vllm:request_max_num_generation_tokens` instead of `vllm:max_num_generation_tokens`
- Stamp `vllm:lora_requests_info` with sub-second time
- KV cache events
- Always send `lora_id` and `lora_name` in map-format `BlockStored` events
- Reference llm-d Code of Conduct in CODE_OF_CONDUCT.md by @davidgs in https://github.com/llm-d/llm-d-inference-sim/pull/767

#### [v1.0.0](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.0.0) — 2026-10-15
- Add multimodal output endpoints: `/v1/audio/speech`, `/v1/images/generate`
- Add `--strict` which enables validation of `/v1/chat/completions` and `/v1/completions` against the embedded vLLM 0.21.0 request schemas and engine-owned semantic checks
- Add `/v1/messages/render` and `/v1/messages/count_tokens`
- The deprecated `--force-dummy-tokenizer` flag was removed. Use empty/undefined `--render-url` to force dummy tokenizer usage
- Reference llm-d Code of Conduct in CODE_OF_CONDUCT.md by @davidgs in https://github.com/llm-d/llm-d-inference-sim/pull/767
- Add sglang's matched_stop field (always null) by @irar2 in https://github.com/llm-d/llm-d-inference-sim/pull/770
- Add multimodal output endpoints: /v1/audio/speech, /v1/images/generat… by @oglok in https://github.com/llm-d/llm-d-inference-sim/pull/716
- Return 500 instead of panicking when the dataset lookup fails by @EugeneVon in https://github.com/llm-d/llm-d-inference-sim/pull/773
- feat: add opt-in vLLM sampling validation by @0z5a in https://github.com/llm-d/llm-d-inference-sim/pull/683
- Make make test work when Docker uses a non-default socket by @irar2 in https://github.com/llm-d/llm-d-inference-sim/pull/775
- Add /v1/messages/render and /v1/messages/count_tokens, and return KV and EC transfer params from /v1/messages by @irar2 in https://github.com/llm-d/llm-d-inference-sim/pull/780
- feat: add support for min_tokens in /chat/completions by @04kash in https://github.com/llm-d/llm-d-inference-sim/pull/737
- Load the in-memory dataset into a shared memdb database by @EugeneVon in https://github.com/llm-d/llm-d-inference-sim/pull/785
- Expose vllm:lora_requests_info only when LoRA is configured and in use by @irar2 in https://github.com/llm-d/llm-d-inference-sim/pull/788
- Release the dataset DB when verification fails, and share the test fixture path by @irar2 in https://github.com/llm-d/llm-d-inference-sim/pull/790

#### [v0.12.0](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v0.12.0) — 2026-10-08
- Add `/v1/responses/render` endpoint
- Add derender endpoints, the inverse of the render endpoints
- KVCache:
- add `--zmq-topic` to override the KV-event topic
- honor cache_salt in simulated KV prefix caching and events
- hybrid ZMQ `bind/dial`
- Add `kv_transfer_params` and `ec_transfer_params` to `/v1/responses`
- Add `kv-cache-dtype` to configuration, expose its value on `vllm:cache_config_info` metric
- Export the standard process metrics
- **Experimental**: Add an SGLang engine backend
- Configuration changes, for details see [configuration docs](https://github.com/llm-d/llm-d-inference-sim/blob/main/docs/configuration.md)
- Unknown keys and stray arguments in CLI and YAML config are rejected now
- Boolean configuration flags behavior became same as vLLM's
- YAML has nested structure now
- Merge release-v0.11 into the main branch by @mayabar in https://github.com/llm-d/llm-d-inference-sim/pull/660

#### [v0.11.4](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v0.11.4) — 2026-10-04
- deps: bump grpc-go to v1.83.2 to fix CVE-2026-84445 by @irar2 in https://github.com/llm-d/llm-d-inference-sim/pull/749
- Backport: hybrid ZMQ bind/dial (#668) by @irar2 in https://github.com/llm-d/llm-d-inference-sim/pull/748

#### [v0.11.2](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v0.11.2) — 2026-08-31
- Add audio content by @mayabar in https://github.com/llm-d/llm-d-inference-sim/pull/659
- Add `--skip-tool-validation` to bypass tool schema meta-validation
- Accept `--tensor-parallel-size` as an ignored flag
- Add function_call tool turns
- Configurable truncated-geometric tool-call count distribution
- Enhanced tool definition flexibility by supporting common JSON schema keywords, normalizing parameter types, and handling missing properties or items gracefully
- Add ZMQ replay endpoint for KV cache events
- Implement `vllm:request_time_per_output_token_seconds` metrics
- The environment variables `HF_ENDPOINT`, `HF_TOKEN`, `HF_HUB_ENDPOINT`, and both casing variants of `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` are now supported for the vLLM renderer in simulator tests
- Bug fix: ZMQ endpoint offset per rank: only Port was offset for ranks > 0, while ZMQEndpoint was not, so all ranks published to the same ZMQ port. Each rank now publishes to endpoint_port + rank.
- Remove deprecated `/ready` endpoint
- Metrics renamed: `vllm:prefix_cache_hits` -> `vllm:prefix_cache_hits_total` and `vllm:prefix_cache_queries` -> `vllm:prefix_cache_queries_total`
- ZMQ topic name changed from `kv@<ip>@<model>` to `kv@<ip>:<port>@<model>` to be consistent with llmd-router
- Prevent silent token/request drops from full or oversized channels, return HTTP code 429
- Random mode now checks only that the prompt leaves room for one response token: `max_tokens` is no longer part of context-window validation, and is clamped instead if it would overflow the window


### Next community release (planned)

**Release candidates / trains in flight**
- [v1.2.0-rc.2](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.2.0-rc.2) (2026-11-10)- [v1.2.0-rc1](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.2.0-rc1) (2026-11-10)  - Fixed tool call streaming to send id and type only in the initial delta.
  - Emit a `cache_threshold` finish chunk for every streamed choice
  - Reject a KV cache size of 0 when the KV cache is enabled
  - Fixes in `mm_payload` support in `.../render`, in `--mm-encoder-only` mode, `ec_transfer_params` is keyed by each part's uuid
  - Allow "caf" in typos config to fix false positive in unicode tests by @mayabar in https://github.com/llm-d/llm-d-inference-sim/pull/861
  - Emit a cache_threshold finish chunk for every streamed choice by @Yaomeng1749 in https://github.com/llm-d/llm-d-inference-sim/pull/835
- [v1.1.0-rc.1](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.1.0-rc.1) (2026-11-03)  - Accept the **model** as a positional command line argument
  - Add support for `min_tokens` in `/v1/chat/completions`
  - Generate JSON content when `response_format` is set to`json_object` or `json_schema` in `/v1/chat/completions`
  - Add output message ID in non-streaming `/v1/responses`
  - Add vLLM endpoints `/v1/systemone` and `/v1/decisions`
  - Honor `min_token` on /v1/completions

**Milestones, roadmaps & open RFCs feeding the next drop**
- [Future](https://github.com/llm-d/llm-d-inference-sim/milestone/5) _(milestone · due TBD · 10/12 issues closed · 2 open PRs)_- [Release v1.1](https://github.com/llm-d/llm-d-inference-sim/milestone/14) _(milestone · due TBD · 1/1 issues closed · 0 open PRs)_- [Release v1.0.1](https://github.com/llm-d/llm-d-inference-sim/milestone/13) _(milestone · due 2026-11-01 · 5/5 issues closed · 0 open PRs)_
## llm-d/llm-d-kv-cache (watch)

Release page: [https://github.com/llm-d/llm-d-kv-cache/releases](https://github.com/llm-d/llm-d-kv-cache/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v1.0.0) — 2026-10-16
- feat(kvevents): reference-count duplicate KV-event removals by @Change72 in https://github.com/llm-d/llm-d-kv-cache/pull/680

#### [v0.9.0](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.9.0) — 2026-06-14
- fs_backend: pin vllm image to cu129 and link simple index by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/584
- fs_backend: migrate kv_offload API to vllm 0.21.0 by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/588
- fs_backend: collapse FileMapper path + add config.json audit by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/585
- feat: Emit storage KV events from the fs backend by @albertoperdomo2 in https://github.com/llm-d/llm-d-kv-cache/pull/571
- Support multiple gpu blocks in a single object store block by @effi-ofer in https://github.com/llm-d/llm-d-kv-cache/pull/558
- fs_backend: strip group_idx before publishing storage event hash by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/604
- fs_backend: add get_offload_block_hash to storage_events test stub by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/613
- feat(kvevents): parse HMA KV event metadata by @sagearc in https://github.com/llm-d/llm-d-kv-cache/pull/612
- feat: Add PVC evictor BlockRemoved events by @albertoperdomo2 in https://github.com/llm-d/llm-d-kv-cache/pull/605
- fs_backend: migrate kv_offload API to vllm 0.22.0 by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/628
- feat: batch KV block copies via cudaMemcpyBatchAsync in fs connector by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/607
- feat(kvblock): trace index add and evict by @larainema in https://github.com/llm-d/llm-d-kv-cache/pull/637
- feat(evictor): implement background empty directory cleanup process by @miroslavln in https://github.com/llm-d/llm-d-kv-cache/pull/619
- feat(kvevents): Track HMA group identity in kv cache index by @sagearc in https://github.com/llm-d/llm-d-kv-cache/pull/627
- feat: Add HMA support to FS connector by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/476

#### [v0.8.1](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.8.1) — 2026-05-25
- _No feature bullets extracted — see [full notes](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.8.1)._

#### [v0.8.0-fs-v0.20](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.8.0-fs-v0.20) — 2026-05-13
- handle full staging pool by @effi-ofer in https://github.com/llm-d/llm-d-kv-cache/pull/560
- Replace BlockSize with BlockSizeTokens by @roytman in https://github.com/llm-d/llm-d-kv-cache/pull/564
- update: remove VLLM_VERSION from makefile by @zdtsw in https://github.com/llm-d/llm-d-kv-cache/pull/556
- correct make target check-buildah to check-builder by @DhritiShikhar in https://github.com/llm-d/llm-d-kv-cache/pull/580
- update: add make target to python lint + fix lint by @zdtsw in https://github.com/llm-d/llm-d-kv-cache/pull/536
- fs_backend: migrate kv_offload API to vllm 0.20.2 by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/582

#### [v0.8.0](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.8.0) — 2026-05-01
- feat(ci): Add nightly race detector CI job by @gyliu513 in https://github.com/llm-d/llm-d-kv-cache/pull/479
- Add dockerfile for fsconnector dev on k8s by @saikat-royc in https://github.com/llm-d/llm-d-kv-cache/pull/468
- enable toolcalling from renderer by @Gregory-Pereira in https://github.com/llm-d/llm-d-kv-cache/pull/507
- update: triv-action SHA1 by @zdtsw in https://github.com/llm-d/llm-d-kv-cache/pull/494
- feat: Heterogeneous BlockSize support by @albertoperdomo2 in https://github.com/llm-d/llm-d-kv-cache/pull/511
- revamp docs by @vMaroon in https://github.com/llm-d/llm-d-kv-cache/pull/528
- feat: Add golden test case for multi-modal by @gyliu513 in https://github.com/llm-d/llm-d-kv-cache/pull/485
- feat(fs_backend): add performance and stress tests by @kfirtoledo in https://github.com/llm-d/llm-d-kv-cache/pull/527
- [1/3] deprecating internal tokenization on the lookup path by @vMaroon in https://github.com/llm-d/llm-d-kv-cache/pull/543
- Add object store support to llm-d storage offloading by @effi-ofer in https://github.com/llm-d/llm-d-kv-cache/pull/499
- documentation by @effi-ofer in https://github.com/llm-d/llm-d-kv-cache/pull/555

#### [v0.7.1](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.7.1) — 2026-04-02
- _No feature bullets extracted — see [full notes](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.7.1)._


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [llm-d v0.6.0](https://github.com/llm-d/llm-d-kv-cache/milestone/4) _(milestone · due TBD · 17/17 issues closed · 0 open PRs)_- [v0.9.0](https://github.com/llm-d/llm-d-kv-cache/milestone/5) _(milestone · due TBD · 3/4 issues closed · 0 open PRs)_- [v0.10](https://github.com/llm-d/llm-d-kv-cache/milestone/6) _(milestone · due TBD · 3/3 issues closed · 0 open PRs)_ — roadmap for v0.10: 
- add support for p2p sharing  
- multi tier throttling (stretch) 
- Move GDS support from llm-d to vllm
- kvevents for secondary tier

vllm: 
- TP agnostic in CPU (currently in cross layer layout only) 
- Add kvcache...
## llm-d/llm-d-latency-predictor (watch)

Release page: [https://github.com/llm-d/llm-d-latency-predictor/releases](https://github.com/llm-d/llm-d-latency-predictor/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-latency-predictor/releases/tag/v1.0.0) — 2026-10-13
- [bugfix] remove leftover testing CI datestamp file by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/70

#### [v0.9.0](https://github.com/llm-d/llm-d-latency-predictor/releases/tag/v0.9.0) — 2026-08-11
- Omni-modality support
- restructuring source directories by component by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/16
- feat: add model export endpoint for seed-based cold start reduction by @madhugoutham in https://github.com/llm-d/llm-d-latency-predictor/pull/34
- update the build-image to be re-usable and call from ci-pr-checks and ci-release by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/54
- swap to cncf runners and fix gha caching issue by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/65
- issues with cncf infra, reverting by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/66
- caching was not a size issue, but a permission issue by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/67
- Add encoder_matched_size and encoder_input_size features for TTFT by @kaushikmitr in https://github.com/llm-d/llm-d-latency-predictor/pull/59
- functional tests initial CI implementation by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/63
- triggering image builds and functional tests by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/68
- triggering image builds and functional tests again by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/69
- Encoder features default on by @kaushikmitr in https://github.com/llm-d/llm-d-latency-predictor/pull/73
- Add BenjaminBraunDev to OWNERS by @BenjaminBraunDev in https://github.com/llm-d/llm-d-latency-predictor/pull/74
- Treat LightGBM/XGBoost as optional deps by catching OSError on import by @modassarrana89-new in https://github.com/llm-d/llm-d-latency-predictor/pull/53
- Fixed Segmentation fault on DataFrame Construction by @modassarrana89-new in https://github.com/llm-d/llm-d-latency-predictor/pull/58

#### [v0.8.0](https://github.com/llm-d/llm-d-latency-predictor/releases/tag/v0.8.0) — 2026-06-23
- Initial setup: rename template placeholders and set ownership by @clubanderson in https://github.com/llm-d/llm-d-latency-predictor/pull/7
- Add python latency predictor by @kaushikmitr in https://github.com/llm-d/llm-d-latency-predictor/pull/8
- Add kaushikmitr to OWNERS by @kaushikmitr in https://github.com/llm-d/llm-d-latency-predictor/pull/18
- permissable linux file permissions for OCP restricted v2 SCC by @Gregory-Pereira in https://github.com/llm-d/llm-d-latency-predictor/pull/24


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [CI/CD Testing Automation](https://github.com/llm-d/llm-d-latency-predictor/milestone/1) _(milestone · due 2026-08-01 · 0/0 issues closed · 0 open PRs)_ — **Due date:** _(target: next release, v0.9.0 — set date when scheduled)_

**Description:**

Target: next release (v0.9.0). Stand up real CI gates beyond lint + dry container build.

Today a PR only gates on `ruff` and a no-push Dockerfil...- [Multimodal Request Support](https://github.com/llm-d/llm-d-latency-predictor/milestone/2) _(milestone · due 2026-08-01 · 0/0 issues closed · 0 open PRs)_ — **Target** next release (v0.9.0).
**Description:**
Extend latency prediction to multimodal requests (image and video inputs), where prefill cost is driven by more than text token count.

Today the predictor's features assume text-only re...
## llm-d/llm-d-pd-utils (watch)

Release page: [https://github.com/llm-d/llm-d-pd-utils/releases](https://github.com/llm-d/llm-d-pd-utils/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-pd-utils/releases/tag/v1.0.0) — 2026-10-20
- Free disk space before image building by @aslom in https://github.com/llm-d/llm-d-pd-utils/pull/4
- link checker - fails PR if links are broken by @clubanderson in https://github.com/llm-d/llm-d-pd-utils/pull/5
- 🌱 Remove per-repo gh-aw typo/link/upstream workflows by @clubanderson in https://github.com/llm-d/llm-d-pd-utils/pull/27
- Add network performance testing and GPU topology discovery for llm-d inference pods by @aslom in https://github.com/llm-d/llm-d-pd-utils/pull/31
- Delete docs/upstream-versions.md by @praveingk in https://github.com/llm-d/llm-d-pd-utils/pull/32
- Added docs and updated README, minor fixes, added script to install NIXL non root by @aslom in https://github.com/llm-d/llm-d-pd-utils/pull/34


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-prism (watch)

Release page: [https://github.com/llm-d/llm-d-prism/releases](https://github.com/llm-d/llm-d-prism/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-prism/releases/tag/v1.0.0) — 2026-10-16
- Separate serving stack from benchmark harness by @diamondburned in https://github.com/llm-d/llm-d-prism/pull/158
- Group BRV0.2 stages by run.eid by @diamondburned in https://github.com/llm-d/llm-d-prism/pull/159
- Feat/timeseries by @ruocco in https://github.com/llm-d/llm-d-prism/pull/151
- Filter benchmark runs by tag by @ruocco in https://github.com/llm-d/llm-d-prism/pull/160
- Compare session and request counts across runs by @ruocco in https://github.com/llm-d/llm-d-prism/pull/164
- Surface stage request errors and group messages by @diamondburned in https://github.com/llm-d/llm-d-prism/pull/168
- Add benchmark withdrawal and split review routes by @diamondburned in https://github.com/llm-d/llm-d-prism/pull/169

#### [v0.1](https://github.com/llm-d/llm-d-prism/releases/tag/v0.1) — 2026-09-10
- _No feature bullets extracted — see [full notes](https://github.com/llm-d/llm-d-prism/releases/tag/v0.1)._


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [Milestone 2: Tiered Prefix Offloading well-lit path in prism](https://github.com/llm-d/llm-d-prism/milestone/2) _(milestone · due 2026-05-22 · 1/1 issues closed · 0 open PRs)_
## llm-d/llm-d-router (watch)

Release page: [https://github.com/llm-d/llm-d-router/releases](https://github.com/llm-d/llm-d-router/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-router/releases/tag/v1.0.0) — 2026-10-16
- **API & Plugin Stability (v1):** `EPPConfig` and `InferenceObjective` graduate to `llm-d.ai/v1`, with `InferenceObjective` supporting multi-pool targeting ([#2923](https://github.com/llm-d/llm-d-router/pull/2923), [#2925](https://github.com/llm-d/llm-d-router/pull/2925), [#3206](https://github.com/llm-d/llm-d-router/pull/3206)). Core EPP plugins are promoted to stable and the stable plugin configuration surface is frozen ([#3160](https://github.com/llm-d/llm-d-router/pull/3160), [#2384](https://github.com/llm-d/llm-d-router/pull/2384)). `priority-holdback-policy` promotes to beta with explicit domain configuration ([#3284](https://github.com/llm-d/llm-d-router/pull/3284), [#2026](https://github.com/llm-d/llm-d-router/pull/2026)).
- **Scheduling, Session Affinity & KV Cache:** New `session-state-producer`, `thunder-agent` session manager, scorer, and per-pod admission gate keep multi-turn agent sessions on the pod holding their KV state ([#2531](https://github.com/llm-d/llm-d-router/pull/2531), [#2968](https://github.com/llm-d/llm-d-router/pull/2968), [#3052](https://github.com/llm-d/llm-d-router/pull/3052), [#3076](https://github.com/llm-d/llm-d-router/pull/3076)). New `endpoint-pin-screener` pins a request to a single endpoint ([#3145](https://github.com/llm-d/llm-d-router/pull/3145)), and `p2p-cost-scorer` scores P2P transfer cost ([#3008](https://github.com/llm-d/llm-d-router/pull/3008)). Selective KV transfer policy ([#2833](https://github.com/llm-d/llm-d-router/pull/2833)), vLLM KV-event snapshot warming on connect ([#2946](https://github.com/llm-d/llm-d-router/pull/2946), [#3401](https://github.com/llm-d/llm-d-router/pull/3401)), SGLang `cache_salt` support ([#3219](https://github.com/llm-d/llm-d-router/pull/3219)), default `0.6` prefix-scoring weight for the `storage` disk-offload tier ([#3463](https://github.com/llm-d/llm-d-router/pull/3463)), Redis `CrossReplicaSyncer` and pod-watch peer discovery ([#2837](https://github.com/llm-d/llm-d-router/pull/2837), [#2501](https://github.com/llm-d/llm-d-router/pull/2501)), and galloping-search and batched-lock KV block indexing ([#3241](https://github.com/llm-d/llm-d-router/pull/3241), [#3243](https://github.com/llm-d/llm-d-router/pull/3243), [#3286](https://github.com/llm-d/llm-d-router/pull/3286), [#3288](https://github.com/llm-d/llm-d-router/pull/3288), [#3318](https://github.com/llm-d/llm-d-router/pull/3318)).
- **Coordinator, Disaggregated P/D & Sidecar:** The coordinator adds pipeline support for `/v1/responses` ([#3130](https://github.com/llm-d/llm-d-router/pull/3130)) and `/v1/messages` ([#3296](https://github.com/llm-d/llm-d-router/pull/3296)), topology-aware P/D routing ([#2319](https://github.com/llm-d/llm-d-router/pull/2319)), and audio/video media disaggregation alongside images ([#2659](https://github.com/llm-d/llm-d-router/pull/2659)). The sidecar proxy adds `/v1/responses` support ([#2987](https://github.com/llm-d/llm-d-router/pull/2987)), exposes SGLang `/generate` ([#2525](https://github.com/llm-d/llm-d-router/pull/2525)), and serves Prometheus `/metrics` ([#1677](https://github.com/llm-d/llm-d-router/pull/1677)).
- **API Coverage, Multimodal & Tokenization:** EPP serves an aggregated `/v1/models` endpoint ([#2308](https://github.com/llm-d/llm-d-router/pull/2308)), tokenizes `/v1/responses` via chat-completions render ([#2963](https://github.com/llm-d/llm-d-router/pull/2963)), supports audio content blocks and audio token footprint estimation ([#2823](https://github.com/llm-d/llm-d-router/pull/2823), [#2886](https://github.com/llm-d/llm-d-router/pull/2886)), adds `vllm.omitMMKwargs` to drop multimodal tensors from render responses ([#3273](https://github.com/llm-d/llm-d-router/pull/3273)), and supports SGLang `/generate` text prompts and experimental rendering ([#3262](https://github.com/llm-d/llm-d-router/pull/3262), [#3397](https://github.com/llm-d/llm-d-router/pull/3397)).
- **High Availability, Autoscaling & Helm:** Horizontal Pod Autoscaler support for EPP and standalone proxy service ([#3133](https://github.com/llm-d/llm-d-router/pull/3133), [#3216](https://github.com/llm-d/llm-d-router/pull/3216)), active-active EPP load sharing in Helm charts ([#3431](https://github.com/llm-d/llm-d-router/pull/3431)), standalone fail-open routing when EPP is unreachable ([#3433](https://github.com/llm-d/llm-d-router/pull/3433)), EPP leader-election lease flags with graceful drain on lease loss and SIGTERM ([#3064](https://github.com/llm-d/llm-d-router/pull/3064), [#3311](https://github.com/llm-d/llm-d-router/pull/3311)), service mode for the latency predictor ([#3339](https://github.com/llm-d/llm-d-router/pull/3339)), and pod/container `securityContext` values ([#2998](https://github.com/llm-d/llm-d-router/pull/2998)).
- **Observability:** End-to-end W3C trace propagation in EPP ([#2702](https://github.com/llm-d/llm-d-router/pull/2702)), OpenTelemetry tracing in the coordinator ([#2975](https://github.com/llm-d/llm-d-router/pull/2975)), Prometheus trace exemplars on EPP latency histograms and flow-control queue duration ([#2774](https://github.com/llm-d/llm-d-router/pull/2774), [#3350](https://github.com/llm-d/llm-d-router/pull/3350), [#3420](https://github.com/llm-d/llm-d-router/pull/3420)), multimodal prefix-cache prediction metrics and span attributes ([#3171](https://github.com/llm-d/llm-d-router/pull/3171), [#3164](https://github.com/llm-d/llm-d-router/pull/3164), [#3272](https://github.com/llm-d/llm-d-router/pull/3272)), and tool-calling telemetry ([#1949](https://github.com/llm-d/llm-d-router/pull/1949)).
- **Gateway API Inference Extension v1.6.2 & Pool Group Removal:** Bumps Gateway API / GAIE to `v1.6.2` and removes support for the legacy `inference.networking.x-k8s.io` pool group ([#3086](https://github.com/llm-d/llm-d-router/pull/3086), [#3195](https://github.com/llm-d/llm-d-router/pull/3195)). Use `inference.networking.k8s.io`.
- **API Graduations (`v1`):** `EPPConfig` and `InferenceObjective` serve `llm-d.ai/v1`; `InferenceObjective` `v1alpha2` is deprecated ([#2923](https://github.com/llm-d/llm-d-router/pull/2923), [#3206](https://github.com/llm-d/llm-d-router/pull/3206)).
- **Removed Plugins, Flags & Metrics:**
- feat(epp): complete W3C trace propagation for OpenTelemetry export by @dayakar349 in https://github.com/llm-d/llm-d-router/pull/2702
- feat(sidecar): expose sglang `/generate` in sidecar proxy and coordinator by @sagearc in https://github.com/llm-d/llm-d-router/pull/2525
- feat(apix): graduate EPPConfig API to v1 by @zdtsw in https://github.com/llm-d/llm-d-router/pull/2923
- feat: add deployment config and guide for multimodal EPP direct routing by @DeanKelly751 in https://github.com/llm-d/llm-d-router/pull/2694
- Add audio content block support to tokenizer for multimodal routing by @RishabhSaini in https://github.com/llm-d/llm-d-router/pull/2823
- Add tool_choice, continue_final_message and max_output_tokens signals to outlen-bucket classifier by @DolevAdas in https://github.com/llm-d/llm-d-router/pull/2727

#### [v0.11.0](https://github.com/llm-d/llm-d-router/releases/tag/v0.11.0) — 2026-09-27
- **Flow control for P/D:** Saturation gating is stage-aware. Prefill and decode are measured separately and admission gates on the busier stage ([#2221](https://github.com/llm-d/llm-d-router/pull/2221)). The beta `max-saturation-detector` combines several detectors and gates on the highest one, and each child can be limited to prefill or decode ([#2827](https://github.com/llm-d/llm-d-router/pull/2827), [#2926](https://github.com/llm-d/llm-d-router/pull/2926)). Queue TTLs can be set per priority band, clients can ask for a shorter one with `x-llm-d-inference-ttl`, and `noEndpointRequestTTL` bounds the wait while the pool is empty ([#2649](https://github.com/llm-d/llm-d-router/pull/2649), [#2284](https://github.com/llm-d/llm-d-router/pull/2284)). New capacity utilization gauges and an `x-llm-d-flow-queue-duration-ms` response header ([#2184](https://github.com/llm-d/llm-d-router/pull/2184), [#2490](https://github.com/llm-d/llm-d-router/pull/2490)).
- **Scheduling and routing:** The new `latency-observation-scorer` ranks endpoints by TTFT measured from real responses ([#2371](https://github.com/llm-d/llm-d-router/pull/2371)). In P/D, load is split by role: input tokens count against prefill and estimated output tokens against decode ([#2396](https://github.com/llm-d/llm-d-router/pull/2396)). The `context-length-aware` scorer can route cached follow-ups by the prefill work that remains ([#2559](https://github.com/llm-d/llm-d-router/pull/2559)). Endpoints tied for the top score take turns instead of one pod getting the whole burst ([#2515](https://github.com/llm-d/llm-d-router/pull/2515), [#2709](https://github.com/llm-d/llm-d-router/pull/2709)). New `turn-priority` fairness strategy and endpoint attribute weight scorer ([#2116](https://github.com/llm-d/llm-d-router/pull/2116), [#2204](https://github.com/llm-d/llm-d-router/pull/2204)).
- **Tokenization and render:** `token-producer` renders Anthropic Messages natively through vLLM `/v1/messages/render`, and falls back to the old conversion when the endpoint is missing ([#2707](https://github.com/llm-d/llm-d-router/pull/2707)). It can balance render calls across discovered endpoints ([#2701](https://github.com/llm-d/llm-d-router/pull/2701)), and supports HTTPS, mTLS and render endpoints started with `--api-key` ([#2664](https://github.com/llm-d/llm-d-router/pull/2664), [#2678](https://github.com/llm-d/llm-d-router/pull/2678), [#2763](https://github.com/llm-d/llm-d-router/pull/2763)). Opt-in xxhash block hashing makes precise prefix hashing about 8x cheaper ([#2237](https://github.com/llm-d/llm-d-router/pull/2237)).
- **API coverage:** SGLang `/generate` ([#2391](https://github.com/llm-d/llm-d-router/pull/2391)), OpenAI text-to-speech ([#2484](https://github.com/llm-d/llm-d-router/pull/2484)), `/v1/images/edits` ([#2562](https://github.com/llm-d/llm-d-router/pull/2562)), and pre-tokenized batch prompts on `/v1/completions` ([#2523](https://github.com/llm-d/llm-d-router/pull/2523)). Paths no parser claims are forwarded to the model server by default through `passthrough-parser` ([#2507](https://github.com/llm-d/llm-d-router/pull/2507)). ATOM is a built-in engine type ([#2476](https://github.com/llm-d/llm-d-router/pull/2476)).
- **Coordinator and DisaggregatedSet:** The coordinator exposes Prometheus metrics, optionally over HTTPS, forwards unregistered paths such as `/v1/models` to a decode pod, and adds an optional async-broker step ([#2435](https://github.com/llm-d/llm-d-router/pull/2435), [#2752](https://github.com/llm-d/llm-d-router/pull/2752), [#2357](https://github.com/llm-d/llm-d-router/pull/2357), [#2325](https://github.com/llm-d/llm-d-router/pull/2325)). EPP replicas agree on DisaggregatedSet revision decisions, and the coordinator keeps the same decision across encode, prefill and decode ([#2570](https://github.com/llm-d/llm-d-router/pull/2570), [#2571](https://github.com/llm-d/llm-d-router/pull/2571), [#2572](https://github.com/llm-d/llm-d-router/pull/2572), [#2576](https://github.com/llm-d/llm-d-router/pull/2576)).
- **Operations:** A `--feature-gates` flag enables gates without restating the whole config ([#2388](https://github.com/llm-d/llm-d-router/pull/2388)). Helm adds Envoy priority routing for EPP failover in standalone mode, `router.epp.deploymentStrategy`, structured `router.epp.pluginsConfig` and `router.imagePullSecrets`, and restarts the EPP pod when its ConfigMaps change ([#2228](https://github.com/llm-d/llm-d-router/pull/2228), [#2603](https://github.com/llm-d/llm-d-router/pull/2603), [#2620](https://github.com/llm-d/llm-d-router/pull/2620), [#2766](https://github.com/llm-d/llm-d-router/pull/2766), [#2460](https://github.com/llm-d/llm-d-router/pull/2460)).
- **Observability:** Logs carry `trace_id` and `span_id`. New spans cover tokenization and the KV-event pipeline, and trace context is read from ext_proc gRPC metadata so traces connect end to end ([#2271](https://github.com/llm-d/llm-d-router/pull/2271), [#2272](https://github.com/llm-d/llm-d-router/pull/2272), [#2830](https://github.com/llm-d/llm-d-router/pull/2830)). Spans carry `service.name` and the pod resource attributes ([#2298](https://github.com/llm-d/llm-d-router/pull/2298)).
- **Fixes:** `golang.org/x/crypto` v0.55.0 for CVE-2026-56854 ([#2739](https://github.com/llm-d/llm-d-router/pull/2739)). Stale precise prefix-cache state after endpoints are removed ([#2824](https://github.com/llm-d/llm-d-router/pull/2824)). The PD Multi Tier decode leg starting before prefill stored its KV ([#2451](https://github.com/llm-d/llm-d-router/pull/2451)). `min_tokens` breaking the prefill leg ([#2593](https://github.com/llm-d/llm-d-router/pull/2593)). MoRI-IO concurrent dispatch ([#2816](https://github.com/llm-d/llm-d-router/pull/2816)). Published standalone charts pointing agentgateway at a missing image tag ([#2732](https://github.com/llm-d/llm-d-router/pull/2732)).
- **Precise prefix cache:** LoRA requests keep `BlockStored` extra keys aligned with request-side keys, restoring precise cache matches ([#2929](https://github.com/llm-d/llm-d-router/pull/2929)).
- **Removed config:** The top-level `saturationDetector` and `parser` fields, use `flowControl.saturationDetector` and `requestHandler.parsers` ([#2838](https://github.com/llm-d/llm-d-router/pull/2838)). The UDS tokenizer: `udsTokenizerConfig` and `indexerConfig.tokenizersPoolConfig` are rejected, set `vllm.url` on `token-producer` instead ([#2512](https://github.com/llm-d/llm-d-router/pull/2512)). `lasDecayFactor` on `program-aware-fairness`, decay uses `lasHalfLifeSeconds` only ([#2120](https://github.com/llm-d/llm-d-router/pull/2120)).
- **Pod label:** `llm-d.ai/role: both` no longer matches. Use `prefill-decode` ([#2509](https://github.com/llm-d/llm-d-router/pull/2509)).
- **Removed metrics:** The legacy `inference_extension_*`, `llm_d_inference_scheduler_*`, core request and inference-pool, and `inference_objective` predicted-latency families. Use the `llm_d_epp_*` series. Three `inference_extension_*` series stay for the workload-variant autoscaler ([#2826](https://github.com/llm-d/llm-d-router/pull/2826), [#2675](https://github.com/llm-d/llm-d-router/pull/2675), [#2821](https://github.com/llm-d/llm-d-router/pull/2821), [#2509](https://github.com/llm-d/llm-d-router/pull/2509)).
- **Coordinator TLS on by default:** The inference listener serves HTTPS. Use https, or set `--secure-coordinator=false` to keep plaintext ([#2805](https://github.com/llm-d/llm-d-router/pull/2805)).
- **JSON logs:** Field names follow OpenTelemetry. Collectors that match on `msg` need to match `body` ([#2643](https://github.com/llm-d/llm-d-router/pull/2643)).
- **Endpoint attribute plugins:** `endpoint-attribute-filter` and `endpoint-attribute-scorer` take a separate `producer` parameter, and the combined `Name/Producer` form is rejected. Out-of-tree plugins that use `AttributeMap` need updating ([#2190](https://github.com/llm-d/llm-d-router/pull/2190)).

#### [v0.10.0](https://github.com/llm-d/llm-d-router/releases/tag/v0.10.0) — 2026-08-17
- **Disaggregated prefill and decode:** RDMA-free KV transfer through the new `offloading` KV connector on the sidecar, now with data-parallel support and a configurable P2P tier port ([#1888](https://github.com/llm-d/llm-d-router/pull/1888), [#2075](https://github.com/llm-d/llm-d-router/pull/2075), [#1937](https://github.com/llm-d/llm-d-router/pull/1937)). Native DisaggregatedSet revision routing for consistent rolling P/D updates ([#2141](https://github.com/llm-d/llm-d-router/pull/2141)). Load-proportional and CPU-tier-aware pull-source selection to avoid transfer hot spots ([#2032](https://github.com/llm-d/llm-d-router/pull/2032), [#2321](https://github.com/llm-d/llm-d-router/pull/2321)).
- **Scheduling and routing:** GPU utilization-aware routing via the DCGM extractor and the generic endpoint-attribute filter and scorer ([#1904](https://github.com/llm-d/llm-d-router/pull/1904)). The `header-profile-handler` selects one scheduling profile per request from a header ([#2176](https://github.com/llm-d/llm-d-router/pull/2176)). The `utilization-filter` (formerly active-request-filter) caps endpoints on any combination of active, running, waiting, and KV-cache utilization ([#2218](https://github.com/llm-d/llm-d-router/pull/2218)). New priority-aware stepped gating and soft-reflective-ceiling policies ([#1592](https://github.com/llm-d/llm-d-router/pull/1592), [#1956](https://github.com/llm-d/llm-d-router/pull/1956)), and a new `session_id` session-affinity strategy ([#2238](https://github.com/llm-d/llm-d-router/pull/2238)).
- **Multimodal:** OpenAI `/v1/images/generations` routing for diffusion backends such as vLLM-Omni ([#1936](https://github.com/llm-d/llm-d-router/pull/1936)), and video input in approximate prefix match ([#1911](https://github.com/llm-d/llm-d-router/pull/1911)).
- **Observability and security:** OpenTelemetry spans over the scoring path and end-to-end P/D trace propagation ([#1834](https://github.com/llm-d/llm-d-router/pull/1834), [#1667](https://github.com/llm-d/llm-d-router/pull/1667)). mTLS for the EPP metrics endpoint and scrape sources, plus configurable ext_proc TLS minimum version and cipher suites ([#1919](https://github.com/llm-d/llm-d-router/pull/1919), [#1858](https://github.com/llm-d/llm-d-router/pull/1858), [#2230](https://github.com/llm-d/llm-d-router/pull/2230)). Bounded metric cardinality for model-name and fairness-id labels ([#1909](https://github.com/llm-d/llm-d-router/pull/1909), [#2119](https://github.com/llm-d/llm-d-router/pull/2119)).
- **Coordinator and availability:** the Coordinator serves `/inference/v1/generate` ([#2077](https://github.com/llm-d/llm-d-router/pull/2077)). Non-leader EPP replicas keep their datastore populated so a request reaching a standby routes instead of returning 503, and `--drain-timeout` adds graceful shutdown ([#1884](https://github.com/llm-d/llm-d-router/pull/1884), [#1885](https://github.com/llm-d/llm-d-router/pull/1885)). Plugin stability levels gate alpha plugins behind `--allow-experimental-plugins` ([#2073](https://github.com/llm-d/llm-d-router/pull/2073)). KV-event replay is bounded and resumable across a dropped response ([#2410](https://github.com/llm-d/llm-d-router/pull/2410)).
- **Action required, out-of-tree UsageLimitPolicy plugins:** `ComputeLimit` now fills a framework-provided ceilings buffer instead of returning a slice ([#2171](https://github.com/llm-d/llm-d-router/pull/2171)).
- **Flow control bounded by default:** `defaultRequestTTL` defaults to 60s and per-band `maxRequests` to 5000. Scale-to-zero deployments should raise `defaultRequestTTL` above their cold-start time ([#2123](https://github.com/llm-d/llm-d-router/pull/2123)). Rejection codes now distinguish an empty pool (503) from retryable backpressure (429) ([#1751](https://github.com/llm-d/llm-d-router/pull/1751), [#2047](https://github.com/llm-d/llm-d-router/pull/2047)).
- **Config renames:** the flow-control queue `MaxMinHeap` is now `PriorityQueue`, and the QueueCapability system and FCFS ListQueue are removed ([#1690](https://github.com/llm-d/llm-d-router/pull/1690), [#1831](https://github.com/llm-d/llm-d-router/pull/1831)). The active-request-filter plugin is now `utilization-filter` ([#2218](https://github.com/llm-d/llm-d-router/pull/2218)).
- **Removed flags:** pd-sidecar flags deprecated since v0.7.0 are removed; use `--kv-connector`, `--enable-tls`, and `--tls-insecure-skip-verify` ([#2054](https://github.com/llm-d/llm-d-router/pull/2054)). `--vllm-port` is deprecated in favor of `--model-server-port` ([#2142](https://github.com/llm-d/llm-d-router/pull/2142)). The deprecated data-layer feature gate is removed ([#1728](https://github.com/llm-d/llm-d-router/pull/1728)).
- **Metric renames:** EPP KV metrics move to the `llm_d_router_epp` subsystem, with the former `kvcache_*` names kept as deprecated aliases. Update dashboards and alerts ([#1886](https://github.com/llm-d/llm-d-router/pull/1886)).
- **Publishing change:** the `-dev` charts and images are no longer published. Use the base charts with `--version v0` and the `:main` image tags ([#2048](https://github.com/llm-d/llm-d-router/pull/2048)).
- Add operations.md guide for right sizing EPP container resources by @jtechapps in https://github.com/llm-d/llm-d-router/pull/1616
- feat(standalone): align agentgateway configuration with upstream GAIE PR 2905 by @abhay1999 in https://github.com/llm-d/llm-d-router/pull/1600
- feat(inflightloadproducer): allow configuring output ratio by @asharkhan3101 in https://github.com/llm-d/llm-d-router/pull/1731
- feat: Enable the disabling of feature gates that are by default on/active by @shmuelk in https://github.com/llm-d/llm-d-router/pull/1728

#### [v0.9.0](https://github.com/llm-d/llm-d-router/releases/tag/v0.9.0) — 2026-06-23
- **Performance Wins:** Drastically reduced memory allocations in `Scheduler.Schedule` by ~90% on large fleets ([PR #1171](https://github.com/llm-d/llm-d-router/pull/1171)) and optimized response usage parsing in the OpenAI parser ([PR #1583](https://github.com/llm-d/llm-d-router/pull/1583)).
- **Key Features & Additions:**
- Added an approximate prefix-cache estimation feature for the Anthropic `v1/messages` API, including tools support ([PR #1508](https://github.com/llm-d/llm-d-router/pull/1508), [PR #1554](https://github.com/llm-d/llm-d-router/pull/1554)).
- Introduced a new `FileDiscovery` plugin to handle YAML/JSON file loading and `fsnotify` file watching ([PR #1135](https://github.com/llm-d/llm-d-router/pull/1135)).
- Enabled all HTTP parsers by default in the EPP ([PR #1488](https://github.com/llm-d/llm-d-router/pull/1488)) and added native metrics mapping for standard NVIDIA Triton Inference Server workloads ([PR #1207](https://github.com/llm-d/llm-d-router/pull/1207)).
- Added stream-aware Time-to-First-Token (TTFT) and Inter-Token Latency (ITL) metrics ([PR #1499](https://github.com/llm-d/llm-d-router/pull/1499), [PR #1591](https://github.com/llm-d/llm-d-router/pull/1591)).
- **Key Bug Fixes:** Resolved a critical memory bound issue by clamping autotuned `blockSizeTokens` in the EPP indexer ([PR #1160](https://github.com/llm-d/llm-d-router/pull/1160)), fixed a ZMQ port range validation issue to prevent subscriber startup failures on multi-rank pods ([PR #1242](https://github.com/llm-d/llm-d-router/pull/1242)), and secured TLS defaults by isolating HTTP clients ([PR #1395](https://github.com/llm-d/llm-d-router/pull/1395)).
- **Configuration Changes:**
- **Metric System Changes:** The legacy metrics feature gate and `pkg/epp/backend/metrics` have been entirely removed ([PR #1418](https://github.com/llm-d/llm-d-router/pull/1418)). Subsystem metrics names have been unified and renamed to `llm_d_epp` ([PR #1661](https://github.com/llm-d/llm-d-router/pull/1661)), and all EPP span attributes are now normalized under the `llm_d.epp.*` namespace ([PR #1670](https://github.com/llm-d/llm-d-router/pull/1670)).
- **Token Producer Backend Deprecation:** Deprecated the UDS-backend in `token-producer` in favor of the newer vLLM render endpoint ([PR #1079](https://github.com/llm-d/llm-d-router/pull/1079)).
- feat(epp): allow Parser.ParseRequest to signal skip and fallback to random endpoint by @zetxqx in https://github.com/llm-d/llm-d-router/pull/882
- Add FULL_DUPLEX_STREAMED requirement by @roytman in https://github.com/llm-d/llm-d-router/pull/892
- add disk cleanup before e2e tests by @roytman in https://github.com/llm-d/llm-d-router/pull/915
- feat: Add Vertex AI parser support by @zetxqx in https://github.com/llm-d/llm-d-router/pull/884
- feat(datalayer): additive ensureDataLayer with InjectDefaults opt-out by @elevran in https://github.com/llm-d/llm-d-router/pull/941

#### [v0.8.0](https://github.com/llm-d/llm-d-router/releases/tag/v0.8.0) — 2026-04-28
- [bug] fix multimodal content dropped in prefix cache scoring and tokenizer chat rendering by @vMaroon in https://github.com/llm-d/llm-d-inference-scheduler/pull/781
- [Docs] Restructure development.md by @elevran in https://github.com/llm-d/llm-d-inference-scheduler/pull/769
- Print Pod statuses and logs if e2e tests fail by @roytman in https://github.com/llm-d/llm-d-inference-scheduler/pull/783
- Propagates relevant environment variables into test container by @roytman in https://github.com/llm-d/llm-d-inference-scheduler/pull/785
- import kvc-v0.7.1 by @vMaroon in https://github.com/llm-d/llm-d-inference-scheduler/pull/796
- Add tests for disaggregated Encoder. by @revit13 in https://github.com/llm-d/llm-d-inference-scheduler/pull/777
- (1/2) import igw v1.5.0-rc1 by @zetxqx in https://github.com/llm-d/llm-d-inference-scheduler/pull/806
- [feat] [cicd] Use distroless/static as default runtime base image by @elevran in https://github.com/llm-d/llm-d-inference-scheduler/pull/795
- Support image build with different base via Maefile and document runtime debugging by @elevran in https://github.com/llm-d/llm-d-inference-scheduler/pull/821
- [cicd] Compare coverage against `main` and latest `release-*` by @elevran in https://github.com/llm-d/llm-d-inference-scheduler/pull/757
- Script to automate migration for GAIE code into llm-d by @elevran in https://github.com/llm-d/llm-d-inference-scheduler/pull/804
- feat: Add support for Responses API by @asharkhan3101 in https://github.com/llm-d/llm-d-inference-scheduler/pull/599
- update image-build-builder rule by @roytman in https://github.com/llm-d/llm-d-inference-scheduler/pull/830
- [cicd] Add release notes action by @elevran in https://github.com/llm-d/llm-d-inference-scheduler/pull/791
- switch active-request scorer's logging from debug to trace by @vMaroon in https://github.com/llm-d/llm-d-inference-scheduler/pull/825


### Next community release (planned)

**Release candidates / trains in flight**
- [v1.0.0-rc.2](https://github.com/llm-d/llm-d-router/releases/tag/v1.0.0-rc.2) (2026-10-16)  - Give the `storage` tier (vLLM's native `OffloadingConnector` disk-offload medium) a default weight of `0.6` in prefix scoring so disk-offloaded blocks count toward prefix affinity without explicit `kvCacheBackendConfigs` ([#3463](https://github.com/llm-d/llm-d-router/pull/3463)).
- [v1.0.0-rc.1](https://github.com/llm-d/llm-d-router/releases/tag/v1.0.0-rc.1) (2026-10-15)  - **API & Plugin Stability (v1):** `EPPConfig` and `InferenceObjective` graduate to `llm-d.ai/v1`, with `InferenceObjective` supporting multi-pool targeting ([#2923](https://github.com/llm-d/llm-d-router/pull/2923), [#2925](https://github.com/llm-d/llm-d-router/pull/2925), [#3206](https://github.com/llm-d/llm-d-router/pull/3206)). Core EPP plugins are promoted to stable and the stable plugin configuration surface is frozen ([#3160](https://github.com/llm-d/llm-d-router/pull/3160), [#2384](https://github.com/llm-d/llm-d-router/pull/2384)). `priority-holdback-policy` promotes to beta with explicit domain configuration ([#3284](https://github.com/llm-d/llm-d-router/pull/3284), [#2026](https://github.com/llm-d/llm-d-router/pull/2026)).
  - **Scheduling, Session Affinity & KV Cache:** New `session-state-producer`, `thunder-agent` session manager, scorer, and per-pod admission gate keep multi-turn agent sessions on the pod holding their KV state ([#2531](https://github.com/llm-d/llm-d-router/pull/2531), [#2968](https://github.com/llm-d/llm-d-router/pull/2968), [#3052](https://github.com/llm-d/llm-d-router/pull/3052), [#3076](https://github.com/llm-d/llm-d-router/pull/3076)). New `endpoint-pin-screener` pins a request to a single endpoint ([#3145](https://github.com/llm-d/llm-d-router/pull/3145)), and `p2p-cost-scorer` scores P2P transfer cost ([#3008](https://github.com/llm-d/llm-d-router/pull/3008)). Selective KV transfer policy ([#2833](https://github.com/llm-d/llm-d-router/pull/2833)), vLLM KV-event snapshot warming on connect ([#2946](https://github.com/llm-d/llm-d-router/pull/2946), [#3401](https://github.com/llm-d/llm-d-router/pull/3401)), SGLang `cache_salt` support ([#3219](https://github.com/llm-d/llm-d-router/pull/3219)), Redis `CrossReplicaSyncer` and pod-watch peer discovery ([#2837](https://github.com/llm-d/llm-d-router/pull/2837), [#2501](https://github.com/llm-d/llm-d-router/pull/2501)), and galloping-search and batched-lock KV block indexing ([#3241](https://github.com/llm-d/llm-d-router/pull/3241), [#3243](https://github.com/llm-d/llm-d-router/pull/3243), [#3286](https://github.com/llm-d/llm-d-router/pull/3286), [#3288](https://github.com/llm-d/llm-d-router/pull/3288), [#3318](https://github.com/llm-d/llm-d-router/pull/3318)).
  - **Coordinator, Disaggregated P/D & Sidecar:** The coordinator adds pipeline support for `/v1/responses` ([#3130](https://github.com/llm-d/llm-d-router/pull/3130)) and `/v1/messages` ([#3296](https://github.com/llm-d/llm-d-router/pull/3296)), topology-aware P/D routing ([#2319](https://github.com/llm-d/llm-d-router/pull/2319)), and audio/video media disaggregation alongside images ([#2659](https://github.com/llm-d/llm-d-router/pull/2659)). The sidecar proxy adds `/v1/responses` support ([#2987](https://github.com/llm-d/llm-d-router/pull/2987)), exposes SGLang `/generate` ([#2525](https://github.com/llm-d/llm-d-router/pull/2525)), and serves Prometheus `/metrics` ([#1677](https://github.com/llm-d/llm-d-router/pull/1677)).
  - **API Coverage, Multimodal & Tokenization:** EPP serves an aggregated `/v1/models` endpoint ([#2308](https://github.com/llm-d/llm-d-router/pull/2308)), tokenizes `/v1/responses` via chat-completions render ([#2963](https://github.com/llm-d/llm-d-router/pull/2963)), supports audio content blocks and audio token footprint estimation ([#2823](https://github.com/llm-d/llm-d-router/pull/2823), [#2886](https://github.com/llm-d/llm-d-router/pull/2886)), adds `vllm.omitMMKwargs` to drop multimodal tensors from render responses ([#3273](https://github.com/llm-d/llm-d-router/pull/3273)), and supports SGLang `/generate` text prompts and experimental rendering ([#3262](https://github.com/llm-d/llm-d-router/pull/3262), [#3397](https://github.com/llm-d/llm-d-router/pull/3397)).
  - **High Availability, Autoscaling & Helm:** Horizontal Pod Autoscaler support for EPP and standalone proxy service ([#3133](https://github.com/llm-d/llm-d-router/pull/3133), [#3216](https://github.com/llm-d/llm-d-router/pull/3216)), active-active EPP load sharing in Helm charts ([#3431](https://github.com/llm-d/llm-d-router/pull/3431)), standalone fail-open routing when EPP is unreachable ([#3433](https://github.com/llm-d/llm-d-router/pull/3433)), EPP leader-election lease flags with graceful drain on lease loss and SIGTERM ([#3064](https://github.com/llm-d/llm-d-router/pull/3064), [#3311](https://github.com/llm-d/llm-d-router/pull/3311)), service mode for the latency predictor ([#3339](https://github.com/llm-d/llm-d-router/pull/3339)), and pod/container `securityContext` values ([#2998](https://github.com/llm-d/llm-d-router/pull/2998)).
  - **Observability:** End-to-end W3C trace propagation in EPP ([#2702](https://github.com/llm-d/llm-d-router/pull/2702)), OpenTelemetry tracing in the coordinator ([#2975](https://github.com/llm-d/llm-d-router/pull/2975)), Prometheus trace exemplars on EPP latency histograms and flow-control queue duration ([#2774](https://github.com/llm-d/llm-d-router/pull/2774), [#3350](https://github.com/llm-d/llm-d-router/pull/3350), [#3420](https://github.com/llm-d/llm-d-router/pull/3420)), multimodal prefix-cache prediction metrics and span attributes ([#3171](https://github.com/llm-d/llm-d-router/pull/3171), [#3164](https://github.com/llm-d/llm-d-router/pull/3164), [#3272](https://github.com/llm-d/llm-d-router/pull/3272)), and tool-calling telemetry ([#1949](https://github.com/llm-d/llm-d-router/pull/1949)).
- [v0.11.0-rc.2](https://github.com/llm-d/llm-d-router/releases/tag/v0.11.0-rc.2) (2026-09-21)  - With KV-event replay disabled, an inference engine that restarts at the same endpoint can retain stale precise prefix-cache state until eviction. Follow [#2853](https://github.com/llm-d/llm-d-router/issues/2853) and [#2854](https://github.com/llm-d/llm-d-router/pull/2854).

**Milestones, roadmaps & open RFCs feeding the next drop**
- [v1.1.0](https://github.com/llm-d/llm-d-router/milestone/12) _(milestone · due 2026-11-25 · 17/41 issues closed · 8 open PRs)_- [#3991 [Proposal] Tokenize once at ingress across vLLM and SGLang (Coordinator + EPP, EPP alone)](https://github.com/llm-d/llm-d-router/issues/3991) _(rfc · open RFC/proposal)_ — **What would you like to be added**:

A tokenize-once design for `llm-d`, written up as a proposal document in PR #3992 (`docs/tokenize-once-at-ingress.md`). This issue tracks the summary and per-m...- [#2409 [RFC]: Proactive P2P KV-Cache Migration API](https://github.com/llm-d/llm-d-router/issues/2409) _(rfc · open RFC/proposal)_ — # RFC: Proactive P2P KV-Cache Migration API

*Builds on [RFC #51639 — Generic Control RPC for KV Connectors](https://github.com/vllm-project/vllm/issues/51639).*

## Summary

Expose an orchestrator...- [#3617 [RFC] native tokens-in/tokens-out](https://github.com/llm-d/llm-d-router/issues/3617) _(rfc · open RFC/proposal)_ — ## Overview

Recent work in vLLM and SGLang separates the frontend from the engine:

<img width="2757" height="781" alt="Image" src="https://github.com/user-attachments/assets/0947ca20-47b8-47a2-81...- [#4078 [RFC] Sampled request/response capture for training-data collection for fine-tuning & RL](https://github.com/llm-d/llm-d-router/issues/4078) _(rfc · open RFC/proposal)_ — ## Overview
We want to sample a small fraction of live inference traffic at the router and export correlated **request/response pairs** to an ingest endpoint, to build a supervised fine-tuning corp...- [#2326 [RFC] llm-d-router Profiler](https://github.com/llm-d/llm-d-router/issues/2326) _(rfc · open RFC/proposal)_ — The [google doc](https://docs.google.com/document/d/1mpRJUPHt9edE79VjJphEj8zG7fkWJ702m9YgmvlQgJo/edit?resourcekey=0-j4HnDoEkLD81kpBGmNGlQw&tab=t.0) has more details.
Feel free to comment on this is...- [#3691 [RFC]: Pre/post-processing (IO) disaggregation for /pooling requests](https://github.com/llm-d/llm-d-router/issues/3691) _(rfc · open RFC/proposal)_ — <!-- markdownlint-disable -->

### Summary

We propose letting the router split vLLM `/pooling` requests that use an IO Processor plugin into three stages: pre-processing, inference and post-proces...- [#3603 [RFC] Flow Control: Per-Endpoint Band Sharing](https://github.com/llm-d/llm-d-router/issues/3603) _(rfc · open RFC/proposal)_ — <!-- Issue title: [RFC] Flow Control: Per-Endpoint Band Sharing -->

Full design document: https://docs.google.com/document/d/1GMh38sq9YJnf-bU13d2ROrV2NqxdzMddYqMpcWAcgWs/edit

## Motivation

### I...- [#3519 [RFC] Stream non-streaming requests upstream so EPP sees the first token](https://github.com/llm-d/llm-d-router/issues/3519) _(rfc · open RFC/proposal)_ — > _**See #3122 which supersedes this. Leaving issue open a bit longer for discussion purposes.**_


**What would you like to be added**:

An opt-in `requestHandler.foldUnaryToStream` setting in `En...
