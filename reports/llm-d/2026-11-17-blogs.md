# llm-d blogs — 2026-11-17

_Since 14d · generated 2026-11-17T20:53:19Z_
Blog index: [https://llm-d.ai/blog](https://llm-d.ai/blog)

## TL;DR for this week

- [Multi-Tenant and Multi-Priority Model Serving with llm-d](https://llm-d.ai/blog/multi-tenant-multi-priority-model-serving-llm-d)
- [From agent traces to replay](https://llm-d.ai/blog/from-agent-traces-to-replay)
- [Serving Moonshot AI's Kimi K3.1 Pro with llm-d across TPUs and GPUs](https://llm-d.ai/blog/deploy-kimi-k3-1-pro-with-llm-d)

## New posts

### [Multi-Tenant and Multi-Priority Model Serving with llm-d](https://llm-d.ai/blog/multi-tenant-multi-priority-model-serving-llm-d)

_2026-11-16_
You have multiple teams consuming multiple models, with use-cases of varying importance — and one pool of expensive GPU hardware to serve them all. You need to impose quotas and priorities so that no team starves another and no batch job exhausts the cluster. In this write-up we walk through a recommended architecture for this scenario built on the llm-d open-source stack, focusing on the llm-d...

**[Read the full post →](https://llm-d.ai/blog/multi-tenant-multi-priority-model-serving-llm-d)**

### [From agent traces to replay](https://llm-d.ai/blog/from-agent-traces-to-replay)

_2026-11-09_
Say you run inference for an agentic product. Sooner or later you have to answer questions like: how will my serving stack hold up when thousands of agents are calling tools at once? What tail latency will a user hit across a long, multi-turn session? Would a different scheduler, a bigger KV cache, or another GPU move those numbers before I commit to buying it? Did last week's model upgrade qui...

**[Read the full post →](https://llm-d.ai/blog/from-agent-traces-to-replay)**

### [Serving Moonshot AI's Kimi K3.1 Pro with llm-d across TPUs and GPUs](https://llm-d.ai/blog/deploy-kimi-k3-1-pro-with-llm-d)

_2026-11-04_
Running multi-trillion-parameter Mixture-of-Experts (MoE) models in production shifts the primary engineering bottleneck from model weights to distributed systems orchestration. With Moonshot AI's Kimi K3.1 Pro ( moonshotai/Kimi-K3.1-Pro ), infrastructure engineers must accommodate a ~2.8-trillion-parameter footprint (~104B active parameters per token across 896 routed experts), a 1M-token cont...

**[Read the full post →](https://llm-d.ai/blog/deploy-kimi-k3-1-pro-with-llm-d)**

