# Learning

Official getting-started guides and tutorials for the projects this tracker follows.

## vLLM

High-throughput LLM inference engine.

- [Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/) — offline inference + `vllm serve`
- [Docs home](https://docs.vllm.ai/)
- [Basic examples](https://docs.vllm.ai/en/stable/getting_started/examples/basic.html)
- [Blog](https://vllm.ai/blog)

## llm-d

Kubernetes-native distributed LLM inference (around vLLM).

- [Quickstart](https://llm-d.ai/docs/getting-started/quickstart) — Optimized Baseline on Kubernetes
- [Well-lit paths](https://llm-d.ai/docs/well-lit-paths) — curated deploy recipes
- [Site](https://llm-d.ai)
- [Guides in repo](https://github.com/llm-d/llm-d/tree/main/guides)

## Praxis AI

AI gateway / router — provider-aware routing, protocol translation, MCP/A2A.

- [Docs hub](https://praxis.fast/ai/)
- [Docker container quickstart](https://praxis.fast/ai/container-quickstart/)
- [Source quickstart (v0.11)](https://praxis.fast/ai/v0.11.0/quickstart/)
- [GitHub + example configs](https://github.com/praxis-proxy/ai)

## vLLM Semantic Router (vSR)

Programmable decision layer that selects or combines models per request.

- [Quickstart / install](https://vllm-sr.ai/docs/installation/)
- [Site](https://vllm-sr.ai/)
- [GitHub](https://github.com/vllm-project/semantic-router)

Install sketch:

```bash
curl -fsSL https://vllm-sr.ai/install.sh | bash -s -- --channel dev
# Dashboard http://localhost:8700 · API http://localhost:8899
```

## vLLM Router (load balancer)

Replica / P/D-aware load balancer for a fleet of vLLM workers (different from Semantic Router).

- [Release blog](https://vllm.ai/blog/2025-12-13-vllm-router-release)
- [GitHub README](https://github.com/vllm-project/router)

```bash
pip install vllm-router
vllm-router --worker-urls http://worker1:8000 http://worker2:8000 --policy consistent_hash
```

## How these relate

| Project | Role |
|---------|------|
| **vLLM** | Run one (or a few) model replicas |
| **vLLM Router** | Balance traffic across vLLM replicas / P/D pools |
| **vLLM Semantic Router** | Choose *which* model (or blend) for each request |
| **llm-d** | Kubernetes stack for production multi-node serving on vLLM |
| **Praxis AI** | Gateway: protocols, providers, policy, tools (MCP/A2A) |
