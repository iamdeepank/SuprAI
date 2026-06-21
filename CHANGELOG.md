# Changelog

All notable changes to SuprAI are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-06-21

### Added

- **`suprai` CLI** — interactive REPL, one-shot prompts, sessions, permissions, MCP, plugins, and skills.
- **Provider routing** — Anthropic, OpenAI-compatible APIs, xAI, and local Ollama via env configuration.
- **Project bootstrap** — `suprai init`, `.suprai/` config, `SUPRAI.md` / memory file discovery.
- **JSON automation** — `--output-format json` across core CLI surfaces for CI and scripting.
- **Companion crates** — `claw-analog` (lean agent loop), `claw-rag-service` (HTTP RAG), mock parity harness.
- **Documentation site** — MkDocs Material site under `docs/` with GitHub Pages deployment.
- **Install paths** — `install.sh` (Linux/macOS/WSL), Windows guide, release binary workflow.

### Changed

- Rebranded user-facing surfaces from legacy CLAW naming to **SuprAI** / `suprai`.
- JSON provenance IDs use `project_suprai`, `user_suprai`, and `suprai_output_format`.

### Documentation

- [Documentation site](https://iamdeepank.github.io/SuprAI/)
- [Installation guide](docs/getting-started/installation.md)
- [CLI usage](docs/guide/cli-usage.md)

[0.1.0]: https://github.com/iamdeepank/SuprAI/releases/tag/v0.1.0
