# Weekly tracker — 2026-11-18

_Generated 2026-11-18T19:12:50Z_

Open the **Files changed** tab on the weekly PR to diff each project's `latest-digest.md` / `latest-pipeline.md` section against last week.

## Projects

### vllm

High-throughput and memory-efficient inference engine for LLMs

**Releases (shipped + next)**

- vllm v0.34.0 shipped with 10 new models, enhancing support for a broader range of LLMs.
- vllm v0.34.0 introduced extensible KV cache by default, improving memory efficiency and flexibility.
- The vllm v0.33.0rc3 release candidate adds support for new models like Reflection Beam-1.0 and upgrades to PyTorch 2.14.
- Semantic-router v0.4.0 recognized 30+ first-time contributors across various improvements.
- vllm v0.34.0 removed Model Runner V1, streamlining the inference engine architecture.
- vllm v0.34.0 delivered performance improvements on Blackwell and MI355X hardware.

→ [`reports/vllm/latest-releases.md`](vllm/latest-releases.md)

**New blogs**

- [Keeping Agents Fast: High-Interactivity Decode with FlyDSL MonoKernels in vLLM](https://vllm.ai/blog/2026-11-18-flydsl-monokernels) explores how vLLM maintains responsiveness in agent systems using AMD Instinct GPUs through specialized decoding techniques.
- [DeepSeek-V4.1-Flash on Vera Rubin NVL72: 58x Throughput vs. GB300 NVL72 at 387 tokens/s](https://vllm.ai/blog/2026-11-12-deepseek-v41-flash-vera-rubin) highlights vLLM's ability to deliver 58x higher throughput for DeepSeek-V4.1-Flash on NVIDIA Vera Rubin compared to GB300.
- [H3-Image Day-0 Support: 4K in 0.87s with Vera Rubin](https://vllm.ai/blog/2026-11-12-minimax-h3-image-rubin) demonstrates vLLM's capability to generate 4K images in under a second using the H3-Image model on Vera Rubin hardware.
- [Reinforcement Learning: Optimizing 0.6B Dense Models on TPU v7 via vLLM](https://vllm.ai/blog/2026-11-12-rl-small-dense-tpu-v7) shows a 107x speedup in RL training for a 0.6B dense model on Google Cloud TPU v7 using vLLM and related tools.

→ [`reports/vllm/latest-blogs.md`](vllm/latest-blogs.md)

**Digest TL;DR**

- Released vllm v0.34.0 with new features and improvements to the core engine.
- Semantic Router introduced agent-based routing and session-level budget enforcement (#6745, #6751).
- Dashboard UI was redesigned with a task-first layout and improved Insights for agent-specific run tracking (#6867, #6747).
- Enabled pricing decisions based on cache receipts for model switches and added support for Vela 3.1 pico packages (#6743, #6840).
- Fixed several compatibility issues, including DeepSeek API handling (#5265) and Anthropic routing failures (#6948).
- Introduced new CLI commands and configuration options for connecting Claude Code and Codex to the gateway (#6123).

→ [`reports/vllm/latest-digest.md`](vllm/latest-digest.md)

---

### llm-d

Kubernetes-native distributed LLM inference (built around vLLM)

**Releases (shipped + next)**

- llm-d v1.0.0 shipped with multi-tenant quality of service, zero-downtime operations, and agent-aware serving for improved production readiness.
- llm-d-incubation/hermes v0.3.1 introduced faster model loading, enhanced prompt templates, and batch inference support.
- llm-d-incubation/llm-d-fast-model-actuation v0.8.0 enables faster model actuation with improved performance and scalability.
- llm-d-incubation/llm-d-lens v0.1.0 brings new capabilities for model analysis and visualization.
- The next community release for llm-d includes a planned CPU cache sharing feature and ongoing work on OpenTelemetry integration.
- llm-d-incubation/hermes is preparing for its next RC with v0.3.0-rc.3, focusing on SR-IOV and Helm deployment improvements.

→ [`reports/llm-d/latest-releases.md`](llm-d/latest-releases.md)

**New blogs**

- [Multi-Tenant and Multi-Priority Model Serving with llm-d](https://llm-d.ai/blog/multi-tenant-multi-priority-model-serving-llm-d) explains how to efficiently manage GPU resources across multiple teams and priorities using the llm-d stack, ensuring fair access and preventing resource exhaustion.

→ [`reports/llm-d/latest-blogs.md`](llm-d/latest-blogs.md)

**Digest TL;DR**

- Released multiple versions of `llm-d-batch-gateway`, including v1.0.1 and v1.1.0-rc1 (deprecated), with improvements in job ownership checks and S3 output handling (#720, #785).
- Introduced support for Intel XPU in the `omni-serving` text-to-video task using vLLM-Omni, along with updated Docker and CI configurations (#2970).
- Added GKE platform support and nightly E2E testing lanes for several guides, including Fast Model Actuation and Workload Autoscaling paths (#3040, #3041, #3042).
- Released `llm-d-validate@v0.1.0`, an end-to-end validation tool for model serving stacks, with features like statistical checks and profile inheritance (#5, #43).
- Enhanced `llm-d-scaling-manager` with support for scaling DisaggregatedSet roles, a capacity planner API, and performance improvements in cold capacity planning (#154, #128).
- Added authentication for Prometheus gates in `llm-d-async` and improved reliability with idempotent enqueue scripts and secure CA certificate handling (#539, #522).

→ [`reports/llm-d/latest-digest.md`](llm-d/latest-digest.md)

---

### praxis

AI gateway / router — provider-aware routing, protocol translation, MCP/A2A (built on Praxis proxy)

**Releases (shipped + next)**

- praxis-proxy/ai v0.11.0 shipped with enhanced security via Policy crypto backend, GPU nightly guardrails, and improved API compatibility through OpenAPI reference updates.
- praxis-proxy/praxis v0.8.0 introduced secure health checks with TLS/HTTPS and an experimental Hyper backend for performance improvements.
- praxis-proxy/grid is preparing for its next RC with v0.3.0-rc.4, focusing on stability and feature refinement ahead of a full release.
- praxis-proxy/ai added cross-provider failover and experimental agentic loops, expanding support for multi-provider workflows and advanced AI interactions.
- Upcoming community drops for praxis-proxy/ai include RFCs to shift cluster references from URLs to provider-agnostic endpoints for improved routing and compliance.
- praxis-proxy/praxis is planning to centralize IP classification logic and improve FIPS compliance testing in the next release cycle.

→ [`reports/praxis/latest-releases.md`](praxis/latest-releases.md)

**Digest TL;DR**

- Released praxis-proxy/ai@v0.11.0 and praxis-proxy/grid@v0.3.1 with key improvements in API conformance, security, and performance (#1950, #594).
- Enhanced NeMo redaction support for OpenAI Responses and Anthropic Messages, improving guardrail filtering capabilities (#1969).
- Introduced verified-identity tier in `external_metering` filter for better tenant identity resolution (#1981).
- Added support for the Conversations API in the FIPS compliance profile, ensuring secure handling of conversation data (#1960).
- Improved CI/CD and documentation workflows with new badge systems, release reports, and dependency updates (#1979, #1941).

→ [`reports/praxis/latest-digest.md`](praxis/latest-digest.md)

---
