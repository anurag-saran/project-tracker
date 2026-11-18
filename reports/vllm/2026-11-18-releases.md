# vllm releases — 2026-11-18

_Generated 2026-11-18T15:23:56Z_

**Docs:** [https://docs.vllm.ai](https://docs.vllm.ai) · [https://vllm.ai/blog](https://vllm.ai/blog)
## TL;DR

- vllm-project/vllm v0.34.0: 15 feature(s)
- vllm-project/vllm next RC/train: v0.33.0rc3

## vllm-project/vllm (core)

Release page: [https://github.com/vllm-project/vllm/releases](https://github.com/vllm-project/vllm/releases)

### Shipped (what went in)

#### [v0.34.0](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) — 2026-11-16
- **10 new models** (Mistral Large 4, MiniMax-M3.1-Flash, Nemotron-3.5-Transcribe, and more!)
- **Extensible KV cache is on by default:** vLLM sizes the KV cache from memory actually free after warmup, so most models get a bigger cache and more throughput.
- **Model Runner V1 is gone.** Model Runner V2 is now the only GPU runner.
- **Big speedups** on Blackwell and MI355X: up to 1.95× decode (Step5 on GB200), 1.6× throughput (GLM-5.3-Flash), 1.24–1.40× faster long-prompt TTFT (GLM-5.3).
- **Upgrade check:** default block size is now 64, ROCm 7.2 images are gone, and `huggingface_hub >= 2.0.0` is required. See [Before you upgrade](#before-you-upgrade).
- On CUDA and ROCm, the KV cache is sized from memory actually free **after** CUDA graph capture and warmup, not from an estimate (#56492).
- **Result:** a larger cache (e.g. MiniMax-M3 on H200: 433k → 672k tokens), so throughput is higher and TTFT lower at high concurrency.
- **Trade-off:** per-token decode latency can rise on some models (TPOT +6–18% on some H200 models at concurrency 128). Opt out with `--gpu-memory-utilization 0.9` or `--no-enable-extensible-kv-cache`.
- Hardened with fixes for allocator fragmentation, startup OOMs and KV connectors (#67296, #67485, #66731, #66523, #66197, #65137, #66605, #66674).
- Model Runner V1 is removed (#63373).
- Dual-batch overlap now runs on MRV2, including with speculative decoding and DCP (#61464).
- **Suffix decoding** runs on MRV2 with a GPU speculator; Arctic Inference is no longer needed (#60339).
- **Custom speculators:** declarative configs plus a `register_speculative_method` plugin API (#63205).
- **CUDA graphs** for MRV2 draft-model speculators (#60989).
- **Adaptive verification** works with XPress (#65175).

#### [v0.32.0](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) — 2026-10-18
- **Structured decisions and generic parsers**: the new `POST /v1/systemone` endpoint answers `choice`, `noul` and `score` questions over a structured state (#59299), is served by default (#60677, #60696), and also runs on `Cloudflare/clef-omni` (#61064), `LiquidAI/d1-3B` (#60676) and DiffusionGemma (#60466). The new `hf` tool and reasoning parser (`--tool-call-parser hf`, `--reasoning-parser hf`) reads the checkpoint's `response_template`, so models that ship it need no model-specific parser (#58604, #58602), in both the Python and Rust frontends (#59005).
- **Low-precision KV cache everywhere**: NVFP4 KV cache now runs on SM8x and SM12x (#46963), SM90 (#60620) and with XQA decode on SM12x (#60452), and on MiniMax-M3 sparse attention on SM100 (#59300); GLM-5.x defaults to an FP8 KV cache on SM100, halving KV memory per rank with 2.3-5.5% more throughput at a 7-11% TTFT cost in the PR's benchmark (#60140, #60281); `fp8_ds_mla` on SM90 gives GLM-5.3-Flash up to 31% more output throughput (#59246); ROCm gains the 4-bit `ultraquant_4bit` KV cache with about 2x the density of FP8 (#57057).
- **Model Runner V2**: a GPU n-gram speculator with variable-length drafts (#40704), Elastic EP (#53934), pipeline parallelism with prefill context parallelism for MLA models (#59139), a stock torch.compile mode (#59079), and MRV2 is now the default on ROCm with the model-specific MRV1 exceptions removed (#56360).
- **Faster startup and serving**: `vllm download-kernels` installs FlashInfer's precompiled kernels (#58765); `vllm preload --preload-autotune` keeps the FlashInfer autotune table warm across restarts (#60085); a shared-memory tensor arena broadcasts large multimodal tensors to workers with one copy (#51207); tokenizers and processors load from the local snapshot (#60825); and with `--api-server-count` above 1 each connection goes to the least-loaded API worker, for 43-85% more req/s on short requests (Qwen3-0.6B, 32 input / 1 output tokens) in the PR's benchmark (#60723).
- **Model support**: new EmbeddingGemma 2 omni-modal embeddings (#60254), MiniCPM-V 4.7 (#58674) and Nemotron 3.5 ASR (#59827); video input in the Transformers modeling backend (#57441); GLM-5.3 sparse MLA index conversions reused across layers (3.5-3.9x on that kernel, #59464) and fused multi-step draft decode (13.3% at concurrency 1, #57443); HiSparse per-request residency caching for up to 58% more throughput on GLM-5.3-NVFP4 on B200 with long, fully GPU-resident contexts at high concurrency (#60083).
- **Security**: fixes for GHSA-4hhp-h66f-j5j7 (chat template resource exhaustion, #50300), GHSA-q97c-p368-75c4 (tokenizer `max_token_id`, #59491) and GHSA-frvg-qw88-hww9 (P2P ZMQ socket exhaustion, #51504); CORS no longer allows every origin by default (#61009); untrusted images are limited to raster formats (#60022); shared-memory multimodal cache handles are signed (#59357); and JSON schemas nested deeper than 64 levels are rejected (#60036).
- **Breaking changes**: Python 3.10 dropped (#60402); default CORS origins restricted (#61009); `transformers>=5.16.1,<5.20.0` and `tokenizers>=0.23.2` (#57387, #59796); torch.compile sequence parallelism and AsyncTP passes removed (#60517); cascade attention removed (#61126); `mamba_cache_mode="all"` removed (#58997); `max_tokens` no longer reserved from the context window (#57035); Responses API reasoning stream events renamed (#59652).

#### [v0.31.0](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) — 2026-10-05
- **DeepSeek-V4.1-Flash performance**: FlashMLA mega attention with the V4.1 NVFP4 compressed KV cache is now the SM100 default (#56935); DeepGEMM sparse MQA logits for the indexer (#56254) and Mega-Gate fusing the gate GEMM with expert selection (#56266); decoder boundaries fuse the TP all-reduce, mHC input preparation (#57643) and the MoE finalize (#58586); a fused small-batch WO-A with inverse RoPE and MXFP8 quant on SM100/SM103 (#58634); the MXFP8 `wo_b` GEMM fused with the sequence-parallel reduce-scatter (#57428); Engram `wkv` sharded across TP ranks (#58678) and Engram host tables shared across co-located DP replicas by default (#57651); encoder CUDA graphs for the vision tower (#56625); and SWA bounded replay that keeps the sliding-window KV out of prefix caching (#56227).
- **Fast restart**: the new `vllm preload` CLI launches the weight-cache daemon that keeps post-quantized weights resident in GPU memory across engine restarts (#56680), now with data parallelism (#57386), MTP draft models (#57312), a `/health` endpoint (#58552) and a readiness wait (#58370). Experimental initialized-engine snapshots (`vllm snapshot create/restore`) use CRIU to restore a fully initialized TP1 engine (#51360).
- **Model Runner V2 and speculative decoding**: draft-model speculative decoding (#43091) and custom logits processors (#56497) on Model Runner V2; the new LiLiCorr drafter (#57934); async scheduling for DFlash (#58065) with the context K/V precompute captured in the draft CUDA graph (#57632); DSpark adaptive verification for Gemma4 (#57263) and variable-length decode for Kimi-K3 (#52988); a DCP target with a non-DCP DSpark draft (#56723); and MoE memory now counted during MRV2 profiling, avoiding OOMs on WideEP deployments (#57270, #58411).
- **Large scale serving**: MoonEP balanced EP all2all backend via `--all2all-backend moonep` (#52101), prefill context parallelism with data parallelism (#57075), a low-SM multimem reduce-scatter for SM100/SM103 (#55072), DeepEPv2 with sequence parallelism (#57210) and EPLB with shared-expert overlap (#57236), a sharding-aware NCCL M2N weight-transfer backend for RL (#51520), and KV offloading back-pressure detection (#50045).
- **Scheduling controls**: `--max-num-active-seqs` caps RUNNING admission independently of `max_num_seqs` (#56758), `--long-prefill-token-threshold` now adapts to the number of waiting prefills instead of chunking a lone request (#57951, #58459), the waiting queue was reworked so requests already holding KV blocks are scheduled first (#58947), and the KV connector + MTP deadlock under KV pressure was fixed (#57104).
- **HiSparse hardening**: MTP verification rows resolved with a union residency kernel (#59235), MTP acceptance collapse under FULL graphs fixed (#59309), no GPU pages without host backing (#59036), a chunked-prefill preemption livelock fixed (#59494), KV cache sized from the groups HiSparse allocates (#59450), and host prefix publication and GPU prefix adoption fixes (#59007, #59282).
- **Security**: per-request `mm_processor_kwargs` and `media_io_kwargs` are rejected unless `--trust-request-mm-kwargs` is set (#58830); prefix-cache extra keys are tagged by source so a LoRA name and a `cache_salt` can no longer collide (#51899), and the LoRA path is part of the block hash (#59335); stale multimodal receiver-cache entries can no longer replace fresh payloads (#57833).
- **Breaking changes**: per-request multimodal kwargs gated (#58830); `tokenizer_mode="slow"` removed (#58545); `--enable-mamba-fine-grained-prefix-cache` renamed to `--enable-mamba-shared-prefix-checkpoint` (#57382); online quantization through `quantization="fp8"` replaced by the `fp8_per_tensor` shorthand (#53585) and Quark silent online quantization removed (#51800); the AllSpark INT8 W8A16 backend removed (#58001); `--enforce-eager` now also disables JIT kernel warmup (#58197); XPU graphs enabled by default with `VLLM_XPU_ENABLE_XPU_GRAPH` removed (#51600).


### Next community release (planned)

**Release candidates / trains in flight**
- [v0.33.0rc3](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) (2026-11-02)  - **New models**: Reflection Beam-1.0 (501B MoE, 23B active) with its DFlash2 drafter (#62074), Yandex AliceAI-Foundation-80B-A3B (#57963), Recursive Flint (40B MoE, 2.5B active) (#62938), Muse Spark Open (#61879), Step-5 Preview (#61727, #63147), NVIDIA Alpamayo 2 Super (#62957), Nemotron-Labs Dory1.0-4B (#60149), Nemotron Parse 3.5 (#61651), MiniCPM-OCR 1.0 (#63095), Domyn Edge (#62544) and the ColUltraVBERT visual document retriever (#62237).
  - **PyTorch 2.14**: vLLM is upgraded to PyTorch 2.14.0, with torchvision 0.29.0 and Triton 3.8.0 (#52183).
  - **CUDA 12.9 dropped**: release wheels and images are CUDA 13.0 only. The CUDA 12.9 wheels and the `-cu129` / `-cu129-ubuntu2404` images are no longer published (#62575); use the default CUDA 13.0 artifacts instead.
  - **libtorch ABI stable CUDA wheel**: the CUDA wheel is now ABI stable with libtorch.
  - **AWS EFA image**: a new `vllm/vllm-openai:v0.33.0-efa` image (x86_64 and aarch64) bundles the AWS EFA libraries and the EFA build of the Mooncake transfer engine, for KV transfer and multi-node serving on EFA-enabled EC2 instances (#58768).
  - **`vllm/vllm` image alias**: every release image is now also published under the shorter `vllm/vllm` name, e.g. `vllm/vllm:v0.33.0`, `vllm/vllm:v0.33.0-efa` and `vllm/vllm:v0.33.0-rocm`.

**Milestones, roadmaps & open RFCs feeding the next drop**
- [v0.33.0 cherry picks](https://github.com/vllm-project/vllm/milestone/40) _(milestone · due TBD · 0/0 issues closed · 0 open PRs)_- [v0.34.0 cherry picks](https://github.com/vllm-project/vllm/milestone/41) _(milestone · due TBD · 0/0 issues closed · 0 open PRs)_
