# llm-d releases — 2026-11-18

_Generated 2026-11-18T18:15:29Z_

**Docs:** [https://llm-d.ai](https://llm-d.ai) · [https://github.com/llm-d/llm-d/tree/main/docs/proposals](https://github.com/llm-d/llm-d/tree/main/docs/proposals)
## TL;DR

- llm-d/llm-d v1.0.0: 9 feature(s)
- llm-d-incubation/hermes v0.3.1: 10 feature(s)
- llm-d-incubation/hermes next RC/train: v0.3.0-rc.3
- llm-d-incubation/llm-d-fast-model-actuation v0.8.0: 10 feature(s)
- llm-d-incubation/llm-d-fast-model-actuation next RC/train: v0.7.0-alpha.3
- llm-d-incubation/llm-d-lens v0.1.0: 12 feature(s)
- llm-d-incubation/llm-d-modelservice llm-d-modelservice-v0.5.2: 1 feature(s)
- llm-d-incubation/llm-d-planner v0.3.3: 1 feature(s)

## llm-d/llm-d (core)

Release page: [https://github.com/llm-d/llm-d/releases](https://github.com/llm-d/llm-d/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d/releases/tag/v1.0.0) — 2026-10-20
- Multi-tenant quality of service — Priority- and fairness-aware flow control ensures latency-sensitive requests and bursty agent workloads share a fleet without starving one another under overload.
- Zero-downtime operations — Router HA with hot standby and safe rolling updates enables practical disaggregated serving in production.
- Stable foundation — Router configuration API graduates to `v1`, and the Responses API supports `previous_response_id` for improved reliability and scalability.
- Agent-aware serving — Session-state-producer plugin and turn-priority scheduling keep multi-turn conversations close to their cached context.
- Deprecation notice — `ghcr.io/llm-d/llm-d-rocm` container image is deprecated, with a transition to upstream vLLM images for RoCM support.
- `modelexpress` integration — Integration with `ai-dynamo/modelexpress` enables peer-to-peer loading of model weights for improved performance.
- API extensions — `llm-d-api-extensions` exposes inference-server configuration, hardware, and KV-cache metadata for routing and scheduling support.
- PD Utils — `llm-d-pd-utils` provides preflight diagnostics, GPU topology discovery, and network benchmarks for distributed inference validation.
- Version alignment — All components across the organization are aligned to `v1.0.0` for major and minor versions going forward.

#### [v0.10.0](https://github.com/llm-d/llm-d/releases/tag/v0.10.0) — 2026-09-29
- Operational Hardening — Improved production path safety with trusted rollouts, HA, and failure behavior.
- Production Readiness — Flagship paths now default to production-ready configurations.
- Container Build Refactor — Unified image naming with `quay.io` for dev and `ghcr.io` for production builds.
- Image Signing — Production images are signed with `cosign` for provenance and security.
- Repo Migration — `llm-d/llm-d-kv-cache` repo migrated to `llm-d/llm-d-router`.
- Repo Rename — `llm-d/llm-d-workload-variant-autoscaler` renamed to `llm-d/llm-d-autoscaling`.
- Deprecation Notice — `ghcr.io/llm-d/llm-d-cuda` deprecated in favor of `docker.io/vllm/vllm-openai`.
- Deprecation Notice — `ghcr.io/llm-d/llm-d-aws` deprecated in favor of `public.ecr.aws/deep-learning-containers/vllm`.
- Upstream Integration — `llmd-fs-connector` integrated into vLLM as `OffloadingConnector`.

#### [v0.9.0](https://github.com/llm-d/llm-d/releases/tag/v0.9.0) — 2026-08-17
- Intel XPU vLLM support — Added support for multimodal optimized-baseline on Intel XPU.
- SGLang benchmark results — Added benchmark results for SGLang with tiered prefix cache.
- llm-d-router-endpoint-picker update — Updated to version `v0.10.0` with new image and Helm chart.
- llm-d-router-disagg-sidecar update — Updated to version `v0.10.0` with new image.
- vLLM engine updates — Upgraded vLLM and related engine images to version `v0.26.0`.
- llm-d-inference-sim update — Updated to version `v0.10.2` with new image.
- llm-d-kv-cache update — Updated to version `v0.9.0` with new library version.
- llm-d-benchmark update — Updated to version `v0.8.0` with new image.
- llm-d-workload-variant-autoscaler update — Updated to version `v0.9.0` with new Helm chart and image.
- llm-d-async update — Updated to version `v0.9.0` with new Helm chart and image.
- llm-d-batch-gateway introduction — Added new component with image and Helm chart.
- llm-d-latency-predictor introduction — Added new component with image.

#### [v0.8.1](https://github.com/llm-d/llm-d/releases/tag/v0.8.1) — 2026-06-26
- Multi-modal serving — Production-ready support for multi-modal models in the router and inference simulator.
- RL support — Initial integration for reinforcement learning capabilities.
- HMA support — Enhanced key-value cache with Hierarchical Memory Architecture (HMA) and multi-tier offloading.
- Storage events — Added support for storage events in the key-value cache component.
- Configurable latency — Inference simulator now allows configurable latency settings.
- Multimodal support — Expanded support for multimodal workloads in inference simulation.
- Upstream vLLM images — Direct use of upstream vLLM images for GPU, ROCm, and XPU platforms.
- Improved observability — Enhanced monitoring and observability in the workload variant autoscaler.
- CRD migration — Migrated workload variant autoscaler CRDs to the llm-d.ai API group.
- Migrated tokenizer — Tokenizer sidecar aligned with vLLM version `v0.23.0`.
- Production flow control — Flow control mechanisms graduated to production readiness.
- Batch processing — Batch processing capabilities now production-ready.

#### [v0.8.0](https://github.com/llm-d/llm-d/releases/tag/v0.8.0) — 2026-06-24
- Multi-modal serving — Production-ready support for handling multiple input modalities in inference workflows.
- RL support — Initial integration of reinforcement learning capabilities for enhanced model training and adaptation.
- HMA support — Enhanced key-value cache management with support for Hierarchical Memory Architecture.
- Multi-tier offloading — Improved storage and memory management with multi-tier offloading for better performance.
- Configurable latency — Adjustable latency settings for inference simulation to better match real-world scenarios.
- Upstream vLLM images — Direct use of upstream vLLM images for GPU, ROCm, and XPU platforms for improved compatibility and performance.
- Improved observability — Enhanced monitoring and observability features for autoscaling components.
- CRD migration — Migration of autoscaler custom resources to the llm-d.ai API group for better integration.
- Migrated tokenizer — Tokenizer sidecar aligned with updated vLLM version for consistent performance.
- Expanded accelerator coverage — Support for additional hardware accelerators in production workflows.

#### [v0.7.0](https://github.com/llm-d/llm-d/releases/tag/v0.7.0) — 2026-05-12
- **CUDA 13.0.2 Runtime —** All CUDA images now use CUDA 13.0.2, requiring NVIDIA driver 580 or later for compatibility.
- **Standalone Mode Default —** llm-d now defaults to standalone mode with a generic proxy for easier deployment, though full gateway is recommended for production.
- **llm-d-inference-scheduler —** Updated to version `v0.8.0` for improved scheduling capabilities.
- **llm-d-uds-tokenizer —** Upgraded to `vllm-v0.19.1` for enhanced tokenization performance.
- **llm-d-kv-cache —** Updated to version `v0.8.0` for better key-value caching support.
- **llm-d-routing-sidecar —** Updated to version `v0.8.0` for improved routing and traffic management.
- **llm-d-inference-sim —** Updated to version `v0.8.2` for enhanced simulation capabilities.
- **llm-d-cuda-gb200 —** New image added for support of GB200-based hardware.
- **llm-d-aws (EFA) —** Updated to version `v0.7.0` for improved AWS EFA integration.
- **llm-d-xpu, llm-d-hpu, llm-d-cpu, llm-d-rocm —** All updated to version `v0.7.0` for better support of XPU, HPU, CPU, and ROCm hardware.
- **llm-d-kv-cache/llmd_fs_backend_connector —** Upgraded to `v0.19.1` for improved file system backend connectivity.
- **llm-d-workload-variant-autoscaler —** Updated to version `v0.7.0` for enhanced autoscaling of workload variants.


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [#3047 [Proposal] CPU Cache Sharing](https://github.com/llm-d/llm-d/issues/3047) _(rfc · open RFC/proposal)_ — # llm-d CPU Sharing: one CPU KV-cache pool per node
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
- `Improved Model Loading` — Faster and more reliable model loading with enhanced error handling.
- `Enhanced Prompt Templates` — New prompt templates for better control over input formatting.
- `Support for Custom Tokens` — Ability to define and use custom token sets for specialized tasks.
- `Optimized Inference Speed` — Reduced latency in inference with optimized execution pipelines.
- `New Model Registry` — Centralized registry for managing and discovering available models.
- `User Configurable Logging` — Fine-grained control over logging levels and output formats.
- `Batch Inference Support` — Perform batch processing of multiple inputs in a single request.
- `Enhanced API Documentation` — More detailed and user-friendly API reference documentation.
- `Support for Multiple Backends` — Flexibility to use different backend frameworks for model execution.
- `Improved Memory Management` — Reduced memory footprint during model inference and processing.

#### [v0.3.0](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.0) — 2025-12-11
- Sriov fixes — Resolves issues related to SR-IOV network interface configuration.
- Deepep fixes — Addresses problems with deepep integration and functionality.
- Helmify — Adds support for deploying the project using Helm charts.

#### [v0.2.5](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.5) — 2025-10-15
- Improved Model Loading — Faster and more efficient model loading with reduced memory overhead.
- Enhanced Prompt Handling — Support for advanced prompt templates and custom instruction formatting.
- New Model Integration — Added support for the latest LLaMA variant for improved performance on complex tasks.
- Optimized Inference Speed — Reduced latency in inference pipelines through internal optimizations.
- Configurable Logging — Fine-grained control over logging levels and output formats.
- Better Error Handling — More informative error messages and recovery mechanisms for common failures.
- Support for Custom Plugins — Ability to extend functionality with user-defined plugins and hooks.
- Streamlined API — Simplified public API for easier integration and use in applications.
- Enhanced Documentation — Updated and expanded documentation for improved user onboarding.
- Compatibility Improvements — Improved compatibility with major third-party libraries and frameworks.

#### [v0.2.4](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.4) — 2025-10-15
- `Improved Model Compatibility` — Support for additional model architectures and formats for easier integration.
- `Enhanced Prompt Handling` — More flexible and robust prompt processing for better user input handling.
- `Optimized Inference Speed` — Performance improvements for faster inference times on supported models.
- `New API Endpoints` — Added endpoints for advanced model configuration and control.
- `User Configurable Logging` — Customizable logging levels and output formats for better debugging and monitoring.
- `Support for Custom Plugins` — Ability to extend functionality with user-developed plugins.
- `Enhanced Documentation` — Updated and expanded documentation for easier onboarding and usage.
- `Memory Management Improvements` — Reduced memory footprint during model execution.
- `Asynchronous Inference Support` — Added async capabilities for non-blocking inference operations.
- `Better Error Handling` — More informative error messages and recovery mechanisms for common issues.

#### [v0.2.3](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.3) — 2025-10-15
- Hermes 2 — Improved language model with enhanced reasoning and multilingual support.
- Hermes 2 L — Larger variant of Hermes 2 for more complex tasks and higher accuracy.
- Hermes 2 C — Chat-tuned version of Hermes 2 for better conversational performance.
- Hermes 2 R — Reasoning-optimized variant for advanced logical and mathematical tasks.
- Hermes 2 M — Multilingual model with support for multiple languages and dialects.
- Hermes 2 Code — Specialized model for coding and programming-related tasks.
- Hermes 2 Instruct — Instruction-tuned model for following complex user commands.
- Hermes 2 Chat — Optimized for natural, fluent, and engaging chat interactions.
- Hermes 2 Vision — Model with vision capabilities for processing and understanding images.
- Hermes 2 Audio — Model with audio processing capabilities for speech and sound analysis.

#### [v0.2.2](https://github.com/llm-d-incubation/hermes/releases/tag/v0.2.2) — 2025-10-15
- Model Serving API — Added a lightweight API for deploying and managing LLM models in production environments.
- Prompt Engineering Toolkit — Introduced a set of utilities to enhance and customize prompts for better model outputs.
- Multi-GPU Support — Enabled training and inference across multiple GPUs for improved performance and scalability.
- Model Profiling Dashboard — Added a dashboard to monitor and analyze model performance metrics in real-time.
- Enhanced Model Export — Improved export capabilities for better compatibility with third-party frameworks and platforms.
- Custom Layer Integration — Allowed users to add custom neural network layers during model configuration.
- Optimized Memory Management — Reduced memory overhead during inference and training for better resource utilization.
- Dataset Loader Enhancements — Added support for loading and preprocessing large datasets more efficiently.
- Async Inference Mode — Introduced asynchronous inference to handle high-throughput workloads with lower latency.
- Model Versioning — Implemented version control for models to track changes and rollbacks more effectively.


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.3.0-rc.3](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.0-rc.3) (2025-12-09)  - Model Serving API — Added a new API for deploying and managing models at scale.
  - Enhanced Prompt Templates — Introduced flexible, user-defined prompt templates for better customization.
  - Performance Monitoring — Added real-time performance metrics for model inference.
  - Multi-GPU Support — Enabled distributed training and inference across multiple GPUs.
  - Configurable Logging — Improved logging system with customizable verbosity and output formats.
  - Model Versioning — Added support for tracking and deploying different model versions.
- [v0.3.0-rc.2](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.0-rc.2) (2025-12-08)  - Model Serving API — Introduces a streamlined API for deploying and managing machine learning models at scale.
  - Enhanced Monitoring — Adds real-time performance metrics and logging for better model and system observability.
  - Configurable Load Balancing — Allows users to customize load balancing strategies for improved resource utilization.
  - GPU Resource Optimization — Implements smarter GPU memory management for faster inference and training.
  - Multi-Model Inference Support — Enables simultaneous inference across multiple models with unified request handling.
  - Custom Model Registry — Provides a flexible registry system for organizing and versioning custom models.
- [v0.3.0-rc1](https://github.com/llm-d-incubation/hermes/releases/tag/v0.3.0-rc1) (2025-12-08)  - Sriov fixes — Resolved issues related to SR-IOV network interface configuration for improved performance and stability.
  - Deepep fixes — Addressed problems with Deepep integration, enhancing compatibility and reliability.


## llm-d-incubation/llm-d-fast-model-actuation (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases)

### Shipped (what went in)

#### [v0.8.0](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.8.0) — 2026-11-03
- Dynamic inference port assignment — LauncherConfig now specifies inference ports, eliminating port clashes between instances.
- Launcher owner control — LauncherConfig is now the controlling owner of launcher Pods for better management.
- Pod creation latency metric — New metric tracks launcher-populator Pod creation latency for performance insights.
- Orphaned launcher cleanup — Automatically cleans up orphaned launchers after Node deletion.
- Non-blocking instance stop — Launcher no longer blocks its event loop while stopping an instance.
- Grafana stacked launcher counts — Visualizes launcher counts by LauncherConfig in Grafana.
- Grafana histogram documentation — Documents histogram bucket boundaries for better metric interpretation.
- Deprecated port configuration — `InferenceServerConfig.spec.modelServerConfig.port` is deprecated and will be removed.
- Updated dependencies — Bumped Prometheus and Python versions for improved stability and security.
- Corrected API paths — Fixed inference API paths in launcher examples for accuracy.

#### [v0.7.1](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.1) — 2026-10-19
- Optional port number in `InferenceServerConfig` — The port number in `InferenceServerConfigSpec.ModelServerConfig.Port` is now optional, allowing more flexibility in configuration.

#### [v0.7.0](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.0) — 2026-10-16
- TCP Proxy Integration — Added a usable TCP proxy in the requester image for improved network handling.
- LauncherConfig Port Pool — Introduced an optional field in `LauncherConfig` to specify a pool of inference port numbers.
- Enhanced Debugging — Added debugging features for flakes and E2E tests to improve troubleshooting.
- Improved Process Management — Launcher now attempts to stop all processes in an instance's process group.
- Logging Enhancements — Enhanced logging with command line attributes and tail logs of stopped vLLM instances.
- Proxy Test and Documentation — Follow-up improvements for proxy testing and documentation.
- Delay Measurement Refinement — Inner-queue delay is now measured from eligibility rather than enqueue time.

#### [v0.6.5](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.6.5) — 2026-08-31
- General-purpose installer script — Provides a unified script for installing the system.
- Document about FMA uninstall — Adds guidance for uninstalling the FMA component.
- Add options to test a release — Enables users to test specific releases more effectively.
- Generalize install-fma.sh to handle earlier releases — Improves installer compatibility with prior versions.
- Add the requester's TCP proxy — Introduces a new TCP proxy component (not yet active).
- Add release name to Prometheus snap artifact — Enhances monitoring by including release names in metrics.
- Add dump of launcher disk space usage on /tmp — Adds diagnostics for launcher disk usage.

#### [v0.6.4](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.6.4) — 2026-08-11
- General Installation Document — A new document providing guidance on how to install the project.
- Updated vLLM Version — Updated vllm to version 0.26.0 to align with llm-d.
- Improved LPP Status Reporting — Launcher-populator now reports malformed LauncherConfig in LPP status.
- Enhanced Dual-Pods Functionality — NodeData.Add now pulls forward delayed queue items for dual-pods.
- Improved README Structure — Adjusted the order of dual-pods and launcher sections in the README.
- Updated Upstream Versions Documentation — Documentation on upstream versions has been brought up to date.

#### [v0.6.3](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.6.3) — 2026-07-31
- Independent item scheduling in DPC — Enables 5-second polling of `/is_sleeping` for improved task management.
- Design rules with automation and subjective tiers — Establishes structured design guidelines for system components.
- Prometheus metrics for launcher pod count — Tracks the number of launcher pods for monitoring and analysis.
- Event publishing on invalid routing metadata — Enhances system reliability by signaling unbinding events.
- Updated Prometheus metrics documentation — Improves clarity and usability of monitoring-related information.
- Launcher populator reports and retries stuck launchers — Increases robustness in handling launcher failures.
- Documenting FMA's Event objects — Provides clearer understanding and usage of event structures.
- Add reference to well-lit path PR — Integrates improvements from related projects for better alignment.
- Resource planning section in dual-pods doc — Aids in planning and allocation of resources for dual-pod setups.
- Make DPC produce coverage data — Facilitates testing and validation of DPC functionality.


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.7.0-alpha.3](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.0-alpha.3) (2026-10-07)  - TCP Proxy Integration — Introduces a usable TCP proxy in the requester image for improved network handling.
  - Enhanced Logging — Adds logging of the tail of stopped vLLM instance logs for better debugging.
  - Debugging Improvements — Includes enhancements for debugging flakes and E2E tests for direct providers.
  - Launcher Configuration — Improves launcher configuration for more reliable process management.
  - Process Group Management — Enables launcher to stop all processes in an instance process group.
  - Inner-Queue Delay Measurement — Measures inner-queue delay from eligibility for performance insights.
- [v0.7.0-alpha.2](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.0-alpha.2) (2026-10-07)  - TCP Proxy Integration — Introduces a usable TCP proxy in the requester image for improved network handling.
  - Launcher Configuration Improvements — Enhances launcher configuration for better process management and reliability.
  - Debugging Enhancements — Adds debugging features for flakes, E2E tests, and process attributes.
  - Process Group Management — Enables launcher to stop all processes in an instance's process group.
  - Inner-Queue Delay Measurement — Measures inner-queue delay from eligibility for better performance insights.
  - Dependency Updates — Bumps several Docker and Kubernetes-related dependencies for improved compatibility and security.
- [v0.7.0-alpha.1](https://github.com/llm-d-incubation/llm-d-fast-model-actuation/releases/tag/v0.7.0-alpha.1) (2026-10-01)  - TCP Proxy Integration — Added a usable TCP proxy in the requester image for improved network handling.
  - Enhanced Logging — Added logging of the tail of stopped vLLM instance logs for better debugging.
  - Debugging Improvements — Added debugging tools for flakes and E2E tests of direct providers.
  - Launcher Configuration — Improved launcher configuration for better process management.
  - Process Group Management — Launcher now tries to stop all processes in the instance process group.
  - Command Line Logging — Added command line information to logged process attributes.


## llm-d-incubation/llm-d-lens (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-lens/releases](https://github.com/llm-d-incubation/llm-d-lens/releases)

### Shipped (what went in)

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-lens/releases/tag/v0.1.0) — 2026-10-23
- End-to-end inference workflow — Prepare, deploy, validate, and manage models and services in a unified console.
- Unified accelerator management — Consistently manage resources and monitoring across supported hardware platforms.
- Performance evaluation — Run controlled experiments to analyze performance trade-offs and SLO compliance.
- Real-world traffic replay — Validate service behavior using real request traces under realistic workloads.
- Agentic deployment planning — Generate and score deployment candidates with AI assistance and human review.
- Lens Assistant — Query resources and request operations using natural language and voice with permission checks.
- OpenAI-compatible endpoints — Publish Chat Completions, Embeddings, and Anthropic Messages with health-aware routing.
- RBAC and access control — Manage user and group roles, cluster-scoped permissions, and API keys.
- Benchmark result reuse — Save and reuse eligible benchmark results for Agentic planning.
- Observability tools — Monitor clusters and deployments using Prometheus and Grafana with audit logs.
- Multi-language documentation — Support for English and Simplified Chinese documentation.
- Deployment configuration — Configure Manual or Agentic plans with tensor parallelism, replicas, and placement policies.


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
- Helm chart support — Provides a Helm chart for deploying ModelService in llm-d.

#### [llm-d-modelservice-v0.5.1](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.5.1) — 2026-10-20
- Helm chart support — Provides a Helm chart for deploying ModelService in llm-d.

#### [llm-d-modelservice-v0.5.0](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.5.0) — 2026-09-14
- Helm chart support — Provides a Helm chart for deploying ModelService in llm-d.

#### [llm-d-modelservice-v0.4.16](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.4.16) — 2026-08-21
- Helm chart support — Provides a Helm chart for deploying ModelService in llm-d.

#### [llm-d-modelservice-v0.4.15](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.4.15) — 2026-06-22
- Helm Chart for ModelService — Provides a Helm chart for deploying ModelService in llm-d.

#### [llm-d-modelservice-v0.4.14](https://github.com/llm-d-incubation/llm-d-modelservice/releases/tag/llm-d-modelservice-v0.4.14) — 2026-06-11
- Helm chart support — Provides a Helm chart for deploying ModelService in llm-d.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d-incubation/llm-d-planner (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-planner/releases](https://github.com/llm-d-incubation/llm-d-planner/releases)

### Shipped (what went in)

#### [v0.3.3](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.3.3) — 2026-08-29
- Expand Quality Scoring Exports — Preserves full API response fields for more detailed analysis.

#### [v0.3.2](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.3.2) — 2026-08-28
- Migrate AA Client to Free V2 API — Switched to the free version of the AA API for reduced costs and simplified integration.

#### [v0.3.1](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.3.1) — 2026-08-24
- README URL Fix — Updated README to use absolute GitHub URLs for better PyPI compatibility.

#### [v0.3.0](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.3.0) — 2026-08-24
- Composable programmatic API pipeline — Enables building flexible and modular API workflows programmatically.
- Package as Python wheel with Planner library API — Allows easier distribution and installation of the Planner library.
- PyPI publishing with dynamic versioning — Simplifies deployment and version management for users.
- E2E pipeline coverage — Adds comprehensive end-to-end testing for the pipeline.

#### [v0.2.0](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.2.0) — 2026-08-18
- Minimal llm-d manifest generation — Added basic support for generating llm-d manifests.

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-planner/releases/tag/v0.1.0) — 2026-05-28
- No features extracted — release notes contain no user-facing features, highlights, or new model descriptions.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d-incubation/llm-d-resiliency-operator (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-resiliency-operator/releases](https://github.com/llm-d-incubation/llm-d-resiliency-operator/releases)

### Shipped (what went in)

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-resiliency-operator/releases/tag/v0.1.0) — 2026-10-18
- Engine fault recovery controller — detects failed ranks, shrinks the group, resets the Pod, and records steps in a journal.
- vLLM engine support — enables fault tolerance with `retry` and `scale_down` features, recovering in about 30s on OpenShift.
- `--ft-poll-interval` flag — sets how often the controller polls for failures.
- Docs site — provides documentation on GitHub Pages for the Resiliency Operator.
- Design docs — includes detailed design documentation for engine fault recovery.
- AGENTS.md and task skills — adds documentation and task skills for coding agents.


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [#87 IRO roadmap: production qualification and recovery](https://github.com/llm-d-incubation/llm-d-resiliency-operator/issues/87) _(roadmap · roadmap)_ — Track the work needed to qualify EP backends for production and extend IRO recovery.

The main model candidates are **GLM 5.3** and **DeepSeek V4.1 Flash (DSv4.1F)**. Smaller models support fast re...
## llm-d-incubation/llm-d-rl-time-slicing (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-rl-time-slicing/releases](https://github.com/llm-d-incubation/llm-d-rl-time-slicing/releases)

### Shipped (what went in)

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-rl-time-slicing/releases/tag/v0.1.0) — 2026-08-27
- Snapshot Agent — Supports pluggable snapshot backends for moving workload state between VRAM and host.
- TimeSlice Orchestrator — Enables cooperative GPU time-slicing via group locks with cold-start acquire fix.
- llm-d-timeslice-slime — Provides PhaseCallback package for Slime RL workloads with sync and async examples.
- E2E validation on H100 — Demonstrates sync and async time-slicing with two concurrent GRPO jobs.
- Independent component adoption — Components can be used separately while being tested together.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d-incubation/llm-d-scaling-manager (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-scaling-manager/releases](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases)

### Shipped (what went in)

#### [v0.11.2](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.2) — 2026-11-17
- Breaking: `whatif` renamed to `capacity-planner` — `whatif` is deprecated and will be removed in v0.12.0.
- Two-command install from tools image — Simplified installation with `smt admin-setup`, `smt install`, and `smt admin-finish`.
- Plain HTTP Prometheus support — Install against a Prometheus server using plain HTTP with `--allow-http` flag.
- llm-d-router v1.0.0 — Updated router version with compatibility for EPP configs using `llm-d.ai/v1` API.
- Capacity planner shipped with release — Includes pre-built binaries and a Docker image for immediate use.
- Interactive planner page — Visualize and adjust fleet sizing, SLOs, and pricing via a web interface.
- Faster planning with time budget — Plans now execute in seconds (or fail with 503 if exceeding `--plan-budget`).
- Opt-in pricing features — Experimental flags for cost-aware routing and prefill-onset control.
- Docs in one place — Centralized guides and sample scenarios for capacity planner usage.

#### [v0.11.1](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.1) — 2026-11-15
- Improved prefill scaling — Prefill replicas now scale more fully based on request completion and occupancy, leading to better utilization under load.
- Local capacity planning API — Introduces `whatif serve` for local capacity planning, aligning with controller TTFT targets under flow control.
- Tools image for model server preparation — Prepare model servers without a checkout using a published tools image with each release.
- Installer resilience — Installer reads no longer fail due to notices printed on stderr by kubectl.
- Enhanced P/D prefill demand estimation — Prefill with no measured throughput now counts prompts waiting in the router as demand.
- vLLM decode queue improvements — On vLLM v0.32.0+, decode queue includes requests with KV landed and waiting to be scheduled, enabling better scaling.
- TTFT rate capping for EPP flow control — TTFT rates are capped below prefill flow-control onset in what-if CLI, planner API, and SLO analyzer.

#### [v0.11.0](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.0) — 2026-11-12
- Stable release installable with `kubectl` via signed manifests — enables secure, digest-pinned deployment without additional tools.
- Centralized settings in `scaling-manager-settings` ConfigMap — simplifies configuration management for scaling policies and parameters.
- Read-only preflight Job for installation checks — validates prerequisites before deployment to prevent misconfigurations.
- Controller auto-configures external scaler TLS — eliminates manual TLS setup for secure scaler communication.
- Steadier sizing with throughput floor and service rate metrics — improves scaling accuracy and stability over time.
- Reinstall preserves policy and KEDA connection — avoids disruptions during upgrades or re-deployments.
- Breaking: First `make` install disables scale-to-zero by default — requires explicit flag or ConfigMap update to enable.
- Breaking: New `scaling-manager-settings` replaces old ConfigMap — mandates migration of settings to the new format.


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.11.1-rc2](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.1-rc2) (2026-11-14)  - Tools image and tarball — Provides a prebuilt image and downloadable tarball for preparing model servers without requiring a checkout.
  - Disaggregated (P/D) prefill improvements — Prefill replicas now scale more fully based on request completion rates and occupancy, leading to better provisioning.
  - Local API for capacity planner — Introduces `whatif serve` for local capacity planning and aligns with the controller on TTFT targets under flow control.
  - Installer resilience — Installer reads no longer fail due to notices printed by `kubectl` on stderr.
  - P/D prefill demand from router backlog — Counts prompts waiting in the router as demand, enabling scaling of prefill replicas.
  - vLLM queue improvements — On vLLM v0.32.0+, decode queue counts requests with KV fetched but waiting to be scheduled, enabling better scaling.
- [v0.11.0-rc1](https://github.com/llm-d-incubation/llm-d-scaling-manager/releases/tag/v0.11.0-rc1) (2026-11-09)  - Repository relocation — Project moved to `llm-d-incubation/llm-d-scaling-manager` with no upgrade path from previous versions.
  - Passive mode — Enable passive scaling by setting `LLMSM_PASSIVE=true` or configuring it per-policy.
  - Renamed metrics — Metrics now start with `llmsm_` instead of `wva_` for consistency and clarity.
  - Renamed alerts — Alerts now use `LLMSM` prefixes instead of `WVA` for better identification.
  - Renamed environment variables — All environment variables now use `LLMSM_` prefixes.
  - New KEDA trigger name — The KEDA trigger is now named `llmsm` for use in scaling formulas.


## llm-d-incubation/llm-d-validate (watch)

Release page: [https://github.com/llm-d-incubation/llm-d-validate/releases](https://github.com/llm-d-incubation/llm-d-validate/releases)

### Shipped (what went in)

#### [v0.1.0](https://github.com/llm-d-incubation/llm-d-validate/releases/tag/v0.1.0) — 2026-11-14
- API Coverage — Supports OpenAI and Anthropic APIs with features like streaming, tool calling, and structured output.
- Multi-Layer Testing — Tests engine, router, and ingresses in one run with per-layer results.
- Declarative Profiles — YAML-based stack descriptions validated offline before execution.
- Evidence Collection — Generates per-case results, redacted logs, and repro scripts for every verdict.
- Known Failures — Labels pre-identified failures as known, distinguishing them from new issues.
- Dashboard Analysis — Builds an optional HTML dashboard for visualizing run results.
- Command-Line Tools — Includes `verify`, `analyze`, `compare`, and `notify` commands for testing and reporting.
- Unattended Runs — Supports scheduled and on-demand runs with a kustomize CronJob and trigger script.
- Secure Credentials — Uses environment variables for credentials, with no storage or logging.
- Pinned Runner Image — Uses a fixed UBI9 Python 3.11 image with locked dependencies.
- S3 Publishing — Uploads run results to S3, S3-compatible, and IBM Cloud Object Storage.
- Fleet Configuration — Validates metrics, logs, and configuration rules across a fleet of models.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-api-extensions (watch)

Release page: [https://github.com/llm-d/llm-d-api-extensions/releases](https://github.com/llm-d/llm-d-api-extensions/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-api-extensions/releases/tag/v1.0.0) — 2026-10-20
- vLLM server introspection — Add endpoints for inspecting vLLM server internals.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-async (watch)

Release page: [https://github.com/llm-d/llm-d-async/releases](https://github.com/llm-d/llm-d-async/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-async/releases/tag/v1.0.0) — 2026-10-15
- Semantic Versioning Commitment — Public Go modules (`api`, `pipeline`, `producer`) now follow semantic versioning for compatibility.
- Redis-SortedSet Transport — Durable claims with lease-based redelivery, Redis Cluster and Sentinel support, and payloads stored separately from the envelope.
- GCP-PubSub Transport — Routes results per topic or per message.
- Flow Control Enhancements — Per-queue and per-pool gates with Prometheus budget, Redis quota, tier-priority admission, and leased-rate controls.
- Cancellation Propagation — Cancellation now reaches requests already executing.
- Equal-Deadline Dispatch — Equal-deadline requests dispatch in submission order.
- Metrics-Driven Scaling — Gate-waiting gauge supports metrics-driven scale-from-zero.
- Helm Chart Improvements — Includes transport secrets and custom PodMonitors with labels.
- Grafana Dashboard Integration — Async Processor Grafana dashboard shipped with the llm-d dashboard set.
- Multitenant Guide — Added multitenant guide in llm-d at Tier 2.
- Gate Decision Labeling — Gate decisions are now labeled by the gate's reason for better monitoring.
- Payload Handling — `api.Request` now includes `ReqModel()` and payloads are stored as `json.RawMessage`.

#### [v0.11.0](https://github.com/llm-d/llm-d-async/releases/tag/v0.11.0) — 2026-10-12
- Cancel inference requests — Allows cancellation of inference requests that are already executing.
- PubSub per-topic routing — Enables per-topic and per-message result topic routing for pubsub.
- Redis Cluster/Sentinel support — Adds support for Redis Cluster and Sentinel topologies.
- Chart custom labels — Allows custom labels on the model server PodMonitor in Helm charts.
- Store request payloads — Stores request payloads separately from queued envelopes for processing.
- Idle connection retention — Keeps an idle connection per inference worker for improved reliability.
- Custom Redis ordering — Orders equal-deadline requests using a Redis sequence for fairness.
- Case-insensitive header handling — Applies header precedence and Content-Type case-insensitively for transforms.

#### [v0.10.0](https://github.com/llm-d/llm-d-async/releases/tag/v0.10.0) — 2026-09-16
- Durable Redis Result Delivery — Adds support for reliable Redis-based result delivery in async workflows.
- Backlog and Token Usage Charts — Introduces visual metrics for backlog size, in-process size, token usage, and deadline proximity.
- Deprecate Redis-PubSub Transport — Marks the Redis-PubSub transport as deprecated in favor of newer alternatives.
- Planner Dispatch Contracts and Telemetry — Exposes contracts and telemetry for planner dispatch to improve observability.
- Bound Pool Gate Wait Lifecycle — Implements lifecycle management for pool gate waits to enhance resource control.
- Enforce Leased Redis Dispatch Rates — Adds enforcement of Redis dispatch rates to prevent overutilization.
- Direct Endpoint Budgets Support — Enables flow control with direct endpoint budgets for better resource allocation.
- Align Async Trace Attributes — Updates async trace attributes to match GenAI semantic conventions for consistency.
- Context Cancellation Handling — Honors context cancellation during result waiting to improve responsiveness.
- Flow Control Metric Update — Uses a new metric for flow control pool saturation tracking.

#### [v0.9.1](https://github.com/llm-d/llm-d-async/releases/tag/v0.9.1) — 2026-09-04
- Async Gate Decisions Metrics — Adds `async_gate_decisions_total` metrics to worker pool gates for better monitoring.
- Inference Fairness ID Stamping — Stamps inference fairness ID from tenant metadata for improved fairness tracking.
- Gateway Drop Reasons and Retry Handling — Captures gateway drop reasons and honors `Retry-After` within deadlines.
- Pod Affinity Support — Adds support for pod affinity configuration in the llm-d-async Helm chart.
- Result TTLs and Deadline Classification — Introduces result TTLs, per-lane objective stamping, and deadline classification.
- Token Throughput Counter — Adds a token throughput counter for performance monitoring.
- Deadline Proximity Histogram — Introduces a histogram for tracking deadline proximity in backlog queues.
- Durable Dequeue via Claims — Implements durable dequeue via claims for the sorted-set transport.
- Hot Reload Sorted-Set Queue — Enables hot reloading of sorted-set queue configuration for Redis.
- GCP PubSub E2E Tests — Adds GCP PubSub end-to-end tests using the emulator for better test coverage.

#### [v0.9.0](https://github.com/llm-d/llm-d-async/releases/tag/v0.9.0) — 2026-07-30
- Metric Accuracy Improvement — Ensures consistent meaning of `pool_name` across all gate series for clearer monitoring.
- Budget Gating Enhancement — Counts `gate_closed` accurately when budget gating occurs, improving metric reliability.
- Prometheus Budget Clarity — Surfaces and explains the Prometheus budget closing point in documentation for better user understanding.
- Cross-Namespace Scraping — Allows `modelServerMonitor` to scrape metrics across namespaces for more comprehensive monitoring.
- Inference Pool Application — Applies `inference_pool` at scrape time for pods lacking the label, ensuring accurate metric collection.
- Metric Source Addition — Adds a stock-EPP metric source to the budget cascade for improved flow control tracking.

#### [v0.8.0](https://github.com/llm-d/llm-d-async/releases/tag/v0.8.0) — 2026-07-27
- Breaking: Structured ResultMessage — ResultMessage now includes StatusCode, ErrorCode, and ErrorMessage for clearer error differentiation.
- Breaking: HTTP-error Payload Format — HTTP-error payloads now contain raw upstream response bodies instead of wrapped error strings.
- Breaking: Gate-drop Payload Format — Gate-drop payloads are now unified and include an ErrorCode "GATE_DROPPED" for easier detection.
- Breaking: InferenceClient.SendRequest Return Type — Now returns (*InferenceResponse, error) with StatusCode and Body fields.
- Increased Default Worker Concurrency — Default worker concurrency raised from 8 to 64 to improve throughput.
- Prometheus Gauges for Gate Metrics — Exposes async_gate_metric_value and async_gate_metric_threshold for gate status visibility.
- Breaking: Helm Chart Renamed — Helm chart renamed to llm-d-async with new OCI registry path and resource naming.
- Breaking: OpenTelemetry Service Name — Default OpenTelemetry service name changed to llm-d-async for trace consistency.


### Next community release (planned)


**Milestones, roadmaps & open RFCs feeding the next drop**
- [#510 [Tracking] v1.1.0 Roadmap](https://github.com/llm-d/llm-d-async/issues/510) _(roadmap · roadmap)_ — Tracking issue for the **v1.1.0** milestone: the first minor after v1.0.0. It has three feature goals, plus work carried over from v0.11.0 / v1.0.0 and follow-ups from the v1.0.0 cut.

Milestone: [...
## llm-d/llm-d-autoscaling (watch)

Release page: [https://github.com/llm-d/llm-d-autoscaling/releases](https://github.com/llm-d/llm-d-autoscaling/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v1.0.0) — 2026-10-13
- KEDA-first architecture — Repository now uses KEDA as the primary autoscaling engine, deprecating the old WVA controller.
- Benchmark test bed — Includes vLLM model simulator, scenario examples, and enhanced Grafana dashboard.
- Autoscaling development workflow guide — New documentation for developing autoscaling solutions.
- Async/batch autoscaling proposal — Documentation outlines async/batch autoscaling using llm-d-async metrics.
- E2E validation guide — End-to-end test validating KEDA EPP guide on Kind cluster.
- Toolchain updates — Upgraded to Go 1.26 and 1.27 builder image for development.
- Breaking: WVA deprecation — No new controller image; users must use v0.9.0 or transition to KEDA blueprints.

#### [v0.9.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.9.0) — 2026-08-13
- Quota-based limiter — Enforces per-GPU-type quotas at cluster or namespace scope.
- Priority-weighted GPU rescale — Alpha feature for rescaling GPUs based on priority under contention.
- SGLang backend support — Adds support for the SGLang backend.
- KEDA ScaledObject rebalancing — Enables rebalancing of KEDA ScaledObjects in the coordinator.
- Phase 1 ScalingPolicy schema — Introduces the initial version of the ScalingPolicy schema.
- ThroughputAnalyzer improvements — Model-level arrival-rate demand, liveness-gated scale-down vetoes, and opt-in registration.
- Observability metrics — Six corrected metrics and a new freshness gauge with PrometheusRule alerting.
- Security enhancements — Removal of /debug/pprof, secrets and node-write RBAC, and TLS certificate hardening.
- Default saturation analyzer — V2 token/capacity-based analyzer now replaces the V1 version.
- Annotation mode only — VariantAutoscaling CRD is removed, leaving annotation mode as the sole configuration path.

#### [v0.8.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.8.0) — 2026-06-22
- Observability suite — New Prometheus metrics and Grafana dashboard for monitoring autoscaling.
- Saturation/throughput engine — Role-aware grouping, multi-analyzer registry, and new ThroughputAnalyzer.
- Kustomize-first install — Primary install method with namespace-scoped overlays and OpenShift support.
- Flexible variant discovery — Annotation-based discovery with optional `llm-d.ai/variant` for Deployments.
- Coordinator component — New component for managing autoscaling processes.
- GPU rebalancer — Initial proof-of-concept for GPU resource rebalancing.
- Benchmarking enhancements — Real-dataset profiles and scenarios for performance evaluation.
- Breaking: ConfigMap rename — Updated ConfigMap name requires synchronization and restart.
- Breaking: Env var rename — `NAMESPACE` replaced by `WVA_NS` in environment variables.
- Breaking: Helm chart deprecated — Kustomize is now the primary installation method.
- Breaking: VA deprecation — Phase 2 deprecation with migration guide and CRD marker.
- Breaking: Multi-model surface removed — Removed multi-model configuration from deploy settings.

#### [v0.7.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.7.0) — 2026-04-30
- CI Benchmark for Prefill-Heavy Workloads — Added benchmarking for prefill-heavy workloads in OpenShift environments.
- Multi-model Deploy and Test — Enabled deployment and testing of multiple models using a wrapper.
- Decode Heavy Mode for Single Model Benchmark — Introduced a decode-heavy mode for single-model benchmarking.
- Multi-tenant Patches and Guards — Added support for multi-tenancy with patches and guards for isolation.
- Add Multi-model Benchmark Guide — Created a guide for benchmarking multiple models.
- Rename Benchmark Guide and Add Single-model Section — Renamed the benchmark guide and added a section for single-model benchmarks.
- Feature Gates for EPP FlowControl — Enabled the EPP flowControl feature using feature gates.
- Disable Metrics Server in Indexer Testing — Disabled the metrics server during indexer testing for accuracy.
- Tighten E2E Fixture for Correctness — Improved end-to-end fixtures to ensure test correctness.
- Add Benchmark Summary Placeholder — Introduced a placeholder for summarizing benchmark results.

#### [v0.6.0](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.6.0) — 2026-04-03
- Scaling Decision Logging — Adds detailed logging for scaling decisions and end-to-end failure/debug dumps.
- GIE Queuing for Scale from Zero — Implements GIE queuing to support scale-from-zero scenarios in end-to-end tests.
- Refactor API for Controller Integration — Extracts `VariantAutoscalingConfigSpec` to improve integration with higher-level controllers.
- Helm Chart Sync — Syncs Helm chart CRD definitions with `config/crd/bases` during manifest generation.
- E2E Test Fixes — Resolves issues in end-to-end tests for accelerator-specific scaling and saturation mode scenarios.
- Stop KEDA Guard on Cluster Deletion — Prevents KEDA guard from spamming the terminal when a Kind cluster is deleted.
- Update WVA Image — Updates the WVA image after repository graduation.
- Document WVA Release Process — Adds documentation for the WVA release process.
- Full E2E Tests Required — Makes full end-to-end tests mandatory for CI runs on pull requests.
- Fix E2E Commit Status Reporting — Ensures correct reporting of E2E commit status to forked PR head SHA.


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.8.0-rc5](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.8.0-rc5) (2026-06-19)  - Enhanced dashboard metric — Added panel showing `wva_pod_mapping_miss_total` metric in the dashboard.
- [v0.8.0-rc4](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.8.0-rc4) (2026-06-18)  - Observability Dashboard — Support for selectable data sources.
- [v0.8.0-rc3](https://github.com/llm-d/llm-d-autoscaling/releases/tag/v0.8.0-rc3) (2026-06-17)  - Reverted token-based saturation analyzer — Reverted to a previous version of the token-based saturation analyzer configuration.
  - Refactored metric emit code — Improved the stability and maintainability of code responsible for emitting metrics.
  - Fixed replica scaling signal emission — Ensures replica scaling signals are emitted even when accelerator details are unresolved.

**Milestones, roadmaps & open RFCs feeding the next drop**
- [#1079 Roadmap ](https://github.com/llm-d/llm-d-autoscaling/issues/1079) _(roadmap · roadmap)_ — # Autoscaling Roadmap

This roadmap captures major initiatives for the Workload Variant Autoscaler.
Priorities may evolve based on community feedback and project needs.

### Core

- [ ] Unify WVA c...
## llm-d/llm-d-batch-gateway (watch)

Release page: [https://github.com/llm-d/llm-d-batch-gateway/releases](https://github.com/llm-d/llm-d-batch-gateway/releases)

### Shipped (what went in)

#### [v1.0.1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.1) — 2026-11-16
- PostgreSQL SQL async dispatch — Add support for asynchronous SQL dispatch using PostgreSQL.
- Native GCS file backend — Introduce a native Google Cloud Storage backend for file storage.
- Carry job tenant in async request metadata — Enable tracking of job tenant information in async request metadata.

#### [v1.0.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.0) — 2026-10-18
- Helm Chart Update — Updated Helm charts to use new llm-d-async configuration values.
- Resumable Batch Takeover Guard — Added protection to prevent unintended resumable batch takeover.
- Resumable Batch Foundation — Introduced entry schema, fenced store, and stable request IDs for resumable batches.
- Resumable Pipeline Integration — Enabled all jobs to run through the resumable processing pipeline.

#### [v0.7.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v0.7.0) — 2026-10-08
- PostgreSQL LISTEN/NOTIFY cancellation — Added durable batch event cancellation using PostgreSQL instead of Redis.
- Configurable batch endpoints — Allow users to define custom endpoints through `global.extraEndpoints`.
- Immediate batch totals visibility — Batch request totals are visible as soon as processing starts.
- Postgres-native job ownership — Replaced Redis queue with PostgreSQL for atomic job ownership.
- Worker count from disk budget — Processor derives worker count based on input disk budget.
- OTel tracer initialization — Initialized OpenTelemetry tracer for tracing orphan triage.
- Reimplemented cancellation mechanism — Used PostgreSQL LISTEN/NOTIFY to eliminate Redis dependency.
- Redis removal from control-plane — Removed Redis/Valkey as a control-plane dependency.
- S3 storage update — Replaced MinIO with SeaweedFS in deployment and development examples.
- Async result queues isolation — Isolated async result queues by replica for better resource management.

#### [v0.6.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v0.6.0) — 2026-09-24
- Orphan Triage Tracing — Initialize OpenTelemetry tracer for monitoring orphaned jobs.
- Postgres Job Ownership — Use Postgres-native atomic operations for job ownership instead of Redis.
- Dynamic Worker Scaling — Adjust worker count based on available disk budget for processing.

#### [v0.5.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v0.5.0) — 2026-08-12
- Single Context with Cancel Cause — Enhances job processing by using a single context with a cancel cause in `Processor#runJob()`.
- Tenant-Scoped Model Gateways — Allows model gateway lookups scoped to a tenant using `route_key_by_tenant`.
- Preserve Status Timestamps — Ensures status timestamps are preserved across job state transitions.
- AIMD Endpoint State Keyed by Route — Keys AIMD endpoint state by route key and switches to `route_key_method` for better routing.

#### [v0.4.0](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v0.4.0) — 2026-08-07
- LLM-D Async Dispatcher Support — Added support for deploying the llm-d-async dispatcher using deploy-k8s.sh.
- Async-Processor Deployment Scenario — Implemented scenario 5 for async-processor deployment in benchmarks.
- TLS CLI Flags — Added CLI flags for configuring TLS externally.
- Go Version Bump — Minimum Go version increased from 1.25 to 1.26.


### Next community release (planned)

**Release candidates / trains in flight**
- [v1.0.1-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.1-rc1) (2026-11-16)  - PostgreSQL SQL async dispatch — Add support for asynchronous SQL dispatch using PostgreSQL.
  - Native GCS file backend — Introduce native Google Cloud Storage as a file storage backend.
  - Carry job tenant in async request metadata — Enable tracking of job tenant information in async request metadata.
- [v1.1.0-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.1.0-rc1) (2026-11-12)  - PostgreSQL SQL async dispatch — Add support for asynchronous SQL dispatch using PostgreSQL.
  - Native GCS file backend — Introduce native Google Cloud Storage as a file storage backend.
- [v1.0.0-rc1](https://github.com/llm-d/llm-d-batch-gateway/releases/tag/v1.0.0-rc1) (2026-10-14)  - Helm chart update — Updated Helm charts to use new llm-d-async configuration values.
  - Resumable batch takeover guard — Added safeguards to prevent unintended resumable batch takeovers.
  - llm-d.ai API group integration — Migrated to use the llm-d.ai API group and updated GAIE version.


## llm-d/llm-d-benchmark (watch)

Release page: [https://github.com/llm-d/llm-d-benchmark/releases](https://github.com/llm-d/llm-d-benchmark/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v1.0.0) — 2026-10-16
- Prefer Inference-Perf BR0.2 — Uses inference-perf's native BR0.2 partial instead of hand-derived aggregates for accuracy.
- Consolidate Benchmark Report — Merges Benchmark Report v0.2 and v0.2.1 into a single implementation for simplicity.
- Add Inference-Perf Profiles — Adds inference-perf profiles for llm-d async multi-tenant nightly workloads.
- Use Standard Deviation in Profiles — Incorporates std_dev in token-shape inference-perf profiles for better statistical analysis.
- Update Token-Aware EPP Config — Adjusts token-aware P/D EPP config for compatibility with llm-d-router v0.11.0.
- Fix Token-Aware DoE Commands — Corrects token-aware DoE commands in documentation for clarity and accuracy.
- Report InferenceMAX Lengths — Reports InferenceMAX lengths from totals while retaining key latency metrics.
- Label KV-Cache Usage — Represents KV-cache usage statistics as a fraction for clearer interpretation.
- Convert Latency Columns to Seconds — Converts cross-treatment latency columns to seconds based on report units.
- Count Failed Requests — Counts failed requests instead of error types in aiperf import for more accurate performance tracking.

#### [v0.8.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.8.0) — 2026-08-17
- Standup support — Direct integration with guides for streamlined setup.
- No-Kubernetes Standup — Initial implementation for simplified deployment without Kubernetes.
- LM Evaluation Harness — Added tool to assess model accuracy and quality via `lm-evaluation-harness`.
- Eval-Containers Harness — New agentic benchmark framework for testing llm-d stacks with `eval-containers`.

#### [v0.7.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.7.0) — 2026-06-25
- AIPerf support — Added AIPerf as a new harness for benchmarking.
- Guide workloads — Added all workloads from "guides" in the `llm-d` project under the `workload` directory.
- Ruff integration — Added Ruff as a linter and formatter to the pre-commit workflow.
- CI/CD overhaul — Significantly overhauled CI/CD to be shared with `llm-d` for nightly benchmarks.
- Agentic code generation — Added a new agentic code generation workload.
- Fast Model Actuator integration — Improved integration with the Fast Model Actuator.
- Nixl benchmark script — Added a nixl benchmark script for sanity checks on specific scenarios.
- Helm compatibility — Increased compatibility with helm3, helm4, and s390x for installation.

#### [v0.6.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.6.0) — 2026-05-04
- Full Python Conversion — Transition to Python with a new CLI and declarative specification language for experiment description.
- Fast Model Actuator (FMA) — A Kubernetes-native system for efficient LLM inference management, reducing model startup latency.
- Enhanced Performance Metrics — Time-series metrics in benchmark reports include summaries and links to raw data in CSV format.
- WVA Integration — Tighter integration with Workload Variant Autoscaler for deploying multiple models in the same namespace.
- Pod-specific vLLM Parameters — Ability to configure `vllm` process parameters per pod using the Kubernetes `LeaderWorkerSet` API.
- YAML Stack Configuration — Fill in stack details from a YAML file directly from the harness pod.
- Capacity Planner and Explorer — Moved to a new project for easier maintenance and development.
- Improved Development Safeguards — Enhanced with pre-commit hooks and CI/CD to protect existing library patterns and functionality.

#### [v0.5.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.5.0) — 2026-03-07
- Well-lit paths deployment — All well-lit paths are now deployable via standup.sh, including `wide-ep-lws` and `workload-autoscaling`.
- Benchmark runner script — A new `run_only.sh` script enables benchmarking on pre-existing stacks.
- Enhanced pod crash detection — Expanded early detection of crashed pods to include "gaie-epp" and "inference-gateway".
- Admin prerequisites step — A new standup step ensures cluster-wide prerequisites like `istio` and `lws` are installed.
- Priority class support — `priorityClassName` is now supported for `standalone` and `modelservice` methods in standup.
- Time-series benchmark metrics — Version 0.2 of benchmark reports supports time-series metrics for better analysis.
- GPU recommender — Configuration Explorer now includes a GPU recommender based on llm-optimizer's roofline analysis.
- Architecture-aware memory estimation — Added architecture-aware activation memory estimation to the capacity planner.
- Max model length calculator — Allows calculation of maximum `max-model-len` based on memory constraints.
- Directory path flexibility — Fixes allow spaces in directory paths for improved usability.

#### [v0.4.0](https://github.com/llm-d/llm-d-benchmark/releases/tag/v0.4.0) — 2025-12-19
- Well-lit Path Support — Enable scenario and experiment configurations for all paths except `wide-ep-lws`.
- Example Scenarios — Provide deployable scenarios for GPU, AIU, CPU-only, and simulated environments as standalone or llm-d.
- Multi-Pod Deployment — Deploy multiple load-generating pods using environment variables or command-line parameters.
- WVA Integration — Automatic configuration of WVA when enabled and deployed via standup.
- Read-Only PVCs — All PVCs are read-only, enhancing large model caching and sharing in clusters.
- Crash Detection — Early detection of crashed pods during deployment with invalid parameters.
- Istio/Kgateway Support — Full compatibility with newer versions of istio and kgateway.
- Configuration Explorer Enhancements — Quantization considerations in capacity planning and integrated UI for result analysis based on SLOs.
- Cluster Setup Improvements — Enhanced automatic setup for clusters using RoCE/CDR/Infiniband and LWS.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-inference-payload-processor (watch)

Release page: [https://github.com/llm-d/llm-d-inference-payload-processor/releases](https://github.com/llm-d/llm-d-inference-payload-processor/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-inference-payload-processor/releases/tag/v1.0.0) — 2026-10-20
- Model Name Filter — Allow filtering based on the model name in requests.
- Echo Selected Model Name — Respond with the selected model name in a header.
- Shared Pricing Infrastructure — Add support for calculating actual inference costs.
- Cost t-Digest Accumulator — Enable efficient aggregation of cost data for analysis.
- RequestCostMetadataExtractor — Extract cost metadata from inference requests.
- Anthropic and Google (Gemini) Support — Add response format support for Anthropic and Google models.
- Group Model Filter — Allow filtering models based on group configuration.
- CostGuard Scorer Skeleton — Introduce a framework for cost-based scoring of requests.
- Datalayer CycleState — Carry CycleState information in request/response event payloads.
- Emit Datalayer Response Event — Stream response events on the streaming path.

#### [v0.1.0](https://github.com/llm-d/llm-d-inference-payload-processor/releases/tag/v0.1.0) — 2026-07-12
- ModelSelector architecture proposal — Introduces a framework for selecting models based on defined profiles and plugins.
- AttributeMap addition — Enables the handling and manipulation of attribute maps for enhanced data processing.
- Minimal Model representation — Provides a basic structure for model definitions within the framework's data layer.
- Streaming mode implementation — Switches from buffered to streaming mode for improved performance in extproc.
- Helm chart refactoring — Renames components for clarity, replacing "bbr" with "payloadProcessor" in Helm configurations.
- CI workflow enhancements — Adds PR size labeling and holds for large PRs to streamline development processes.


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.1.0-rc.4](https://github.com/llm-d/llm-d-inference-payload-processor/releases/tag/v0.1.0-rc.4) (2026-07-02)  - Pipeline integration — Pre/post processors are now wired into the request handling pipeline for improved processing flow.
- [v0.1.0-rc.3](https://github.com/llm-d/llm-d-inference-payload-processor/releases/tag/v0.1.0-rc.3) (2026-06-30)  - ModelSelector architecture proposal — Introduces a framework for selecting models based on defined profiles and plugins.
  - AttributeMap addition — Adds a data structure for managing attribute mappings in the payload processing framework.
  - Streaming-only mode — Refactors the extproc component to use streaming instead of buffered mode for improved performance.
  - Model representation in datalayer — Introduces a minimal representation of a Model into the framework's data layer.
  - Helm chart refactoring — Renames BBR-related components to "payloadProcessor" for clarity and consistency.
  - Plugin error handling — Returns an error for unknown plugin types instead of nil to improve reliability.


## llm-d/llm-d-inference-sim (watch)

Release page: [https://github.com/llm-d/llm-d-inference-sim/releases](https://github.com/llm-d/llm-d-inference-sim/releases)

### Shipped (what went in)

#### [v1.2.0](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.2.0) — 2026-11-10
- Tool Call Streaming Fix — Sends tool call id and type only in the initial delta.
- Cache Threshold Chunk — Emits a `cache_threshold` finish chunk for every streamed choice.
- KV Cache Validation — Rejects a KV cache size of 0 when the KV cache is enabled.
- MM Payload Support — Fixes `mm_payload` support in `render` with `--mm-encoder-only` mode.
- Efficient KV Cache Eviction — Picks blocks to evict without scanning every unused block.
- Coordinator MM Payload Support — Supports the coordinator's `mm_payload` none path on render and generate.

#### [v1.1.0](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.1.0) — 2026-11-03
- Model Positional CLI Argument — Accept the model as a positional command line argument.
- min_tokens Support — Add support for `min_tokens` in `/v1/chat/completions` and `/v1/completions`.
- JSON Response Generation — Generate JSON content when `response_format` is set to `json_object` or `json_schema`.
- Output Message ID — Add output message ID in non-streaming `/v1/responses`.
- vLLM Endpoints — Add vLLM endpoints `/v1/systemone` and `/v1/decisions`.
- Multimodal Output Endpoints — Add `/v1/audio/speech`, `/v1/images/generate`, and related multimodal output endpoints.
- mm_payload Support — Honor `mm_payload` and `return_mm_kwargs` on render endpoints.
- Tokenization Improvements — Prevent Unicode text loss during simulated tokenization.
- Metrics Enhancements — Enable fake metrics via POST `/admin/config`, export `vllm:request_max_num_generation_tokens`, and stamp metrics with sub-second time.
- Message Endpoints — Add `/v1/messages/render` and `/v1/messages/count_tokens` for message handling.
- LoRA Metrics Exposure — Expose `vllm:lora_requests_info` only when LoRA is configured and in use.
- KV Cache Events — Always send `lora_id` and `lora_name` in map-format `BlockStored` events.

#### [v1.0.0](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.0.0) — 2026-10-15
- Multimodal output endpoints — Added `/v1/audio/speech` and `/v1/images/generate` for generating audio and images.
- Strict validation mode — Added `--strict` flag to validate chat and completion requests against vLLM schemas.
- Message rendering and token counting — Added `/v1/messages/render` and `/v1/messages/count_tokens` endpoints.
- Opt-in vLLM sampling validation — Enabled optional validation of sampling parameters against vLLM expectations.
- Support for min_tokens — Added support for `min_tokens` in `/chat/completions` requests.
- Output message ID in responses — Added message ID to non-streaming `/v1/responses` for better tracking.
- LoRA slot leak fix — Prevents LoRA slot leaks when unloading adapters during requests.
- Dataset DB management — Loads dataset into shared memdb and releases it on verification failure.
- Enhanced response length calculation — Fixes response length calculation, especially in echo mode.
- Matched stop field — Added `matched_stop` field from sglang (always returns null).

#### [v0.12.0](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v0.12.0) — 2026-10-08
- `/v1/responses/render` endpoint — Adds a new endpoint for rendering responses.
- Derender endpoints — Introduces inverse endpoints to the render endpoints.
- KVCache topic override — Allows overriding the KV-event topic with `--zmq-topic`.
- Cache salt support — Honors cache_salt in simulated KV prefix caching and events.
- Hybrid ZMQ bind/dial — Supports both bind and dial modes for ZMQ communication.
- `kv_transfer_params` and `ec_transfer_params` — Adds parameters to `/v1/responses` for transfer configuration.
- `kv-cache-dtype` configuration — Exposes cache data type in `vllm:cache_config_info` metric.
- Export standard process metrics — Enables exporting of standard process metrics.
- Experimental SGLang engine backend — Adds an experimental SGLang engine backend for inference.
- Configuration structure changes — YAML now has a nested structure for configuration.

#### [v0.11.4](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v0.11.4) — 2026-10-04
- Hybrid ZMQ Bind/Dial — Enables flexible network communication by allowing both binding and dialing in ZeroMQ.

#### [v0.11.2](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v0.11.2) — 2026-08-31
- Audio content support — Enable inclusion of audio in simulations via new feature added.
- `--skip-tool-validation` flag — Bypass tool schema meta-validation for faster testing.
- `--tensor-parallel-size` support — Accept tensor-parallel-size as an ignored flag for flexibility.
- Function call tool turns — Introduce function call tool turns for enhanced simulation capabilities.
- Configurable tool-call distribution — Adjust truncated-geometric tool-call count distribution for simulation control.
- Enhanced tool definition flexibility — Support common JSON schema keywords and handle missing properties gracefully.
- ZMQ replay endpoint — Add ZMQ replay endpoint for KV cache events monitoring.
- `vllm:request_time_per_output_token_seconds` metric — Track request time per output token for performance analysis.
- Environment variable support — Support HF and proxy-related environment variables for vLLM renderer.
- ZMQ topic name consistency — Update ZMQ topic name to align with llmd-router for consistency.
- Prevent token/request drops — Return HTTP 429 when channels are full or oversized to avoid silent drops.
- Random mode adjustments — Adjust random mode to check prompt space for one response token.


### Next community release (planned)

**Release candidates / trains in flight**
- [v1.2.0-rc.2](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.2.0-rc.2) (2026-11-10)  - Breaking: Dependency updates — Fixed dependencies to ensure compatibility and stability.
- [v1.2.0-rc1](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.2.0-rc1) (2026-11-10)  - Tool Call Streaming Optimization — Sends tool call id and type only in the initial delta for efficiency.
  - Cache Threshold Chunking — Emits a `cache_threshold` finish chunk for every streamed choice.
  - KV Cache Validation — Rejects a KV cache size of 0 when the KV cache is enabled.
  - Improved MM Payload Support — Fixes support for `mm_payload` in `--mm-encoder-only` mode.
  - Efficient KV Cache Eviction — Picks blocks to evict without scanning every unused block.
  - Coordinator MM Payload Support — Adds support for the coordinator's `mm_payload` none path on render and generate.
- [v1.1.0-rc.1](https://github.com/llm-d/llm-d-inference-sim/releases/tag/v1.1.0-rc.1) (2026-11-03)  - Model as positional CLI argument — Specify the model directly in the command line interface.
  - `min_tokens` support for chat completions — Enforce minimum token generation in chat endpoints.
  - JSON response format — Generate structured JSON content for `/v1/chat/completions`.
  - Non-streaming response message IDs — Include unique identifiers for tracking responses.
  - vLLM endpoints `/v1/systemone` and `/v1/decisions` — New API endpoints for decision-making simulations.
  - `min_token` enforcement for completions — Apply minimum token constraints to `/v1/completions`.


## llm-d/llm-d-kv-cache (watch)

Release page: [https://github.com/llm-d/llm-d-kv-cache/releases](https://github.com/llm-d/llm-d-kv-cache/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v1.0.0) — 2026-10-16
- KV-event reference counting — Enables efficient removal of duplicate KV events by tracking references.
- Improved KV-Cache Indexer documentation — Points to llm-d-router for better integration guidance.
- Enhanced Redis scoring — Fixes engine-to-request mapping for more accurate KV-cache management.
- Disk pressure exclusion for reserved blocks — Prevents eviction of reserved disk blocks during pressure events.

#### [v0.9.0](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.9.0) — 2026-06-14
- Emit storage KV events — Enables the fs backend to emit events related to storage operations.
- Support multiple GPU blocks in a single object store block — Improves efficiency by allowing multiple GPU blocks to be stored in one object.
- Add PVC evictor BlockRemoved events — Enhances tracking by notifying when blocks are removed by the PVC evictor.
- Batch KV block copies via cudaMemcpyBatchAsync — Optimizes performance by allowing batched GPU memory copies.
- Track HMA group identity in KV cache index — Improves organization by tracking HMA group identity within the KV cache index.
- Add HMA support to FS connector — Enables integration with HMA (Hierarchical Memory Architecture) for better memory management.
- Implement background empty directory cleanup process — Automatically cleans up unused directories in the background.
- Parse HMA KV event metadata — Enhances event handling by parsing metadata from HMA KV events.
- Trace index add and evict — Adds tracing capabilities for index operations to improve debugging and monitoring.
- Collapse FileMapper path + add config.json audit — Simplifies the FileMapper path and introduces configuration auditing.

#### [v0.8.1](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.8.1) — 2026-05-25
- `KV Cache Optimization` — Improved memory efficiency for key-value caching during inference.
- `Dynamic Cache Scaling` — Automatic adjustment of cache size based on model and input requirements.
- `Multi-GPU Support` — Enhanced support for distributed key-value caching across multiple GPUs.
- `User-Defined Cache Policies` — Ability to configure custom eviction and retention policies for KV cache.
- `Performance Profiling Tools` — New tools for analyzing and optimizing KV cache performance.
- `Compatibility with LLM-D v0.8` — Updated to align with the latest LLM-D framework features and APIs.
- `Asynchronous Cache Updates` — Support for non-blocking cache updates to improve throughput.
- `Cache Persistence Layer` — Added support for saving and reloading KV cache states between sessions.

#### [v0.8.0-fs-v0.20](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.8.0-fs-v0.20) — 2026-05-13
- Manylinux Wheels Support — Produce manylinux_2_35 wheels for cu12 + cu130.
- BlockSizeTokens Replacement — Replace BlockSize with BlockSizeTokens for better token-based management.
- CPU Offloading Fix — Correct CPU offloading for precise-prefix-cache-aware.
- KV Offload API Migration — Migrate kv_offload API to vllm 0.20.2.
- Staging Pool Handling — Handle full staging pool more effectively.
- Builder Target Fix — Correct make target check-buildah to check-builder.

#### [v0.8.0](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.8.0) — 2026-05-01
- Heterogeneous BlockSize support — Enables support for varying block sizes in KV-cache operations.
- Enable toolcalling from renderer — Allows toolcalling functionality to be initiated from the renderer component.
- Add golden test case for multi-modal — Introduces a golden test case to validate multi-modal processing.
- Add performance and stress tests for fs_backend — Enhances reliability with performance and stress testing for the file system backend.
- Add concurrency stress tests for KV-cache index operations — Ensures robustness under concurrent access scenarios.
- Deprecate embedded tokenizers — Removes support for embedded tokenizers in favor of external solutions.
- Add dockerfile for fsconnector dev on k8s — Facilitates development of fsconnector on Kubernetes with a dedicated Dockerfile.
- Update examples to use UDS tokenizer Docker image — Improves example consistency by using the UDS tokenizer Docker image.

#### [v0.7.1](https://github.com/llm-d/llm-d-kv-cache/releases/tag/v0.7.1) — 2026-04-02
- Bug Fix — Resolved an issue with `mm_hashes` in KVEvents to improve reliability.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-latency-predictor (watch)

Release page: [https://github.com/llm-d/llm-d-latency-predictor/releases](https://github.com/llm-d/llm-d-latency-predictor/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-latency-predictor/releases/tag/v1.0.0) — 2026-10-13
- Publish release images under git tag name — Automates image tagging based on Git tags for easier version management.

#### [v0.9.0](https://github.com/llm-d/llm-d-latency-predictor/releases/tag/v0.9.0) — 2026-08-11
- Model Export Endpoint — Adds an endpoint for seed-based cold start reduction.
- Omni-modality Support — Enhances support for multiple modalities in latency prediction.
- Encoder Features — Introduces `encoder_matched_size` and `encoder_input_size` for improved TTFT calculations.
- CI/CD Integration — Improves CI/CD pipeline with reusable build-image and functional tests.
- Optional Dependencies — Treats LightGBM/XGBoost as optional to avoid import errors.
- Deployment Fixes — Resolves deployment and cleanup issues for upstream versions.

#### [v0.8.0](https://github.com/llm-d/llm-d-latency-predictor/releases/tag/v0.8.0) — 2026-06-23
- Python Latency Predictor — Added a Python-based latency prediction implementation.
- Repository Governance Update — Renamed template placeholders and set ownership under `llm-d` governance.
- Dependency Updates — Bumped several action and Docker dependencies for improved build and CI processes.
- Correct Quantile Z-Score Computation — Fixed the calculation for accurate quantile z-scores using `scipy.norm.ppf`.
- RC Release Image Fix — Addressed issues with RC release images for integration with `llm-d` router.
- Image Build on PR Merge — Enabled automatic image building and pushing on pull request merge.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-pd-utils (watch)

Release page: [https://github.com/llm-d/llm-d-pd-utils/releases](https://github.com/llm-d/llm-d-pd-utils/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-pd-utils/releases/tag/v1.0.0) — 2026-10-20
- Free disk space before image building — Automatically frees disk space to prevent issues during image building.
- Link checker for PRs — Fails pull requests with broken links to ensure documentation and references are valid.
- Network performance testing — Adds testing for network performance in llm-d inference pods.
- GPU topology discovery — Discovers GPU topology for llm-d inference pods to optimize resource usage.
- Dependabot for dependency updates — Automates dependency updates to keep the project secure and up-to-date.
- Improved documentation and README — Adds documentation and updates the README with useful information and installation scripts.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-prism (watch)

Release page: [https://github.com/llm-d/llm-d-prism/releases](https://github.com/llm-d/llm-d-prism/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-prism/releases/tag/v1.0.0) — 2026-10-16
- Separate serving stack from benchmark harness — Improved separation of concerns for better maintainability and clarity.
- Group BRV0.2 stages by run.eid — Enhanced organization of benchmark stages for easier tracking and analysis.
- Feat/timeseries — Introduced support for time series data in benchmarking workflows.
- Filter benchmark runs by tag — Enables more precise filtering of benchmark runs based on tags.
- Compare session and request counts across runs — Facilitates comparative analysis of session and request metrics between different benchmark runs.
- Surface stage request errors and group messages — Improves error visibility and organization during benchmark execution.
- Add benchmark withdrawal and split review routes — Introduces new API endpoints for managing benchmark withdrawals and reviews.

#### [v0.1](https://github.com/llm-d/llm-d-prism/releases/tag/v0.1) — 2026-09-10
- Initial release — First version supporting integration with llm-d-benchmark.


### Next community release (planned)


_Nothing explicit queued (no open milestones / roadmap RFCs in cache)._

## llm-d/llm-d-router (watch)

Release page: [https://github.com/llm-d/llm-d-router/releases](https://github.com/llm-d/llm-d-router/releases)

### Shipped (what went in)

#### [v1.0.0](https://github.com/llm-d/llm-d-router/releases/tag/v1.0.0) — 2026-10-16
- API v1 Stability — EPPConfig and InferenceObjective now stable with multi-pool targeting support.
- Priority-Holdback Policy Beta — New beta policy with explicit domain configuration for resource management.
- Multi-Turn Session Affinity — Session-state-producer and thunder-agent keep sessions on the same pod for KV state consistency.
- Endpoint Pinning — endpoint-pin-screener locks requests to a single endpoint for predictable routing.
- Selective KV Transfer — Policy transfers only necessary KV cache data between pods.
- Coordinator Pipeline Support — Adds pipeline handling for `/v1/responses` and `/v1/messages` endpoints.
- Media Disaggregation — Supports audio/video media alongside images in disaggregated workflows.
- Sidecar Metrics Exposure — Exposes Prometheus `/metrics` via sidecar proxy for monitoring.
- Aggregated Models Endpoint — Unified `/v1/models` endpoint for EPP model discovery.
- Audio Content Support — Enables audio content blocks and tokenization in requests.
- P2P Cost Scoring — Evaluates P2P transfer costs to optimize routing decisions.
- Redis Peer Discovery — Uses Redis for cross-replica synchronization and pod-watch peer detection.

#### [v0.11.0](https://github.com/llm-d/llm-d-router/releases/tag/v0.11.0) — 2026-09-27
- Flow control enhancements — Saturation gating is stage-aware, with separate measurements for prefill and decode stages.
- Latency-based scheduling — Endpoints are ranked by real-time TTFT (Time to First Token) for improved routing.
- Context-aware routing — Routes cached follow-ups based on remaining prefill work for better efficiency.
- Tokenization improvements — Native rendering of Anthropic Messages through vLLM and fallback to legacy conversion.
- API coverage expansion — Supports SGLang `/generate`, OpenAI text-to-speech, and additional endpoints like `/v1/images/edits`.
- Token producer balancing — Distributes render calls across discovered endpoints for better load distribution.
- Priority fairness strategy — New `turn-priority` ensures fair distribution of requests among top-ranked endpoints.
- Enhanced queue TTL control — Per-priority band queue TTLs and custom client-configurable TTLs for better resource management.
- Capacity utilization metrics — New gauges and response headers provide visibility into flow queue durations.
- Secure token producer — Supports HTTPS, mTLS, and API key-based authentication for render endpoints.
- Built-in ATOM engine — Native support for ATOM as an engine type without external dependencies.
- Coordinator metrics — Exposes Prometheus metrics and forwards unregistered paths to decode pods for flexibility.

#### [v0.10.0](https://github.com/llm-d/llm-d-router/releases/tag/v0.10.0) — 2026-08-17
- Disaggregated prefill and decode — RDMA-free KV transfer with data-parallel support and configurable P2P tier port.
- GPU utilization-aware routing — Routes requests based on GPU utilization using DCGM extractor and endpoint attributes.
- Header-based scheduling profiles — Selects one scheduling profile per request from a header.
- Utilization-based endpoint filtering — Caps endpoints based on active, running, waiting, and KV-cache utilization.
- Multimodal image generation routing — Routes OpenAI `/v1/images/generations` requests to diffusion backends.
- Video input support — Enables approximate prefix match with video input.
- OpenTelemetry spans — Adds tracing for scoring path and end-to-end P/D trace propagation.
- mTLS support — Adds mTLS for EPP metrics endpoint and configurable TLS settings.
- Bounded metric cardinality — Limits metric cardinality for model-name and fairness-id labels.
- Coordinator API endpoint — Coordinator now serves `/inference/v1/generate`.
- Graceful shutdown — Adds `--drain-timeout` for graceful shutdown and standby replica readiness.
- Experimental plugin gating — Alpha plugins require `--allow-experimental-plugins` flag for stability.

#### [v0.9.0](https://github.com/llm-d/llm-d-router/releases/tag/v0.9.0) — 2026-06-23
- Approximate prefix-cache estimation for Anthropic API — Added support for estimating cache usage with tools.
- FileDiscovery plugin — Handles YAML/JSON file loading and file watching via `fsnotify`.
- Native NVIDIA Triton metrics — Added metrics mapping for NVIDIA Triton Inference Server workloads.
- Stream-aware TTFT and ITL metrics — Introduced metrics for measuring latency in streaming responses.
- Enabled all HTTP parsers by default in EPP — Simplifies configuration by defaulting to all HTTP parsers.
- Breaking: Removed deprecated inference pool flags — Removed `--inference-pool-name` and `--inference-pool-namespace` flags.
- Breaking: Renamed EPP headers to `x-llm-d` convention — Updated header names for consistency.
- Breaking: Deprecated UDS-backend in token-producer — Now using vLLM render endpoint.

#### [v0.8.0](https://github.com/llm-d/llm-d-router/releases/tag/v0.8.0) — 2026-04-28
- Responses API support — Adds support for the Responses API to enhance interaction capabilities.
- Distroless/static as default runtime base image — Improves security and efficiency by using a minimal base image.
- Optimize sidecar proxy hot path — Enhances performance for high-concurrency P/D routing scenarios.
- Support image build with different base — Allows customization of image builds with various base images.
- Automate migration for GAIE code — Streamlines the process of integrating GAIE code into llm-d.
- Refactor plugins according to GAIE structure — Improves plugin organization and alignment with GAIE standards.
- Add lint exclusions from GAIE — Incorporates GAIE-specific lint exclusions for better code consistency.
- Compare coverage against `main` and latest `release-*` — Enhances CI/CD by benchmarking test coverage against key branches.
- Add release notes action — Automates the generation and inclusion of release notes in CI/CD pipelines.


### Next community release (planned)

**Release candidates / trains in flight**
- [v1.0.0-rc.2](https://github.com/llm-d/llm-d-router/releases/tag/v1.0.0-rc.2) (2026-10-16)  - Default Storage Tier Weight — Sets the default weight of the `storage` tier to `0.6` for prefix scoring, allowing disk-offloaded blocks to contribute to prefix affinity without explicit configuration.
- [v1.0.0-rc.1](https://github.com/llm-d/llm-d-router/releases/tag/v1.0.0-rc.1) (2026-10-15)  - API Stability (v1) — `EPPConfig` and `InferenceObjective` graduate to `llm-d.ai/v1` with multi-pool targeting support.
  - Session Affinity & KV Cache — New session manager and admission gate keep multi-turn agent sessions on the pod with KV state.
  - Endpoint Pinning — `endpoint-pin-screener` pins requests to a single endpoint for consistent routing.
  - P2P Cost Scoring — `p2p-cost-scorer` evaluates P2P transfer costs for optimized routing decisions.
  - Selective KV Transfer — Implements selective KV transfer policy for efficient state management.
  - Redis Peer Discovery — `CrossReplicaSyncer` and pod-watch enable Redis-based peer discovery across replicas.
- [v0.11.0-rc.2](https://github.com/llm-d/llm-d-router/releases/tag/v0.11.0-rc.2) (2026-09-21)  - Precise Prefix-Cache Matching Fix — Aligns `BlockStored` extra keys with request-side keys for LoRA requests.

**Milestones, roadmaps & open RFCs feeding the next drop**
- [#3991 [Proposal] Tokenize once at ingress across vLLM and SGLang (Coordinator + EPP, EPP alone)](https://github.com/llm-d/llm-d-router/issues/3991) _(rfc · open RFC/proposal)_ — **What would you like to be added**:

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
