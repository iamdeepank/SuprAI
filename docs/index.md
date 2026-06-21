# SuprAI

**Version 0.1.0** — Rust CLI agent harness — interactive coding assistant with tools, sessions, permissions, MCP, plugins, and skills.

The primary binary is **`suprai`**. It targets developers who want a local, auditable agent over their codebase with optional automation via JSON output.

Start here: [Quick start](getting-started/quick-start.md)

## What you get

| Capability | Description |
|------------|-------------|
| **Interactive REPL** | Chat-style shell with slash commands, tab completion, and session resume |
| **Tools** | Read, write, edit, grep, glob, bash, web search, sub-agents, todos |
| **Providers** | Anthropic, OpenAI-compatible APIs, xAI, local Ollama / llama.cpp / vLLM |
| **Sessions** | Persisted conversation history under `.suprai/sessions/` |
| **MCP & plugins** | Extend tools and hooks without forking the CLI |
| **JSON mode** | `--output-format json` for CI and automation |

## Quick start

=== "Windows (PowerShell)"

    ```powershell
    git clone https://github.com/iamdeepank/SuprAI.git
    cd SuprAI
    copy .env.example .env
    # Edit .env with your API key

    cd rust
    cargo build -p rusty-claude-cli --release
    cd ..

    .\rust\target\release\suprai.exe doctor
    .\rust\target\release\suprai.exe prompt "say hello"
  ```

=== "macOS / Linux"

    ```bash
    git clone https://github.com/iamdeepank/SuprAI.git
    cd SuprAI
    cp .env.example .env
    # Edit .env with your API key

    ./install.sh --release
    rust/target/release/suprai doctor
    rust/target/release/suprai prompt "say hello"
    ```

See [Installation](getting-started/installation.md) for all platforms and [Configuration](getting-started/configuration.md) for API keys and models.

## Repository layout

| Path | Role |
|------|------|
| `rust/` | Rust workspace — builds the `suprai` CLI |
| `.suprai/` | Project config (model, sessions, plugins) |
| `.suprai.json` | Project-level config overrides |
| `src/` + `tests/` | Python reference helpers (not the runtime) |

## Ecosystem components

Beyond the main CLI, the workspace includes:

- **`suprai-analog`** (`claw-analog` crate) — lean tool loop for CI and scripting (NDJSON)
- **`claw-rag-service`** — HTTP RAG ingest/query + optional web UI ([RAG docs](rag-web-ui.md))
- **`docker-compose.yml`** — Qdrant + RAG service for local semantic search stacks

Read [Architecture & concept](guide/architecture.md) for the full picture.

## Documentation map

- **New users** → [Installation](getting-started/installation.md) → [CLI usage](guide/cli-usage.md)
- **Local models** → [OpenAI-compatible providers](local-openai-compatible-providers.md)
- **Contributors** → [Building & testing](developer/building.md) → [Contributing](developer/contributing.md)

## License

MIT — see the [LICENSE](https://github.com/iamdeepank/SuprAI/blob/main/LICENSE) file in the repository.
