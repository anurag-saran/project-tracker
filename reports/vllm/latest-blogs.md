# vllm blogs — 2026-11-18

_Since 7d · generated 2026-11-18T14:03:44Z_
Blog index: [https://vllm.ai/blog](https://vllm.ai/blog)

## TL;DR for this month

- [Keeping Agents Fast: High-Interactivity Decode with FlyDSL MonoKernels in vLLM](https://vllm.ai/blog/2026-11-18-flydsl-monokernels)
- [DeepSeek-V4.1-Flash on Vera Rubin NVL72: 58x Throughput vs. GB300 NVL72 at 387 tokens/s](https://vllm.ai/blog/2026-11-12-deepseek-v41-flash-vera-rubin)
- [H3-Image Day-0 Support: 4K in 0.87s with Vera Rubin](https://vllm.ai/blog/2026-11-12-minimax-h3-image-rubin)
- [Inkling 2 Small on vLLM: Day-0 Support](https://vllm.ai/blog/2026-11-12-inkling2-small)
- [Reinforcement Learning: Optimizing 0.6B Dense Models on TPU v7 via vLLM](https://vllm.ai/blog/2026-11-12-rl-small-dense-tpu-v7)

## New posts

### [Keeping Agents Fast: High-Interactivity Decode with FlyDSL MonoKernels in vLLM](https://vllm.ai/blog/2026-11-18-flydsl-monokernels)

_2026-11-18_ · Felix Li, Lingpeng Jin, Hattie Wu, Carlus Huang, Fangzhou Ai, Zaidy Ali, Amanzhol Salykov, Hyukjoon Lee, Ziming Huang, Jun Chen, Yifeng Huang, Bin Ding, Xiaobing Zhang, Yi Gan, Vinayak Gokhale, Hon...
How FlyDSL MonoKernels keep agents responsive with high-interactivity decode in vLLM on AMD Instinct GPUs, using model-specific fusion, data-ready handoffs, and specialized-decode integration.

**[Read the full post →](https://vllm.ai/blog/2026-11-18-flydsl-monokernels)**

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

