# vllm blogs — 2026-11-17

_Since 14d · generated 2026-11-17T20:53:13Z_
Blog index: [https://vllm.ai/blog](https://vllm.ai/blog)

## TL;DR for this week

- [DeepSeek-V4.1-Flash on Vera Rubin NVL72: 58x Throughput vs. GB300 NVL72 at 387 tokens/s](https://vllm.ai/blog/2026-11-12-deepseek-v41-flash-vera-rubin)
- [H3-Image Day-0 Support: 4K in 0.87s with Vera Rubin](https://vllm.ai/blog/2026-11-12-minimax-h3-image-rubin)
- [Inkling 2 Small on vLLM: Day-0 Support](https://vllm.ai/blog/2026-11-12-inkling2-small)
- [Reinforcement Learning: Optimizing 0.6B Dense Models on TPU v7 via vLLM](https://vllm.ai/blog/2026-11-12-rl-small-dense-tpu-v7)
- [Encoder Disaggregation in vLLM: Scaling Multimodal Serving with EPD](https://vllm.ai/blog/2026-11-11-encoder-disaggregation-epd)
- [Migrating vLLM to the LibTorch Stable ABI](https://vllm.ai/blog/2026-11-06-stable-abi-cuda)
- [VeRL-Omni v0.3.0: Async Training and Broader Multimodal Post-Training](https://vllm.ai/blog/2026-11-06-verl-omni-v0-3-0)
- [Zero Mismatch, Simple Async RL: REINFORCE Zero, DeepSeek-V4.1 and Kimi K3.1](https://vllm.ai/blog/2026-11-06-zero-mismatch-async-rl)

## New posts

### [DeepSeek-V4.1-Flash on Vera Rubin NVL72: 58x Throughput vs. GB300 NVL72 at 387 tokens/s](https://vllm.ai/blog/2026-11-12-deepseek-v41-flash-vera-rubin)

_2026-11-12_ · Inferact and the vLLM Team
On one NVIDIA Vera Rubin NVL72 rack, vLLM serves DeepSeek-V4.1-Flash on SemiAnalysis AgentX at 1.7M tokens/s per GPU at a P90 of 387 tokens/s per user, 58x GB300 NVL72 at the same interactivity.

**[Read the full post →](https://vllm.ai/blog/2026-11-12-deepseek-v41-flash-vera-rubin)**

### [H3-Image Day-0 Support: 4K in 0.87s with Vera Rubin](https://vllm.ai/blog/2026-11-12-minimax-h3-image-rubin)

_2026-11-12_ · vLLM-Omni team
H3-Image on Vera Rubin: 0.87-second 4K generation or 6,115 images/hour on four GPUs, with projected API revenue and support across consumer and data-center hardware.

**[Read the full post →](https://vllm.ai/blog/2026-11-12-minimax-h3-image-rubin)**

### [Inkling 2 Small on vLLM: Day-0 Support](https://vllm.ai/blog/2026-11-12-inkling2-small)

_2026-11-12_ · Inferact and Thinking Machines
vLLM supports Thinking Machines' Inkling 2 Small from day 0: attention residuals, a new decode kernel for relative-bias attention, all-reduce fused with the ops around it, and DSpark speculative decoding.

**[Read the full post →](https://vllm.ai/blog/2026-11-12-inkling2-small)**

### [Reinforcement Learning: Optimizing 0.6B Dense Models on TPU v7 via vLLM](https://vllm.ai/blog/2026-11-12-rl-small-dense-tpu-v7)

_2026-11-12_ · Loki Chen, Yang Song, Hongye Xie, Ming Lei, Greg Rehm, Chongyang Bai, Dre Olgiati, Bob Kamma, Tej Choudhary, Hang Cui, Imed Zitouni, Hamed Firooz (Meta ASA); Mingfu Liang, Kavosh Asadi, Yufei Li, F...
Co-designing RL for a Qwen3-0.6B dense policy on Google Cloud TPU v7 across vLLM, Tunix, MaxText, and Pallas, with a 107x end-to-end speedup from ~100 minutes to ~56 seconds per true-8K RL cycle.

**[Read the full post →](https://vllm.ai/blog/2026-11-12-rl-small-dense-tpu-v7)**

### [Encoder Disaggregation in vLLM: Scaling Multimodal Serving with EPD](https://vllm.ai/blog/2026-11-11-encoder-disaggregation-epd)

_2026-11-11_ · Inferact, InferMatrix, IBM, and Mooncake
Recent advances in vLLM encoder disaggregation: metadata-only multimodal requests, dedicated encoder execution, remote embedding transfer, cross-encoder caching, and lower-overhead EPD routing.

**[Read the full post →](https://vllm.ai/blog/2026-11-11-encoder-disaggregation-epd)**

### [Migrating vLLM to the LibTorch Stable ABI](https://vllm.ai/blog/2026-11-06-stable-abi-cuda)

_2026-11-06_ · vLLM Team, Red Hat PyTorch Team, and Meta PyTorch Team
How vLLM migrated its CUDA build and compiled dependencies to the LibTorch Stable ABI, enabling compatible PyTorch upgrades without rebuilding vLLM.

**[Read the full post →](https://vllm.ai/blog/2026-11-06-stable-abi-cuda)**

### [VeRL-Omni v0.3.0: Async Training and Broader Multimodal Post-Training](https://vllm.ai/blog/2026-11-06-verl-omni-v0-3-0)

_2026-11-06_ · VeRL-Omni Team
VeRL-Omni v0.3.0 expands async RL, makes the V1 trainer the default, and adds reproducible recipes for audio-video generation and multimodal understanding.

**[Read the full post →](https://vllm.ai/blog/2026-11-06-verl-omni-v0-3-0)**

### [Zero Mismatch, Simple Async RL: REINFORCE Zero, DeepSeek-V4.1 and Kimi K3.1](https://vllm.ai/blog/2026-11-06-zero-mismatch-async-rl)

_2026-11-06_ · Ao Shen (Inferact), Jian Hu (NVIDIA Research), Yan Bai (NVIDIA DevTech), Shekhar Pandey (AMD), and the REINFORCE Zero authors
Asynchronous RL trains on stale weights. Align rollout and training kernels bit for bit, and unclipped importance sampling corrects that lag. Plus zero-mismatch RL for DeepSeek-V4.1-Flash, Kimi K3.1 and AMD MI355X.

**[Read the full post →](https://vllm.ai/blog/2026-11-06-zero-mismatch-async-rl)**

### [Introducing Kinference: An Open Source Inference Control Plane for vLLM and Kubernetes](https://vllm.ai/blog/2026-11-04-introducing-kinference)

_2026-11-04_ · the Kinference Team
Kinference is a new open source inference control plane for building scalable inference platforms with vLLM and Kubernetes, providing token rate limiting, tenant usage and cost tracking, intelligent load balancing, and inference policies.

**[Read the full post →](https://vllm.ai/blog/2026-11-04-introducing-kinference)**

### [vLLM Delivers Day-0 Support for Kimi K3.1 Pro](https://vllm.ai/blog/2026-11-04-kimi-k31-pro)

_2026-11-04_ · Inferact and the vLLM Team
vLLM supports Kimi K3.1 Pro on day 0: sparse attention on a KDA hybrid, a packed KV cache with FP8 or NVFP4 latents and MXFP4 index keys, token-sharded prefill, decode context parallelism, and fused low-latency decode.

**[Read the full post →](https://vllm.ai/blog/2026-11-04-kimi-k31-pro)**

