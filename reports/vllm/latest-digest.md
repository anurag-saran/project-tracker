# vllm digest — 2026-11-18

_Since 7d · generated 2026-11-18T17:44:50Z_

## TL;DR for this month

- Release vllm-project/vllm@v0.34.0
- vllm-project/semantic-router/bench: 2 PRs merged
- vllm-project/semantic-router/config: 40 PRs merged
- vllm-project/semantic-router/dashboard: 62 PRs merged
- vllm-project/semantic-router/e2e: 36 PRs merged

## vllm-project/vllm (core)

### Releases
- [v0.34.0](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) — 2026-11-16: v0.34.0

### Highlights
- New release **v0.34.0** — v0.34.0

## vllm-project/semantic-router (core)


### bench

### Features
- Enabled binding of listener rules to vSR agent plugins for configuration-driven guarding/redacting (#6507). Allows recipes to define keyword-based access controls and data masking policies in YAML, improving configuration flexibility.

### Fixes
- Resolved DeepSeek API compatibility issue by accepting non-canonical `prompt_cache_hit_tokens`/`prompt_cache_miss_tokens` fields in usage reports (#5265). Prevents JSON decoding errors from upstream responses while maintaining schema validation for other fields.

**First-time contributors:** ZireaelK
### config

# vllm-project/semantic-router Module: config PR Summary

## Features
- Added agent-based routing and subagent role classification to enforce model selection per session (#6751).
- Enabled pricing of model switches using cache receipts for cost optimization (#6743).
- Introduced default session and agent identity headers for OpenCode and Codex compatibility (#6681).
- Implemented budget enforcement per run and user window with idle timeout support (#6745).
- Redesigned the Dashboard UI with a task-first layout and design system (#6867).

## Performance
- Bounded Router Replay prompt size to 64 KiB by default and limited tool trace storage (#6452, #6457).
- Optimized long input scanning in guard rules to fit signal deadlines with adaptive window sizing (#6363).
- Configurable standalone gateway drain timeout and h2c support for graceful shutdown (#6456).

## Fixes
- Resolved signed thinking block routing failures in Anthropic Messages requests (#6948).
- Fixed jailbreak rules to properly handle tool results without input.tool_results (#6908).
- Prevented developer messages from being dropped when models lack the developer role (#6859).
- Corrected pricing logic for models with zero or missing currency definitions (#6721).
- Ensured applied and Kubernetes keys are excluded from saved configs (#6709).

## Breaking or deprecations
- Default routing records now persist across Router restarts via file-based replay store (#6705).
- `cache_economics_config` now uses session/agent-based pricing instead of global defaults (#6743).

## Infra
- Split MoM V1 conformance tests into 8 parallel jobs to reduce CI runtime (#6440).
- Added support for Vela 3.1 pico packages in model runtime (#6840).
- Improved CI/CD pipeline for model runtime package validation (#6840).

### dashboard

# vllm-project/semantic-router Dashboard PR Summary

## Features
- Redesigned Dashboard UI with a design system and task-first pages (#6867)  
- Enabled identifying DeepSeek Harness requests in agent signals and Router Replay (#6836)  
- Added support for Vela 3.1 pico packages in model runtime (#6840)  
- Implemented agent-based routing and blocking for Claude Code and Codex (#6751)  
- Enhanced Insights with agent-specific run trees in Replay and traces (#6747)  
- Introduced per-run and user-window spend budget enforcement (#6745)  
- Enabled pricing decisions based on cache receipts for model switches (#6743)  
- Added Codex memory routing through gateway to chosen models (#6641)  
- Improved Codex insights with turn-specific model tracking (#6635)  
- Added support for Codex approval reviews in Insights (#6634)  
- Enabled masking placeholders across requests and restarts (#6632)  

## Performance
- Optimized Insights queries with bounded, cancellable scans for large histories (#6792)  

## Fixes
- Fixed ConfigMap reading for Router config in Kubernetes (#6959)  
- Sanitized error messages in MCP panel for clearer failure reasons (#6834)  
- Prevented exposing internal

**First-time contributors:** Ti-Avanti, ZireaelK
### e2e

# vllm-project/semantic-router e2e Module PR Summary

## Features
- **Route requests by agent role and request class** (#6751): Enables fine-grained control over model selection and protection for subagents, ensuring alignment between subagent decisions and model protections.
- **Preserve Vela 3.1-fast yes/no semantics** (#6391): Maintains legacy question-answer behavior while supporting new router options and isolation.
- **Relay encrypted reasoning back to providers** (#6592): Prevents data loss in Codex sessions by retaining encrypted reasoning details in responses.
- **Serve listener rules to vSR agent plugins** (#6507): Allows plugins to enforce rules for guarding and redacting content based on listener configurations.

## Performance
- **Remove redundant port-forward wait in E2E tests** (#6602): Reduces test execution time and uncovers hidden race conditions.
- **Adjust CPU requests for E2E profiles** (#6419): Ensures tests run efficiently on GitHub runners without unnecessary resource contention.
- **Parallelize Router and Envoy Gateway installation** (#6377): Speeds up E2E setup by installing components concurrently.

## Fixes
- **Fix first-run setup test flakiness** (#6863): Ensures tests wait for the server to be ready, preventing false failures.
- **Handle Claude Code cache compaction correctly** (#6851): Avoids errors when dispatching cache control directives to Chat Completions backends.
- **Bound h2c Upgrade body reads before gateway processing** (#6611): Prevents oversized payloads from bypassing gateway limits.
- **Preserve generated images in stored responses** (#6608): Ensures image data is retained for history replay and continuation.

## Breaking or deprecations
- **Change Router Replay's default prompt capture mode** (#6449): Shifts from implicit to explicit configuration for privacy-aware

### src

# vllm-project/semantic-router - src Module PR Summary

## Features

- Price login and keyed models from the catalog, including Anthropic and OpenAI models, with list prices sourced from official pricing pages (#6678).
- Serve the Vela 3.1 pico packages in the model runtime, including updated documentation and test cases (#6840).
- Show each agent run as one tree in Replay, traces, and Insights, with agent metadata captured from request headers (#6747).

## Performance

- Answer Insights from one bounded, cancellable scan per filter, improving performance and usability of large history (#6792).
- Keep applied, Kubernetes, and gateway keys out of saved configs, reducing configuration bloat and improving security (#6709).

## Fixes

- Refuse prompts that exceed the context window on the Router's own count and provide a fallback response (#6348).
- Pass a streamed tool call cut by the output limit to the client, ensuring compatibility with backend stream limits (#5972).
- Fix handling of long inputs in the guard by reading every part of the input and reporting when it fails (#6346).

## Breaking or deprecations

- Connect Claude Code and Codex CLI to the gateway with `vllm-sr connect`, introducing new CLI commands and configuration options (#6123).
- Enforce spend budgets per run and per user window, introducing new configuration parameters for cost control (#6745).

## Infra

- Add a locked uv environment for the multimodal small embedding trainer, ensuring consistent and reproducible environments (#5267).
- Add a VS Code extension that serves the gateway's models, enabling VS Code chat to use the gateway (#6644).

**First-time contributors:** ErikJiang, PyExtreme, ZireaelK, glitch-ux, qati, yaojiejia
### tools

# vllm-project/semantic-router - tools Module PR Summary

## Features
- Added model pricing information for Anthropic and OpenAI models in the catalog, sourced from official pricing pages (#6678).
- Introduced support for serving Vela 3.1 pico packages in the model runtime, enhancing inference capabilities (#6840).
- Implemented tracking of which models served each turn in Codex, improving visibility into model usage (#6635).

## Performance
- Made the standalone gateway's drain configurable and enabled draining of h2c requests, improving graceful shutdown behavior (#6456).

## Fixes
- Prevented applied, Kubernetes, and gateway keys from being saved in configurations, ensuring secure key management (#6709).
- Fixed handling of tool calls cut by output limits, ensuring clients receive partial results with appropriate finish reasons (#6313).
- Corrected handling of encrypted reasoning to ensure it is relayed back to the provider (#6592).

## Breaking or deprecations
- No breaking changes or deprecations reported in the provided PRs.

## Infra
- Added a VS Code extension to serve the gateway's models, enhancing developer experience (#6644).
- Improved CI diagnostics for PR Gate suite and rollup mismatches, ensuring accurate status reporting (#6497).

**First-time contributors:** ZireaelK
### website

# Features

- Added pricing for Anthropic and OpenAI models from the catalog, sourced from official pricing pages (#6678).
- Introduced support for Vela 3.1 pico packages in the model runtime, including documentation and testing (#6840).
- Enabled Replay, traces, and Insights to display each agent run as a tree, using headers from the harness (#6747).

# Performance

- Improved handling of long input processing in the guard by reading every part and indicating when it fails to read (#6346).
- Optimized Insights performance by scanning only a bounded, cancellable subset of the history per filter, improving responsiveness (#6792).

# Fixes

- Fixed a bug where the Router refused prompts that fit within a model's context window, adding fallback handling (#6348).
- Resolved an issue where the Router returned an invalid stream tool argument when output limits cut a tool call mid-stream (#5972).
- Ensured that encrypted reasoning from Responses is relayed back to the provider, preserving data integrity (#6592).

# Breaking or deprecations

- Updated training projects to use Python 3.11 and pinned a patched `filelock` version to address security advisories (#6336).

# Infra

- Added a VS Code extension to serve the gateway's models, enabling chat model selection and streaming replies (#6644).
- Implemented end-to-end harness checking in `vllm-sr connect`, providing setup status visibility (#6637).



