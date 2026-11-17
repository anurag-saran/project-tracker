# vllm digest — 2026-11-17

_Since 7d · generated 2026-11-17T02:42:58Z_

## TL;DR for this week

- Release vllm-project/llm-compressor@0.9.0.6
- Release vllm-project/humming@v0.1.20
- Release vllm-project/vllm@v0.34.0
- vllm-project/vllm/.buildkite: 41 PRs merged
- vllm-project/vllm/.pre-commit-config.yaml: 2 PRs merged

## vllm-project/vllm (core)

### Releases
- [v0.34.0](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) — 2026-11-16: v0.34.0
### .buildkite

Summary unavailable (null LLM). Source items:
- #49700 [EPLB] Expose narrow state overrides for out-of-tree devices [documentation, rocm, ready, ci/build, deepseek, nvidia, DSv4, kimi, k3] (+671/-307) by @freyfwt files: .buildkite/test_areas/expert_parallelism.yaml, docs/design/plugin_system.md, tests/distributed/test_eplb_algo.py, tests/distributed/test_eplb_extension_hooks.py, tests/distributed/test_eplb_utils.py, vllm/config/parallel.py, vllm/distributed/eplb/async_worker.py, vllm/distributed/eplb/eplb_state.py, vllm/distributed/eplb/policy/__init__.py, vllm/distributed/eplb/policy/abstract.py, vllm/distributed/eplb/policy/default.py, vllm/platforms/interface.py
- Keep built-in selector `Literal`...
- #65186 [Perf][GDN] Export Triton prefill checkpoints via per-sequence buffers [documentation, performance, ready, ci/build] (+380/-20) by @specture724 files: .buildkite/test_areas/engine.yaml, tests/kernels/fla/test_chunk_gated_delta_rule.py, tests/v1/e2e/general/test_mamba_prefix_cache.py, vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py, vllm/third_party/flash_linear_attention/ops/chunk.py, vllm/third_party/flash_linear_attention/ops/chunk_delta_h.py
- The existing dense `chunk_gated_delta_rule`...
- #65656 [Perf][DSV4.1] Accelerate candidate prefill and decode with CuTe [ready, ci/build, deepseek, DSv4.1] (+1538/-24) by @chaunceyjiang files: .buildkite/test_areas/kernels.yaml, tests/model_executor/layers/test_mla_short_prefill_indexer.py, tests/models/deepseek_v41/nvidia/test_candidate_indexer.py, vllm/config/attention.py, vllm/model_executor/models/config.py, vllm/models/deepseek_v41/attention.py, vllm/models/deepseek_v41/nvidia/ops/candidate_indexer.py, vllm/models/deepseek_v41/nvidia/ops/candidate_paged_logits.py
- #65107 [CI/Build] Mirror release and nightly images to the vllm/vllm, vllm/vllm-rocm and vllm/vllm-xpu DockerHub aliases [documentation, rocm, intel-gpu, ci/build, cpu] (+91/-23) by @khluu files: .buildkite/scripts/publish-release-images.sh, .buildkite/scripts/push-nightly-builds-cpu.sh, .buildkite/scripts/push-nightly-builds.sh, .buildkite/scripts/rocm/publish.sh, .buildkite/scripts/xpu/push-nightly-builds-xpu.sh, docs/deployment/docker.md
- **Release** (`publish-release-images.sh`):
- #67993 [ROCm][CI] Retarget 8 MI300 1 GPU jobs to the mi300_dpx queue [rocm, ci/build, verified] (+22/-22) by @sheralskumar files: .buildkite/test-amd.yaml, .buildkite/test_areas/misc.yaml, .buildkite/test_areas/pytorch.yaml, .buildkite/test_areas/spec_decode.yaml
- 8 steps in .buildkite/test-amd.yaml now run on amd_mi300_dpx.
- 3 steps in .buildkite/test_areas/*.yaml now run on amd_mi300_dpx....
- #67094 [Spec Decode] Add DSpine support [documentation, new-model, speculative-decoding, ready, ci/build, qwen, mrv2, dflash] (+569/-21) by @shanjiaz files: .buildkite/test_areas/spec_decode.yaml, docs/features/speculative_decoding/README.md, tests/models/registry.py, tests/v1/e2e/spec_decode/acceptance_rates/dflash/test_dflash.py, vllm/model_executor/models/qwen3_dspine.py, vllm/model_executor/models/registry.py, vllm/transformers_utils/configs/eagle.py, vllm/transformers_utils/configs/speculators/algos.py, vllm/transformers_utils/configs/speculators/base.py, vllm/v1/worker/gpu/spec_decode/dflash2/speculator.py, vllm/v1/worker/gpu/spec_decode/dspine/__init__.py, vllm/v1/worker/gpu/spec_decode/dspine/config.py
- Supports Tencent and Speculators checkpoint layouts through one model implementation.

**First-time contributors:** Isotr0py, Jaeyeong-CHOI, LantaoJin, NickLucche, Ronald1995, Thangnguyenvn98, YizhouZ, aarushjain29, afierka-intel, avininjamay8, azaidy, benenzhu, bnellnm, chaojun-zhang, charxwu, chaunceyjiang, freyfwt, hao-aaron, hmellor, jzakrzew, khluu, lcskrishna, mickaelseznec, qianlihuang, shanjiaz, sheralskumar, specture724, xsxszab, yma11, zxd1997066
### .pre-commit-config.yaml

Summary unavailable (null LLM). Source items:
- #66672 [CI][ROCm] Bake torchao into the ROCm test image off the default path and re-enable MI300/MI355 Quantization [rocm, ci/build, quantization] (+196/-131) by @Thangnguyenvn98 files: .buildkite/test-amd.yaml, .buildkite/test_areas/quantization.yaml, .pre-commit-config.yaml, docker/Dockerfile, docker/Dockerfile.rocm, requirements/test/quantization_deps.in, requirements/test/quantization_deps_cuda.txt, requirements/test/quantization_deps_rocm.txt, tools/pre_commit/test_tethering_allowlist.txt
**Stacked on #66194.** Until #66194 merges, this PR's diff also shows its commit, which bakes torchao and conch into the CUDA image and re-enables H200 Quantization. Those li...
- #67533 [Chore] Remove deprecated `rope_scaling` usage and forbid it in pre-commit [ready, torch.compile, deepseek, rust, kimi, pooling, recipe] (+116/-218) by @hmellor files: .pre-commit-config.yaml, recipes/models/MiniMaxAI/MiniMax-M3.yaml, rust/src/cmd/src/cli/tests.rs, tests/model_executor/test_bailing_mrope.py, tests/models/language/pooling/test_nomic_max_model_len.py, tests/transformers_utils/test_bailing_moe_v3_vl_config.py, tests/v1/attention/test_sparse_mla_backends.py, tools/pre_commit/check_forbidden_strings.py, vllm/compilation/passes/fusion/qk_norm_rope_kvcache_fusion.py, vllm/config/speculative.py, vllm/model_executor/layers/mamba/linear/bailing_linear_attn.py, vllm/model_executor/models/bailing_moe_linear.py
- On the Transformers floor (5.16.1), `config.rope_scaling` is a property returning `config.rope_parameters`, s...

**First-time contributors:** Thangnguyenvn98, hmellor
### CMakeLists.txt

Summary unavailable (null LLM). Source items:
- #45559 [ROCm][Kernel] Extend skinny gemm N=5 to N=8 cases on GFX12 (RDNA4) using  SWMMAC optimization [rocm, ready, ci/build] (+1072/-7) by @keneoneth files: CMakeLists.txt, csrc/rocm/ops.h, csrc/rocm/skinny_gemms.cuh, csrc/rocm/skinny_gemms_swmmac.cu, csrc/rocm/torch_bindings.cpp, tests/kernels/quantization/test_rocm_skinny_gemms.py, tests/model_executor/layers/test_rocm_unquantized_gemm.py, vllm/_custom_ops.py, vllm/model_executor/layers/utils.py

**First-time contributors:** keneoneth
### benchmarks

Summary unavailable (null LLM). Source items:
- #65992 [ROCm][DSv4.1][Perf] Run the fused mHC seams as AITER's single-launch HIP Mega-MHC [performance, rocm, ready, deepseek] (+870/-23) by @davzhuAMD files: benchmarks/kernels/benchmark_mhc_seam_rocm.py, tests/kernels/mhc/test_mhc_kernels.py, vllm/_aiter_ops.py, vllm/model_executor/layers/mhc.py, vllm/models/deepseek_v41/amd/mhc.py, vllm/models/deepseek_v41/amd/model.py
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py

**First-time contributors:** davzhuAMD, njhill
### cmake

Summary unavailable (null LLM). Source items:
- #67280 [Build] Bump vllm-flash-attn to 8dd9eaea (flash-attention#218, #208) [ready, ci/build] (+1/-1) by @jhaotingc files: cmake/external_projects/vllm_flash_attn.cmake
- [flash-attention#218](https://github.com/vllm-project/flash-attention/pull/218): finishes the FP8 QK-split scores before the PV passes in the SM90 CuTe kernel.
- [flash-attention#208](https://github.com/vllm-project/flash-attention/pull/208): marks the package compatible with Python 3.14.
- ...
- #67181 [Bugfix][Kernel] Bump DeepGEMM for the MegaMoE combine-readiness fix under CUDA graph replay [bug, ready, ci/build, nvidia] (+3/-2) by @gau-nernst files: cmake/external_projects/deepgemm.cmake
- DeepGEMM MegaMoE (`--moe-backend deep_gemm_mega_moe`) no long...

**First-time contributors:** gau-nernst, jhaotingc
### csrc

Summary unavailable (null LLM). Source items:
- #45559 [ROCm][Kernel] Extend skinny gemm N=5 to N=8 cases on GFX12 (RDNA4) using  SWMMAC optimization [rocm, ready, ci/build] (+1072/-7) by @keneoneth files: CMakeLists.txt, csrc/rocm/ops.h, csrc/rocm/skinny_gemms.cuh, csrc/rocm/skinny_gemms_swmmac.cu, csrc/rocm/torch_bindings.cpp, tests/kernels/quantization/test_rocm_skinny_gemms.py, tests/model_executor/layers/test_rocm_unquantized_gemm.py, vllm/_custom_ops.py, vllm/model_executor/layers/utils.py
- #62550 [Model] Add opt-in PrimTS attention for Step5 on Blackwell [ready, ci/build, nvidia] (+1504/-118) by @PerkzZheng files: csrc/fused_qknorm_rope_cache_kernel.cu, csrc/ops.h, csrc/torch_bindings.cpp, tests/kernels/test_fused_qknorm_rope_cache.py, tests/models/step5/test_prims_ts_attention.py, vllm/_custom_ops.py, vllm/config/kernel.py, vllm/models/step5/common/ops/prefill_indexer_metadata.py, vllm/models/step5/common/ops/sparse_indexer.py, vllm/models/step5/nvidia/flashinfer_sparse.py, vllm/models/step5/nvidia/model.py, vllm/models/step5/nvidia/ops/attention_gate.py
- #63524 [Bugfix][KV Offload] Report only written blocks from fs tier store jobs [bug, ready, nixl] (+177/-33) by @AdvayMonga files: csrc/fs_io.cpp, tests/v1/kv_offload/tiering/test_backpressure.py, tests/v1/kv_offload/tiering/test_fs_tier.py, tests/v1/kv_offload/tiering/test_tiering_offloading.py, vllm/v1/kv_offload/tiering/fs/io.py, vllm/v1/kv_offload/tiering/fs/manager.py
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py

**First-time contributors:** AdvayMonga, PerkzZheng, keneoneth, njhill
### csrc-rocm

Summary unavailable (null LLM). Source items:
- #45559 [ROCm][Kernel] Extend skinny gemm N=5 to N=8 cases on GFX12 (RDNA4) using  SWMMAC optimization [rocm, ready, ci/build] (+1072/-7) by @keneoneth files: CMakeLists.txt, csrc/rocm/ops.h, csrc/rocm/skinny_gemms.cuh, csrc/rocm/skinny_gemms_swmmac.cu, csrc/rocm/torch_bindings.cpp, tests/kernels/quantization/test_rocm_skinny_gemms.py, tests/model_executor/layers/test_rocm_unquantized_gemm.py, vllm/_custom_ops.py, vllm/model_executor/layers/utils.py

**First-time contributors:** keneoneth
### docker

Summary unavailable (null LLM). Source items:
- #64176 [ROCm][CI] Re-enable VLLM_GPU_SYNC_CHECK=error in the ROCm test image [bug, rocm, ci/build, deepseek, DSv4] (+29/-5) by @AndreasKaratzas files: docker/Dockerfile.rocm, tests/models/test_dsv41_mono_layers.py, tests/models/test_dsv4_mono_layers.py
**Depends on #66397, #66400, #66398, #66399. Merge this one last.** Those PRs fix the syncs that f...
- #66672 [CI][ROCm] Bake torchao into the ROCm test image off the default path and re-enable MI300/MI355 Quantization [rocm, ci/build, quantization] (+196/-131) by @Thangnguyenvn98 files: .buildkite/test-amd.yaml, .buildkite/test_areas/quantization.yaml, .pre-commit-config.yaml, docker/Dockerfile, docker/Dockerfile.rocm, requirements/test/quantization_deps.in, requirements/test/quantization_deps_cuda.txt, requirements/test/quantization_deps_rocm.txt, tools/pre_commit/test_tethering_allowlist.txt
**Stacked on #66194.** Until #66194 merges, this PR's diff also shows its commit, which bakes torchao and conch into the CUDA image and re-enables H200 Quantization. Those li...

**First-time contributors:** Thangnguyenvn98
### docker-Dockerfile

Summary unavailable (null LLM). Source items:
- #66672 [CI][ROCm] Bake torchao into the ROCm test image off the default path and re-enable MI300/MI355 Quantization [rocm, ci/build, quantization] (+196/-131) by @Thangnguyenvn98 files: .buildkite/test-amd.yaml, .buildkite/test_areas/quantization.yaml, .pre-commit-config.yaml, docker/Dockerfile, docker/Dockerfile.rocm, requirements/test/quantization_deps.in, requirements/test/quantization_deps_cuda.txt, requirements/test/quantization_deps_rocm.txt, tools/pre_commit/test_tethering_allowlist.txt
**Stacked on #66194.** Until #66194 merges, this PR's diff also shows its commit, which bakes torchao and conch into the CUDA image and re-enables H200 Quantization. Those li...

**First-time contributors:** Thangnguyenvn98
### docker-Dockerfile.rocm

Summary unavailable (null LLM). Source items:
- #64176 [ROCm][CI] Re-enable VLLM_GPU_SYNC_CHECK=error in the ROCm test image [bug, rocm, ci/build, deepseek, DSv4] (+29/-5) by @AndreasKaratzas files: docker/Dockerfile.rocm, tests/models/test_dsv41_mono_layers.py, tests/models/test_dsv4_mono_layers.py
**Depends on #66397, #66400, #66398, #66399. Merge this one last.** Those PRs fix the syncs that f...
- #66672 [CI][ROCm] Bake torchao into the ROCm test image off the default path and re-enable MI300/MI355 Quantization [rocm, ci/build, quantization] (+196/-131) by @Thangnguyenvn98 files: .buildkite/test-amd.yaml, .buildkite/test_areas/quantization.yaml, .pre-commit-config.yaml, docker/Dockerfile, docker/Dockerfile.rocm, requirements/test/quantization_deps.in, requirements/test/quantization_deps_cuda.txt, requirements/test/quantization_deps_rocm.txt, tools/pre_commit/test_tethering_allowlist.txt
**Stacked on #66194.** Until #66194 merges, this PR's diff also shows its commit, which bakes torchao and conch into the CUDA image and re-enables H200 Quantization. Those li...

**First-time contributors:** Thangnguyenvn98
### docs-features-quantization

Summary unavailable (null LLM). Source items:
- #67267 [Quant] LUT-B: fit per-channel block32 weight scales [documentation, quantization] (+201/-52) by @mgoin files: docs/features/quantization/online.md, tests/kernels/moe/test_lut_b_moe.py, vllm/model_executor/layers/quantization/utils/lut_b_utils.py
- #67006 [Quantization] Online weight-only NVFP4 for dense linear layers [documentation, ready, nvidia, quantization] (+349/-63) by @stecasta files: docs/features/quantization/online.md, tests/model_executor/kernels/test_b12x_linear.py, tests/quantization/test_online.py, vllm/config/quantization.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/nvfp4/b12x.py, vllm/model_executor/kernels/linear/nvfp4/base.py, vllm/model_executor/kernels/linear/nvfp4/flashinfer.py, vllm/model_executor/layers/quantization/__init__.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/lm_head.py, vllm/model_executor/layers/quantization/online/nvfp4.py
- #65802 [Model Loader] Direct reload of online-quantized modules [documentation, ready, gpt-oss, quantization, kimi] (+411/-25) by @hao-aaron files: docs/features/quantization/online.md, docs/training/direct_reload.md, docs/training/layerwise.md, docs/training/weight_transfer/README.md, tests/model_executor/model_loader/test_direct_reload.py, tests/quantization/test_online_loading.py, vllm/config/vllm.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/loading.py, vllm/model_executor/model_loader/reload/plan.py, vllm/model_executor/models/gpt_oss.py
- #62708 [ROCm][Quantization] Add load-time int4 lm_head quantization for RDNA… [documentation, rocm, ready, quantization] (+705/-14) by @xiao-llm files: docs/features/quantization/online.md, tests/quantization/test_online_int4_lm_head.py, vllm/config/quantization.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/int4.py, vllm/model_executor/layers/quantization/online/lm_head.py
- #65974 [MoE][NVIDIA] Support SM107 in flashinfer_moe_ep_cutedsl for NVFP4 experts for FI 0.7.3 [documentation, ready, deepseek, nvidia] (+517/-35) by @Victor49152 files: docs/features/quantization/modelopt.md, docs/serving/expert_parallel_deployment.md, tests/kernels/moe/test_flashinfer_moe_ep.py, tests/models/test_deepseek_v4_fi_moe_ep.py, vllm/config/kernel.py, vllm/model_executor/layers/fused_moe/experts/flashinfer_moe_ep.py, vllm/model_executor/layers/fused_moe/flashinfer_moe_ep.py
- #67693 [Model Loader] Fill dummy FP8 weights with random codes across the range [documentation, ready] (+64/-19) by @WoosukKwon files: docs/features/quantization/modelopt.md, tests/model_executor/test_weight_utils.py, vllm/model_executor/model_loader/weight_utils.py
- On GB200 (DeepSeek-V4.1-Flash, DEP4), dummy-weight timings of large prefill steps were up to
- #61815 [Quantization] Allow online per-channel fp8 quantization of an unquantized lm_head [documentation, quantization, verified] (+250/-32) by @riceharvest files: docs/features/quantization/online.md, tests/quantization/test_online.py, vllm/model_executor/layers/quantization/base_config.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/fp8.py, vllm/model_executor/layers/quantization/online/requantization.py
- #59460 [Quantization] Make activation-quantization fallbacks explicit, add VLLM_STRICT_QUANT_SCHEME [documentation, intel-gpu, cpu, nvidia, quantization] (+798/-113) by @mgoin files: docs/features/quantization/README.md, tests/kernels/moe/test_b12x.py, tests/kernels/moe/test_moe_kernel_oracle.py, tests/kernels/quantization/test_mxfp4_kernel_selection.py, tests/kernels/quantization/test_scaled_mm_kernel_selection.py, tests/quantization/test_humming_mxfp4_block_fp8.py, vllm/envs.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/base.py, vllm/model_executor/kernels/linear/mxfp4/base.py, vllm/model_executor/kernels/linear/mxfp4/humming.py, vllm/model_executor/kernels/linear/mxfp4/marlin.py

**First-time contributors:** Victor49152, WoosukKwon, hao-aaron, mgoin, riceharvest, stecasta, xiao-llm
### docs-models-pooling_models

Summary unavailable (null LLM). Source items:
- #62785 [Bugfix][Pooling] Honor the CrossEncoder activation saved by Sentence Transformers v6 [bug, documentation, ready, multi-modality, llama, pooling] (+77/-5) by @cycancode files: docs/models/pooling_models/scoring.md, tests/models/multimodal/pooling/test_llama_nemotron_vl.py, vllm/transformers_utils/config.py

**First-time contributors:** cycancode
### docs-training-weight_transfer

Summary unavailable (null LLM). Source items:
- #65802 [Model Loader] Direct reload of online-quantized modules [documentation, ready, gpt-oss, quantization, kimi] (+411/-25) by @hao-aaron files: docs/features/quantization/online.md, docs/training/direct_reload.md, docs/training/layerwise.md, docs/training/weight_transfer/README.md, tests/model_executor/model_loader/test_direct_reload.py, tests/quantization/test_online_loading.py, vllm/config/vllm.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/loading.py, vllm/model_executor/model_loader/reload/plan.py, vllm/model_executor/models/gpt_oss.py
- #66375 [Perf][Bugfix][RL] Fix sparse NCCL update OOM and improve performance [bug, documentation, ready] (+210/-31) by @ShuoleiWang files: docs/training/weight_transfer/nccl.md, tests/distributed/test_weight_transfer.py, vllm/distributed/weight_transfer/sparse_nccl_engine.py
- **Memory:** a worker keeps every patch on the GPU until the last one arrives, 6 bytes per changed element on every rank whatever the TP size. On the default config the extensible KV cache leaves about 3 GiB free, so a one-shot `send_weights` on Qwen3-30B-A3B at TP4 fails at 1.25% of elements changed, after some ...

**First-time contributors:** ShuoleiWang, hao-aaron
### docs-usage-security.md

Summary unavailable (null LLM). Source items:
- #67316 [Bugfix][Security] Check the uncompressed size of embedding archives before torch.load [bug, documentation, ready, multi-modality] (+118/-3) by @LeizhenZhang files: docs/usage/security.md, tests/renderers/test_sparse_tensor_validation.py, vllm/multimodal/media/audio.py, vllm/multimodal/media/image.py, vllm/multimodal/media/video.py, vllm/renderers/embed_utils.py, vllm/utils/sparse_utils.py
- #65994 [Rust Frontend][gRPC] Add the Render service with RenderChat [documentation, ready, rust] (+1681/-65) by @Dao007forever files: docs/usage/security.md, rust/README.md, rust/proto/README.md, rust/proto/build.rs, rust/proto/inference.proto, rust/proto/render.proto, rust/proto/src/lib.rs, rust/src/chat/src/error.rs, rust/src/cmd/src/cli.rs, rust/src/cmd/src/cli/tests.rs, rust/src/server/src/grpc/convert.rs, rust/src/server/src/grpc/health.rs

**First-time contributors:** Dao007forever, LeizhenZhang
### recipes

Summary unavailable (null LLM). Source items:
- #67722 [Recipe] Kimi-K3.1-Pro: add the B300 AgentX disaggregated preset, align with InferenceX#5068 [ready, kimi, recipe] (+295/-0) by @mispa-ms files: recipes/models/moonshotai/Kimi-K3.1-Pro.yaml
- #67807 [Recipe] Kimi-K3.1-Pro: serve the Inferact/Kimi-K3.1-Pro-DSpark draft and fix the B300 baseline [ready, dflash, kimi, recipe] (+59/-45) by @zixi-qi files: recipes/models/moonshotai/Kimi-K3.1-Pro.yaml
- #67055 [Recipe][ROCm] ripple-65b on mi350x and mi355x [rocm, ready, recipe] (+20/-8) by @jamesETsmith files: recipes/models/ricursiveAI/Ripple-65B-Preview.yaml
- Marks the BF16 variant verified on MI350X too.
- Adds an AMD override that selects `ROCM_AITER_UNIFIED_ATTN` with `VLLM_ROCM_USE_AITER=1`, in both the rendered command and the guide's `docker run` example. Without the override, ROCm auto-selects ...
- #67586 [ROCm][Docs] Add DeepSeek-V4.1-Flash MI300X AgentX preset [rocm, ready, deepseek, verified, recipe] (+128/-1) by @lishuoshuo-amd files: recipes/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml
- Add 12 opt-in points, concurrency 1/2/4/8/16/32 for TP8 and TP4, scoped to the measured 0909 checkpoint.
- Pin the...
- #67817 [Recipe] Kimi-K3.1-Pro: MI355X kimi-k31-5c14fe8 image and SP prefill, align with InferenceX#5089 [ready, kimi, recipe] (+24/-19) by @seungrokj files: recipes/models/moonshotai/Kimi-K3.1-Pro.yaml
- **Image.**
- The preset pins `vllm/vllm-openai-rocm:kimi-k31...
- #67600 [Recipe] Kimi-K3.1-Pro: MI355X AgentX preset covering all six InferenceX#5043 concurrencies [ready, kimi, recipe] (+149/-155) by @seungrokj files: recipes/models/moonshotai/Kimi-K3.1-Pro.yaml

**First-time contributors:** hmellor, jamesETsmith, lishuoshuo-amd, mispa-ms, seungrokj, zixi-qi
### requirements

Summary unavailable (null LLM). Source items:
- #67502 [CI] Bump Transformers version to 5.23.0 [ci/build, multi-modality, qwen, cpu, glm] (+136/-201) by @hmellor files: requirements/common.txt, requirements/test/cpu.txt, requirements/test/cuda.in, requirements/test/cuda.txt, requirements/test/kv_connectors_cuda.txt, requirements/test/nightly-torch.txt, requirements/test/rocm.in, requirements/test/rocm.txt, requirements/test/xpu.in, requirements/test/xpu.txt, tests/models/multimodal/processing/test_qwen3_asr.py, tests/models/multimodal/processing/test_qwen3_omni.py
- `requirements/common.txt` allows `transformers >= 5.16.1, < 5.24.0`, and CI pins 5.23.0.
- Breaking changes in 5.23 (`ep_router` removal huggingface/transformers#49615, exporters, Wav2Vec2ProcessorWithLM, serve) do ...
- #66672 [CI][ROCm] Bake torchao into the ROCm test image off the default path and re-enable MI300/MI355 Quantization [rocm, ci/build, quantization] (+196/-131) by @Thangnguyenvn98 files: .buildkite/test-amd.yaml, .buildkite/test_areas/quantization.yaml, .pre-commit-config.yaml, docker/Dockerfile, docker/Dockerfile.rocm, requirements/test/quantization_deps.in, requirements/test/quantization_deps_cuda.txt, requirements/test/quantization_deps_rocm.txt, tools/pre_commit/test_tethering_allowlist.txt
**Stacked on #66194.** Until #66194 merges, this PR's diff also shows its commit, which bakes torchao and conch into the CUDA image and re-enables H200 Quantization. Those li...

**First-time contributors:** Thangnguyenvn98, hmellor
### requirements-rocm

Summary unavailable (null LLM). Source items:
- #67502 [CI] Bump Transformers version to 5.23.0 [ci/build, multi-modality, qwen, cpu, glm] (+136/-201) by @hmellor files: requirements/common.txt, requirements/test/cpu.txt, requirements/test/cuda.in, requirements/test/cuda.txt, requirements/test/kv_connectors_cuda.txt, requirements/test/nightly-torch.txt, requirements/test/rocm.in, requirements/test/rocm.txt, requirements/test/xpu.in, requirements/test/xpu.txt, tests/models/multimodal/processing/test_qwen3_asr.py, tests/models/multimodal/processing/test_qwen3_omni.py
- `requirements/common.txt` allows `transformers >= 5.16.1, < 5.24.0`, and CI pins 5.23.0.
- Breaking changes in 5.23 (`ep_router` removal huggingface/transformers#49615, exporters, Wav2Vec2ProcessorWithLM, serve) do ...
- #66672 [CI][ROCm] Bake torchao into the ROCm test image off the default path and re-enable MI300/MI355 Quantization [rocm, ci/build, quantization] (+196/-131) by @Thangnguyenvn98 files: .buildkite/test-amd.yaml, .buildkite/test_areas/quantization.yaml, .pre-commit-config.yaml, docker/Dockerfile, docker/Dockerfile.rocm, requirements/test/quantization_deps.in, requirements/test/quantization_deps_cuda.txt, requirements/test/quantization_deps_rocm.txt, tools/pre_commit/test_tethering_allowlist.txt
**Stacked on #66194.** Until #66194 merges, this PR's diff also shows its commit, which bakes torchao and conch into the CUDA image and re-enables H200 Quantization. Those li...

**First-time contributors:** Thangnguyenvn98, hmellor
### rust

Summary unavailable (null LLM). Source items:
- #67708 [Rust Frontend] Support --tokens-only [ready, rust] (+77/-22) by @devshah-cohere files: rust/src/cmd/src/cli.rs, rust/src/cmd/src/cli/tests.rs, rust/src/cmd/src/cli/unsupported.rs, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py
- Accepts `--tokens-only` on `vllm-rs serve` and through the launcher's `--args-json`.
- Implies `--enable-scale-out`, so the scale-out routes, including `/inference/v1/generate`, are registered even with an explicit `--enable-scale-out false`, matching Python's dedicated mod...
- #67893 [Rust Frontend] Serve /inference/v1/abort_requests [rust] (+233/-36) by @BugenZhao files: rust/src/server/src/routes.rs, rust/src/server/src/routes/inference/abort_requests.rs, rust/src/server/src/routes/inference/mod.rs, rust/src/server/src/routes/tests.rs, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py
- `/infere...
- #67399 [Rust Frontend] Honor X-Vllm-Priority on generate and reject unparsable request headers [documentation, rust] (+259/-201) by @BugenZhao files: docs/serving/online_serving/openai_compatible_server.md, docs/serving/online_serving/token_in_token_out.md, rust/src/server/src/routes/inference/generate.rs, rust/src/server/src/routes/inference/generate/convert.rs, rust/src/server/src/routes/openai/chat_completions.rs, rust/src/server/src/routes/openai/chat_completions/convert.rs, rust/src/server/src/routes/openai/completions.rs, rust/src/server/src/routes/openai/completions/convert.rs, rust/src/server/src/routes/openai/responses.rs, rust/src/server/src/routes/render.rs, rust/src/server/src/routes/tests.rs, rust/src/server/src/routes/tokenize.rs
- #67400 [Rust Frontend] Accept features together with content_parts on /generate [rust] (+428/-136) by @BugenZhao files: rust/src/chat/src/error.rs, rust/src/chat/src/lib.rs, rust/src/chat/src/multimodal.rs, rust/src/chat/src/multimodal/input.rs, rust/src/chat/src/multimodal/preprocessed.rs, rust/src/server/src/grpc/media.rs, rust/src/server/src/grpc/tests.rs, rust/src/server/src/routes/inference/generate.rs, rust/src/server/src/routes/inference/generate/types.rs, rust/src/server/src/routes/tests.rs
- #63773 [Bugfix][Rust Frontend] Preserve SentencePiece leading spaces in logprobs [bug, rust] (+188/-4) by @reidliu41 files: rust/src/text/src/output/logprobs.rs, rust/src/tokenizer/src/hf.rs, rust/src/tokenizer/src/lib.rs
- Prevents distinct tokens such as `▁the` and `the` from both being reported as `"the"`.
- Prevents `top_logprobs` entr...
- #67729 [Rust Frontend] Fix tests that fail when sharing one test process [rust] (+39/-27) by @BugenZhao files: rust/src/chat/src/multimodal/audio.rs, rust/src/server/src/routes/tests.rs, rust/src/tracing/src/timing.rs
- #67872 [Rust Frontend] Support --kv-sharing-fast-prefill [rust] (+249/-11) by @BugenZhao files: rust/src/cmd/src/cli/unsupported.rs, rust/src/engine-core-client/src/client.rs, rust/src/engine-core-client/src/mock_engine.rs, rust/src/engine-core-client/src/protocol/handshake.rs, rust/src/engine-core-client/src/tests/client.rs, rust/src/engine-core-client/src/tests/python_compat.py, rust/src/llm/src/error.rs, rust/src/llm/src/lib.rs, rust/src/llm/tests/generate.rs, rust/src/server/src/routes/tests.rs, rust/src/text/src/error.rs, vllm/v1/engine/__init__.py

**First-time contributors:** BugenZhao, Dao007forever, Isotr0py, devshah-cohere, hmellor, liangjuf, njhill, reidliu41, tomasruizt, twu3202, vito-lin-dev
### rust-src-bench

Summary unavailable (null LLM). Source items:
- #64156 [Spec Decode] Consistent drafted, verified and accepted token counts [documentation, performance, frontend, speculative-decoding, mrv2, rust, scheduler] (+461/-97) by @tomasruizt files: docs/features/speculative_decoding/acceptance_metrics.md, rust/src/bench/src/benchmark.rs, rust/src/bench/src/output/console.rs, rust/src/bench/src/output/json.rs, rust/src/chat/src/event.rs, rust/src/chat/src/output/structured.rs, rust/src/chat/src/stream.rs, rust/src/engine-core-client/src/metrics.rs, rust/src/engine-core-client/src/protocol/output.rs, rust/src/engine-core-client/src/protocol/stats.rs, rust/src/llm/src/log_stats.rs, rust/src/metrics/src/scheduler.rs
- **`drafted`**: tokens that came out of the drafter, including grammar-invalid ones.
- **`verified` (new)**: drafted tokens that went into the target forward pass.
- **`accepted`**: unchanged.

**First-time contributors:** tomasruizt
### rust-src-server

Summary unavailable (null LLM). Source items:
- #67893 [Rust Frontend] Serve /inference/v1/abort_requests [rust] (+233/-36) by @BugenZhao files: rust/src/server/src/routes.rs, rust/src/server/src/routes/inference/abort_requests.rs, rust/src/server/src/routes/inference/mod.rs, rust/src/server/src/routes/tests.rs, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py
- `/infere...
- #67399 [Rust Frontend] Honor X-Vllm-Priority on generate and reject unparsable request headers [documentation, rust] (+259/-201) by @BugenZhao files: docs/serving/online_serving/openai_compatible_server.md, docs/serving/online_serving/token_in_token_out.md, rust/src/server/src/routes/inference/generate.rs, rust/src/server/src/routes/inference/generate/convert.rs, rust/src/server/src/routes/openai/chat_completions.rs, rust/src/server/src/routes/openai/chat_completions/convert.rs, rust/src/server/src/routes/openai/completions.rs, rust/src/server/src/routes/openai/completions/convert.rs, rust/src/server/src/routes/openai/responses.rs, rust/src/server/src/routes/render.rs, rust/src/server/src/routes/tests.rs, rust/src/server/src/routes/tokenize.rs
- #67400 [Rust Frontend] Accept features together with content_parts on /generate [rust] (+428/-136) by @BugenZhao files: rust/src/chat/src/error.rs, rust/src/chat/src/lib.rs, rust/src/chat/src/multimodal.rs, rust/src/chat/src/multimodal/input.rs, rust/src/chat/src/multimodal/preprocessed.rs, rust/src/server/src/grpc/media.rs, rust/src/server/src/grpc/tests.rs, rust/src/server/src/routes/inference/generate.rs, rust/src/server/src/routes/inference/generate/types.rs, rust/src/server/src/routes/tests.rs
- #67870 [Rust Frontend] Domain-tag multimodal cache keys like Python [rust] (+46/-15) by @BugenZhao files: rust/src/chat/src/multimodal.rs, rust/src/server/src/grpc/tests.rs, rust/src/server/src/routes/inference/generate/features.rs, rust/src/server/src/routes/tests.rs
- #67869 [Rust Frontend] Return 500 for engine errors on non-streaming generate [rust] (+39/-4) by @BugenZhao files: rust/src/server/src/routes/inference/generate.rs, rust/src/server/src/routes/tests.rs
- Non-s...
- #66878 [Rust Frontend] Support n > 1 on /inference/v1/generate [ready, rust] (+264/-87) by @devshah-cohere files: rust/src/server/src/routes/inference/generate.rs, rust/src/server/src/routes/inference/generate/convert.rs, rust/src/server/src/routes/inference/generate/types.rs, rust/src/server/src/routes/inference/generate/validate.rs, rust/src/server/src/routes/tests.rs
- #64156 [Spec Decode] Consistent drafted, verified and accepted token counts [documentation, performance, frontend, speculative-decoding, mrv2, rust, scheduler] (+461/-97) by @tomasruizt files: docs/features/speculative_decoding/acceptance_metrics.md, rust/src/bench/src/benchmark.rs, rust/src/bench/src/output/console.rs, rust/src/bench/src/output/json.rs, rust/src/chat/src/event.rs, rust/src/chat/src/output/structured.rs, rust/src/chat/src/stream.rs, rust/src/engine-core-client/src/metrics.rs, rust/src/engine-core-client/src/protocol/output.rs, rust/src/engine-core-client/src/protocol/stats.rs, rust/src/llm/src/log_stats.rs, rust/src/metrics/src/scheduler.rs
- **`drafted`**: tokens that came out of the drafter, including grammar-invalid ones.
- **`verified` (new)**: drafted tokens that went into the target forward pass.
- **`accepted`**: unchanged.

**First-time contributors:** BugenZhao, devshah-cohere, tomasruizt
### tests-aiter

Summary unavailable (null LLM). Source items:
- #65711 [ROCm][Perf] Use tuned AITER Triton `gemm_a8w8` for per-tensor FP8 decode GEMMs on gfx950 [rocm, ready] (+410/-2) by @amd-jrosas files: tests/kernels/quantization/test_rocm_aiter_triton_per_tensor_fp8.py, vllm/_aiter_ops.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/scaled_mm/aiter.py
- #65788 [XPU][UT] Enable v1/attention tests on XPU [intel-gpu, ci/build, deepseek, nvidia, verified] (+251/-130) by @YizhouZ files: .buildkite/intel_jobs/attention_intel.yaml, tests/v1/attention/test_deepseek_v4_swa_visible.py, tests/v1/attention/test_gdn_aiter_flydsl.py, tests/v1/attention/test_indexer_dcp_localize.py, tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py, tests/v1/attention/test_kpool_indexer_block_sizes.py, tests/v1/attention/test_kpool_tail_slot_mapping.py, tests/v1/attention/test_mamba_align_block_table.py, tests/v1/attention/test_mla_backends.py, tests/v1/attention/test_sparse_indexer_decode_seq_lens.py, tests/v1/attention/test_sparse_mla_backends.py, tests/v1/attention/test_vit_attn_wrappers.py
- #67845 [CI][ROCm] Fix the DSv4.1 sparse MLA forward_mqa test after #66842 [rocm, ready, ci/build, deepseek, verified] (+9/-0) by @LantaoJin files: .buildkite/test-amd.yaml, .buildkite/test_areas/attention.yaml, tests/v1/attention/test_rocm_aiter_triton_sparse_mla.py
- #66842 made `DeepseekV41ROCMAiterMLAAttention.forward_mqa` read `self.use...

**First-time contributors:** LantaoJin, YizhouZ, amd-jrosas
### tests-distributed-test_pipeline_parallel.py

Summary unavailable (null LLM). Source items:
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py

**First-time contributors:** njhill
### tests-distributed-test_weight_transfer.py

Summary unavailable (null LLM). Source items:
- #66375 [Perf][Bugfix][RL] Fix sparse NCCL update OOM and improve performance [bug, documentation, ready] (+210/-31) by @ShuoleiWang files: docs/training/weight_transfer/nccl.md, tests/distributed/test_weight_transfer.py, vllm/distributed/weight_transfer/sparse_nccl_engine.py
- **Memory:** a worker keeps every patch on the GPU until the last one arrives, 6 bytes per changed element on every rank whatever the TP size. On the default config the extensible KV cache leaves about 3 GiB free, so a one-shot `send_weights` on Qwen3-30B-A3B at TP4 fails at 1.25% of elements changed, after some ...

**First-time contributors:** ShuoleiWang
### tests-entrypoints

Summary unavailable (null LLM). Source items:
- #67708 [Rust Frontend] Support --tokens-only [ready, rust] (+77/-22) by @devshah-cohere files: rust/src/cmd/src/cli.rs, rust/src/cmd/src/cli/tests.rs, rust/src/cmd/src/cli/unsupported.rs, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py
- Accepts `--tokens-only` on `vllm-rs serve` and through the launcher's `--args-json`.
- Implies `--enable-scale-out`, so the scale-out routes, including `/inference/v1/generate`, are registered even with an explicit `--enable-scale-out false`, matching Python's dedicated mod...
- #67893 [Rust Frontend] Serve /inference/v1/abort_requests [rust] (+233/-36) by @BugenZhao files: rust/src/server/src/routes.rs, rust/src/server/src/routes/inference/abort_requests.rs, rust/src/server/src/routes/inference/mod.rs, rust/src/server/src/routes/tests.rs, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py
- `/infere...
- #64965 [Bugfix][Attention] Reject TORCH_SDPA for decoder attention [bug, verified] (+87/-8) by @aarongdeng files: tests/config/test_multimodal_config.py, tests/engine/test_arg_utils.py, tests/entrypoints/llm/test_generate.py, tests/v1/attention/test_backend_per_kind.py, vllm/config/attention.py, vllm/engine/arg_utils.py
- #61788 [Rust Frontend] Pass pulled object storage model dir to the Rust frontend [frontend, ready, rust] (+80/-0) by @Lucas-Fernandes-Martins files: tests/entrypoints/launchers/api_server/test_api_server_process_manager.py, vllm/entrypoints/cli/serve.py, vllm/v1/utils.py
- #67408 [Bugfix] Reject bad_words on generate servers without a tokenizer [bug, documentation, frontend, ready] (+37/-1) by @nien-hui files: docs/serving/online_serving/token_in_token_out.md, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py, vllm/entrypoints/scale_out/token_in_token_out/serving.py
- #67606 [ROCm][Bugfix] Run the Canary WER correctness test in fp32 [bug, rocm] (+5/-2) by @AndreasKaratzas files: tests/entrypoints/speech_to_text/correctness/test_transcription_api_correctness.py
- The flake is one utterance falling into a greedy repetition loop...
- #67742 [CI] Require batch invariance for derender parity tests [ready, batch-invariance] (+4/-1) by @gty111 files: tests/entrypoints/scale_out/derender/test_derender_parity.py
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py

**First-time contributors:** BugenZhao, Lucas-Fernandes-Martins, PerryZhang01, aarongdeng, devshah-cohere, gty111, hickeyma, nien-hui, njhill, tomasruizt
### tests-entrypoints-llm

Summary unavailable (null LLM). Source items:
- #64965 [Bugfix][Attention] Reject TORCH_SDPA for decoder attention [bug, verified] (+87/-8) by @aarongdeng files: tests/config/test_multimodal_config.py, tests/engine/test_arg_utils.py, tests/entrypoints/llm/test_generate.py, tests/v1/attention/test_backend_per_kind.py, vllm/config/attention.py, vllm/engine/arg_utils.py

**First-time contributors:** aarongdeng
### tests-entrypoints-openai

Summary unavailable (null LLM). Source items:
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py
- #64156 [Spec Decode] Consistent drafted, verified and accepted token counts [documentation, performance, frontend, speculative-decoding, mrv2, rust, scheduler] (+461/-97) by @tomasruizt files: docs/features/speculative_decoding/acceptance_metrics.md, rust/src/bench/src/benchmark.rs, rust/src/bench/src/output/console.rs, rust/src/bench/src/output/json.rs, rust/src/chat/src/event.rs, rust/src/chat/src/output/structured.rs, rust/src/chat/src/stream.rs, rust/src/engine-core-client/src/metrics.rs, rust/src/engine-core-client/src/protocol/output.rs, rust/src/engine-core-client/src/protocol/stats.rs, rust/src/llm/src/log_stats.rs, rust/src/metrics/src/scheduler.rs
- **`drafted`**: tokens that came out of the drafter, including grammar-invalid ones.
- **`verified` (new)**: drafted tokens that went into the target forward pass.
- **`accepted`**: unchanged.
- #63357 [Bugfix][Frontend] Honor --response-role and echo in chat derender [bug, documentation, frontend, ready] (+345/-48) by @hickeyma files: docs/serving/online_serving/derenderer.md, docs/serving/online_serving/token_in_token_out.md, tests/entrypoints/openai/chat_completion/test_message_assembly.py, tests/entrypoints/scale_out/derender/test_derender.py, tests/entrypoints/scale_out/derender/test_derender_parity.py, tests/entrypoints/scale_out/derender/test_derender_stream.py, vllm/entrypoints/launchers/api_server/app_state.py, vllm/entrypoints/launchers/render/app_state.py, vllm/entrypoints/openai/chat_completion/batch_serving.py, vllm/entrypoints/openai/chat_completion/message_assembly.py, vllm/entrypoints/openai/chat_completion/serving.py, vllm/entrypoints/scale_out/token_in_token_out/protocol.py
**Depends on #63434. See https://github....

**First-time contributors:** hickeyma, njhill, tomasruizt
### tests-entrypoints-rl

Summary unavailable (null LLM). Source items:
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py

**First-time contributors:** njhill
### tests-entrypoints-scale_out

Summary unavailable (null LLM). Source items:
- #67708 [Rust Frontend] Support --tokens-only [ready, rust] (+77/-22) by @devshah-cohere files: rust/src/cmd/src/cli.rs, rust/src/cmd/src/cli/tests.rs, rust/src/cmd/src/cli/unsupported.rs, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py
- Accepts `--tokens-only` on `vllm-rs serve` and through the launcher's `--args-json`.
- Implies `--enable-scale-out`, so the scale-out routes, including `/inference/v1/generate`, are registered even with an explicit `--enable-scale-out false`, matching Python's dedicated mod...
- #67893 [Rust Frontend] Serve /inference/v1/abort_requests [rust] (+233/-36) by @BugenZhao files: rust/src/server/src/routes.rs, rust/src/server/src/routes/inference/abort_requests.rs, rust/src/server/src/routes/inference/mod.rs, rust/src/server/src/routes/tests.rs, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py
- `/infere...
- #67408 [Bugfix] Reject bad_words on generate servers without a tokenizer [bug, documentation, frontend, ready] (+37/-1) by @nien-hui files: docs/serving/online_serving/token_in_token_out.md, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py, vllm/entrypoints/scale_out/token_in_token_out/serving.py
- #67742 [CI] Require batch invariance for derender parity tests [ready, batch-invariance] (+4/-1) by @gty111 files: tests/entrypoints/scale_out/derender/test_derender_parity.py
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py
- #67564 [CI][Multimodal] Use `uuid:`-tagged cache key for features in /generate test and docs [documentation, ready] (+3/-3) by @PerryZhang01 files: docs/serving/online_serving/token_in_token_out.md, tests/entrypoints/scale_out/token_in_token_out/test_serving_multimodal_tokens.py
- #64156 [Spec Decode] Consistent drafted, verified and accepted token counts [documentation, performance, frontend, speculative-decoding, mrv2, rust, scheduler] (+461/-97) by @tomasruizt files: docs/features/speculative_decoding/acceptance_metrics.md, rust/src/bench/src/benchmark.rs, rust/src/bench/src/output/console.rs, rust/src/bench/src/output/json.rs, rust/src/chat/src/event.rs, rust/src/chat/src/output/structured.rs, rust/src/chat/src/stream.rs, rust/src/engine-core-client/src/metrics.rs, rust/src/engine-core-client/src/protocol/output.rs, rust/src/engine-core-client/src/protocol/stats.rs, rust/src/llm/src/log_stats.rs, rust/src/metrics/src/scheduler.rs
- **`drafted`**: tokens that came out of the drafter, including grammar-invalid ones.
- **`verified` (new)**: drafted tokens that went into the target forward pass.

**First-time contributors:** BugenZhao, PerryZhang01, devshah-cohere, gty111, hickeyma, nien-hui, njhill, tomasruizt
### tests-entrypoints-serve

Summary unavailable (null LLM). Source items:
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py

**First-time contributors:** njhill
### tests-entrypoints-speech_to_text

Summary unavailable (null LLM). Source items:
- #67606 [ROCm][Bugfix] Run the Canary WER correctness test in fp32 [bug, rocm] (+5/-2) by @AndreasKaratzas files: tests/entrypoints/speech_to_text/correctness/test_transcription_api_correctness.py
- The flake is one utterance falling into a greedy repetition loop...

### tests-evals

Summary unavailable (null LLM). Source items:
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py

**First-time contributors:** njhill
### tests-kernels

Summary unavailable (null LLM). Source items:
- #65186 [Perf][GDN] Export Triton prefill checkpoints via per-sequence buffers [documentation, performance, ready, ci/build] (+380/-20) by @specture724 files: .buildkite/test_areas/engine.yaml, tests/kernels/fla/test_chunk_gated_delta_rule.py, tests/v1/e2e/general/test_mamba_prefix_cache.py, vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py, vllm/third_party/flash_linear_attention/ops/chunk.py, vllm/third_party/flash_linear_attention/ops/chunk_delta_h.py
- The existing dense `chunk_gated_delta_rule`...
- #67067 [Perf][Muse Spark] FP8 KV cache for the specialized decode (+939/-190) by @jeejeelee files: tests/kernels/test_muse_spark_fp8_kv_decode.py, vllm/models/muse_spark/nvidia/specialized_decode/cutedsl/attention/attn2.py, vllm/models/muse_spark/nvidia/specialized_decode/cutedsl/attention/kv_format.py, vllm/models/muse_spark/nvidia/specialized_decode/cutedsl/attention/qkv_front.py, vllm/models/muse_spark/nvidia/specialized_decode/cutedsl/common/primitives.py, vllm/models/muse_spark/nvidia/specialized_decode/runtime/__init__.py, vllm/models/muse_spark/nvidia/specialized_decode/runtime/cute_ops.py, vllm/models/muse_spark/nvidia/specialized_decode/runtime/draft.py, vllm/models/muse_spark/nvidia/specialized_decode/runtime/providers.py
- FP8 KV: TPOT -6.0% vs the stock decode at 150k context, gsm8k unchanged.
- FP8 KV with SWA layers kept BF16: TPOT -5.6% vs stock, gsm8k unchanged.
- #65578 [Perf][Kernel] Fuse GELU + NVFP4 quant for BERT-style FFNs [ready, torch.compile, ci/build, quantization] (+128/-80) by @gkswns0531 files: tests/kernels/test_fused_quant_activation.py, vllm/model_executor/layers/fusion/act_nvfp4_quant.py, vllm/model_executor/layers/fusion/fused_act_quant.py, vllm/model_executor/models/bert.py
- #68025 [ROCm][CI] Skip wvSplitKQ fp8 skinny GEMM test where the kernel is not built [rocm, ready] (+7/-0) by @afriedri files: tests/kernels/quantization/test_rocm_skinny_gemms.py
- #67267 [Quant] LUT-B: fit per-channel block32 weight scales [documentation, quantization] (+201/-52) by @mgoin files: docs/features/quantization/online.md, tests/kernels/moe/test_lut_b_moe.py, vllm/model_executor/layers/quantization/utils/lut_b_utils.py
- #45559 [ROCm][Kernel] Extend skinny gemm N=5 to N=8 cases on GFX12 (RDNA4) using  SWMMAC optimization [rocm, ready, ci/build] (+1072/-7) by @keneoneth files: CMakeLists.txt, csrc/rocm/ops.h, csrc/rocm/skinny_gemms.cuh, csrc/rocm/skinny_gemms_swmmac.cu, csrc/rocm/torch_bindings.cpp, tests/kernels/quantization/test_rocm_skinny_gemms.py, tests/model_executor/layers/test_rocm_unquantized_gemm.py, vllm/_custom_ops.py, vllm/model_executor/layers/utils.py
- #65711 [ROCm][Perf] Use tuned AITER Triton `gemm_a8w8` for per-tensor FP8 decode GEMMs on gfx950 [rocm, ready] (+410/-2) by @amd-jrosas files: tests/kernels/quantization/test_rocm_aiter_triton_per_tensor_fp8.py, vllm/_aiter_ops.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/scaled_mm/aiter.py
- #67215 [Bugfix][MiniMax-M3] Drop the stale config read from the FlashInfer indexer builder [bug, ready, ci/build, nvidia, verified, minimax] (+5/-24) by @Jaeyeong-CHOI files: .buildkite/test_areas/kernels.yaml, tests/kernels/attention/test_minimax_m3.py, vllm/models/minimax_m3/nvidia/indexer_flashinfer.py
- #66653 [MoE] Disable expanded DeepEP v2 dispatch in all execution modes [ready, ci/build, nvidia] (+198/-186) by @bnellnm files: .buildkite/test_areas/kernels.yaml, tests/kernels/moe/parallel_utils.py, tests/kernels/moe/test_deepep_v2_async_finalize.py, tests/kernels/moe/test_deepep_v2_moe.py, tests/kernels/moe/test_moe.py, vllm/model_executor/layers/fused_moe/all2all_utils.py, vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py

**First-time contributors:** Isotr0py, Jaeyeong-CHOI, NickLucche, Pb314314, PerkzZheng, Victor49152, aarushjain29, afierka-intel, afriedri, algebra-MCX, amd-jrosas, azaidy, bnellnm, chaojun-zhang, davzhuAMD, gau-nernst, gkswns0531, jbelofamd, jeejeelee, keneoneth, lesj0610, limou102, lishuoshuo-amd, mgoin, njhill, sfeng33, specture724, stecasta, tuukkjs, vgokhale, wangyicong52, zixi-qi, zohaibm-amd
### tests-kernels-moe

Summary unavailable (null LLM). Source items:
- #67267 [Quant] LUT-B: fit per-channel block32 weight scales [documentation, quantization] (+201/-52) by @mgoin files: docs/features/quantization/online.md, tests/kernels/moe/test_lut_b_moe.py, vllm/model_executor/layers/quantization/utils/lut_b_utils.py
- #66653 [MoE] Disable expanded DeepEP v2 dispatch in all execution modes [ready, ci/build, nvidia] (+198/-186) by @bnellnm files: .buildkite/test_areas/kernels.yaml, tests/kernels/moe/parallel_utils.py, tests/kernels/moe/test_deepep_v2_async_finalize.py, tests/kernels/moe/test_deepep_v2_moe.py, tests/kernels/moe/test_moe.py, vllm/model_executor/layers/fused_moe/all2all_utils.py, vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py
- #64406 [Perf][MoE] OCP MX emulation: dequantize only the routed experts [ready, quantization] (+187/-6) by @jbelofamd files: tests/kernels/moe/test_ocp_mx_moe.py, vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe.py
- #64641 [Fast Start] Add weights mirror support for daemon2daemon [documentation, rocm, frontend, ci/build, nvidia] (+2123/-391) by @Isotr0py files: .buildkite/test_areas/distributed.yaml, docs/features/preload.md, tests/kernels/moe/test_flashinfer.py, tests/model_executor/model_loader/test_weight_cache.py, vllm/config/load.py, vllm/entrypoints/cli/preload.py, vllm/model_executor/model_loader/__init__.py, vllm/model_executor/model_loader/utils.py, vllm/model_executor/model_loader/weight_cache/daemon.py, vllm/model_executor/model_loader/weight_cache/ipc_loader.py, vllm/model_executor/model_loader/weight_cache/protocol.py, vllm/model_executor/model_loader/weight_cache/transport.py
- #62807 [XPU][LoRA] Support unquantized MoE LoRA [intel-gpu, ci/build, quantization] (+366/-17) by @chaojun-zhang files: .buildkite/intel_jobs/lora_intel.yaml, tests/kernels/moe/test_unquantized_backend_selection.py, tests/lora/test_fused_moe_lora_kernel.py, vllm/lora/ops/triton_ops/fused_moe_lora_op.py, vllm/lora/punica_wrapper/punica_xpu.py, vllm/model_executor/layers/fused_moe/experts/lora_experts_mixin.py, vllm/model_executor/layers/fused_moe/experts/xpu_moe.py, vllm/model_executor/layers/fused_moe/oracle/unquantized.py
- `XPUExperts` now mixes in `LoRAExpertsMixin` as a single class, mirroring `TritonExperts`. FP8 / BlockFP8 / WNA16 / MXFP4 opt out via `supports_lora()`.
- The ...
- #65974 [MoE][NVIDIA] Support SM107 in flashinfer_moe_ep_cutedsl for NVFP4 experts for FI 0.7.3 [documentation, ready, deepseek, nvidia] (+517/-35) by @Victor49152 files: docs/features/quantization/modelopt.md, docs/serving/expert_parallel_deployment.md, tests/kernels/moe/test_flashinfer_moe_ep.py, tests/models/test_deepseek_v4_fi_moe_ep.py, vllm/config/kernel.py, vllm/model_executor/layers/fused_moe/experts/flashinfer_moe_ep.py, vllm/model_executor/layers/fused_moe/flashinfer_moe_ep.py
- #64753 [Quantization][MoE] Keep NVFP4 expert scales CSF-compressed on the GPU with B12X [ready, quantization] (+295/-8) by @stecasta files: tests/kernels/moe/test_b12x.py, vllm/config/kernel.py, vllm/model_executor/layers/fused_moe/b12x.py, vllm/model_executor/layers/fused_moe/oracle/nvfp4.py, vllm/model_executor/layers/quantization/modelopt.py
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py
- #66799 [Perf][MoE] Mask DP padding rows in grouped top-k routing by default [ready, verified] (+56/-14) by @Pb314314 files: tests/kernels/moe/test_grouped_topk.py, vllm/envs.py, vllm/model_executor/layers/fused_moe/layer.py, vllm/model_executor/layers/fused_moe/router/base_router.py, vllm/model_executor/layers/fused_moe/router/grouped_topk_router.py, vllm/model_executor/layers/fused_moe/router/router_factory.py
- #64086 [Bugfix][MoE] Preserve invalid expert IDs in NIXL round-robin mapping [bug, ready, ci/build, kv-connector, nixl] (+81/-1) by @algebra-MCX files: tests/kernels/moe/test_nixl_prepare_finalize.py, vllm/model_executor/layers/fused_moe/prepare_finalize/nixl_ep.py

**First-time contributors:** Isotr0py, Pb314314, Victor49152, algebra-MCX, bnellnm, chaojun-zhang, jbelofamd, mgoin, njhill, stecasta
### tests-lora

Summary unavailable (null LLM). Source items:
- #62807 [XPU][LoRA] Support unquantized MoE LoRA [intel-gpu, ci/build, quantization] (+366/-17) by @chaojun-zhang files: .buildkite/intel_jobs/lora_intel.yaml, tests/kernels/moe/test_unquantized_backend_selection.py, tests/lora/test_fused_moe_lora_kernel.py, vllm/lora/ops/triton_ops/fused_moe_lora_op.py, vllm/lora/punica_wrapper/punica_xpu.py, vllm/model_executor/layers/fused_moe/experts/lora_experts_mixin.py, vllm/model_executor/layers/fused_moe/experts/xpu_moe.py, vllm/model_executor/layers/fused_moe/oracle/unquantized.py
- `XPUExperts` now mixes in `LoRAExpertsMixin` as a single class, mirroring `TritonExperts`. FP8 / BlockFP8 / WNA16 / MXFP4 opt out via `supports_lora()`.
- The ...
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py

**First-time contributors:** chaojun-zhang, njhill
### tests-models

Summary unavailable (null LLM). Source items:
- #62590 [ROCm][Perf][Qwen4Exp] Tune sparse GQA prefill profile on gfx942 and gfx950 [rocm, ready, qwen] (+15/-0) by @tc3oliver files: tests/models/qwen4_exp/test_qsa_amd.py, vllm/models/qwen4_exp/amd/ops/qsa.py
- #65656 [Perf][DSV4.1] Accelerate candidate prefill and decode with CuTe [ready, ci/build, deepseek, DSv4.1] (+1538/-24) by @chaunceyjiang files: .buildkite/test_areas/kernels.yaml, tests/model_executor/layers/test_mla_short_prefill_indexer.py, tests/models/deepseek_v41/nvidia/test_candidate_indexer.py, vllm/config/attention.py, vllm/model_executor/models/config.py, vllm/models/deepseek_v41/attention.py, vllm/models/deepseek_v41/nvidia/ops/candidate_indexer.py, vllm/models/deepseek_v41/nvidia/ops/candidate_paged_logits.py
- #68005 [Bugfix][DSv4.1] Import the SM80/SM90 metadata builders lazily [bug, deepseek] (+34/-25) by @Thangnguyenvn98 files: tests/models/deepseek_v41/nvidia/specialized_decode/test_metadata_graph_state.py, vllm/models/deepseek_v41/nvidia/specialized_decode/runtime/metadata_graphs.py
- #67094 [Spec Decode] Add DSpine support [documentation, new-model, speculative-decoding, ready, ci/build, qwen, mrv2, dflash] (+569/-21) by @shanjiaz files: .buildkite/test_areas/spec_decode.yaml, docs/features/speculative_decoding/README.md, tests/models/registry.py, tests/v1/e2e/spec_decode/acceptance_rates/dflash/test_dflash.py, vllm/model_executor/models/qwen3_dspine.py, vllm/model_executor/models/registry.py, vllm/transformers_utils/configs/eagle.py, vllm/transformers_utils/configs/speculators/algos.py, vllm/transformers_utils/configs/speculators/base.py, vllm/v1/worker/gpu/spec_decode/dflash2/speculator.py, vllm/v1/worker/gpu/spec_decode/dspine/__init__.py, vllm/v1/worker/gpu/spec_decode/dspine/config.py
- Supports Tencent and Speculators checkpoint layouts through one model implementation.
- Reuses existing candidate sampli...
- #59208 [Bugfix][Distributed] Guard cross-node symmetric-memory rendezvous [bug, torch.compile, ci/build, kimi, k3] (+503/-16) by @mickaelseznec files: .buildkite/test_areas/distributed.yaml, tests/distributed/test_custom_all_reduce.py, tests/distributed/test_dcp_direct_a2a_lse_reduce.py, tests/distributed/test_nvlink_fabric.py, tests/distributed/test_symm_mem_allreduce.py, tests/models/kimi_k3/test_latent_moe_tail.py, vllm/distributed/device_communicators/custom_all_reduce.py, vllm/distributed/device_communicators/nvlink_fabric.py, vllm/distributed/device_communicators/symm_mem.py, vllm/envs.py, vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py, vllm/models/kimi_k3/nvidia/latent_moe_runner.py
- classifies gr...
- #63086 [ROCm][Kimi-K3] Enable encoder graph capture for Kimi-K3 Vision Tower [rocm, ready, torch.compile, ci/build, multi-modality, nvidia, kimi, k3] (+394/-0) by @samutamm files: tests/models/multimodal/generation/test_vit_cudagraph.py, vllm/models/kimi_k3/amd/encoder_cudagraph.py, vllm/models/kimi_k3/amd/model.py
- #67984 [ROCm][Bugfix] Port Mistral Large 4 AMD indexer cache to get_kv_cache_config [bug, rocm, ready, mistral] (+24/-5) by @xaguilar-amd files: tests/models/mistral/test_fused_ops.py, vllm/models/mistral/amd/indexer.py, vllm/models/mistral/amd/ops/indexer.py
- Fixes th...
- #64176 [ROCm][CI] Re-enable VLLM_GPU_SYNC_CHECK=error in the ROCm test image [bug, rocm, ci/build, deepseek, DSv4] (+29/-5) by @AndreasKaratzas files: docker/Dockerfile.rocm, tests/models/test_dsv41_mono_layers.py, tests/models/test_dsv4_mono_layers.py

**First-time contributors:** JaredforReal, LantaoJin, NickLucche, PerkzZheng, PerryZhang01, Ronald1995, Thangnguyenvn98, Victor49152, aarushjain29, azaidy, chaunceyjiang, chuncaohenli, cjackal, cycancode, gau-nernst, gordan12, gty111, hlin99, hmellor, ilmarkov, khluu, limou102, mickaelseznec, njhill, paulpak58, qianlihuang, samutamm, shadowmodder, shanjiaz, subhashpolisetti, tc3oliver, wangyicong52, xaguilar-amd, xs1128, xsxszab, yannicks1, yibol9768-alt, zRzRzRzRzRzRzR, zixi-qi, zzznnn-1
### tests-models-pooling

Summary unavailable (null LLM). Source items:
- #67888 [CI] Fix SPLADE late-interaction reset test after ec_connector.reset() (#66846) [ready, pooling] (+2/-0) by @PerryZhang01 files: tests/models/language/pooling/test_splade_sparse_pooler.py
- #67716 [CI] Load gte-Qwen2 without remote code in test_non_causal_models [ready, qwen, pooling] (+3/-1) by @hmellor files: tests/models/language/pooling/test_auto_prefix_cache_support.py
- gte-Qwen2's remote `modeling_qwen.py` has no `"vllm"...
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py
- #67533 [Chore] Remove deprecated `rope_scaling` usage and forbid it in pre-commit [ready, torch.compile, deepseek, rust, kimi, pooling, recipe] (+116/-218) by @hmellor files: .pre-commit-config.yaml, recipes/models/MiniMaxAI/MiniMax-M3.yaml, rust/src/cmd/src/cli/tests.rs, tests/model_executor/test_bailing_mrope.py, tests/models/language/pooling/test_nomic_max_model_len.py, tests/transformers_utils/test_bailing_moe_v3_vl_config.py, tests/v1/attention/test_sparse_mla_backends.py, tools/pre_commit/check_forbidden_strings.py, vllm/compilation/passes/fusion/qk_norm_rope_kvcache_fusion.py, vllm/config/speculative.py, vllm/model_executor/layers/mamba/linear/bailing_linear_attn.py, vllm/model_executor/models/bailing_moe_linear.py
- On the Transformers floor (5.16.1), `config.rope_scaling` is a property returning `config.rope_parameters`, s...
- #62785 [Bugfix][Pooling] Honor the CrossEncoder activation saved by Sentence Transformers v6 [bug, documentation, ready, multi-modality, llama, pooling] (+77/-5) by @cycancode files: docs/models/pooling_models/scoring.md, tests/models/multimodal/pooling/test_llama_nemotron_vl.py, vllm/transformers_utils/config.py

**First-time contributors:** PerryZhang01, cycancode, hmellor, njhill
### tests-models-transformers

Summary unavailable (null LLM). Source items:
- #67519 [Bugfix] Fix EAGLE-3 on Transformers backend VLMs [bug, speculative-decoding, ready] (+47/-47) by @hmellor files: tests/models/transformers/test_backend.py, tests/v1/e2e/spec_decode/eagle/test_eagle_correctness.py, vllm/model_executor/models/transformers/base.py
- EAGLE-3 works with VLMs on the Transformers backend (e.g. Qwen2.5-VL, Idefics3) instead of failing at startup with `assert isinstance(model_output, tuple)`.
- Re-enables the `qwen3_eagle3-transformers` EAGLE-3 ...

**First-time contributors:** hmellor
### tests-multimodal

Summary unavailable (null LLM). Source items:
- #67611 [Bugfix][Audio] Treat zero decode limits as disabled [bug, ready, multi-modality] (+114/-7) by @Woolgathererer files: tests/multimodal/media/test_audio.py, vllm/multimodal/media/audio.py
- `VLLM_MAX_AUDIO_DECODE_DURATION_S=0` and `VLLM_MAX_AUD...
- #67632 [Model] Remove OpenPangu-VL [documentation, ready, multi-modality] (+27/-1818) by @hmellor files: docs/models/supported_models.md, examples/generate/multimodal/vision_language_multi_image_offline.py, examples/generate/multimodal/vision_language_offline.py, tests/models/multimodal/test_openpangu_vl.py, tests/models/registry.py, tests/multimodal/test_video.py, vllm/model_executor/layers/rotary_embedding/__init__.py, vllm/model_executor/layers/rotary_embedding/mrope_interleaved.py, vllm/model_executor/models/openpangu.py, vllm/model_executor/models/openpangu_vl.py, vllm/model_executor/models/registry.py, vllm/multimodal/video.py
- https://github.com/vllm-project/vllm/pull/56390 (`openpangu` video loader `num_frames=-1` crash)
- `FreedomIntelligence/openPang...
- #66473 [Bugfix][Multimodal] Domain-separate content digests and caller uuids in mm hashes [bug, ready, multi-modality, deepseek] (+61/-8) by @shadowmodder files: tests/models/multimodal/processing/test_deepseek_vl2.py, tests/models/multimodal/processing/test_h2ovl.py, tests/models/multimodal/processing/test_unlimited_ocr.py, tests/multimodal/test_processing.py, vllm/multimodal/processing/inputs.py

**First-time contributors:** Woolgathererer, hmellor, shadowmodder
### tests-multimodal-media

Summary unavailable (null LLM). Source items:
- #67611 [Bugfix][Audio] Treat zero decode limits as disabled [bug, ready, multi-modality] (+114/-7) by @Woolgathererer files: tests/multimodal/media/test_audio.py, vllm/multimodal/media/audio.py
- `VLLM_MAX_AUDIO_DECODE_DURATION_S=0` and `VLLM_MAX_AUD...

**First-time contributors:** Woolgathererer
### tests-nemotron

Summary unavailable (null LLM). Source items:
- #62785 [Bugfix][Pooling] Honor the CrossEncoder activation saved by Sentence Transformers v6 [bug, documentation, ready, multi-modality, llama, pooling] (+77/-5) by @cycancode files: docs/models/pooling_models/scoring.md, tests/models/multimodal/pooling/test_llama_nemotron_vl.py, vllm/transformers_utils/config.py

**First-time contributors:** cycancode
### tests-quantization

Summary unavailable (null LLM). Source items:
- #63272 [ROCm][Quantization][Perf] Fuse the block Hadamard input rotation into AITER's MXFP4 activation quant [documentation, rocm, ready, ci/build, quantization] (+179/-30) by @mjkvaak-amd files: tests/quantization/test_input_hadamard.py, tests/quantization/test_online_mxfp4.py, vllm/model_executor/kernels/linear/mxfp4/aiter.py, vllm/model_executor/kernels/linear/mxfp4/base.py, vllm/model_executor/layers/quantization/input_hadamard.py, vllm/model_executor/layers/quantization/online/mxfp4.py, vllm/model_executor/layers/quantization/quark/quark.py, vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py
- #66497 [Model][DSv4.1] DeepSeek-V4.1 on A100 (SM80) and H100 (SM90) [ready, ci/build, deepseek, nvidia, specialized] (+15394/-80) by @yaoyaoding files: .buildkite/test_areas/models_basic.yaml, tests/kernels/mhc/test_mhc_kernels.py, tests/models/deepseek_v41/nvidia/conftest.py, tests/models/deepseek_v41/nvidia/specialized_decode/ampere/__init__.py, tests/models/deepseek_v41/nvidia/specialized_decode/ampere/reference.py, tests/models/deepseek_v41/nvidia/specialized_decode/ampere/test_all_gather.py, tests/models/deepseek_v41/nvidia/specialized_decode/ampere/test_all_reduce.py, tests/models/deepseek_v41/nvidia/specialized_decode/ampere/test_gemv.py, tests/models/deepseek_v41/nvidia/specialized_decode/ampere/test_indexer_row_shard.py, tests/models/deepseek_v41/nvidia/specialized_decode/ampere/test_kernels.py, tests/models/deepseek_v41/nvidia/specialized_decode/ampere/test_mhc.py, tests/models/deepseek_v41/nvidia/specialized_decode/ampere/test_mhc_projection.py
- #67917 [CI][Test] Compare logprobs in the Machete bf16 repeat-run test [ready, nvidia] (+14/-5) by @khluu files: tests/quantization/test_cutlass_w4a16.py
- #67006 [Quantization] Online weight-only NVFP4 for dense linear layers [documentation, ready, nvidia, quantization] (+349/-63) by @stecasta files: docs/features/quantization/online.md, tests/model_executor/kernels/test_b12x_linear.py, tests/quantization/test_online.py, vllm/config/quantization.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/nvfp4/b12x.py, vllm/model_executor/kernels/linear/nvfp4/base.py, vllm/model_executor/kernels/linear/nvfp4/flashinfer.py, vllm/model_executor/layers/quantization/__init__.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/lm_head.py, vllm/model_executor/layers/quantization/online/nvfp4.py
- #67938 [ROCm][CI] Widen the bound of test_quark_online_rotation_wikitext [rocm, ready] (+4/-2) by @bogdan-petkovic files: tests/quantization/test_quark.py
- #65802 [Model Loader] Direct reload of online-quantized modules [documentation, ready, gpt-oss, quantization, kimi] (+411/-25) by @hao-aaron files: docs/features/quantization/online.md, docs/training/direct_reload.md, docs/training/layerwise.md, docs/training/weight_transfer/README.md, tests/model_executor/model_loader/test_direct_reload.py, tests/quantization/test_online_loading.py, vllm/config/vllm.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/loading.py, vllm/model_executor/model_loader/reload/plan.py, vllm/model_executor/models/gpt_oss.py
- #66118 [RL][Model Loader] Load FP8 indexer wk and MLA projections independently, as FP8 or BF16, in any scale layout [ready, ci/build, deepseek, quantization] (+908/-907) by @hao-aaron files: .buildkite/test_areas/quantization.yaml, tests/model_executor/model_loader/test_deepseek_v32_weight_loading.py, tests/quantization/test_fp8_dequant.py, tests/quantization/test_quark.py, vllm/model_executor/layers/quantization/dequant_linear.py, vllm/model_executor/layers/quantization/utils/quant_utils.py, vllm/model_executor/layers/sparse_attn_indexer.py, vllm/model_executor/models/deepseek_mtp.py, vllm/model_executor/models/deepseek_v2.py, vllm/models/deepseek_v32/amd/model.py, vllm/models/deepseek_v32/amd/mtp.py, vllm/models/deepseek_v32/attention.py
- #62708 [ROCm][Quantization] Add load-time int4 lm_head quantization for RDNA… [documentation, rocm, ready, quantization] (+705/-14) by @xiao-llm files: docs/features/quantization/online.md, tests/quantization/test_online_int4_lm_head.py, vllm/config/quantization.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/int4.py, vllm/model_executor/layers/quantization/online/lm_head.py
- #67752 [CI][Test] Patch the platform class, not the instance, in the humming quantization tests [ready, quantization] (+10/-3) by @khluu files: tests/quantization/test_humming_mxfp4_block_fp8.py
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py
- #67568 [Cherry-pick][v0.34.0] [Model] Add Mistral Large 4 (#64534) [new-model, rocm, speculative-decoding, ci/build, kv-connector, nvidia, quantization, mrv2, mistral, dflash, hisparse] (+20702/-199) by @NickLucche files: .buildkite/test_areas/models_basic.yaml, tests/distributed/test_dcp_a2a.py, tests/distributed/test_dcp_direct_a2a_lse_reduce.py, tests/kernels/attention/test_triton_decode_attention.py, tests/models/mistral/mistral_large4/amd_specialized_decode/__init__.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_fp8_kv_cache.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_runtime.py, tests/models/mistral/test_fused_ops.py, tests/models/mistral/test_ml4_dspark.py, tests/models/registry.py, tests/quantization/test_modelopt.py, tests/quantization/test_quark.py
- `mla_attention.py`: keeps the `prepare_mqa_query` / `_prepare_mqa_query` re...

**First-time contributors:** MadhavJivrajani, NickLucche, afriedri, bogdan-petkovic, fxmarty-amd, gau-nernst, hao-aaron, khluu, mgoin, mjkvaak-amd, njhill, riceharvest, stecasta, xiao-llm
### tests-quark

Summary unavailable (null LLM). Source items:
- #67938 [ROCm][CI] Widen the bound of test_quark_online_rotation_wikitext [rocm, ready] (+4/-2) by @bogdan-petkovic files: tests/quantization/test_quark.py
- #66118 [RL][Model Loader] Load FP8 indexer wk and MLA projections independently, as FP8 or BF16, in any scale layout [ready, ci/build, deepseek, quantization] (+908/-907) by @hao-aaron files: .buildkite/test_areas/quantization.yaml, tests/model_executor/model_loader/test_deepseek_v32_weight_loading.py, tests/quantization/test_fp8_dequant.py, tests/quantization/test_quark.py, vllm/model_executor/layers/quantization/dequant_linear.py, vllm/model_executor/layers/quantization/utils/quant_utils.py, vllm/model_executor/layers/sparse_attn_indexer.py, vllm/model_executor/models/deepseek_mtp.py, vllm/model_executor/models/deepseek_v2.py, vllm/models/deepseek_v32/amd/model.py, vllm/models/deepseek_v32/amd/mtp.py, vllm/models/deepseek_v32/attention.py
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py
- #67568 [Cherry-pick][v0.34.0] [Model] Add Mistral Large 4 (#64534) [new-model, rocm, speculative-decoding, ci/build, kv-connector, nvidia, quantization, mrv2, mistral, dflash, hisparse] (+20702/-199) by @NickLucche files: .buildkite/test_areas/models_basic.yaml, tests/distributed/test_dcp_a2a.py, tests/distributed/test_dcp_direct_a2a_lse_reduce.py, tests/kernels/attention/test_triton_decode_attention.py, tests/models/mistral/mistral_large4/amd_specialized_decode/__init__.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_fp8_kv_cache.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_runtime.py, tests/models/mistral/test_fused_ops.py, tests/models/mistral/test_ml4_dspark.py, tests/models/registry.py, tests/quantization/test_modelopt.py, tests/quantization/test_quark.py
- `mla_attention.py`: keeps the `prepare_mqa_query` / `_prepare_mqa_query` re...
- #67549 [CI/Build] Fix docstring Markdown style in test_quark.py [ready] (+1/-1) by @MadhavJivrajani files: tests/quantization/test_quark.py
- `check-docstring-style` passes again on `main`. Before this fix it failed with the error below ([failing run on main](https://github.com/vllm-project/vllm/actions/runs/43499925550)):
- #65951 [Bugfix][Quantization] Handle dict-valued Quark `algo_config` in `maybe_update_config` [bug, ready, quantization] (+14/-0) by @afriedri files: tests/quantization/test_quark.py, vllm/model_executor/layers/quantization/quark/quark.py
- #64534 [Model] Add Mistral Large 4 [documentation, new-model, rocm, structured-output, frontend, speculative-decoding, ready, ci/build, tool-calling, deepseek, cpu, kv-connector, nvidia, quantization, mrv2, mistral, dflash, kv-cache-manager, hisparse, nixl] (+20739/-226) by @NickLucche files: .buildkite/test_areas/models_basic.yaml, tests/distributed/test_dcp_a2a.py, tests/distributed/test_dcp_direct_a2a_lse_reduce.py, tests/kernels/attention/test_triton_decode_attention.py, tests/models/mistral/mistral_large4/amd_specialized_decode/__init__.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_fp8_kv_cache.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_runtime.py, tests/models/mistral/test_fused_ops.py, tests/models/mistral/test_ml4_dspark.py, tests/models/registry.py, tests/quantization/test_modelopt.py, tests/quantization/test_quark.py
- Mistral-Large-4-1T-A52B (FP8) and -NVFP4 on model runner V2
- Sparse MLA with the DSA indexer, cross-layer KV sharing, SSMax
- DSpark speculative decoding

**First-time contributors:** MadhavJivrajani, NickLucche, afriedri, bogdan-petkovic, hao-aaron, njhill
### tests-renderers

Summary unavailable (null LLM). Source items:
- #67316 [Bugfix][Security] Check the uncompressed size of embedding archives before torch.load [bug, documentation, ready, multi-modality] (+118/-3) by @LeizhenZhang files: docs/usage/security.md, tests/renderers/test_sparse_tensor_validation.py, vllm/multimodal/media/audio.py, vllm/multimodal/media/image.py, vllm/multimodal/media/video.py, vllm/renderers/embed_utils.py, vllm/utils/sparse_utils.py
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py

**First-time contributors:** LeizhenZhang, njhill
### tests-rocm

Summary unavailable (null LLM). Source items:
- #68025 [ROCm][CI] Skip wvSplitKQ fp8 skinny GEMM test where the kernel is not built [rocm, ready] (+7/-0) by @afriedri files: tests/kernels/quantization/test_rocm_skinny_gemms.py
- #45559 [ROCm][Kernel] Extend skinny gemm N=5 to N=8 cases on GFX12 (RDNA4) using  SWMMAC optimization [rocm, ready, ci/build] (+1072/-7) by @keneoneth files: CMakeLists.txt, csrc/rocm/ops.h, csrc/rocm/skinny_gemms.cuh, csrc/rocm/skinny_gemms_swmmac.cu, csrc/rocm/torch_bindings.cpp, tests/kernels/quantization/test_rocm_skinny_gemms.py, tests/model_executor/layers/test_rocm_unquantized_gemm.py, vllm/_custom_ops.py, vllm/model_executor/layers/utils.py
- #65711 [ROCm][Perf] Use tuned AITER Triton `gemm_a8w8` for per-tensor FP8 decode GEMMs on gfx950 [rocm, ready] (+410/-2) by @amd-jrosas files: tests/kernels/quantization/test_rocm_aiter_triton_per_tensor_fp8.py, vllm/_aiter_ops.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/scaled_mm/aiter.py
- #66032 [ROCm][CI] Make /ci rocm cache a cache-only CI build that also copies the runtime [documentation, rocm, ci/build] (+265/-59) by @AndreasKaratzas files: .buildkite/image_build/amd_rocm_cache.yaml, .buildkite/scripts/rocm/build.sh, .github/workflows/scripts/run_ci_command.py, .github/workflows/scripts/test_run_ci_command.py, docs/contributing/README.md, tests/tools/test_rocm_build.py
- The cache build is a `main` build of the ci pipeline that runs only the new `rocm-ba...
- #67845 [CI][ROCm] Fix the DSv4.1 sparse MLA forward_mqa test after #66842 [rocm, ready, ci/build, deepseek, verified] (+9/-0) by @LantaoJin files: .buildkite/test-amd.yaml, .buildkite/test_areas/attention.yaml, tests/v1/attention/test_rocm_aiter_triton_sparse_mla.py
- #66842 made `DeepseekV41ROCMAiterMLAAttention.forward_mqa` read `self.use...
- #65985 [ROCm][Muse Spark] DSpark draft layers as one persistent FlyDSL launch (--monokernel) [rocm, ready, ci/build, verified, dflash] (+2422/-20) by @azaidy files: .buildkite/test_areas/models_basic.yaml, tests/models/test_muse_spark_rocm_drafter.py, vllm/models/muse_spark/amd/dspark.py, vllm/models/muse_spark/amd/mono/decoder.py, vllm/models/muse_spark/amd/mono/drafter.py, vllm/models/muse_spark/amd/mono/kernels/attn_frag.py, vllm/models/muse_spark/amd/mono/kernels/draft.py
- #67377 [Perf][ROCm][DSv4.1] DeepSeek-V4.1-Flash: dense MXFP8 GEMMs and wo_a on AITER's tuned FlyDSL kernels, and a faster MXFP8 activation quant (MI355X) [rocm, ready, deepseek, quantization, verified] (+286/-24) by @limou102 files: tests/kernels/quantization/test_rocm_mxfp8_linear.py, tests/models/test_dsv41_mono_numerics.py, vllm/_aiter_ops.py, vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py, vllm/model_executor/kernels/linear/mxfp8/rocm_native.py, vllm/model_executor/layers/quantization/utils/mxfp8_utils.py, vllm/models/deepseek_v41/amd/mono_decode.py, vllm/v1/attention/ops/rocm_aiter_mla_sparse.py
- #67297 [Perf] Use `slots=True` on all internal dataclasses [performance, rocm, structured-output, frontend, speculative-decoding, ready, ray, torch.compile, multi-modality, tool-calling, llama, qwen, deepseek, cpu, gpt-oss, kv-connector, nvidia, quantization, mrv2, mistral] (+995/-966) by @njhill files: benchmarks/attention_benchmarks/batch_spec.py, benchmarks/attention_benchmarks/common.py, benchmarks/backend_request_func.py, benchmarks/benchmark_prefix_caching.py, benchmarks/benchmark_serving_structured_output.py, benchmarks/benchmark_topk_topp.py, benchmarks/fused_kernels/layernorm_rms_benchmarks.py, benchmarks/fused_kernels/silu_mul_block_quant_benchmark.py, benchmarks/kernels/benchmark_2d_silu_mul_fp8_quant.py, benchmarks/kernels/benchmark_gdn_chunk.py, benchmarks/kernels/benchmark_kimi_k3_attn_res.py, benchmarks/kernels/benchmark_lora.py
- #66933 [ROCm] M3.1 GEMM improvements [rocm, ready] (+74/-2) by @vgokhale files: tests/kernels/test_gate_linear_rocm_dispatch.py, vllm/model_executor/layers/fused_moe/router/gate_linear.py
- #67555 [ROCm][CI] Stub dcp_world_size in the merged-cache sparse MLA test [rocm, ready] (+7/-2) by @aarushjain29 files: tests/kernels/attention/test_rocm_triton_attn_dsv4.py, tests/v1/test_outputs.py

**First-time contributors:** LantaoJin, aarushjain29, afriedri, amd-jrosas, azaidy, keneoneth, limou102, njhill, vgokhale, zohaibm-amd
### tests-v1-core

Summary unavailable (null LLM). Source items:
- #66938 [Perf][Mamba] Optimize prefill splits for mid-block resume (3 forward passes to 1) [kv-cache-manager] (+293/-7) by @wzhao18 files: tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py, tests/v1/core/test_mamba_align_chunk_split.py, tests/v1/e2e/general/test_mamba_prefix_cache.py, vllm/v1/core/single_type_kv_cache_manager.py, vllm/v1/kv_cache_interface.py
- #62056 [Feature][AuxOutput] Support routed experts with P/D disaggregation [frontend, ready, kv-connector, scheduler] (+200/-92) by @faresobeid files: tests/config/test_aux_output_config.py, tests/distributed/aux_output_connector/test_store.py, tests/v1/core/test_scheduler.py, vllm/config/vllm.py, vllm/distributed/aux_output_connector/connector.py, vllm/distributed/aux_output_connector/worker.py
- The prefill instance (`max_tokens=1`) returns rows `[0, R)`. `R` is the prompt length minus the KV connector's prefill backoff.
- The proxy sen...
- #67717 [Bugfix][Mamba] Don't cache a block that a mid-block prefill resume ran past [bug, ready, kv-cache-manager] (+175/-0) by @wzhao18 files: tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py, vllm/v1/core/single_type_kv_cache_manager.py
- #65534 [Core][MM] Make the multimodal encoder cache size configurable  [ready, cpu, mrv2] (+174/-8) by @HangruiCao2000 files: tests/v1/core/test_encoder_cache_manager.py, tests/v1/worker/test_encoder_runner.py, vllm/config/scheduler.py, vllm/engine/arg_utils.py, vllm/v1/core/encoder_cache_manager.py, vllm/v1/worker/cpu/encoder_runner.py, vllm/v1/worker/gpu/mm/encoder_runner.py, vllm/v1/worker/utils.py
- **What:** `SchedulerConfig.encoder_cache_size` is derived from `max_num_batched_tokens` and is `Field(init=False)` with a standing `# TODO (ywang96): Make this configurable.` This adds `--encoder-cache-size`. `None` keeps today's derivation, so **no behaviour change unless it is set**.
- **Why:** they are different quantities. `max_num_encoder_input_tokens` is a per-step **c...
- #67599 [Bugfix][AuxOutput] Size the routed-experts row cache from one source [bug, ready, scheduler] (+99/-36) by @aoshen02 files: tests/distributed/aux_output_connector/test_store.py, tests/model_executor/test_routed_experts_capture.py, tests/v1/core/test_scheduler.py, vllm/distributed/aux_output_connector/connector.py, vllm/distributed/aux_output_connector/worker.py, vllm/model_executor/layers/fused_moe/routed_experts_capturer.py, vllm/v1/core/sched/scheduler.py
- The scheduler (`AuxOutputSchedulerConnector._capacity`) keeps `num_blocks` KV blocks of rows, doubled when a KV connector is configured, and ignores `aux_output_config.max_bytes`.
- The worker store (`initialize_output_storage`) uses `max_bytes` when set, otherwise `num_blocks * hashes_per_kv_block` objects, with ...
- #64156 [Spec Decode] Consistent drafted, verified and accepted token counts [documentation, performance, frontend, speculative-decoding, mrv2, rust, scheduler] (+461/-97) by @tomasruizt files: docs/features/speculative_decoding/acceptance_metrics.md, rust/src/bench/src/benchmark.rs, rust/src/bench/src/output/console.rs, rust/src/bench/src/output/json.rs, rust/src/chat/src/event.rs, rust/src/chat/src/output/structured.rs, rust/src/chat/src/stream.rs, rust/src/engine-core-client/src/metrics.rs, rust/src/engine-core-client/src/protocol/output.rs, rust/src/engine-core-client/src/protocol/stats.rs, rust/src/llm/src/log_stats.rs, rust/src/metrics/src/scheduler.rs

**First-time contributors:** HangruiCao2000, aoshen02, faresobeid, tomasruizt, wzhao18
### tests-v1-determinism

Summary unavailable (null LLM). Source items:
- #67806 [Bugfix] Select only batch-invariant MXFP8 linear kernels under VLLM_BATCH_INVARIANT [bug, quantization, batch-invariance] (+116/-2) by @sfeng33 files: tests/kernels/quantization/test_mxfp8_kernel_selection.py, tests/v1/determinism/test_mx_linear_batch_invariant.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel.py, vllm/model_executor/kernels/linear/mxfp8/emulation.py, vllm/model_executor/kernels/linear/mxfp8/humming.py, vllm/model_executor/kernels/linear/mxfp8/rocm_native.py

**First-time contributors:** sfeng33
### tests-v1-kv_connector

Summary unavailable (null LLM). Source items:
- #64574 [Bugfix][ROCm][KV Connector] MoRIIO: fix port collision with TP > 1 and DP > 1 [bug, rocm, ready, kv-connector] (+279/-41) by @lucasliao0403 files: tests/v1/kv_connector/unit/moriio/test_moriio_pipeline_parallel.py, tests/v1/kv_connector/unit/moriio/test_moriio_read_tp.py, tests/v1/kv_connector/unit/moriio/test_moriio_remote_pod.py, tests/v1/kv_connector/unit/moriio/test_moriio_write_done_routing.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py
- A MoRIIO instance with TP > 1 and DP > 1 (here prefill TP2 x DP2 x EP4) starts and serves requests. Before this change, prefill hung at ...
- #65575 [KV Connector][Mooncake] Fail pulls from a lost prefill worker [documentation, ready, kv-connector, mooncake] (+167/-5) by @CJJ1008 files: docs/features/mooncake_connector_usage.md, tests/v1/kv_connector/unit/test_mooncake_connector.py, tests/v1/kv_connector/unit/test_mooncake_stats.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py, vllm/utils/network_utils.py
- #66583 [KV Offload] Set the CPU tier up in the background under async_init [documentation, ready, kv-connector, nixl] (+390/-25) by @Etelis files: docs/features/kv_offloading_usage.md, tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py, tests/v1/kv_connector/unit/offloading_connector/test_worker.py, tests/v1/kv_connector/unit/offloading_connector/utils.py, tests/v1/kv_offload/cpu/test_shared_offload_region.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/common.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py, vllm/v1/kv_offload/base.py, vllm/v1/kv_offload/cpu/gpu_worker.py, vllm/v1/kv_offload/cpu/shared_offload_region.py, vllm/v1/kv_offload/cpu/spec.py
- The setup thread switches itself to relaxed capture mode, so pinning can't invalid...
- #65672 [Bugfix][Mooncake] Make early prefill abort cleanup idempotent [bug, documentation, ready, kv-connector, mooncake] (+32/-3) by @staryxchen files: tests/v1/kv_connector/unit/test_mooncake_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py
- An abort that reaches `record_send_reqs` before a transfer record exists, or after that record was ...
- #67486 [Bugfix][KV Offload] Avoid false flushes for shared Full Attention prefixes [bug, ready, kv-connector] (+189/-12) by @Alex-ai-future files: tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py
- A new request that shares Full Attention prefix blocks no longer adds the prior request's pending store to `jobs_to_flush`, avoiding an unnecessary wait.
- A genuinely reallocat...
- #67656 [Perf][KV Connector][MooncakeConnector] Submit Mooncake transfer descriptors with array API [ready, kv-connector, mooncake] (+421/-193) by @zhou-yuhan files: tests/v1/kv_connector/unit/test_mooncake_connector.py, tests/v1/kv_connector/unit/test_mooncake_connector_hma.py, tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py, tests/v1/kv_connector/unit/test_mooncake_stats.py, tests/v1/kv_connector/unit/test_mooncake_transfer_backend.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/transfer/backend.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/transfer/te.py
- #62474 [Bugfix][ROCm][MoRIIO] Slice WRITE heads by each layer's head count [bug, rocm, ready, kv-connector] (+179/-14) by @tjtanaa files: tests/v1/kv_connector/unit/moriio/test_moriio_hetero_tp_write.py, tests/v1/kv_connector/unit/moriio/test_moriio_write_done_routing.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py

**First-time contributors:** Alex-ai-future, CAICAIIs, CJJ1008, Etelis, SyaOtiLan, avininjamay8, charxwu, itayalroy, ketor, liusy58, lucasliao0403, seyfal, staryxchen, tjtanaa, zhou-yuhan
### tests-v1-kv_offload

Summary unavailable (null LLM). Source items:
- #66583 [KV Offload] Set the CPU tier up in the background under async_init [documentation, ready, kv-connector, nixl] (+390/-25) by @Etelis files: docs/features/kv_offloading_usage.md, tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py, tests/v1/kv_connector/unit/offloading_connector/test_worker.py, tests/v1/kv_connector/unit/offloading_connector/utils.py, tests/v1/kv_offload/cpu/test_shared_offload_region.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/common.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py, vllm/v1/kv_offload/base.py, vllm/v1/kv_offload/cpu/gpu_worker.py, vllm/v1/kv_offload/cpu/shared_offload_region.py, vllm/v1/kv_offload/cpu/spec.py
- The setup thread switches itself to relaxed capture mode, so pinning can't invalid...
- #62058 [KV Offload] Explain EFAULT from a full /dev/shm in _madvise_populate_write [ready, hisparse, nixl] (+48/-1) by @mushroomcarbon files: tests/v1/kv_offload/cpu/test_shared_offload_region.py, vllm/v1/kv_offload/cpu/shared_offload_region.py
- #67788 [Bugfix][KV Offload] Report transferred bytes in tiering metrics [bug, ready, nixl] (+35/-0) by @waizuichougou files: tests/v1/kv_offload/tiering/test_metrics.py, tests/v1/kv_offload/tiering/test_tiering_offloading.py, vllm/v1/kv_offload/tiering/metrics.py
- Avoid counting FS blocks skipped because they already exist as bytes written.
- Preserve the existing fallback and partial-failure accounting.
- Tests cover reported byte counts, including z...
- #67258 [KV Offload] Add mmap_path to SharedOffloadRegion [ready, nixl] (+75/-6) by @omerpaz95 files: tests/v1/kv_offload/cpu/test_shared_offload_region.py, vllm/v1/kv_offload/cpu/shared_offload_region.py
- #67607 [KV Offload][Bugfix] Hold P2P e2e test ports until the tiers bind them [bug, ready, nixl] (+34/-18) by @AndreasKaratzas files: tests/v1/kv_offload/tiering/test_p2p_lifecycle_e2e.py
- The P2P lifecycle e2e tests no longer release their ZMQ control ports before the engines bind them. Each port stays reserved from f...
- #63524 [Bugfix][KV Offload] Report only written blocks from fs tier store jobs [bug, ready, nixl] (+177/-33) by @AdvayMonga files: csrc/fs_io.cpp, tests/v1/kv_offload/tiering/test_backpressure.py, tests/v1/kv_offload/tiering/test_fs_tier.py, tests/v1/kv_offload/tiering/test_tiering_offloading.py, vllm/v1/kv_offload/tiering/fs/io.py, vllm/v1/kv_offload/tiering/fs/manager.py

**First-time contributors:** AdvayMonga, Etelis, mushroomcarbon, omerpaz95, waizuichougou
### tools

Summary unavailable (null LLM). Source items:
- #66672 [CI][ROCm] Bake torchao into the ROCm test image off the default path and re-enable MI300/MI355 Quantization [rocm, ci/build, quantization] (+196/-131) by @Thangnguyenvn98 files: .buildkite/test-amd.yaml, .buildkite/test_areas/quantization.yaml, .pre-commit-config.yaml, docker/Dockerfile, docker/Dockerfile.rocm, requirements/test/quantization_deps.in, requirements/test/quantization_deps_cuda.txt, requirements/test/quantization_deps_rocm.txt, tools/pre_commit/test_tethering_allowlist.txt
**Stacked on #66194.** Until #66194 merges, this PR's diff also shows its commit, which bakes torchao and conch into the CUDA image and re-enables H200 Quantization. Those li...
- #67533 [Chore] Remove deprecated `rope_scaling` usage and forbid it in pre-commit [ready, torch.compile, deepseek, rust, kimi, pooling, recipe] (+116/-218) by @hmellor files: .pre-commit-config.yaml, recipes/models/MiniMaxAI/MiniMax-M3.yaml, rust/src/cmd/src/cli/tests.rs, tests/model_executor/test_bailing_mrope.py, tests/models/language/pooling/test_nomic_max_model_len.py, tests/transformers_utils/test_bailing_moe_v3_vl_config.py, tests/v1/attention/test_sparse_mla_backends.py, tools/pre_commit/check_forbidden_strings.py, vllm/compilation/passes/fusion/qk_norm_rope_kvcache_fusion.py, vllm/config/speculative.py, vllm/model_executor/layers/mamba/linear/bailing_linear_attn.py, vllm/model_executor/models/bailing_moe_linear.py
- On the Transformers floor (5.16.1), `config.rope_scaling` is a property returning `config.rope_parameters`, s...
- #67304 Delete tools/flashinfer-build.sh [nvidia] (+0/-64) by @mgoin files: tools/flashinfer-build.sh
---
- [ ] I used vLLM's `/pr-checklist` skill. (Mandatory for agents, optional for humans).
- [ ] AI assistance was used during the creation of this PR.
- [ ] **Design Fit:** Minimizes impact on core components, reuses existing functionality, and justi...

**First-time contributors:** Thangnguyenvn98, hmellor, mgoin
### tools-pre_commit

Summary unavailable (null LLM). Source items:
- #66672 [CI][ROCm] Bake torchao into the ROCm test image off the default path and re-enable MI300/MI355 Quantization [rocm, ci/build, quantization] (+196/-131) by @Thangnguyenvn98 files: .buildkite/test-amd.yaml, .buildkite/test_areas/quantization.yaml, .pre-commit-config.yaml, docker/Dockerfile, docker/Dockerfile.rocm, requirements/test/quantization_deps.in, requirements/test/quantization_deps_cuda.txt, requirements/test/quantization_deps_rocm.txt, tools/pre_commit/test_tethering_allowlist.txt
**Stacked on #66194.** Until #66194 merges, this PR's diff also shows its commit, which bakes torchao and conch into the CUDA image and re-enables H200 Quantization. Those li...
- #67533 [Chore] Remove deprecated `rope_scaling` usage and forbid it in pre-commit [ready, torch.compile, deepseek, rust, kimi, pooling, recipe] (+116/-218) by @hmellor files: .pre-commit-config.yaml, recipes/models/MiniMaxAI/MiniMax-M3.yaml, rust/src/cmd/src/cli/tests.rs, tests/model_executor/test_bailing_mrope.py, tests/models/language/pooling/test_nomic_max_model_len.py, tests/transformers_utils/test_bailing_moe_v3_vl_config.py, tests/v1/attention/test_sparse_mla_backends.py, tools/pre_commit/check_forbidden_strings.py, vllm/compilation/passes/fusion/qk_norm_rope_kvcache_fusion.py, vllm/config/speculative.py, vllm/model_executor/layers/mamba/linear/bailing_linear_attn.py, vllm/model_executor/models/bailing_moe_linear.py
- On the Transformers floor (5.16.1), `config.rope_scaling` is a property returning `config.rope_parameters`, s...

**First-time contributors:** Thangnguyenvn98, hmellor
### vllm

Summary unavailable (null LLM). Source items:
- #64574 [Bugfix][ROCm][KV Connector] MoRIIO: fix port collision with TP > 1 and DP > 1 [bug, rocm, ready, kv-connector] (+279/-41) by @lucasliao0403 files: tests/v1/kv_connector/unit/moriio/test_moriio_pipeline_parallel.py, tests/v1/kv_connector/unit/moriio/test_moriio_read_tp.py, tests/v1/kv_connector/unit/moriio/test_moriio_remote_pod.py, tests/v1/kv_connector/unit/moriio/test_moriio_write_done_routing.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py
- A MoRIIO instance with TP > 1 and DP > 1 (here prefill TP2 x DP2 x EP4) starts and serves requests. Before this change, prefill hung at ...
- #62590 [ROCm][Perf][Qwen4Exp] Tune sparse GQA prefill profile on gfx942 and gfx950 [rocm, ready, qwen] (+15/-0) by @tc3oliver files: tests/models/qwen4_exp/test_qsa_amd.py, vllm/models/qwen4_exp/amd/ops/qsa.py
- #49700 [EPLB] Expose narrow state overrides for out-of-tree devices [documentation, rocm, ready, ci/build, deepseek, nvidia, DSv4, kimi, k3] (+671/-307) by @freyfwt files: .buildkite/test_areas/expert_parallelism.yaml, docs/design/plugin_system.md, tests/distributed/test_eplb_algo.py, tests/distributed/test_eplb_extension_hooks.py, tests/distributed/test_eplb_utils.py, vllm/config/parallel.py, vllm/distributed/eplb/async_worker.py, vllm/distributed/eplb/eplb_state.py, vllm/distributed/eplb/policy/__init__.py, vllm/distributed/eplb/policy/abstract.py, vllm/distributed/eplb/policy/default.py, vllm/platforms/interface.py
- Keep built-in selector `Literal`...
- #65186 [Perf][GDN] Export Triton prefill checkpoints via per-sequence buffers [documentation, performance, ready, ci/build] (+380/-20) by @specture724 files: .buildkite/test_areas/engine.yaml, tests/kernels/fla/test_chunk_gated_delta_rule.py, tests/v1/e2e/general/test_mamba_prefix_cache.py, vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py, vllm/third_party/flash_linear_attention/ops/chunk.py, vllm/third_party/flash_linear_attention/ops/chunk_delta_h.py
- The existing dense `chunk_gated_delta_rule`...
- #67067 [Perf][Muse Spark] FP8 KV cache for the specialized decode (+939/-190) by @jeejeelee files: tests/kernels/test_muse_spark_fp8_kv_decode.py, vllm/models/muse_spark/nvidia/specialized_decode/cutedsl/attention/attn2.py, vllm/models/muse_spark/nvidia/specialized_decode/cutedsl/attention/kv_format.py, vllm/models/muse_spark/nvidia/specialized_decode/cutedsl/attention/qkv_front.py, vllm/models/muse_spark/nvidia/specialized_decode/cutedsl/common/primitives.py, vllm/models/muse_spark/nvidia/specialized_decode/runtime/__init__.py, vllm/models/muse_spark/nvidia/specialized_decode/runtime/cute_ops.py, vllm/models/muse_spark/nvidia/specialized_decode/runtime/draft.py, vllm/models/muse_spark/nvidia/specialized_decode/runtime/providers.py
- FP8 KV: TPOT -6.0% vs the stock decode at 150k context, gsm8k unchanged.
- FP8 KV with SWA layers kept BF16: TPOT -5.6% vs stock, gsm8k unchanged.
- #65656 [Perf][DSV4.1] Accelerate candidate prefill and decode with CuTe [ready, ci/build, deepseek, DSv4.1] (+1538/-24) by @chaunceyjiang files: .buildkite/test_areas/kernels.yaml, tests/model_executor/layers/test_mla_short_prefill_indexer.py, tests/models/deepseek_v41/nvidia/test_candidate_indexer.py, vllm/config/attention.py, vllm/model_executor/models/config.py, vllm/models/deepseek_v41/attention.py, vllm/models/deepseek_v41/nvidia/ops/candidate_indexer.py, vllm/models/deepseek_v41/nvidia/ops/candidate_paged_logits.py
- #59506 [Bugfix][Frontend] Don't crash beam search on an extreme length_penalty [bug, frontend, ready] (+33/-1) by @khluu files: tests/test_request_input_bounds.py, vllm/entrypoints/generate/beam_search/utils.py, vllm/sampling_params.py

**First-time contributors:** 0z5a, AdvayMonga, Alex-ai-future, Ankur-singh, BugenZhao, CAICAIIs, CJJ1008, Etelis, Fangzhou-Ai, HangruiCao2000, Isotr0py, Jaeyeong-CHOI, JaredforReal, JonSnow1807, LantaoJin, LeizhenZhang, Liangliang-Ma, Lucas-Fernandes-Martins, MatthewBonanni, NickLucche, Pb314314, PerkzZheng, Ronald1995, RyanMa29, ShuoleiWang, Thangnguyenvn98, Victor49152, Woolgathererer, WoosukKwon, ZhouXiaoya25, aarongdeng, afierka-intel, afriedri, alex-jw-brooks, algebra-MCX, amd-jrosas, amirfr3, aoshen02, arpera, avininjamay8, azaidy, benenzhu, bnellnm, cenab, chaojun-zhang, chaunceyjiang, chenyzhang-nvidia, chuncaohenli, cjackal, cycancode, davzhuAMD, ekagra-ranjan, faresobeid, freyfwt, fxmarty-amd, gau-nernst, gkswns0531, gordan12, grYe99, gty111, hao-aaron, hickeyma, hlin99, hmellor, hongxiayang, iharshlalakiya, ilmarkov, imthomp, jbelofamd, jeejeelee, jiaqiang-dot-liu, jzakrzew, keneoneth, ketor, khluu, lesj0610, limou102, linsun12, lishuoshuo-amd, liusy58, lucasliao0403, mgoin, mickaelseznec, mjkvaak-amd, mushroomcarbon, nien-hui, njhill, omerpaz95, paulpak58, phambinhfin, porridgewithraisins, pranavabbott, qianlihuang, rasyosef, riceharvest, samutamm, seyfal, sfeng33, shadowmodder, shanjiaz, simon-veitner-redhat, specture724, staryxchen, stecasta, subhashpolisetti, tc3oliver, tjtanaa, tomasruizt, tuukkjs, umarkovi-amd, vadiklyutiy, vgokhale, waizuichougou, wangyicong52, wtdcode, wzhao18, xaguilar-amd, xiao-llm, xinli-sw, xinyu-intel, xs1128, xsxszab, yannicks1, yeshihai, yewentao256, yibol9768-alt, yiliu30, zRzRzRzRzRzRzR, zhou-yuhan, zixi-qi, zohaibm-amd
### vllm-aiter

Summary unavailable (null LLM). Source items:
- #65711 [ROCm][Perf] Use tuned AITER Triton `gemm_a8w8` for per-tensor FP8 decode GEMMs on gfx950 [rocm, ready] (+410/-2) by @amd-jrosas files: tests/kernels/quantization/test_rocm_aiter_triton_per_tensor_fp8.py, vllm/_aiter_ops.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/scaled_mm/aiter.py
- #63272 [ROCm][Quantization][Perf] Fuse the block Hadamard input rotation into AITER's MXFP4 activation quant [documentation, rocm, ready, ci/build, quantization] (+179/-30) by @mjkvaak-amd files: tests/quantization/test_input_hadamard.py, tests/quantization/test_online_mxfp4.py, vllm/model_executor/kernels/linear/mxfp4/aiter.py, vllm/model_executor/kernels/linear/mxfp4/base.py, vllm/model_executor/layers/quantization/input_hadamard.py, vllm/model_executor/layers/quantization/online/mxfp4.py, vllm/model_executor/layers/quantization/quark/quark.py, vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py
- #59098 [Bugfix][ROCm] Fix ROCM_AITER_FA context loss on out-of-order batches [bug, rocm, ready, mrv2] (+160/-33) by @phambinhfin files: tests/v1/attention/test_attention_backends.py, tests/v1/attention/test_attention_splitting.py, tests/v1/worker/test_cp_utils.py, vllm/v1/attention/backends/rocm_aiter_fa.py, vllm/v1/attention/backends/utils.py
- #67377 [Perf][ROCm][DSv4.1] DeepSeek-V4.1-Flash: dense MXFP8 GEMMs and wo_a on AITER's tuned FlyDSL kernels, and a faster MXFP8 activation quant (MI355X) [rocm, ready, deepseek, quantization, verified] (+286/-24) by @limou102 files: tests/kernels/quantization/test_rocm_mxfp8_linear.py, tests/models/test_dsv41_mono_numerics.py, vllm/_aiter_ops.py, vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py, vllm/model_executor/kernels/linear/mxfp8/rocm_native.py, vllm/model_executor/layers/quantization/utils/mxfp8_utils.py, vllm/models/deepseek_v41/amd/mono_decode.py, vllm/v1/attention/ops/rocm_aiter_mla_sparse.py

**First-time contributors:** amd-jrosas, limou102, mjkvaak-amd, phambinhfin
### vllm-compilation

Summary unavailable (null LLM). Source items:
- #67533 [Chore] Remove deprecated `rope_scaling` usage and forbid it in pre-commit [ready, torch.compile, deepseek, rust, kimi, pooling, recipe] (+116/-218) by @hmellor files: .pre-commit-config.yaml, recipes/models/MiniMaxAI/MiniMax-M3.yaml, rust/src/cmd/src/cli/tests.rs, tests/model_executor/test_bailing_mrope.py, tests/models/language/pooling/test_nomic_max_model_len.py, tests/transformers_utils/test_bailing_moe_v3_vl_config.py, tests/v1/attention/test_sparse_mla_backends.py, tools/pre_commit/check_forbidden_strings.py, vllm/compilation/passes/fusion/qk_norm_rope_kvcache_fusion.py, vllm/config/speculative.py, vllm/model_executor/layers/mamba/linear/bailing_linear_attn.py, vllm/model_executor/models/bailing_moe_linear.py
- On the Transformers floor (5.16.1), `config.rope_scaling` is a property returning `config.rope_parameters`, s...

**First-time contributors:** hmellor
### vllm-config

Summary unavailable (null LLM). Source items:
- #49700 [EPLB] Expose narrow state overrides for out-of-tree devices [documentation, rocm, ready, ci/build, deepseek, nvidia, DSv4, kimi, k3] (+671/-307) by @freyfwt files: .buildkite/test_areas/expert_parallelism.yaml, docs/design/plugin_system.md, tests/distributed/test_eplb_algo.py, tests/distributed/test_eplb_extension_hooks.py, tests/distributed/test_eplb_utils.py, vllm/config/parallel.py, vllm/distributed/eplb/async_worker.py, vllm/distributed/eplb/eplb_state.py, vllm/distributed/eplb/policy/__init__.py, vllm/distributed/eplb/policy/abstract.py, vllm/distributed/eplb/policy/default.py, vllm/platforms/interface.py
- Keep built-in selector `Literal`...
- #65656 [Perf][DSV4.1] Accelerate candidate prefill and decode with CuTe [ready, ci/build, deepseek, DSv4.1] (+1538/-24) by @chaunceyjiang files: .buildkite/test_areas/kernels.yaml, tests/model_executor/layers/test_mla_short_prefill_indexer.py, tests/models/deepseek_v41/nvidia/test_candidate_indexer.py, vllm/config/attention.py, vllm/model_executor/models/config.py, vllm/models/deepseek_v41/attention.py, vllm/models/deepseek_v41/nvidia/ops/candidate_indexer.py, vllm/models/deepseek_v41/nvidia/ops/candidate_paged_logits.py
- #67315 [Config] Make --monokernel and decode_backend=latency_specialized one switch [ready] (+69/-7) by @hongxiayang files: tests/test_config.py, vllm/config/kernel.py, vllm/config/vllm.py, vllm/models/muse_spark/amd/dspark.py
- #66320 [ROCm][Model] Run Qwen3.5 on the eager breakable-graph model on MI355X [rocm, ready, ci/build, qwen] (+1473/-27) by @AndreasKaratzas files: .buildkite/test_areas/models_basic.yaml, .buildkite/test_areas/spec_decode.yaml, tests/kernels/core/test_fused_allreduce_gemma_rms_norm.py, tests/kernels/mamba/test_gdn_output_projection.py, tests/models/qwen3_5/test_amd_model.py, tests/models/test_qwen3_5.py, tests/test_config.py, vllm/config/vllm.py, vllm/model_executor/models/qwen3_next.py, vllm/models/qwen3_5/__init__.py, vllm/models/qwen3_5/amd/__init__.py, vllm/models/qwen3_5/amd/model.py
- `qwen3_5/amd/model.py`, `amd/mtp.py`: copy of the NVIDIA model with the ROCm counterparts of its fusions: Triton Gemma RMSNorm, the row-parallel all-reduce deferred into AITER's fused ...
- #62550 [Model] Add opt-in PrimTS attention for Step5 on Blackwell [ready, ci/build, nvidia] (+1504/-118) by @PerkzZheng files: csrc/fused_qknorm_rope_cache_kernel.cu, csrc/ops.h, csrc/torch_bindings.cpp, tests/kernels/test_fused_qknorm_rope_cache.py, tests/models/step5/test_prims_ts_attention.py, vllm/_custom_ops.py, vllm/config/kernel.py, vllm/models/step5/common/ops/prefill_indexer_metadata.py, vllm/models/step5/common/ops/sparse_indexer.py, vllm/models/step5/nvidia/flashinfer_sparse.py, vllm/models/step5/nvidia/model.py, vllm/models/step5/nvidia/ops/attention_gate.py
- #67006 [Quantization] Online weight-only NVFP4 for dense linear layers [documentation, ready, nvidia, quantization] (+349/-63) by @stecasta files: docs/features/quantization/online.md, tests/model_executor/kernels/test_b12x_linear.py, tests/quantization/test_online.py, vllm/config/quantization.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/nvfp4/b12x.py, vllm/model_executor/kernels/linear/nvfp4/base.py, vllm/model_executor/kernels/linear/nvfp4/flashinfer.py, vllm/model_executor/layers/quantization/__init__.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/lm_head.py, vllm/model_executor/layers/quantization/online/nvfp4.py
- #65901 [Perf] Add opt-in FlashInfer multimodal encoder autotuning [documentation, ready, ci/build, multi-modality, nvidia] (+508/-3) by @jzakrzew files: .buildkite/test_areas/models_multimodal.yaml, tests/model_executor/test_flashinfer_autotune_warmup.py, tests/model_executor/test_flashinfer_encoder_autotune.py, vllm/config/kernel.py, vllm/model_executor/warmup/flashinfer_autotune_cache.py, vllm/model_executor/warmup/kernel_warmup.py
--kernel-config '{"enable_flashinfer_mm_encoder_autotune": true}'
- Tunes encoder kernels using multimodal profiling inputs and FlashInfer’s per-operation token buckets.
- Improves offline image embedding thr...

**First-time contributors:** BugenZhao, HangruiCao2000, Isotr0py, NickLucche, PerkzZheng, Victor49152, aarongdeng, arpera, benenzhu, chaunceyjiang, faresobeid, freyfwt, hao-aaron, hmellor, hongxiayang, ilmarkov, jzakrzew, ketor, linsun12, stecasta, xiao-llm, zRzRzRzRzRzRzR
### vllm-config-cache.py

Summary unavailable (null LLM). Source items:
- #66605 [KVConnector] Let external connectors declare KV cache memory registration [ready, kv-connector, mooncake, nixl] (+279/-72) by @ketor files: tests/v1/engine/test_engine_args.py, tests/v1/kv_connector/unit/utils.py, vllm/config/cache.py, vllm/config/kv_transfer.py, vllm/config/vllm.py, vllm/distributed/kv_transfer/kv_connector/factory.py, vllm/distributed/kv_transfer/kv_connector/v1/base.py, vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake_store/connector.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py
- New classmethod `KVConnectorBase_V1.r...

**First-time contributors:** ketor
### vllm-distributed-kv_transfer

Summary unavailable (null LLM). Source items:
- #64574 [Bugfix][ROCm][KV Connector] MoRIIO: fix port collision with TP > 1 and DP > 1 [bug, rocm, ready, kv-connector] (+279/-41) by @lucasliao0403 files: tests/v1/kv_connector/unit/moriio/test_moriio_pipeline_parallel.py, tests/v1/kv_connector/unit/moriio/test_moriio_read_tp.py, tests/v1/kv_connector/unit/moriio/test_moriio_remote_pod.py, tests/v1/kv_connector/unit/moriio/test_moriio_write_done_routing.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py
- A MoRIIO instance with TP > 1 and DP > 1 (here prefill TP2 x DP2 x EP4) starts and serves requests. Before this change, prefill hung at ...
- #65575 [KV Connector][Mooncake] Fail pulls from a lost prefill worker [documentation, ready, kv-connector, mooncake] (+167/-5) by @CJJ1008 files: docs/features/mooncake_connector_usage.md, tests/v1/kv_connector/unit/test_mooncake_connector.py, tests/v1/kv_connector/unit/test_mooncake_stats.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py, vllm/utils/network_utils.py
- #66583 [KV Offload] Set the CPU tier up in the background under async_init [documentation, ready, kv-connector, nixl] (+390/-25) by @Etelis files: docs/features/kv_offloading_usage.md, tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py, tests/v1/kv_connector/unit/offloading_connector/test_worker.py, tests/v1/kv_connector/unit/offloading_connector/utils.py, tests/v1/kv_offload/cpu/test_shared_offload_region.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/common.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py, vllm/v1/kv_offload/base.py, vllm/v1/kv_offload/cpu/gpu_worker.py, vllm/v1/kv_offload/cpu/shared_offload_region.py, vllm/v1/kv_offload/cpu/spec.py
- The setup thread switches itself to relaxed capture mode, so pinning can't invalid...
- #65672 [Bugfix][Mooncake] Make early prefill abort cleanup idempotent [bug, documentation, ready, kv-connector, mooncake] (+32/-3) by @staryxchen files: tests/v1/kv_connector/unit/test_mooncake_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py
- An abort that reaches `record_send_reqs` before a transfer record exists, or after that record was ...
- #67486 [Bugfix][KV Offload] Avoid false flushes for shared Full Attention prefixes [bug, ready, kv-connector] (+189/-12) by @Alex-ai-future files: tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py
- A new request that shares Full Attention prefix blocks no longer adds the prior request's pending store to `jobs_to_flush`, avoiding an unnecessary wait.
- A genuinely reallocat...
- #67656 [Perf][KV Connector][MooncakeConnector] Submit Mooncake transfer descriptors with array API [ready, kv-connector, mooncake] (+421/-193) by @zhou-yuhan files: tests/v1/kv_connector/unit/test_mooncake_connector.py, tests/v1/kv_connector/unit/test_mooncake_connector_hma.py, tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py, tests/v1/kv_connector/unit/test_mooncake_stats.py, tests/v1/kv_connector/unit/test_mooncake_transfer_backend.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/transfer/backend.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/transfer/te.py
- #62474 [Bugfix][ROCm][MoRIIO] Slice WRITE heads by each layer's head count [bug, rocm, ready, kv-connector] (+179/-14) by @tjtanaa files: tests/v1/kv_connector/unit/moriio/test_moriio_hetero_tp_write.py, tests/v1/kv_connector/unit/moriio/test_moriio_write_done_routing.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py

**First-time contributors:** Alex-ai-future, CAICAIIs, CJJ1008, Etelis, NickLucche, amirfr3, avininjamay8, ketor, liusy58, lucasliao0403, seyfal, staryxchen, tjtanaa, zhou-yuhan
### vllm-distributed-weight_transfer

Summary unavailable (null LLM). Source items:
- #65487 [Bugfix][Distributed] Order packed NCCL loads after the caller stream [bug, documentation, ready] (+54/-155) by @hao-aaron files: tests/distributed/test_packed_tensor.py, vllm/distributed/weight_transfer/packed_tensor.py
- #66375 [Perf][Bugfix][RL] Fix sparse NCCL update OOM and improve performance [bug, documentation, ready] (+210/-31) by @ShuoleiWang files: docs/training/weight_transfer/nccl.md, tests/distributed/test_weight_transfer.py, vllm/distributed/weight_transfer/sparse_nccl_engine.py
- **Memory:** a worker keeps every patch on the GPU until the last one arrives, 6 bytes per changed element on every rank whatever the TP size. On the default config the extensible KV cache leaves about 3 GiB free, so a one-shot `send_weights` on Qwen3-30B-A3B at TP4 fails at 1.25% of elements changed, after some ...

**First-time contributors:** ShuoleiWang, hao-aaron
### vllm-engine

Summary unavailable (null LLM). Source items:
- #64965 [Bugfix][Attention] Reject TORCH_SDPA for decoder attention [bug, verified] (+87/-8) by @aarongdeng files: tests/config/test_multimodal_config.py, tests/engine/test_arg_utils.py, tests/entrypoints/llm/test_generate.py, tests/v1/attention/test_backend_per_kind.py, vllm/config/attention.py, vllm/engine/arg_utils.py
- #65534 [Core][MM] Make the multimodal encoder cache size configurable  [ready, cpu, mrv2] (+174/-8) by @HangruiCao2000 files: tests/v1/core/test_encoder_cache_manager.py, tests/v1/worker/test_encoder_runner.py, vllm/config/scheduler.py, vllm/engine/arg_utils.py, vllm/v1/core/encoder_cache_manager.py, vllm/v1/worker/cpu/encoder_runner.py, vllm/v1/worker/gpu/mm/encoder_runner.py, vllm/v1/worker/utils.py
- **What:** `SchedulerConfig.encoder_cache_size` is derived from `max_num_batched_tokens` and is `Field(init=False)` with a standing `# TODO (ywang96): Make this configurable.` This adds `--encoder-cache-size`. `None` keeps today's derivation, so **no behaviour change unless it is set**.
- **Why:** they are different quantities. `max_num_encoder_input_tokens` is a per-step **c...
- #63483 [Core][DBO] Dual batch overlap under pure tensor parallelism (split PR of M3.1) [documentation, rocm, ready, mrv2] (+452/-39) by @benenzhu files: docs/design/dbo.md, tests/distributed/test_pynccl.py, tests/v1/worker/test_dbo_pure_tp.py, vllm/config/parallel.py, vllm/config/vllm.py, vllm/distributed/device_communicators/pynccl.py, vllm/distributed/parallel_state.py, vllm/engine/arg_utils.py, vllm/model_executor/layers/fused_allreduce_gemma_rms_norm.py, vllm/model_executor/layers/fused_moe/modular_kernel.py, vllm/platforms/interface.py, vllm/platforms/rocm.py
**Split PR of M3.1 (#63232; the model itself landed in main as #64111):** the engine part of its ROCm work, dual batch overlap under pure TP, split out to be reviewed and merged on its own.

**First-time contributors:** HangruiCao2000, aarongdeng, benenzhu
### vllm-engine-arg_utils.py

Summary unavailable (null LLM). Source items:
- #64965 [Bugfix][Attention] Reject TORCH_SDPA for decoder attention [bug, verified] (+87/-8) by @aarongdeng files: tests/config/test_multimodal_config.py, tests/engine/test_arg_utils.py, tests/entrypoints/llm/test_generate.py, tests/v1/attention/test_backend_per_kind.py, vllm/config/attention.py, vllm/engine/arg_utils.py
- #65534 [Core][MM] Make the multimodal encoder cache size configurable  [ready, cpu, mrv2] (+174/-8) by @HangruiCao2000 files: tests/v1/core/test_encoder_cache_manager.py, tests/v1/worker/test_encoder_runner.py, vllm/config/scheduler.py, vllm/engine/arg_utils.py, vllm/v1/core/encoder_cache_manager.py, vllm/v1/worker/cpu/encoder_runner.py, vllm/v1/worker/gpu/mm/encoder_runner.py, vllm/v1/worker/utils.py
- **What:** `SchedulerConfig.encoder_cache_size` is derived from `max_num_batched_tokens` and is `Field(init=False)` with a standing `# TODO (ywang96): Make this configurable.` This adds `--encoder-cache-size`. `None` keeps today's derivation, so **no behaviour change unless it is set**.
- **Why:** they are different quantities. `max_num_encoder_input_tokens` is a per-step **c...
- #63483 [Core][DBO] Dual batch overlap under pure tensor parallelism (split PR of M3.1) [documentation, rocm, ready, mrv2] (+452/-39) by @benenzhu files: docs/design/dbo.md, tests/distributed/test_pynccl.py, tests/v1/worker/test_dbo_pure_tp.py, vllm/config/parallel.py, vllm/config/vllm.py, vllm/distributed/device_communicators/pynccl.py, vllm/distributed/parallel_state.py, vllm/engine/arg_utils.py, vllm/model_executor/layers/fused_allreduce_gemma_rms_norm.py, vllm/model_executor/layers/fused_moe/modular_kernel.py, vllm/platforms/interface.py, vllm/platforms/rocm.py
**Split PR of M3.1 (#63232; the model itself landed in main as #64111):** the engine part of its ROCm work, dual batch overlap under pure TP, split out to be reviewed and merged on its own.

**First-time contributors:** HangruiCao2000, aarongdeng, benenzhu
### vllm-entrypoints-cli

Summary unavailable (null LLM). Source items:
- #61788 [Rust Frontend] Pass pulled object storage model dir to the Rust frontend [frontend, ready, rust] (+80/-0) by @Lucas-Fernandes-Martins files: tests/entrypoints/launchers/api_server/test_api_server_process_manager.py, vllm/entrypoints/cli/serve.py, vllm/v1/utils.py
- #64641 [Fast Start] Add weights mirror support for daemon2daemon [documentation, rocm, frontend, ci/build, nvidia] (+2123/-391) by @Isotr0py files: .buildkite/test_areas/distributed.yaml, docs/features/preload.md, tests/kernels/moe/test_flashinfer.py, tests/model_executor/model_loader/test_weight_cache.py, vllm/config/load.py, vllm/entrypoints/cli/preload.py, vllm/model_executor/model_loader/__init__.py, vllm/model_executor/model_loader/utils.py, vllm/model_executor/model_loader/weight_cache/daemon.py, vllm/model_executor/model_loader/weight_cache/ipc_loader.py, vllm/model_executor/model_loader/weight_cache/protocol.py, vllm/model_executor/model_loader/weight_cache/transport.py

**First-time contributors:** Isotr0py, Lucas-Fernandes-Martins
### vllm-entrypoints-openai

Summary unavailable (null LLM). Source items:
- #63357 [Bugfix][Frontend] Honor --response-role and echo in chat derender [bug, documentation, frontend, ready] (+345/-48) by @hickeyma files: docs/serving/online_serving/derenderer.md, docs/serving/online_serving/token_in_token_out.md, tests/entrypoints/openai/chat_completion/test_message_assembly.py, tests/entrypoints/scale_out/derender/test_derender.py, tests/entrypoints/scale_out/derender/test_derender_parity.py, tests/entrypoints/scale_out/derender/test_derender_stream.py, vllm/entrypoints/launchers/api_server/app_state.py, vllm/entrypoints/launchers/render/app_state.py, vllm/entrypoints/openai/chat_completion/batch_serving.py, vllm/entrypoints/openai/chat_completion/message_assembly.py, vllm/entrypoints/openai/chat_completion/serving.py, vllm/entrypoints/scale_out/token_in_token_out/protocol.py
**Depends on #63434. See https://github....

**First-time contributors:** hickeyma
### vllm-entrypoints-scale_out

Summary unavailable (null LLM). Source items:
- #67408 [Bugfix] Reject bad_words on generate servers without a tokenizer [bug, documentation, frontend, ready] (+37/-1) by @nien-hui files: docs/serving/online_serving/token_in_token_out.md, tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py, vllm/entrypoints/scale_out/token_in_token_out/serving.py
- #63357 [Bugfix][Frontend] Honor --response-role and echo in chat derender [bug, documentation, frontend, ready] (+345/-48) by @hickeyma files: docs/serving/online_serving/derenderer.md, docs/serving/online_serving/token_in_token_out.md, tests/entrypoints/openai/chat_completion/test_message_assembly.py, tests/entrypoints/scale_out/derender/test_derender.py, tests/entrypoints/scale_out/derender/test_derender_parity.py, tests/entrypoints/scale_out/derender/test_derender_stream.py, vllm/entrypoints/launchers/api_server/app_state.py, vllm/entrypoints/launchers/render/app_state.py, vllm/entrypoints/openai/chat_completion/batch_serving.py, vllm/entrypoints/openai/chat_completion/message_assembly.py, vllm/entrypoints/openai/chat_completion/serving.py, vllm/entrypoints/scale_out/token_in_token_out/protocol.py
**Depends on #63434. See https://github....

**First-time contributors:** hickeyma, nien-hui
### vllm-kernels

Summary unavailable (null LLM). Source items:
- #67725 [Perf][Qwen4Exp] Fuse the MTP drafter's pre-FC Gemma RMSNorms into one Triton launch [qwen] (+178/-12) by @gau-nernst files: tests/kernels/core/test_fused_pre_fc_norms.py, tests/models/qwen4_exp/test_config.py, vllm/kernels/triton/fused_pre_fc_norms.py, vllm/models/qwen4_exp/nvidia/mtp.py
- The drafter's two pre-FC norms (embedding, width `H`; hidden, width `hc_count*H`) run as one launch instead...

**First-time contributors:** gau-nernst
### vllm-lora

Summary unavailable (null LLM). Source items:
- #62807 [XPU][LoRA] Support unquantized MoE LoRA [intel-gpu, ci/build, quantization] (+366/-17) by @chaojun-zhang files: .buildkite/intel_jobs/lora_intel.yaml, tests/kernels/moe/test_unquantized_backend_selection.py, tests/lora/test_fused_moe_lora_kernel.py, vllm/lora/ops/triton_ops/fused_moe_lora_op.py, vllm/lora/punica_wrapper/punica_xpu.py, vllm/model_executor/layers/fused_moe/experts/lora_experts_mixin.py, vllm/model_executor/layers/fused_moe/experts/xpu_moe.py, vllm/model_executor/layers/fused_moe/oracle/unquantized.py
- `XPUExperts` now mixes in `LoRAExpertsMixin` as a single class, mirroring `TritonExperts`. FP8 / BlockFP8 / WNA16 / MXFP4 opt out via `supports_lora()`.
- The ...

**First-time contributors:** chaojun-zhang
### vllm-model_executor-determinism

Summary unavailable (null LLM). Source items:
- #67179 [Doc] Correct the batch-invariance comment on Hopper/Blackwell split-k [ready, batch-invariance] (+6/-3) by @imthomp files: vllm/model_executor/determinism/batch_invariant.py
- #65931 [Kernel][Perf] Add H100 BF16 batch-invariant matmul configs for gpt-oss [ready, qwen, deepseek, gpt-oss, glm, batch-invariance] (+75/-0) by @imthomp files: vllm/model_executor/determinism/batch_invariant_configs.py

**First-time contributors:** imthomp
### vllm-model_executor-kernels

Summary unavailable (null LLM). Source items:
- #59208 [Bugfix][Distributed] Guard cross-node symmetric-memory rendezvous [bug, torch.compile, ci/build, kimi, k3] (+503/-16) by @mickaelseznec files: .buildkite/test_areas/distributed.yaml, tests/distributed/test_custom_all_reduce.py, tests/distributed/test_dcp_direct_a2a_lse_reduce.py, tests/distributed/test_nvlink_fabric.py, tests/distributed/test_symm_mem_allreduce.py, tests/models/kimi_k3/test_latent_moe_tail.py, vllm/distributed/device_communicators/custom_all_reduce.py, vllm/distributed/device_communicators/nvlink_fabric.py, vllm/distributed/device_communicators/symm_mem.py, vllm/envs.py, vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py, vllm/models/kimi_k3/nvidia/latent_moe_runner.py
- classifies gr...

**First-time contributors:** mickaelseznec
### vllm-model_executor-layers

Summary unavailable (null LLM). Source items:
- #65186 [Perf][GDN] Export Triton prefill checkpoints via per-sequence buffers [documentation, performance, ready, ci/build] (+380/-20) by @specture724 files: .buildkite/test_areas/engine.yaml, tests/kernels/fla/test_chunk_gated_delta_rule.py, tests/v1/e2e/general/test_mamba_prefix_cache.py, vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py, vllm/third_party/flash_linear_attention/ops/chunk.py, vllm/third_party/flash_linear_attention/ops/chunk_delta_h.py
- The existing dense `chunk_gated_delta_rule`...
- #67267 [Quant] LUT-B: fit per-channel block32 weight scales [documentation, quantization] (+201/-52) by @mgoin files: docs/features/quantization/online.md, tests/kernels/moe/test_lut_b_moe.py, vllm/model_executor/layers/quantization/utils/lut_b_utils.py
- #59564 [Perf] Use value-only reduction for FP8 group quantization [ready, torch.compile, quantization, verified] (+1/-1) by @porridgewithraisins files: vllm/model_executor/layers/quantization/input_quant_fp8.py
- The issue is simply that the compiled one uses `torch.max(...)[0]` which causes a reduction over values and indices, whereas the cuda one correctly only reduces values.
- Replacing it with `amax()` immediately resolves the issue and compiled is now uniformly faster than cuda.
- #66653 [MoE] Disable expanded DeepEP v2 dispatch in all execution modes [ready, ci/build, nvidia] (+198/-186) by @bnellnm files: .buildkite/test_areas/kernels.yaml, tests/kernels/moe/parallel_utils.py, tests/kernels/moe/test_deepep_v2_async_finalize.py, tests/kernels/moe/test_deepep_v2_moe.py, tests/kernels/moe/test_moe.py, vllm/model_executor/layers/fused_moe/all2all_utils.py, vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py
- #64406 [Perf][MoE] OCP MX emulation: dequantize only the routed experts [ready, quantization] (+187/-6) by @jbelofamd files: tests/kernels/moe/test_ocp_mx_moe.py, vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe.py
- #63272 [ROCm][Quantization][Perf] Fuse the block Hadamard input rotation into AITER's MXFP4 activation quant [documentation, rocm, ready, ci/build, quantization] (+179/-30) by @mjkvaak-amd files: tests/quantization/test_input_hadamard.py, tests/quantization/test_online_mxfp4.py, vllm/model_executor/kernels/linear/mxfp4/aiter.py, vllm/model_executor/kernels/linear/mxfp4/base.py, vllm/model_executor/layers/quantization/input_hadamard.py, vllm/model_executor/layers/quantization/online/mxfp4.py, vllm/model_executor/layers/quantization/quark/quark.py, vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py
- #67006 [Quantization] Online weight-only NVFP4 for dense linear layers [documentation, ready, nvidia, quantization] (+349/-63) by @stecasta files: docs/features/quantization/online.md, tests/model_executor/kernels/test_b12x_linear.py, tests/quantization/test_online.py, vllm/config/quantization.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/nvfp4/b12x.py, vllm/model_executor/kernels/linear/nvfp4/base.py, vllm/model_executor/kernels/linear/nvfp4/flashinfer.py, vllm/model_executor/layers/quantization/__init__.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/lm_head.py, vllm/model_executor/layers/quantization/online/nvfp4.py
- #65802 [Model Loader] Direct reload of online-quantized modules [documentation, ready, gpt-oss, quantization, kimi] (+411/-25) by @hao-aaron files: docs/features/quantization/online.md, docs/training/direct_reload.md, docs/training/layerwise.md, docs/training/weight_transfer/README.md, tests/model_executor/model_loader/test_direct_reload.py, tests/quantization/test_online_loading.py, vllm/config/vllm.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/loading.py, vllm/model_executor/model_loader/reload/plan.py, vllm/model_executor/models/gpt_oss.py
- #66118 [RL][Model Loader] Load FP8 indexer wk and MLA projections independently, as FP8 or BF16, in any scale layout [ready, ci/build, deepseek, quantization] (+908/-907) by @hao-aaron files: .buildkite/test_areas/quantization.yaml, tests/model_executor/model_loader/test_deepseek_v32_weight_loading.py, tests/quantization/test_fp8_dequant.py, tests/quantization/test_quark.py, vllm/model_executor/layers/quantization/dequant_linear.py, vllm/model_executor/layers/quantization/utils/quant_utils.py, vllm/model_executor/layers/sparse_attn_indexer.py, vllm/model_executor/models/deepseek_mtp.py, vllm/model_executor/models/deepseek_v2.py, vllm/models/deepseek_v32/amd/model.py, vllm/models/deepseek_v32/amd/mtp.py, vllm/models/deepseek_v32/attention.py

**First-time contributors:** JaredforReal, NickLucche, Pb314314, Ronald1995, Victor49152, afierka-intel, afriedri, algebra-MCX, aoshen02, benenzhu, bnellnm, chaojun-zhang, cjackal, fxmarty-amd, gau-nernst, hao-aaron, hmellor, jbelofamd, limou102, liusy58, mgoin, mjkvaak-amd, porridgewithraisins, riceharvest, seyfal, specture724, stecasta, umarkovi-amd, vgokhale, xiao-llm, yiliu30
### vllm-model_executor-model_loader

Summary unavailable (null LLM). Source items:
- #65802 [Model Loader] Direct reload of online-quantized modules [documentation, ready, gpt-oss, quantization, kimi] (+411/-25) by @hao-aaron files: docs/features/quantization/online.md, docs/training/direct_reload.md, docs/training/layerwise.md, docs/training/weight_transfer/README.md, tests/model_executor/model_loader/test_direct_reload.py, tests/quantization/test_online_loading.py, vllm/config/vllm.py, vllm/model_executor/layers/quantization/online/base.py, vllm/model_executor/layers/quantization/online/loading.py, vllm/model_executor/model_loader/reload/plan.py, vllm/model_executor/models/gpt_oss.py
- #64641 [Fast Start] Add weights mirror support for daemon2daemon [documentation, rocm, frontend, ci/build, nvidia] (+2123/-391) by @Isotr0py files: .buildkite/test_areas/distributed.yaml, docs/features/preload.md, tests/kernels/moe/test_flashinfer.py, tests/model_executor/model_loader/test_weight_cache.py, vllm/config/load.py, vllm/entrypoints/cli/preload.py, vllm/model_executor/model_loader/__init__.py, vllm/model_executor/model_loader/utils.py, vllm/model_executor/model_loader/weight_cache/daemon.py, vllm/model_executor/model_loader/weight_cache/ipc_loader.py, vllm/model_executor/model_loader/weight_cache/protocol.py, vllm/model_executor/model_loader/weight_cache/transport.py
- #67693 [Model Loader] Fill dummy FP8 weights with random codes across the range [documentation, ready] (+64/-19) by @WoosukKwon files: docs/features/quantization/modelopt.md, tests/model_executor/test_weight_utils.py, vllm/model_executor/model_loader/weight_utils.py
- On GB200 (DeepSeek-V4.1-Flash, DEP4), dummy-weight timings of large prefill steps were up to
- #65965 [Bugfix] Apply `WeightsMapper` stacked rules last, and fix the `--mm-encoder-only` shared root check [bug, speculative-decoding, ready, deepseek, gpt-oss, quantization, mistral, beam] (+146/-125) by @hmellor files: tests/model_executor/model_loader/test_mm_encoder_only_weight_filter.py, tests/models/test_utils.py, vllm/model_executor/model_loader/default_loader.py, vllm/model_executor/model_loader/weight_utils.py, vllm/model_executor/models/cosmos3_edge.py, vllm/model_executor/models/utils.py
- `WeightsMapper` applies `orig_to_new_stacked` after every other rule, and its fields are declared in the order they run. Previously stacked rules renamed `.k_pro...

**First-time contributors:** Isotr0py, WoosukKwon, hao-aaron, hmellor
### vllm-model_executor-models

Summary unavailable (null LLM). Source items:
- #67094 [Spec Decode] Add DSpine support [documentation, new-model, speculative-decoding, ready, ci/build, qwen, mrv2, dflash] (+569/-21) by @shanjiaz files: .buildkite/test_areas/spec_decode.yaml, docs/features/speculative_decoding/README.md, tests/models/registry.py, tests/v1/e2e/spec_decode/acceptance_rates/dflash/test_dflash.py, vllm/model_executor/models/qwen3_dspine.py, vllm/model_executor/models/registry.py, vllm/transformers_utils/configs/eagle.py, vllm/transformers_utils/configs/speculators/algos.py, vllm/transformers_utils/configs/speculators/base.py, vllm/v1/worker/gpu/spec_decode/dflash2/speculator.py, vllm/v1/worker/gpu/spec_decode/dspine/__init__.py, vllm/v1/worker/gpu/spec_decode/dspine/config.py
- Supports Tencent and Speculators checkpoint layouts through one model implementation.
- Reuses existing candidate sampli...
- #66320 [ROCm][Model] Run Qwen3.5 on the eager breakable-graph model on MI355X [rocm, ready, ci/build, qwen] (+1473/-27) by @AndreasKaratzas files: .buildkite/test_areas/models_basic.yaml, .buildkite/test_areas/spec_decode.yaml, tests/kernels/core/test_fused_allreduce_gemma_rms_norm.py, tests/kernels/mamba/test_gdn_output_projection.py, tests/models/qwen3_5/test_amd_model.py, tests/models/test_qwen3_5.py, tests/test_config.py, vllm/config/vllm.py, vllm/model_executor/models/qwen3_next.py, vllm/models/qwen3_5/__init__.py, vllm/models/qwen3_5/amd/__init__.py, vllm/models/qwen3_5/amd/model.py
- `qwen3_5/amd/model.py`, `amd/mtp.py`: copy of the NVIDIA model with the ROCm counterparts of its fusions: Triton Gemma RMSNorm, the row-parallel all-reduce deferred into AITER's fused ...
- #66118 [RL][Model Loader] Load FP8 indexer wk and MLA projections independently, as FP8 or BF16, in any scale layout [ready, ci/build, deepseek, quantization] (+908/-907) by @hao-aaron files: .buildkite/test_areas/quantization.yaml, tests/model_executor/model_loader/test_deepseek_v32_weight_loading.py, tests/quantization/test_fp8_dequant.py, tests/quantization/test_quark.py, vllm/model_executor/layers/quantization/dequant_linear.py, vllm/model_executor/layers/quantization/utils/quant_utils.py, vllm/model_executor/layers/sparse_attn_indexer.py, vllm/model_executor/models/deepseek_mtp.py, vllm/model_executor/models/deepseek_v2.py, vllm/models/deepseek_v32/amd/model.py, vllm/models/deepseek_v32/amd/mtp.py, vllm/models/deepseek_v32/attention.py
- #66866 [Model] Support sequence parallelism with pipeline parallelism for Qwen3-Next, Qwen3.5 and DeepSeek-V2/V3 [ready, qwen, deepseek] (+25/-14) by @xsxszab files: vllm/model_executor/models/deepseek_v2.py, vllm/model_executor/models/qwen3_5.py, vllm/model_executor/models/qwen3_next.py, vllm/models/qwen3_5/nvidia/model.py
- #66821 [Transformers backend] Serve Qwen2 with the Transformers modeling backend [documentation, speculative-decoding, ci/build, qwen, mistral, dflash, kimi, glm, cohere] (+264/-568) by @hmellor files: .buildkite/test-amd.yaml, .buildkite/test_areas/lm_eval.yaml, .buildkite/test_areas/models_language.yaml, .buildkite/test_areas/spec_decode.yaml, docs/models/supported_models.md, tests/v1/e2e/spec_decode/eagle/test_eagle3_pp.py, vllm/model_executor/models/domyn_edge.py, vllm/model_executor/models/dots_ocr.py, vllm/model_executor/models/fireredasr2.py, vllm/model_executor/models/kimi_audio.py, vllm/model_executor/models/mimo.py, vllm/model_executor/models/mimo_mtp.py
- `Qwen2ForCausalLM` and `Qwen2Model` checkpoints resolve t...
- #67502 [CI] Bump Transformers version to 5.23.0 [ci/build, multi-modality, qwen, cpu, glm] (+136/-201) by @hmellor files: requirements/common.txt, requirements/test/cpu.txt, requirements/test/cuda.in, requirements/test/cuda.txt, requirements/test/kv_connectors_cuda.txt, requirements/test/nightly-torch.txt, requirements/test/rocm.in, requirements/test/rocm.txt, requirements/test/xpu.in, requirements/test/xpu.txt, tests/models/multimodal/processing/test_qwen3_asr.py, tests/models/multimodal/processing/test_qwen3_omni.py
- `requirements/common.txt` allows `transformers >= 5.16.1, < 5.24.0`, and CI pins 5.23.0.
- Breaking changes in 5.23 (`ep_router` removal huggingface/transformers#49615, exporters, Wav2Vec2ProcessorWithLM, serve) do ...

**First-time contributors:** cjackal, gordan12, hao-aaron, hmellor, jiaqiang-dot-liu, shanjiaz, xsxszab
### vllm-models-amd

Summary unavailable (null LLM). Source items:
- #62590 [ROCm][Perf][Qwen4Exp] Tune sparse GQA prefill profile on gfx942 and gfx950 [rocm, ready, qwen] (+15/-0) by @tc3oliver files: tests/models/qwen4_exp/test_qsa_amd.py, vllm/models/qwen4_exp/amd/ops/qsa.py
- #63086 [ROCm][Kimi-K3] Enable encoder graph capture for Kimi-K3 Vision Tower [rocm, ready, torch.compile, ci/build, multi-modality, nvidia, kimi, k3] (+394/-0) by @samutamm files: tests/models/multimodal/generation/test_vit_cudagraph.py, vllm/models/kimi_k3/amd/encoder_cudagraph.py, vllm/models/kimi_k3/amd/model.py
- #67984 [ROCm][Bugfix] Port Mistral Large 4 AMD indexer cache to get_kv_cache_config [bug, rocm, ready, mistral] (+24/-5) by @xaguilar-amd files: tests/models/mistral/test_fused_ops.py, vllm/models/mistral/amd/indexer.py, vllm/models/mistral/amd/ops/indexer.py
- Fixes th...
- #67315 [Config] Make --monokernel and decode_backend=latency_specialized one switch [ready] (+69/-7) by @hongxiayang files: tests/test_config.py, vllm/config/kernel.py, vllm/config/vllm.py, vllm/models/muse_spark/amd/dspark.py
- #66320 [ROCm][Model] Run Qwen3.5 on the eager breakable-graph model on MI355X [rocm, ready, ci/build, qwen] (+1473/-27) by @AndreasKaratzas files: .buildkite/test_areas/models_basic.yaml, .buildkite/test_areas/spec_decode.yaml, tests/kernels/core/test_fused_allreduce_gemma_rms_norm.py, tests/kernels/mamba/test_gdn_output_projection.py, tests/models/qwen3_5/test_amd_model.py, tests/models/test_qwen3_5.py, tests/test_config.py, vllm/config/vllm.py, vllm/model_executor/models/qwen3_next.py, vllm/models/qwen3_5/__init__.py, vllm/models/qwen3_5/amd/__init__.py, vllm/models/qwen3_5/amd/model.py
- `qwen3_5/amd/model.py`, `amd/mtp.py`: copy of the NVIDIA model with the ROCm counterparts of its fusions: Triton Gemma RMSNorm, the row-parallel all-reduce deferred into AITER's fused ...
- #66118 [RL][Model Loader] Load FP8 indexer wk and MLA projections independently, as FP8 or BF16, in any scale layout [ready, ci/build, deepseek, quantization] (+908/-907) by @hao-aaron files: .buildkite/test_areas/quantization.yaml, tests/model_executor/model_loader/test_deepseek_v32_weight_loading.py, tests/quantization/test_fp8_dequant.py, tests/quantization/test_quark.py, vllm/model_executor/layers/quantization/dequant_linear.py, vllm/model_executor/layers/quantization/utils/quant_utils.py, vllm/model_executor/layers/sparse_attn_indexer.py, vllm/model_executor/models/deepseek_mtp.py, vllm/model_executor/models/deepseek_v2.py, vllm/models/deepseek_v32/amd/model.py, vllm/models/deepseek_v32/amd/mtp.py, vllm/models/deepseek_v32/attention.py
- #67853 [ROCm][DSv4.1][Perf] Always use the unfolded layer-0 mHC entry on gfx942 [rocm, ready, deepseek, verified] (+85/-23) by @lishuoshuo-amd files: tests/kernels/mhc/test_mhc_kernels.py, vllm/models/deepseek_v41/amd/model.py, vllm/models/deepseek_v41/amd/mono_decode.py
- #67866 [Perf][KDA] Export Triton KDA prefill checkpoints via a per-sequence buffer [documentation, kimi] (+266/-22) by @JaredforReal files: tests/models/glm5next/test_kda_recurrent.py, tests/models/kimi_k3/test_kda.py, vllm/model_executor/layers/mamba/kda_checkpoint.py, vllm/models/glm5next/amd/ops/third_party/kda/kernels.py, vllm/models/glm5next/common/kda.py, vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py, vllm/models/kimi_k3/nvidia/kda.py, vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py, vllm/third_party/flash_linear_attention/ops/chunk_delta_h.py
- #65985 [ROCm][Muse Spark] DSpark draft layers as one persistent FlyDSL launch (--monokernel) [rocm, ready, ci/build, verified, dflash] (+2422/-20) by @azaidy files: .buildkite/test_areas/models_basic.yaml, tests/models/test_muse_spark_rocm_drafter.py, vllm/models/muse_spark/amd/dspark.py, vllm/models/muse_spark/amd/mono/decoder.py, vllm/models/muse_spark/amd/mono/drafter.py, vllm/models/muse_spark/amd/mono/kernels/attn_frag.py, vllm/models/muse_spark/amd/mono/kernels/draft.py
- #66842 [ROCm][DeepSeek-V4.1] Enable eager prefill context parallel for DeepSeek-V4.1-Flash [documentation, rocm, ready, ci/build, deepseek] (+155/-12) by @AndreasKaratzas files: docs/serving/context_parallel_deployment.md, tests/models/test_deepseek_v41_pcp.py, vllm/models/deepseek_v41/amd/model.py, vllm/models/deepseek_v41/amd/rocm.py, vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py

**First-time contributors:** JaredforReal, NickLucche, Ronald1995, azaidy, cjackal, davzhuAMD, gty111, hao-aaron, hmellor, hongxiayang, ilmarkov, limou102, lishuoshuo-amd, samutamm, tc3oliver, vgokhale, xaguilar-amd
### vllm-models-deepseek_v4

Summary unavailable (null LLM). Source items:
- #64252 [Bugfix][XPU] Apply attn_sink in the DeepSeek-V4 sparse MLA Triton kernel [bug, intel-gpu, ci/build, deepseek, DSv4] (+336/-4) by @afierka-intel files: tests/kernels/attention/test_xpu_mla_sparse.py, vllm/models/deepseek_v4/xpu/xpu_sparse.py, vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py, vllm/v1/attention/ops/xpu_mla_sparse.py
- **Problem:** On XPU the DeepSeek-V4 sparse-MLA path never applied the per-head `attn_sink` (the prefill call site did not pass it and `xpu_sparse_decode_fp8()` accepted it but dropped it), unlike the NVIDIA, ROCm and CPU backends, so the softmax was silently wrong, by 105–118 % of the output for a row with 1 valid key and 0.2–0.8 % for 512–2048 keys (fp32 reference, sinks from the released V4...
- #64515 [Bugfix][XPU] Use int64 token index in the DeepSeek-V4 qnorm/RoPE kernel [bug, intel-gpu, ci/build, deepseek, DSv4] (+89/-1) by @afierka-intel files: tests/kernels/test_deepseek_v4_xpu_qnorm_rope_large_batch.py, vllm/models/deepseek_v4/xpu/xpu_qnorm_rope_kv_fp8_insert.py
- **Problem:** `_xpu_qnorm_rope_kernel` (`vllm/models/deepseek_v4/xpu/xpu_qnorm_rope_kv_fp8_insert.py`) computes `token_idx * num_heads * HEAD_DIM` in int32, so the Q address wraps once a step holds more than 2^31 Q elements (65,536 tokens with 64 local heads); on Intel Arc Pro B60 this ends in `UR_RESULT_ERROR_DEVICE_LOST`. The 1M-context DeepSeek-V4 models hit this with a single prompt over 6...
- #64827 [DeepSeek-V4] Warm the DeepGEMM kernels DeepSeek-V4/V4.1 JIT-compile at runtime [ready, deepseek, DSv4] (+606/-15) by @HangruiCao2000 files: tests/model_executor/test_deep_gemm_warmup.py, tests/model_executor/test_mhc_prenorm_gemm_warmup.py, vllm/model_executor/kernels/mhc/tilelang.py, vllm/model_executor/kernels/mhc/warmup.py, vllm/model_executor/warmup/deep_gemm_warmup.py, vllm/model_executor/warmup/kernel_warmup.py, vllm/models/deepseek_v4/nvidia/model.py, vllm/models/deepseek_v41/nvidia/model.py
- #61395 [EPLB] Support heterogeneous DeepSeek V4/V4.1 DSpark draft experts [documentation, speculative-decoding, qwen, deepseek, mrv2, DSv4, dflash, DSv4.1] (+1483/-306) by @ilmarkov files: docs/features/speculative_decoding/README.md, docs/serving/expert_parallel_deployment.md, tests/distributed/test_eplb_spec_decode.py, tests/distributed/test_eplb_utils.py, tests/model_executor/test_qwen3_omni.py, tests/models/test_deepseek_v4_mega_moe.py, tests/models/test_dspark_mla.py, tests/test_config.py, tests/v1/spec_decode/test_draft_attention_backend_override.py, tests/v1/spec_decode/test_draft_moe_backend_override.py, tests/v1/spec_decode/test_lilicorr.py, tests/v1/worker/test_dspark_utils.py
- #57985 [Model] Extend device-side mm normalization to DeepSeekV4 Vision / DeepSeekV41 [documentation, ready, multi-modality, deepseek, nvidia, DSv4, DSv4.1] (+198/-23) by @cjackal files: docs/design/mm_processing.md, tests/models/multimodal/processing/test_deepseek_v4_vl.py, vllm/models/deepseek_v4/common/mm_preprocess.py, vllm/models/deepseek_v4/common/vision.py, vllm/models/deepseek_v4/common/vl_model.py, vllm/models/deepseek_v41/amd/vl_model.py, vllm/models/deepseek_v41/common/mm_preprocess.py, vllm/models/deepseek_v41/common/vl_cudagraph.py, vllm/models/deepseek_v41/nvidia/vl_model.py

**First-time contributors:** HangruiCao2000, afierka-intel, cjackal, ilmarkov
### vllm-models-kimi_k3

Summary unavailable (null LLM). Source items:
- #67866 [Perf][KDA] Export Triton KDA prefill checkpoints via a per-sequence buffer [documentation, kimi] (+266/-22) by @JaredforReal files: tests/models/glm5next/test_kda_recurrent.py, tests/models/kimi_k3/test_kda.py, vllm/model_executor/layers/mamba/kda_checkpoint.py, vllm/models/glm5next/amd/ops/third_party/kda/kernels.py, vllm/models/glm5next/common/kda.py, vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py, vllm/models/kimi_k3/nvidia/kda.py, vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py, vllm/third_party/flash_linear_attention/ops/chunk_delta_h.py
- #66784 [Bugfix][Model Loader] Handle merged-linear padding for Qwen4Exp and Kimi KDA [bug, ready, ci/build, qwen, kimi, batch-invariance] (+155/-71) by @Ronald1995 files: .buildkite/test_areas/models_basic.yaml, tests/model_executor/model_loader/test_direct_reload.py, tests/model_executor/model_loader/test_load_plan.py, tests/model_executor/model_loader/test_stacked_shard_tracking.py, tests/models/kimi_k3/test_amd_kda_loading.py, tests/models/qwen4_exp/test_hc_ops.py, vllm/model_executor/layers/linear.py, vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py, vllm/models/kimi_k3/amd/kda.py, vllm/models/kimi_k3/nvidia/kda.py, vllm/models/qwen4_exp/amd/hyperconnection.py, vllm/models/qwen4_exp/nvidia/hyperconnection.py
- `MergedColumnParallelLinear(padding_size=N)`: callers pass only real `out...

**First-time contributors:** JaredforReal, Ronald1995
### vllm-models-qwen4_exp

Summary unavailable (null LLM). Source items:
- #62590 [ROCm][Perf][Qwen4Exp] Tune sparse GQA prefill profile on gfx942 and gfx950 [rocm, ready, qwen] (+15/-0) by @tc3oliver files: tests/models/qwen4_exp/test_qsa_amd.py, vllm/models/qwen4_exp/amd/ops/qsa.py
- #67725 [Perf][Qwen4Exp] Fuse the MTP drafter's pre-FC Gemma RMSNorms into one Triton launch [qwen] (+178/-12) by @gau-nernst files: tests/kernels/core/test_fused_pre_fc_norms.py, tests/models/qwen4_exp/test_config.py, vllm/kernels/triton/fused_pre_fc_norms.py, vllm/models/qwen4_exp/nvidia/mtp.py
- The drafter's two pre-FC norms (embedding, width `H`; hidden, width `hc_count*H`) run as one launch instead...
- #67728 [Perf][Qwen4Exp] Drop the defensive zero fill from the QSA output path [qwen] (+8/-2) by @gau-nernst files: tests/models/qwen4_exp/test_qsa_reference.py, vllm/models/qwen4_exp/nvidia/qsa.py
- Eliminate one full padded-output zero fill per QSA layer dur...
- #66784 [Bugfix][Model Loader] Handle merged-linear padding for Qwen4Exp and Kimi KDA [bug, ready, ci/build, qwen, kimi, batch-invariance] (+155/-71) by @Ronald1995 files: .buildkite/test_areas/models_basic.yaml, tests/model_executor/model_loader/test_direct_reload.py, tests/model_executor/model_loader/test_load_plan.py, tests/model_executor/model_loader/test_stacked_shard_tracking.py, tests/models/kimi_k3/test_amd_kda_loading.py, tests/models/qwen4_exp/test_hc_ops.py, vllm/model_executor/layers/linear.py, vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py, vllm/models/kimi_k3/amd/kda.py, vllm/models/kimi_k3/nvidia/kda.py, vllm/models/qwen4_exp/amd/hyperconnection.py, vllm/models/qwen4_exp/nvidia/hyperconnection.py
- `MergedColumnParallelLinear(padding_size=N)`: callers pass only real `out...

**First-time contributors:** Ronald1995, gau-nernst, tc3oliver
### vllm-multimodal

Summary unavailable (null LLM). Source items:
- #65829 [Model] Add LFM3-Omni [documentation, new-model, ready, multi-modality] (+685/-1) by @paulpak58 files: docs/models/supported_models.md, tests/models/multimodal/processing/test_lfm3_omni.py, tests/models/registry.py, vllm/model_executor/models/lfm3_omni.py, vllm/model_executor/models/registry.py, vllm/multimodal/video.py, vllm/transformers_utils/config.py, vllm/transformers_utils/configs/__init__.py, vllm/transformers_utils/configs/lfm3_omni.py, vllm/transformers_utils/processors/__init__.py, vllm/transformers_utils/processors/lfm3_omni.py
- LFM3: #65826
- LFM3-VL: #65827
- LFM3-Audio: #65828
- LFM3-Omni: #65829
- #67316 [Bugfix][Security] Check the uncompressed size of embedding archives before torch.load [bug, documentation, ready, multi-modality] (+118/-3) by @LeizhenZhang files: docs/usage/security.md, tests/renderers/test_sparse_tensor_validation.py, vllm/multimodal/media/audio.py, vllm/multimodal/media/image.py, vllm/multimodal/media/video.py, vllm/renderers/embed_utils.py, vllm/utils/sparse_utils.py
- #67611 [Bugfix][Audio] Treat zero decode limits as disabled [bug, ready, multi-modality] (+114/-7) by @Woolgathererer files: tests/multimodal/media/test_audio.py, vllm/multimodal/media/audio.py
- `VLLM_MAX_AUDIO_DECODE_DURATION_S=0` and `VLLM_MAX_AUD...
- #67632 [Model] Remove OpenPangu-VL [documentation, ready, multi-modality] (+27/-1818) by @hmellor files: docs/models/supported_models.md, examples/generate/multimodal/vision_language_multi_image_offline.py, examples/generate/multimodal/vision_language_offline.py, tests/models/multimodal/test_openpangu_vl.py, tests/models/registry.py, tests/multimodal/test_video.py, vllm/model_executor/layers/rotary_embedding/__init__.py, vllm/model_executor/layers/rotary_embedding/mrope_interleaved.py, vllm/model_executor/models/openpangu.py, vllm/model_executor/models/openpangu_vl.py, vllm/model_executor/models/registry.py, vllm/multimodal/video.py
- https://github.com/vllm-project/vllm/pull/56390 (`openpangu` video loader `num_frames=-1` crash)
- `FreedomIntelligence/openPang...
- #67105 [Bugfix][Audio] Fall back to soundfile when torchcodec fails to decode [bug, ready, multi-modality] (+30/-12) by @ekagra-ranjan files: vllm/multimodal/media/audio.py

**First-time contributors:** LeizhenZhang, Woolgathererer, ekagra-ranjan, hmellor, paulpak58, shadowmodder
### vllm-multimodal-media

Summary unavailable (null LLM). Source items:
- #67316 [Bugfix][Security] Check the uncompressed size of embedding archives before torch.load [bug, documentation, ready, multi-modality] (+118/-3) by @LeizhenZhang files: docs/usage/security.md, tests/renderers/test_sparse_tensor_validation.py, vllm/multimodal/media/audio.py, vllm/multimodal/media/image.py, vllm/multimodal/media/video.py, vllm/renderers/embed_utils.py, vllm/utils/sparse_utils.py
- #67611 [Bugfix][Audio] Treat zero decode limits as disabled [bug, ready, multi-modality] (+114/-7) by @Woolgathererer files: tests/multimodal/media/test_audio.py, vllm/multimodal/media/audio.py
- `VLLM_MAX_AUDIO_DECODE_DURATION_S=0` and `VLLM_MAX_AUD...
- #67105 [Bugfix][Audio] Fall back to soundfile when torchcodec fails to decode [bug, ready, multi-modality] (+30/-12) by @ekagra-ranjan files: vllm/multimodal/media/audio.py
- `load_audio(backend="auto")` decodes MP3s that FFmpeg ab...

**First-time contributors:** LeizhenZhang, Woolgathererer, ekagra-ranjan
### vllm-platforms-xpu.py

Summary unavailable (null LLM). Source items:
- #64255 [XPU][MLA] Register XPUFlashAttnMLABackend for FLASH_ATTN_MLA in XPU [intel-gpu, verified] (+12/-2) by @ZhouXiaoya25 files: vllm/platforms/xpu.py

**First-time contributors:** ZhouXiaoya25
### vllm-quark

Summary unavailable (null LLM). Source items:
- #63272 [ROCm][Quantization][Perf] Fuse the block Hadamard input rotation into AITER's MXFP4 activation quant [documentation, rocm, ready, ci/build, quantization] (+179/-30) by @mjkvaak-amd files: tests/quantization/test_input_hadamard.py, tests/quantization/test_online_mxfp4.py, vllm/model_executor/kernels/linear/mxfp4/aiter.py, vllm/model_executor/kernels/linear/mxfp4/base.py, vllm/model_executor/layers/quantization/input_hadamard.py, vllm/model_executor/layers/quantization/online/mxfp4.py, vllm/model_executor/layers/quantization/quark/quark.py, vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py
- #67568 [Cherry-pick][v0.34.0] [Model] Add Mistral Large 4 (#64534) [new-model, rocm, speculative-decoding, ci/build, kv-connector, nvidia, quantization, mrv2, mistral, dflash, hisparse] (+20702/-199) by @NickLucche files: .buildkite/test_areas/models_basic.yaml, tests/distributed/test_dcp_a2a.py, tests/distributed/test_dcp_direct_a2a_lse_reduce.py, tests/kernels/attention/test_triton_decode_attention.py, tests/models/mistral/mistral_large4/amd_specialized_decode/__init__.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_fp8_kv_cache.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_runtime.py, tests/models/mistral/test_fused_ops.py, tests/models/mistral/test_ml4_dspark.py, tests/models/registry.py, tests/quantization/test_modelopt.py, tests/quantization/test_quark.py
- `mla_attention.py`: keeps the `prepare_mqa_query` / `_prepare_mqa_query` re...
- #65951 [Bugfix][Quantization] Handle dict-valued Quark `algo_config` in `maybe_update_config` [bug, ready, quantization] (+14/-0) by @afriedri files: tests/quantization/test_quark.py, vllm/model_executor/layers/quantization/quark/quark.py
- #59460 [Quantization] Make activation-quantization fallbacks explicit, add VLLM_STRICT_QUANT_SCHEME [documentation, intel-gpu, cpu, nvidia, quantization] (+798/-113) by @mgoin files: docs/features/quantization/README.md, tests/kernels/moe/test_b12x.py, tests/kernels/moe/test_moe_kernel_oracle.py, tests/kernels/quantization/test_mxfp4_kernel_selection.py, tests/kernels/quantization/test_scaled_mm_kernel_selection.py, tests/quantization/test_humming_mxfp4_block_fp8.py, vllm/envs.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/base.py, vllm/model_executor/kernels/linear/mxfp4/base.py, vllm/model_executor/kernels/linear/mxfp4/humming.py, vllm/model_executor/kernels/linear/mxfp4/marlin.py
- #64534 [Model] Add Mistral Large 4 [documentation, new-model, rocm, structured-output, frontend, speculative-decoding, ready, ci/build, tool-calling, deepseek, cpu, kv-connector, nvidia, quantization, mrv2, mistral, dflash, kv-cache-manager, hisparse, nixl] (+20739/-226) by @NickLucche files: .buildkite/test_areas/models_basic.yaml, tests/distributed/test_dcp_a2a.py, tests/distributed/test_dcp_direct_a2a_lse_reduce.py, tests/kernels/attention/test_triton_decode_attention.py, tests/models/mistral/mistral_large4/amd_specialized_decode/__init__.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_fp8_kv_cache.py, tests/models/mistral/mistral_large4/amd_specialized_decode/test_runtime.py, tests/models/mistral/test_fused_ops.py, tests/models/mistral/test_ml4_dspark.py, tests/models/registry.py, tests/quantization/test_modelopt.py, tests/quantization/test_quark.py
- Mistral-Large-4-1T-A52B (FP8) and -NVFP4 on model runner V2
- Sparse MLA with the DSA indexer, cross-layer KV sharing, SSMax
- DSpark speculative decoding
- DCP/PCP long context, NIXL P/D, HiSparse host KV offload
- NVIDIA (Blackwel...

**First-time contributors:** NickLucche, afriedri, mgoin, mjkvaak-amd
### vllm-renderers

Summary unavailable (null LLM). Source items:
- #67316 [Bugfix][Security] Check the uncompressed size of embedding archives before torch.load [bug, documentation, ready, multi-modality] (+118/-3) by @LeizhenZhang files: docs/usage/security.md, tests/renderers/test_sparse_tensor_validation.py, vllm/multimodal/media/audio.py, vllm/multimodal/media/image.py, vllm/multimodal/media/video.py, vllm/renderers/embed_utils.py, vllm/utils/sparse_utils.py
- #63357 [Bugfix][Frontend] Honor --response-role and echo in chat derender [bug, documentation, frontend, ready] (+345/-48) by @hickeyma files: docs/serving/online_serving/derenderer.md, docs/serving/online_serving/token_in_token_out.md, tests/entrypoints/openai/chat_completion/test_message_assembly.py, tests/entrypoints/scale_out/derender/test_derender.py, tests/entrypoints/scale_out/derender/test_derender_parity.py, tests/entrypoints/scale_out/derender/test_derender_stream.py, vllm/entrypoints/launchers/api_server/app_state.py, vllm/entrypoints/launchers/render/app_state.py, vllm/entrypoints/openai/chat_completion/batch_serving.py, vllm/entrypoints/openai/chat_completion/message_assembly.py, vllm/entrypoints/openai/chat_completion/serving.py, vllm/entrypoints/scale_out/token_in_token_out/protocol.py
**Depends on #63434. See https://github....

**First-time contributors:** LeizhenZhang, hickeyma
### vllm-rocm

Summary unavailable (null LLM). Source items:
- #67806 [Bugfix] Select only batch-invariant MXFP8 linear kernels under VLLM_BATCH_INVARIANT [bug, quantization, batch-invariance] (+116/-2) by @sfeng33 files: tests/kernels/quantization/test_mxfp8_kernel_selection.py, tests/v1/determinism/test_mx_linear_batch_invariant.py, vllm/model_executor/kernels/linear/__init__.py, vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel.py, vllm/model_executor/kernels/linear/mxfp8/emulation.py, vllm/model_executor/kernels/linear/mxfp8/humming.py, vllm/model_executor/kernels/linear/mxfp8/rocm_native.py
- #59098 [Bugfix][ROCm] Fix ROCM_AITER_FA context loss on out-of-order batches [bug, rocm, ready, mrv2] (+160/-33) by @phambinhfin files: tests/v1/attention/test_attention_backends.py, tests/v1/attention/test_attention_splitting.py, tests/v1/worker/test_cp_utils.py, vllm/v1/attention/backends/rocm_aiter_fa.py, vllm/v1/attention/backends/utils.py
- #64641 [Fast Start] Add weights mirror support for daemon2daemon [documentation, rocm, frontend, ci/build, nvidia] (+2123/-391) by @Isotr0py files: .buildkite/test_areas/distributed.yaml, docs/features/preload.md, tests/kernels/moe/test_flashinfer.py, tests/model_executor/model_loader/test_weight_cache.py, vllm/config/load.py, vllm/entrypoints/cli/preload.py, vllm/model_executor/model_loader/__init__.py, vllm/model_executor/model_loader/utils.py, vllm/model_executor/model_loader/weight_cache/daemon.py, vllm/model_executor/model_loader/weight_cache/ipc_loader.py, vllm/model_executor/model_loader/weight_cache/protocol.py, vllm/model_executor/model_loader/weight_cache/transport.py
- #66842 [ROCm][DeepSeek-V4.1] Enable eager prefill context parallel for DeepSeek-V4.1-Flash [documentation, rocm, ready, ci/build, deepseek] (+155/-12) by @AndreasKaratzas files: docs/serving/context_parallel_deployment.md, tests/models/test_deepseek_v41_pcp.py, vllm/models/deepseek_v41/amd/model.py, vllm/models/deepseek_v41/amd/rocm.py, vllm/models/deepseek_v41/common/ops/fused_compress_quant_cache.py
- DeepSeek-V4.1-Flash serves with `--prefill-context-parallel-size 2` on ROCm. On main it fails at startup with `NotImple...
- #65658 [ROCm][PP] Stage hand-off on SDMA copy engines (--pp-sdma-handoff) [rocm, ready, ci/build] (+495/-72) by @benenzhu files: .buildkite/test_areas/distributed.yaml, tests/distributed/test_pp_transport.py, vllm/distributed/pp_transport/__init__.py, vllm/distributed/pp_transport/copy_engine.py, vllm/distributed/pp_transport/rocm_sdma.py, vllm/envs.py
- #67377 [Perf][ROCm][DSv4.1] DeepSeek-V4.1-Flash: dense MXFP8 GEMMs and wo_a on AITER's tuned FlyDSL kernels, and a faster MXFP8 activation quant (MI355X) [rocm, ready, deepseek, quantization, verified] (+286/-24) by @limou102 files: tests/kernels/quantization/test_rocm_mxfp8_linear.py, tests/models/test_dsv41_mono_numerics.py, vllm/_aiter_ops.py, vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py, vllm/model_executor/kernels/linear/mxfp8/rocm_native.py, vllm/model_executor/layers/quantization/utils/mxfp8_utils.py, vllm/models/deepseek_v41/amd/mono_decode.py, vllm/v1/attention/ops/rocm_aiter_mla_sparse.py
- #63483 [Core][DBO] Dual batch overlap under pure tensor parallelism (split PR of M3.1) [documentation, rocm, ready, mrv2] (+452/-39) by @benenzhu files: docs/design/dbo.md, tests/distributed/test_pynccl.py, tests/v1/worker/test_dbo_pure_tp.py, vllm/config/parallel.py, vllm/config/vllm.py, vllm/distributed/device_communicators/pynccl.py, vllm/distributed/parallel_state.py, vllm/engine/arg_utils.py, vllm/model_executor/layers/fused_allreduce_gemma_rms_norm.py, vllm/model_executor/layers/fused_moe/modular_kernel.py, vllm/platforms/interface.py, vllm/platforms/rocm.py
**Split PR of M3.1 (#63232; the model itself landed in main as #64111):** the engine part of its ROCm work, dual batch overlap under pure TP, split out to be reviewed and merged on its own.
- #67344 [ROCm][gfx1151] ROCM_RDNA_ATTN: prefer 16-token KV blocks [rocm, verified] (+18/-0) by @zohaibm-amd files: tests/kernels/attention/test_rocm_rdna_hip.py, vllm/v1/attention/backends/rocm_rdna_attn.py
- With `--attention-backend ROCM_RDNA_ATTN` and no `-...

**First-time contributors:** Isotr0py, benenzhu, limou102, phambinhfin, sfeng33, zohaibm-amd
### vllm-sampling_params.py

Summary unavailable (null LLM). Source items:
- #59506 [Bugfix][Frontend] Don't crash beam search on an extreme length_penalty [bug, frontend, ready] (+33/-1) by @khluu files: tests/test_request_input_bounds.py, vllm/entrypoints/generate/beam_search/utils.py, vllm/sampling_params.py
- A large negative penalty underflows that to `0.0`, which raises `ZeroDivisionError: float division by zero`.
- A large positive one raises `OverflowError`.

**First-time contributors:** khluu
### vllm-third_party-flash_linear_attention

Summary unavailable (null LLM). Source items:
- #65186 [Perf][GDN] Export Triton prefill checkpoints via per-sequence buffers [documentation, performance, ready, ci/build] (+380/-20) by @specture724 files: .buildkite/test_areas/engine.yaml, tests/kernels/fla/test_chunk_gated_delta_rule.py, tests/v1/e2e/general/test_mamba_prefix_cache.py, vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py, vllm/third_party/flash_linear_attention/ops/chunk.py, vllm/third_party/flash_linear_attention/ops/chunk_delta_h.py
- The existing dense `chunk_gated_delta_rule`...
- #67866 [Perf][KDA] Export Triton KDA prefill checkpoints via a per-sequence buffer [documentation, kimi] (+266/-22) by @JaredforReal files: tests/models/glm5next/test_kda_recurrent.py, tests/models/kimi_k3/test_kda.py, vllm/model_executor/layers/mamba/kda_checkpoint.py, vllm/models/glm5next/amd/ops/third_party/kda/kernels.py, vllm/models/glm5next/common/kda.py, vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py, vllm/models/kimi_k3/nvidia/kda.py, vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py, vllm/third_party/flash_linear_attention/ops/chunk_delta_h.py
- #67733 [Perf][GDN] Drop the prefill copies of the fused spec-decode path (+69/-39) by @gau-nernst files: tests/kernels/fla/test_fla_layernorm_guard.py, tests/kernels/mamba/test_gdn_fused_mtp.py, vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py, vllm/model_executor/warmup/qwen_triton_warmup.py, vllm/third_party/flash_linear_attention/ops/layernorm_guard.py
- Remove the ou...

**First-time contributors:** JaredforReal, gau-nernst, specture724
### vllm-v1-attention

Summary unavailable (null LLM). Source items:
- #59208 [Bugfix][Distributed] Guard cross-node symmetric-memory rendezvous [bug, torch.compile, ci/build, kimi, k3] (+503/-16) by @mickaelseznec files: .buildkite/test_areas/distributed.yaml, tests/distributed/test_custom_all_reduce.py, tests/distributed/test_dcp_direct_a2a_lse_reduce.py, tests/distributed/test_nvlink_fabric.py, tests/distributed/test_symm_mem_allreduce.py, tests/models/kimi_k3/test_latent_moe_tail.py, vllm/distributed/device_communicators/custom_all_reduce.py, vllm/distributed/device_communicators/nvlink_fabric.py, vllm/distributed/device_communicators/symm_mem.py, vllm/envs.py, vllm/model_executor/kernels/linear/cute_dsl/gemm_rs_ar.py, vllm/models/kimi_k3/nvidia/latent_moe_runner.py
- classifies gr...
- #59098 [Bugfix][ROCm] Fix ROCM_AITER_FA context loss on out-of-order batches [bug, rocm, ready, mrv2] (+160/-33) by @phambinhfin files: tests/v1/attention/test_attention_backends.py, tests/v1/attention/test_attention_splitting.py, tests/v1/worker/test_cp_utils.py, vllm/v1/attention/backends/rocm_aiter_fa.py, vllm/v1/attention/backends/utils.py
- #64252 [Bugfix][XPU] Apply attn_sink in the DeepSeek-V4 sparse MLA Triton kernel [bug, intel-gpu, ci/build, deepseek, DSv4] (+336/-4) by @afierka-intel files: tests/kernels/attention/test_xpu_mla_sparse.py, vllm/models/deepseek_v4/xpu/xpu_sparse.py, vllm/models/deepseek_v4/xpu/xpu_sparse_decode_fp8.py, vllm/v1/attention/ops/xpu_mla_sparse.py
- **Problem:** On XPU the DeepSeek-V4 sparse-MLA path never applied the per-head `attn_sink` (the prefill call site did not pass it and `xpu_sparse_decode_fp8()` accepted it but dropped it), unlike the NVIDIA, ROCm and CPU backends, so the softmax was silently wrong, by 105–118 % of the output for a row with 1 valid key and 0.2–0.8 % for 512–2048 keys (fp32 reference, sinks from the released V4...
- #67377 [Perf][ROCm][DSv4.1] DeepSeek-V4.1-Flash: dense MXFP8 GEMMs and wo_a on AITER's tuned FlyDSL kernels, and a faster MXFP8 activation quant (MI355X) [rocm, ready, deepseek, quantization, verified] (+286/-24) by @limou102 files: tests/kernels/quantization/test_rocm_mxfp8_linear.py, tests/models/test_dsv41_mono_numerics.py, vllm/_aiter_ops.py, vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py, vllm/model_executor/kernels/linear/mxfp8/rocm_native.py, vllm/model_executor/layers/quantization/utils/mxfp8_utils.py, vllm/models/deepseek_v41/amd/mono_decode.py, vllm/v1/attention/ops/rocm_aiter_mla_sparse.py
- #62800 [Bugfix] Fix KV cache pages for hybrid models with draft layers [bug, ready, cpu, kv-connector, nvidia, mrv2, mooncake, nixl] (+483/-80) by @seyfal files: tests/v1/attention/test_backend_per_kind.py, tests/v1/attention/test_group_head_counts.py, tests/v1/attention/test_kpool_indexer_block_sizes.py, tests/v1/attention/test_sparse_mla_kv_cache_layout.py, tests/v1/kv_connector/unit/offloading_connector/test_worker.py, tests/v1/kv_connector/unit/test_nixl_desc_geometry.py, tests/v1/worker/test_attn_utils.py, tests/v1/worker/test_gpu_model_runner.py, vllm/distributed/kv_transfer/kv_connector/utils.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py
- #67344 [ROCm][gfx1151] ROCM_RDNA_ATTN: prefer 16-token KV blocks [rocm, verified] (+18/-0) by @zohaibm-amd files: tests/kernels/attention/test_rocm_rdna_hip.py, vllm/v1/attention/backends/rocm_rdna_attn.py
- With `--attention-backend ROCM_RDNA_ATTN` and no `-...
- #62515 [Spec Decode] Enable adaptive verification for `FlashInferMLASparseSM90Backend` [ready, nvidia] (+22/-5) by @cjackal files: tests/v1/worker/test_attn_utils.py, vllm/v1/attention/backends/mla/flashinfer_mla_sparse_sm90.py
- Set `FlashInferMLASparseSM90Builder.get_varlen_cudagraph_max_query_len`
- #62964 [Bugfix][Spec Decode] Keep FlashInfer CUDA graphs for drafters with their own head count [bug, speculative-decoding, ready, nvidia, mrv2, kv-cache-manager] (+50/-18) by @seyfal files: tests/v1/attention/test_attention_backends.py, tests/v1/attention/test_group_head_counts.py, vllm/v1/attention/backends/flashinfer.py

**First-time contributors:** afierka-intel, cjackal, limou102, mickaelseznec, phambinhfin, seyfal, zohaibm-amd
### vllm-v1-core

Summary unavailable (null LLM). Source items:
- #66938 [Perf][Mamba] Optimize prefill splits for mid-block resume (3 forward passes to 1) [kv-cache-manager] (+293/-7) by @wzhao18 files: tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py, tests/v1/core/test_mamba_align_chunk_split.py, tests/v1/e2e/general/test_mamba_prefix_cache.py, vllm/v1/core/single_type_kv_cache_manager.py, vllm/v1/kv_cache_interface.py
- #66846 [Bugfix][EPD] Clear ECMooncakeConnector local cache on reset_encoder_cache [bug, ready, cpu, mrv2, scheduler, mooncake] (+871/-5) by @grYe99 files: tests/v1/ec_connector/unit/test_mooncake_reset_local_cache.py, tests/v1/worker/test_gpu_model_runner_v2.py, vllm/distributed/ec_transfer/ec_connector/base.py, vllm/distributed/ec_transfer/ec_connector/mooncake/memory.py, vllm/distributed/ec_transfer/ec_connector/mooncake/reservation.py, vllm/distributed/ec_transfer/ec_connector/mooncake/scheduler.py, vllm/distributed/ec_transfer/ec_connector/mooncake/state.py, vllm/distributed/ec_transfer/ec_connector/mooncake/worker.py, vllm/distributed/ec_transfer/ec_connector/mooncake_ec_connector.py, vllm/v1/core/sched/scheduler.py, vllm/v1/worker/cpu/ec_connector.py, vllm/v1/worker/cpu/standalone_model_runner.py
- #67717 [Bugfix][Mamba] Don't cache a block that a mid-block prefill resume ran past [bug, ready, kv-cache-manager] (+175/-0) by @wzhao18 files: tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py, vllm/v1/core/single_type_kv_cache_manager.py
- #65534 [Core][MM] Make the multimodal encoder cache size configurable  [ready, cpu, mrv2] (+174/-8) by @HangruiCao2000 files: tests/v1/core/test_encoder_cache_manager.py, tests/v1/worker/test_encoder_runner.py, vllm/config/scheduler.py, vllm/engine/arg_utils.py, vllm/v1/core/encoder_cache_manager.py, vllm/v1/worker/cpu/encoder_runner.py, vllm/v1/worker/gpu/mm/encoder_runner.py, vllm/v1/worker/utils.py
- **What:** `SchedulerConfig.encoder_cache_size` is derived from `max_num_batched_tokens` and is `Field(init=False)` with a standing `# TODO (ywang96): Make this configurable.` This adds `--encoder-cache-size`. `None` keeps today's derivation, so **no behaviour change unless it is set**.
- **Why:** they are different quantities. `max_num_encoder_input_tokens` is a per-step **c...
- #67599 [Bugfix][AuxOutput] Size the routed-experts row cache from one source [bug, ready, scheduler] (+99/-36) by @aoshen02 files: tests/distributed/aux_output_connector/test_store.py, tests/model_executor/test_routed_experts_capture.py, tests/v1/core/test_scheduler.py, vllm/distributed/aux_output_connector/connector.py, vllm/distributed/aux_output_connector/worker.py, vllm/model_executor/layers/fused_moe/routed_experts_capturer.py, vllm/v1/core/sched/scheduler.py
- The scheduler (`AuxOutputSchedulerConnector._capacity`) keeps `num_blocks` KV blocks of rows, doubled when a KV connector is configured, and ignores `aux_output_config.max_bytes`.
- The worker store (`initialize_output_storage`) uses `max_bytes` when set, otherwise `num_blocks * hashes_per_kv_block` objects, with ...
- #64156 [Spec Decode] Consistent drafted, verified and accepted token counts [documentation, performance, frontend, speculative-decoding, mrv2, rust, scheduler] (+461/-97) by @tomasruizt files: docs/features/speculative_decoding/acceptance_metrics.md, rust/src/bench/src/benchmark.rs, rust/src/bench/src/output/console.rs, rust/src/bench/src/output/json.rs, rust/src/chat/src/event.rs, rust/src/chat/src/output/structured.rs, rust/src/chat/src/stream.rs, rust/src/engine-core-client/src/metrics.rs, rust/src/engine-core-client/src/protocol/output.rs, rust/src/engine-core-client/src/protocol/stats.rs, rust/src/llm/src/log_stats.rs, rust/src/metrics/src/scheduler.rs
- **`drafted`**: tokens that came out of the drafter, including grammar-invalid ones.
- **`verified` (new)**: drafted tokens that went into the target forward pass.

**First-time contributors:** HangruiCao2000, aoshen02, grYe99, tomasruizt, wzhao18
### vllm-v1-engine

Summary unavailable (null LLM). Source items:
- #67872 [Rust Frontend] Support --kv-sharing-fast-prefill [rust] (+249/-11) by @BugenZhao files: rust/src/cmd/src/cli/unsupported.rs, rust/src/engine-core-client/src/client.rs, rust/src/engine-core-client/src/mock_engine.rs, rust/src/engine-core-client/src/protocol/handshake.rs, rust/src/engine-core-client/src/tests/client.rs, rust/src/engine-core-client/src/tests/python_compat.py, rust/src/llm/src/error.rs, rust/src/llm/src/lib.rs, rust/src/llm/tests/generate.rs, rust/src/server/src/routes/tests.rs, rust/src/text/src/error.rs, vllm/v1/engine/__init__.py

**First-time contributors:** BugenZhao
### vllm-v1-hisparse

Summary unavailable (null LLM). Source items:
- #67516 [Bugfix][HiSparse] Fix GLM-5.3-Flash startup: derive resident/hot specs without grouping on workers [bug, ready, glm, hisparse] (+139/-57) by @MatthewBonanni files: tests/v1/worker/test_attn_utils.py, vllm/v1/hisparse/binding.py, vllm/v1/hisparse/layout.py

**First-time contributors:** MatthewBonanni
### vllm-v1-kv_cache_interface.py

Summary unavailable (null LLM). Source items:
- #66938 [Perf][Mamba] Optimize prefill splits for mid-block resume (3 forward passes to 1) [kv-cache-manager] (+293/-7) by @wzhao18 files: tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py, tests/v1/core/test_mamba_align_chunk_split.py, tests/v1/e2e/general/test_mamba_prefix_cache.py, vllm/v1/core/single_type_kv_cache_manager.py, vllm/v1/kv_cache_interface.py
- #62800 [Bugfix] Fix KV cache pages for hybrid models with draft layers [bug, ready, cpu, kv-connector, nvidia, mrv2, mooncake, nixl] (+483/-80) by @seyfal files: tests/v1/attention/test_backend_per_kind.py, tests/v1/attention/test_group_head_counts.py, tests/v1/attention/test_kpool_indexer_block_sizes.py, tests/v1/attention/test_sparse_mla_kv_cache_layout.py, tests/v1/kv_connector/unit/offloading_connector/test_worker.py, tests/v1/kv_connector/unit/test_nixl_desc_geometry.py, tests/v1/worker/test_attn_utils.py, tests/v1/worker/test_gpu_model_runner.py, vllm/distributed/kv_transfer/kv_connector/utils.py, vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py, vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py

**First-time contributors:** seyfal, wzhao18
### vllm-v1-kv_offload

Summary unavailable (null LLM). Source items:
- #66583 [KV Offload] Set the CPU tier up in the background under async_init [documentation, ready, kv-connector, nixl] (+390/-25) by @Etelis files: docs/features/kv_offloading_usage.md, tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py, tests/v1/kv_connector/unit/offloading_connector/test_worker.py, tests/v1/kv_connector/unit/offloading_connector/utils.py, tests/v1/kv_offload/cpu/test_shared_offload_region.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/common.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py, vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py, vllm/v1/kv_offload/base.py, vllm/v1/kv_offload/cpu/gpu_worker.py, vllm/v1/kv_offload/cpu/shared_offload_region.py, vllm/v1/kv_offload/cpu/spec.py
- The setup thread switches itself to relaxed capture mode, so pinning can't invalid...
- #62058 [KV Offload] Explain EFAULT from a full /dev/shm in _madvise_populate_write [ready, hisparse, nixl] (+48/-1) by @mushroomcarbon files: tests/v1/kv_offload/cpu/test_shared_offload_region.py, vllm/v1/kv_offload/cpu/shared_offload_region.py
- #67788 [Bugfix][KV Offload] Report transferred bytes in tiering metrics [bug, ready, nixl] (+35/-0) by @waizuichougou files: tests/v1/kv_offload/tiering/test_metrics.py, tests/v1/kv_offload/tiering/test_tiering_offloading.py, vllm/v1/kv_offload/tiering/metrics.py
- Avoid counting FS blocks skipped because they already exist as bytes written.
- Preserve the existing fallback and partial-failure accounting.
- Tests cover reported byte counts, including z...
- #67258 [KV Offload] Add mmap_path to SharedOffloadRegion [ready, nixl] (+75/-6) by @omerpaz95 files: tests/v1/kv_offload/cpu/test_shared_offload_region.py, vllm/v1/kv_offload/cpu/shared_offload_region.py
- #63524 [Bugfix][KV Offload] Report only written blocks from fs tier store jobs [bug, ready, nixl] (+177/-33) by @AdvayMonga files: csrc/fs_io.cpp, tests/v1/kv_offload/tiering/test_backpressure.py, tests/v1/kv_offload/tiering/test_fs_tier.py, tests/v1/kv_offload/tiering/test_tiering_offloading.py, vllm/v1/kv_offload/tiering/fs/io.py, vllm/v1/kv_offload/tiering/fs/manager.py

**First-time contributors:** AdvayMonga, Etelis, mushroomcarbon, omerpaz95, waizuichougou
### vllm-v1-metrics

Summary unavailable (null LLM). Source items:
- #64156 [Spec Decode] Consistent drafted, verified and accepted token counts [documentation, performance, frontend, speculative-decoding, mrv2, rust, scheduler] (+461/-97) by @tomasruizt files: docs/features/speculative_decoding/acceptance_metrics.md, rust/src/bench/src/benchmark.rs, rust/src/bench/src/output/console.rs, rust/src/bench/src/output/json.rs, rust/src/chat/src/event.rs, rust/src/chat/src/output/structured.rs, rust/src/chat/src/stream.rs, rust/src/engine-core-client/src/metrics.rs, rust/src/engine-core-client/src/protocol/output.rs, rust/src/engine-core-client/src/protocol/stats.rs, rust/src/llm/src/log_stats.rs, rust/src/metrics/src/scheduler.rs
- **`drafted`**: tokens that came out of the drafter, including grammar-invalid ones.
- **`verified` (new)**: drafted tokens that went into the target forward pass.
- **`accepted`**: unchanged.

**First-time contributors:** tomasruizt
### vllm-v1-spec_decode

Summary unavailable (null LLM). Source items:
- #64156 [Spec Decode] Consistent drafted, verified and accepted token counts [documentation, performance, frontend, speculative-decoding, mrv2, rust, scheduler] (+461/-97) by @tomasruizt files: docs/features/speculative_decoding/acceptance_metrics.md, rust/src/bench/src/benchmark.rs, rust/src/bench/src/output/console.rs, rust/src/bench/src/output/json.rs, rust/src/chat/src/event.rs, rust/src/chat/src/output/structured.rs, rust/src/chat/src/stream.rs, rust/src/engine-core-client/src/metrics.rs, rust/src/engine-core-client/src/protocol/output.rs, rust/src/engine-core-client/src/protocol/stats.rs, rust/src/llm/src/log_stats.rs, rust/src/metrics/src/scheduler.rs
- **`drafted`**: tokens that came out of the drafter, including grammar-invalid ones.
- **`verified` (new)**: drafted tokens that went into the target forward pass.
- **`accepted`**: unchanged.

**First-time contributors:** tomasruizt
### vllm-v1-worker

Summary unavailable (null LLM). Source items:
- #49700 [EPLB] Expose narrow state overrides for out-of-tree devices [documentation, rocm, ready, ci/build, deepseek, nvidia, DSv4, kimi, k3] (+671/-307) by @freyfwt files: .buildkite/test_areas/expert_parallelism.yaml, docs/design/plugin_system.md, tests/distributed/test_eplb_algo.py, tests/distributed/test_eplb_extension_hooks.py, tests/distributed/test_eplb_utils.py, vllm/config/parallel.py, vllm/distributed/eplb/async_worker.py, vllm/distributed/eplb/eplb_state.py, vllm/distributed/eplb/policy/__init__.py, vllm/distributed/eplb/policy/abstract.py, vllm/distributed/eplb/policy/default.py, vllm/platforms/interface.py
- Keep built-in selector `Literal`...
- #64306 [Spec Decode][MRV2] Pass NewRequestData to speculator add_request; add shutdown hook [documentation, speculative-decoding, ready, mrv2] (+76/-11) by @chenyzhang-nvidia files: docs/features/speculative_decoding/README.md, tests/v1/spec_decode/test_suffix_speculator.py, tests/v1/worker/test_gpu_model_runner_v2.py, vllm/v1/worker/gpu/model_runner.py, vllm/v1/worker/gpu/spec_decode/speculator.py, vllm/v1/worker/gpu/spec_decode/suffix/speculator.py
- `add_request(req_index, new_req_data)` also receives the request's `NewRequestData`, as `model_state.add_request` does.
- New `shutdown()`, called w...
- #67094 [Spec Decode] Add DSpine support [documentation, new-model, speculative-decoding, ready, ci/build, qwen, mrv2, dflash] (+569/-21) by @shanjiaz files: .buildkite/test_areas/spec_decode.yaml, docs/features/speculative_decoding/README.md, tests/models/registry.py, tests/v1/e2e/spec_decode/acceptance_rates/dflash/test_dflash.py, vllm/model_executor/models/qwen3_dspine.py, vllm/model_executor/models/registry.py, vllm/transformers_utils/configs/eagle.py, vllm/transformers_utils/configs/speculators/algos.py, vllm/transformers_utils/configs/speculators/base.py, vllm/v1/worker/gpu/spec_decode/dflash2/speculator.py, vllm/v1/worker/gpu/spec_decode/dspine/__init__.py, vllm/v1/worker/gpu/spec_decode/dspine/config.py
- Supports Tencent and Speculators checkpoint layouts through one model implementation.
- Reuses existing candidate sampli...
- #67571 [MRV2][Spec Decode] Cap dummy-run requests by their draft slots [ready, mrv2] (+26/-18) by @JonSnow1807 files: tests/v1/worker/test_gpu_model_runner_v2.py, vllm/v1/worker/gpu/model_runner.py
- #65565 [Refactor][Worker] Expose platform initialization hooks [documentation, ready, ci/build] (+11/-4) by @Ronald1995 files: vllm/v1/worker/gpu_worker.py
- `_validate_profiler_config()` allows subclasses to validate their device's profiler configuration.
- `_make_elastic_ep_...

**First-time contributors:** 0z5a, Ankur-singh, HangruiCao2000, JonSnow1807, Ronald1995, RyanMa29, alex-jw-brooks, benenzhu, chenyzhang-nvidia, cjackal, freyfwt, grYe99, ilmarkov, njhill, seyfal, shanjiaz, simon-veitner-redhat, tomasruizt, vadiklyutiy, wtdcode, xsxszab, yewentao256, yibol9768-alt, zixi-qi

### Highlights
- New release **v0.34.0** — v0.34.0

## vllm-project/DeepGEMM (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #64 Fix SM90 tf32_hc_prenorm_gemm WGMMA register reuse race (cherry-pick deepseek-ai#448) (+63/-1) by @mgoin files: deep_gemm/include/deep_gemm/impls/sm90_tf32_hc_prenorm_gemm.cuh, tests/test_hyperconnection.py
- #63 SM90 paged MQA metadata: take the batch size at runtime (+11/-9) by @mgoin files: csrc/jit_kernels/impls/sm90_fp8_mqa_logits.hpp, deep_gemm/include/deep_gemm/scheduler/sm90_paged_mqa_logits.cuh
- #59 Fix MegaMoE combine readiness under CUDA graph replay (cherry-pick deepseek-ai#451) (+21/-9) by @gau-nernst files: deep_gemm/include/deep_gemm/impls/sm100_bf16_mega_moe.cuh, deep_gemm/include/deep_gemm/impls/sm100_fp8_fp4_mega_moe.cuh, deep_gemm/include/deep_gemm/impls/sm100_fp8_fp4_mega_moe_situ.cuh, deep_gemm/include/deep_gemm/impls/sm100_nvfp4_mega_moe.cuh, deep_gemm/include/deep_gemm/layout/mega_moe.cuh


## vllm-project/FlashMLA (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #37 Sm90 small heads etap prefill support (+640/-1) by @huishi-hs files: csrc/cuda_kernels/legacy/sm90/prefill/sparse/etap.cuh, csrc/cuda_kernels/legacy/sm90/prefill/sparse/phase1.cuh, tests/bench_small_heads_sparse_prefill.py, tests/test_flash_mla_sparse_prefill.py


## vllm-project/MSA (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #52 m3_topk: split long decode rows over a CTA (+154/-3) by @caitlinw-nvidia files: python/fmha_sm100/csrc/include/indexer_topk/m3_topk.cuh, python/fmha_sm100/csrc/include/indexer_topk/topk_select.cuh


## vllm-project/afd-plugin (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #585 test(GPU): Cleanup M2N GPU tests [NVIDIA, ready] (+76/-163) by @ronenkat files: afd_plugin/connectors/gpu/deepep_m2n/connector.py, tests/gpu/README.md, tests/gpu/deepep_m2n_harness.py, tests/gpu/test_deepep_m2n_gpu.py, tests/unit/connectors/test_deepep_m2n_connector.py
- Related issue(s): #512
- Closing keyword, only if fully resolved: Clos...
- #594 [CI]: Test for reporting ready pipeline steps as GitHub checks [NVIDIA, ready] (+8/-0) by @ronenkat files: .buildkite/cuda/test-ready.yml
- #562 refactor: decouple shared FFN components from model adapters [documentation, Ascend, NVIDIA, ready] (+1557/-1037) by @lirx-pd files: .agents/skills/review-pr/references/features/async-cam-ubatching.md, .agents/skills/review-pr/references/features/dspark-draft.md, afd_plugin/compat/patches/gpu_deepseek_v4_dbo.py, afd_plugin/connectors/npu/async_cam_runtime/async_cam_layered.py, afd_plugin/connectors/npu/async_cam_runtime/async_cam_layout.py, afd_plugin/connectors/npu/async_cam_runtime/async_cam_mega.py, afd_plugin/envs.py, afd_plugin/ffn_faas/platforms/ffn_model/deepseek_v4/npu/v4_weights.py, afd_plugin/ffn_faas/platforms/npu/model.py, afd_plugin/forward_context.py, afd_plugin/model_executor/ffn/__init__.py, afd_plugin/model_executor/ffn/npu/__init__.py
- Related issue(s): #565 .
- Closing keyword, only if fully resolved: None.
- In scope: Share...
- #591 docs: refresh WeChat community QR code [documentation] (+0/-0) by @david6666666 files: docs/assets/WeChat.png
- Refresh the WeChat QR image currently referenced by the README.
- Supersedes the QR image from #556.
- The new QR image states it is valid for seven days, until 2026-11-23; refresh it after expiration if needed.


## vllm-project/agentic-api (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #520 feat: model MCP require_approval as a typed policy (+4391/-19) by @sohom-cs files: CHANGELOG.md, crates/agentic-server-core/src/tool/executors.rs, crates/agentic-server-core/src/tool/executors/tests.rs, crates/agentic-server-core/src/tool/mcp/handler.rs, crates/agentic-server-core/src/types/tools/mcp_approval.rs, crates/agentic-server-core/src/types/tools/mod.rs, crates/agentic-server-core/src/types/tools/params.rs, crates/agentic-server-core/tests/cassettes/README.md, crates/agentic-server-core/tests/cassettes/mcp/mcp-approval-gateway-gpt-5.6-sol-nonstreaming.yaml, crates/agentic-server-core/tests/cassettes/mcp/mcp-approval-openai-gpt-5.6-sol-nonstreaming.yaml, crates/agentic-server-core/tests/cassettes/record_cassette.py, crates/agentic-server-core/tests/cassettes/record_mcp_cassettes.sh
- #531 fix: reject unknown conversation id instead of implicit creation (+2298/-993) by @justrightnow files: ARCHITECTURE.md, crates/agentic-server-core/src/executor/error.rs, crates/agentic-server-core/src/executor/modes/conversation.rs, crates/agentic-server-core/src/executor/rehydrate.rs, crates/agentic-server-core/src/storage/conversation.rs, crates/agentic-server-core/src/storage/models/conversation.rs, crates/agentic-server-core/src/storage/types/errors.rs, crates/agentic-server-core/tests/cassettes/README.md, crates/agentic-server-core/tests/cassettes/record_cassette.py, crates/agentic-server-core/tests/cassettes/record_responses_api_cassettes.sh, crates/agentic-server-core/tests/cassettes/responses/response-conversation-gateway.yaml, crates/agentic-server-core/tests/cassettes/responses/response-conversation-openai.yaml
- #545 test: share an input item types helper across gateway continuation tests (+19/-20) by @Than0316 files: crates/agentic-server-core/tests/mcp_tool_test.rs, crates/agentic-server-core/tests/support/mod.rs, crates/agentic-server-core/tests/web_search_tool_test.rs
- `cargo test -p agentic-server-core --test mcp_tool_test --test web_search_tool_test --test hosted_too...
- #512 feat: validate Responses capabilities per model (+1880/-614) by @skyloevil files: ARCHITECTURE.md, README.md, crates/agentic-llm-d/src/main.rs, crates/agentic-llm-d/src/runner.rs, crates/agentic-llm-d/tests/split_execution_integration.rs, crates/agentic-server-core/src/config.rs, crates/agentic-server-core/src/config/responses.rs, crates/agentic-server-core/src/executor/compaction.rs, crates/agentic-server-core/src/executor/engine/multi_agent_tests/service_tier.rs, crates/agentic-server-core/src/executor/error.rs, crates/agentic-server-core/src/executor/rehydrate.rs, crates/agentic-server-core/src/executor/request.rs
- #533 chore: document what a turn persists and update the roadmap (+732/-844) by @maralbahari files: .agents/skills/storage-schema-change/SKILL.md, AGENTS.md, ARCHITECTURE.md, README.md, ROADMAP.md, docs/api/index.md, docs/guides/configuration.md, docs/guides/messages-server-tools.md, docs/guides/web-search.md, mkdocs.yaml, website/content/docs/api/index.md
- #537 Avoid quadratic copying when assembling Messages stream deltas (+32/-5) by @SProst files: crates/agentic-server-core/src/executor/messages_stream/blocks.rs
**Messages string deltas now append in place, closing the quadratic-copying path while preserving stream assembly.**
- `append_str` mutates existing `Value::String` buffers with `push_str`, so fragments no longer recopy the accumulated prefix.
- The shared helper covers model-controlled text, thinking, and signature deltas, preventing CPU and allocator amplification across every re...
- #495 docs: add security policy and reporting guidance (+61/-0) by @SProst files: SECURITY.md
- Add a repository-specific security policy covering vulnerability reporting, version and scope triage, and coordinated disclosure.


## vllm-project/aibrix (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #3462 [Bug] Forward vLLM-Omni synchronous video requests [kind/documentation, area/runtime] (+1152/-23) by @Suyi32 files: python/aibrix/README.md, python/aibrix/aibrix/openai_frontend/engine/proxy_engine.py, python/aibrix/aibrix/openai_frontend/proxy/runtime/engine_spec.py, python/aibrix/aibrix/openai_frontend/proxy/runtime/video_sync.py, python/aibrix/tests/openai_frontend/test_endpoint_boundaries.py, python/aibrix/tests/openai_frontend/test_proxy_fault_tolerance.py, python/aibrix/tests/openai_frontend/test_video_sync.py
- #3385 [Bug] Reopen a lost KV event replay socket, and fail the gap open if it stays lost (+164/-3) by @sohom-cs files: pkg/cache/kvcache/zmq_client.go, pkg/cache/kvcache/zmq_client_test.go
- #3197 [Feat] Pass encoders' ec_transfer_params to the request that consumes them [kind/documentation, area/gateway, area/website, area/installation, area/kv-cache] (+499/-49) by @theminjunchoi files: docs/source/features/gateway-routing/pd-disaggregation.rst, docs/source/locale/zh_CN/LC_MESSAGES/features/gateway-routing/pd-disaggregation.po, pkg/plugins/gateway/algorithms/pd/encode/encode.go, pkg/plugins/gateway/algorithms/pd/encode/encode_test.go, pkg/plugins/gateway/algorithms/pd/encode/selection_test.go, pkg/plugins/gateway/algorithms/pd/encode/stage.go, pkg/plugins/gateway/algorithms/pd_readme.md, samples/disaggregation/vllm/1e1p1d-ec-nixl.yaml
- #3383 [Bug] Don't hold pod events on the KV event replay in Start and Stop (+356/-19) by @sohom-cs files: pkg/cache/kvcache/zmq_client.go, pkg/cache/kvcache/zmq_client_regression_test.go, pkg/cache/kvcache/zmq_client_test.go
- #3416 [Bug] Reject non-finite values in LoadEnvFloat (+40/-1) by @yisususu files: pkg/utils/util.go, pkg/utils/util_test.go
- #3455 [Misc] Parse only the metric families the gateway reads from engine scrapes (+1233/-20) by @dogeONE-bit files: pkg/cache/pod_metrics_scrape_benchmark_test.go, pkg/metrics/engine_fetcher.go, pkg/metrics/family_filter.go, pkg/metrics/family_filter_test.go, pkg/metrics/testdata/vllm_metrics.txt
- #3467 [Feat] Run the inflight saturation filter on the candidate set [kind/documentation, area/gateway, area/website] (+783/-60) by @saylee21 files: docs/source/features/gateway-routing/gateway-plugins.rst, docs/source/locale/zh_CN/LC_MESSAGES/features/gateway-routing/gateway-plugins.po, pkg/plugins/gateway/ENV_VARS.md, pkg/plugins/gateway/algorithms/candidates.go, pkg/plugins/gateway/algorithms/candidates_test.go, pkg/plugins/gateway/algorithms/fleet_routing_benchmark_test.go, pkg/plugins/gateway/algorithms/routing_profile_knobs_test.go, pkg/plugins/gateway/gateway.go, pkg/plugins/gateway/gateway_inflight.go, pkg/plugins/gateway/gateway_test_helpers.go, pkg/plugins/gateway/inflight_metrics.go, pkg/plugins/gateway/inflight_ordering_test.go
**New order ...
- #3458 [Bug] Break multi-strategy score ties by running requests before pod name [area/gateway] (+245/-2) by @sh0116 files: pkg/plugins/gateway/algorithms/load_balance.go, pkg/plugins/gateway/algorithms/router.go, pkg/plugins/gateway/algorithms/router_test.go
- #3429 [Bug] Clarify ModelWarmup control-plane exclusion diagnostics [area/orchestration] (+155/-48) by @googs1025 files: pkg/controller/modelwarmup/continuous_lifecycle.go, pkg/controller/modelwarmup/modelwarmup_controller.go, pkg/controller/modelwarmup/modelwarmup_controller_test.go, pkg/controller/modelwarmup/reconcile_snapshot.go, pkg/controller/modelwarmup/reconcile_snapshot_test.go
- Preserve the existing `NodeNotAuthorized` target status reason while giving control-plane exclusions a specific message.
- Explain the same rest...


## vllm-project/ci-infra (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #777 [CI][ROCm] Add AITER_NIGHTLY to Pipeline Generator [vllm-modelperf] (+514/-39) by @josh-schell-amd files: README.md, buildkite/ci_selector/DESIGN.md, buildkite/ci_selector/README.md, buildkite/ci_selector/tests/test_generator_contract.py, buildkite/pipeline_generator/README.md, buildkite/pipeline_generator/amd.py, buildkite/pipeline_generator/buildkite_step.py, buildkite/pipeline_generator/global_config.py, buildkite/pipeline_generator/pipeline_generator.py, buildkite/pipeline_generator/recorder_switches.py, buildkite/pipeline_generator/selector_gate.py, buildkite/tests/pipeline_generator/conftest.py
- `image-build-amd` (vLLM's `build.sh`) selects the newest compatible AITER nightly wheel, matching the ROCm, torch and Python versions in the ci_base image, and installs it into the test image, which goes to `rocm/vllm-...
- #914 [ci-selector] Write CUDA kernel names at launch so recordings no longer need the exit footer (+851/-157) by @tahsintunan files: buildkite/ci_selector/recorders/kernrec/README.md, buildkite/ci_selector/recorders/kernrec/build.sh, buildkite/ci_selector/recorders/kernrec/cross-build.sh, buildkite/ci_selector/recorders/kernrec/kernel_table.py, buildkite/ci_selector/recorders/kernrec/kernrec.c, buildkite/ci_selector/recorders/kernrec/libkernrec.so, buildkite/ci_selector/recorders/kernrec/test-cuda.sh, buildkite/ci_selector/recorders/kernrec/test_cuda_callbacks.c, buildkite/ci_selector/tests/recorders/test_kernel_table.py
- A CUDA recording only counts as complete when its process writes the `# end` footer at normal exit. Many processes never get there: vLLM kills the engine process 5 s into shutdown, and forked children leave through `os._exit`, which skips the code that writes the footer. One such process makes its whole step unusable, so only about half the CUDA rows can be used (130 of 250 on nig...
- #913 [ci-selector] Stop always picking AMD jobs that set `automatic_shard` (+71/-9) by @tahsintunan files: buildkite/ci_selector/ci_selector/codemap/classify.py, buildkite/ci_selector/ci_selector/handwritten.py, buildkite/ci_selector/tests/test_buildkite.py, buildkite/ci_selector/tests/test_classify.py
- AMD jobs can set `automatic_shard` in their `mirror: amd:` block. The selector didn't know this setting, and it picks every job that has a setting it doesn't know, just in case. So about 200 AMD jobs were picked on every PR, whatever the PR changed. On a PR that changes one test file, this change cuts the AMD jobs picked from 207 to 3, and the NVIDIA jobs picked stay exactly the s...
- #912 [kernrec] Keep the ROCm recorder off the AMD TurboQuant LM Eval steps (+42/-1) by @AndreasKaratzas files: buildkite/pipeline_generator/buildkite_step.py, buildkite/tests/pipeline_generator/test_kernrec.py
- #907 [AMD][CI] Add mi300_dpx device for the amd_mi300_dpx queue (+28/-10) by @sheralskumar files: buildkite/pipeline_generator/amd.py, buildkite/pipeline_generator/constants.py, buildkite/tests/pipeline_generator/test_amd.py
- `constants.py`: add `DeviceType.AMD_MI300_DPX` and `AgentQueue....
- #908 [pipeline-generator] Find the tracing helpers in the CPU test image (+39/-3) by @Thangnguyenvn98 files: buildkite/pipeline_generator/buildkite_step.py, buildkite/tests/pipeline_generator/test_step.py
- #899 [ci-selector] Bootstrap ~2.6 min faster: build the import graph once and parse the coverage table once (+277/-68) by @latioswang files: .gitignore, buildkite/ci_selector/README.md, buildkite/ci_selector/ci_selector/cli.py, buildkite/ci_selector/ci_selector/codemap/graph/imports.py, buildkite/ci_selector/ci_selector/coverage/rules.py, buildkite/ci_selector/ci_selector/coverage/source.py, buildkite/ci_selector/ci_selector/decide.py, buildkite/ci_selector/ci_selector/scripts/fetch_functions.py, buildkite/ci_selector/tests/coverage/test_publish_and_fetch.py, buildkite/ci_selector/tests/coverage/test_rowkeys_resolve.py, buildkite/ci_selector/tests/test_cli_modes.py, buildkite/ci_selector/tests/test_dynamic_sites.py
- the import graph of the vLLM tree (~5.9k files) is built once instead of twice;


## vllm-project/compressed-tensors (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #1008 [Quantization] Restrict int/float quantization [ready] (+21/-5) by @kylesayrs files: src/compressed_tensors/compressors/naive_quantized/base.py, tests/test_compressors/model_compressors/test_transformers_integration.py, tests/test_compressors/test_compress_decompress_module.py, tests/test_modeling/test_deepseekv3_kvcache_quant.py
* W8A8 goes to naive (to leverage cutlass)
* All else go to packed


## vllm-project/flash-attention (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #208 Mark compatible with Python 3.14 (+1/-1) by @amarshall files: CMakeLists.txt
---
- #218 [Cute,Fwd,Sm90] Finish the FP8 QK-split scores before the PV passes (+8/-4) by @jhaotingc files: flash_attn/cute/flash_fwd_sm90.py


## vllm-project/guidellm (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #1587 feat(warnings): warn when more than 5% of requests errored (+227/-25) by @yaokaiy files: docs/en/guides/warnings.md, src/guidellm/benchmark/schemas/warnings.py, src/guidellm/benchmark/warnings.py, src/guidellm/schemas/benchmark/warnings.py, tests/unit/benchmark/test_warnings.py
- #1591 docs: update multimodal preprocessing examples (+75/-119) by @git-jxj files: docs/en/guides/multimodal/audio.md, docs/en/guides/multimodal/image.md, docs/en/guides/multimodal/video.md, docs/zh/guides/multimodal/audio.md, docs/zh/guides/multimodal/image.md, docs/zh/guides/multimodal/video.md
- #1290 fix(csv): retain zero-valued measurement statistics (+160/-28) by @git-jxj files: docs/en/guides/outputs.md, src/guidellm/benchmark/outputs/csv.py, src/guidellm/benchmark/schemas/metrics.py, tests/unit/benchmark/schemas/test_metrics.py, tests/unit/benchmark/test_csv_output.py
- Preserve status ...
- #1583 Report choice index 0 in the mock server's streamed completions [community contribution, bug] (+119/-2) by @sohailshk files: src/guidellm/mock_server/handlers/completions.py, tests/integration/mock_server/__init__.py, tests/integration/mock_server/test_completions_stream.py, tests/unit/mock_server/handlers/__init__.py, tests/unit/mock_server/handlers/test_completions.py
- #1455 fix: vary synthetic image and video across benchmarks [community contribution, bug] (+95/-13) by @boqiny files: src/guidellm/data/deserializers/synthetic_image.py, src/guidellm/data/deserializers/synthetic_video.py, src/guidellm/utils/vision.py, tests/unit/data/deserializers/test_synthetic_multimodal.py
- #1549 Send `extras` headers and params on the health check and the models list [community contribution, feature, cli] (+41/-4) by @wguo7 files: src/guidellm/backends/openai/http.py, tests/unit/backends/openai/test_http.py
- `validate()` and `available_models()` no...
- #1573 Gitignore common editor configs and add Direnv support (+20/-0) by @sjmonson files: .envrc, .gitignore
- #1459 perf(backends): buffer streamed tool-call arguments (+128/-34) by @Butterski files: docs/en/guides/tool_calling.md, src/guidellm/backends/openai/request_handlers.py, tests/unit/backends/openai/test_request_handlers.py
- Preserve exact arguments, Unicode, tool IDs, names, and ordering.
- Preserve received arguments across partial...


## vllm-project/humming (watch)

### Releases
- [v0.1.20](https://github.com/vllm-project/humming/releases/tag/v0.1.20) — 2026-11-16: v0.1.20
### Changes

Summary unavailable (null LLM). Source items:
- #211 fix(packaging): resolve Linux cu12/cu13 extras through cuda-toolkit (+13/-8) by @mgoin files: README.md, pyproject.toml
- #206 perf(moe): improve SM103 MXFP4 x MXFP8 pipelines and heuristics (+262/-22) by @jinzhen-lin files: humming/config/config.py, humming/include/humming/epilogue/gmem_writer.cuh, humming/include/humming/kernel/humming_umma.cuh, humming/include/humming/memory/g2s_loader/loader_a.cuh, humming/include/humming/memory/g2s_loader/loader_as.cuh, humming/include/humming/memory/g2s_pipeline.cuh, humming/include/humming/scheduler.cuh, humming/include/humming/utils/context.cuh, humming/kernel/humming.py, humming/tune/sm100.py, tests/kernels/humming/test_moe.py
- #196 fix(cuda): preserve 64-bit element counts in weight dequantization (+64/-2) by @xijiaat files: humming/include/humming/kernel/dequant_weight.cuh, humming/kernel/dequant_weight.py, tests/kernels/test_dequant_weight.py
- `uint64_t total_size` in `dequant_unpacked_fp_type`.
- `ctypes.c_uint64` for the corresponding Python launch argument.
- #207 feat(weight): add packed weight type conversion (+659/-85) by @jinzhen-lin files: humming/include/humming/kernel/convert_weight.cuh, humming/include/humming/kernel/pack_weight.cuh, humming/kernel/convert_weight.py, humming/kernel/pack_weight.py, humming/kernel/unpack_weight.py, humming/layer.py, humming/ops/__init__.py, humming/ops/weight.py, humming/schema/autoround.py, humming/schema/awq.py, humming/schema/base.py, humming/schema/bitnet.py
- #202 fix(jit): let nvrtc_compile find libnvrtc-builtins on Linux (+15/-0) by @tiny-star3 files: humming/csrc/nvrtc_compile.cpp
- #208 perf(tune): use the warp-specialized ring for short-K SM90 indexed A8 MoE (+18/-7) by @mgoin files: humming/tune/sm90_policies.py
- #203 fix(transform): split non-power-of-two weight scale groups (+89/-1) by @mgoin files: humming/transform.py, tests/kernels/humming/test_scale.py
- #204 fix(ops): accept non-contiguous zero points in repack_weight (+28/-1) by @mgoin files: humming/ops/weight.py, tests/kernels/humming/test_zero_point.py
- #199 fix(process_input): limit the wide-vector rules to SM90 and SM100 (+31/-5) by @mgoin files: humming/tune/process_input.py, tests/test_process_input_tuning.py
- #197 perf(process_input): use wider vectors on large SM90/SM100 grids (+145/-2) by @mgoin files: humming/tune/process_input.py, tests/test_process_input_tuning.py

### Highlights
- New release **v0.1.20** — v0.1.20

## vllm-project/llm-compressor (watch)

### Releases
- [0.9.0.6](https://github.com/vllm-project/llm-compressor/releases/tag/0.9.0.6) — 2026-11-10: v0.9.0.6
### Changes

Summary unavailable (null LLM). Source items:
- #3522 [Docs] Add Research Hub entry: Arabic vs English calibration for W4A16, NVFP4 and FP8 on Qwen3-8B [documentation, ready] (+304/-0) by @mahmoudzahran01 files: docs/research/w4a16-nvfp4-arabic-calibration-qwen3-mahmoudzahran01.md
**Setup.** English (UltraChat), Arabic (Aya) and 50/50 mixed calibration sets, 512 x 2048 packed tokens each, for W4A16 GPTQ and NVFP4, plus FP8 dynamic. Evaluated 0-shot on ArabicMMLU and MMLU with lm-eval's vLLM backend, on one DGX Spa...
- #3514 [Tracing] Share Gemma4's shared_kv_states dict across traced layers [ready] (+109/-3) by @dundysm files: src/llmcompressor/pipelines/cache.py, src/llmcompressor/pipelines/sequential/helpers.py, tests/llmcompressor/pipelines/sequential/test_shared_kv_states.py
- #3502 [Bugfix] Keep lm_head disabled when the sequential pipeline onloads subgraphs [ready] (+59/-3) by @jontb files: src/llmcompressor/utils/helpers.py, tests/llmcompressor/utils/test_helpers.py
- #3454 Tune imatrix observer defaults and remove Triton patience buffer [ready, Refactor, iMatrix] (+49/-143) by @HDCharles files: docs/guides/observers.md, src/llmcompressor/observers/grid_search.py, src/llmcompressor/observers/imatrix.py, src/llmcompressor/observers/mse.py, tests/llmcompressor/observers/test_imatrix.py, tests/llmcompressor/observers/test_mse.py
- #3517 [Tests] Fix compressed-tensors tests for transformers 5.23 dequantize semantics [ready] (+49/-16) by @kylesayrs files: tests/llmcompressor/transformers/compression/test_decompress.py, tests/llmcompressor/transformers/compression/test_quantization.py, tests/llmcompressor/transformers/compression/test_run_compressed.py, tests/llmcompressor/transformers/kv_cache/test_kv_cache.py
- transformers 5.23.0 changed `CompressedTensorsConfig(dequantize=True)` to load a plain dense model with no quantization metadata (huggingface/transformers#50238), instead of wrapping modules with compressed-tensors schemes and decompressing them in place
- this broke tests in the transformers CI job (see e.g. builds 2631 and 2633), all of which relied on the old behavior:
- `test_q...
- #3509 Update imatrix_mse observer description in documentation [documentation, ready] (+1/-1) by @HDCharles files: docs/guides/observers.md
- #3498 [Docs] Update README Muse Spark Open MXFP4xFP8 checkpoint [documentation, ready] (+4/-2) by @bartowski1182 files: README.md
- #3499 [Docs] Add Mistral 4 Example [documentation, ready] (+107/-0) by @Roderick-Wu files: examples/model_free_ptq/mistral_large_4_mxfp4xfp8.py

### Highlights
- New release **0.9.0.6** — v0.9.0.6

## vllm-project/recipes (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #1261 Mark what a recipe is on its card; omni recipes carry the vLLM-Omni ring (+277/-51) by @esmeetu files: src/app/[org]/[repo]/page.js, src/app/[org]/page.js, src/app/browse/page.js, src/components/icons/OmniMark.jsx, src/components/recipes/BrowseList.jsx, src/components/recipes/ModelSidebar.jsx, src/components/recipes/RecipeCardGrid.jsx, src/components/recipes/task-icons.js, src/lib/recipe-utils.js
- **Tasks were the weakest element on the card.** They came last, in the faint `subtle` badge style, and often wrapped to a second line. Yet the kind of model is the first thing a reader filters by.
- **"Omni" says too little.** It is vLLM-Omni's product name. All 32 omni recipes are generation models (image, video ...
- #1260 Link the vLLM version badge to its release notes; add Adventists AI (+49/-13) by @esmeetu files: .agents/skills/add-recipe/SKILL.md, SCHEMA.md, src/app/[org]/[repo]/page.js, src/lib/command-synthesis.js, src/lib/providers.js
- #1259 Make shared recipe links render what the page shows, for people and agents (+77/-24) by @esmeetu files: CLAUDE.md, next.config.mjs, src/app/api/page.js, src/components/recipes/CommandBuilder.jsx
**1. Restored choices never reached the address bar.** On mount, the builder restores the reader's saved hardware (global) and their per-recipe strategy, frontend, features, KV offload and node count from localStorage (`CommandBuilder.jsx`, the mount ef...
- #1258 Group the Presets tab by hardware, opening the builder's GPU (+74/-12) by @esmeetu files: CLAUDE.md, src/app/[org]/[repo]/page.js, src/components/recipes/ConfigSections.jsx
- #1257 Track command copies, preset picks and Advanced opens (+41/-14) by @esmeetu files: src/components/recipes/CommandBuilder.jsx
- how many visits end with the command copied,
- which hardware readers are on, and how many of them see tuned presets,
- whether readers pick presets, and whether they switch between them without copying,
- whether the expert rows are used at all.


## vllm-project/router (watch)


### Changes

Summary unavailable (null LLM). Source items:
- #225 [Bugfix] Authenticate HTTP worker health checks [bug, ready] (+466/-115) by @StevenWang-CY files: docs/cli_reference.md, src/backend/health.rs, src/core/worker.rs, src/kv_index/discovery.rs, src/routers/http/pd_kv_state.rs, src/routers/http/pd_router.rs, src/routers/http/router.rs
- #588 docs: refresh WeChat group QR code [ready] (+0/-0) by @david6666666 files: docs/assets/WeChat.png
- #500 feat(pd): defer Decode selection to Prefill completion in sequential P/D dispatch [enhancement, ready] (+1879/-190) by @KaisennHu files: src/metrics.rs, src/policies/cache_aware.rs, src/policies/kv_aware.rs, src/policies/mod.rs, src/routers/http/pd_router.rs, src/routers/http/pd_types.rs, src/routers/http/vllm_pd_router.rs, tests/rust/common/mock_vllm_rs.rs, tests/rust/grpc_pd_routing.rs
- #551 docs(grpc): show how to read a healthy probe [ready] (+46/-1) by @herotai214 files: docs/backend/grpc.md
- Document that a quiet worker log is normal for a `grpc://` health probe. The router calls `grpc.health.v1` Check in the background and stores the result. A Rust gRPC worker does not log that RPC.
- `curl -sS http://127.0.0.1:30000/health` reads the stored result and prints `All servers healthy` with status 200. It does not call the worker.
- `curl -sS -o /dev/null -w "%{http_code}...
- #441 [Test] Add end-to-end coverage for KV-aware routing policy [ready, CI/CD] (+1395/-8) by @KaisennHu files: pyproject.toml, tests/python/fixtures/mock_worker.py, tests/python/fixtures/router_manager.py, tests/python/integration/conftest.py, tests/python/integration/load_balancing/test_kv_aware.py
- KV cac...
- #477 [Test] add pd merge perf test case [ready, CI/CD] (+2182/-17) by @zhumingjue138 files: .buildkite/README.md, .buildkite/ci_mirror_hardwares.yml, .buildkite/test-nightly.yml, tests/python/e2e/perf/README.md, tests/python/e2e/perf/conftest.py, tests/python/e2e/perf/process.py, tests/python/e2e/perf/router_policy/README.md, tests/python/e2e/perf/router_policy/case_loader.py, tests/python/e2e/perf/router_policy/cases/cache_aware.json, tests/python/e2e/perf/router_policy/cases/kv_aware.json, tests/python/e2e/perf/router_policy/cases/kv_aware_aff.json, tests/python/e2e/perf/router_policy/conftest.py
- #537 ci: skip thin LTO in premerge release builds [ready, CI/CD] (+65/-0) by @amitcoder79 files: .buildkite/README.md, .buildkite/pipeline.yml
- #510 fix(pd): scope decode session affinity by named LoRA [bug, ready] (+422/-30) by @xuxiongchen files: src/backend/preprocess.rs, src/policies/kv_aware.rs, src/routers/http/pd_router.rs, src/routers/http/pd_types.rs, src/routers/http/vllm_pd_router.rs


