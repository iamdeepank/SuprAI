# Rust workspace

The SuprAI runtime is a Cargo workspace under `rust/`. The user-facing binary is **`suprai`**, built from the `rusty-claude-cli` crate.

## Quick commands

```bash
cd rust
cargo build --workspace
cargo build -p rusty-claude-cli --release   # optimized suprai binary
cargo test --workspace
cargo run -p rusty-claude-cli -- --help
```

Windows: `.\target\debug\suprai.exe` or `.\target\release\suprai.exe`

## Workspace layout

```text
rust/
├── Cargo.toml              # Workspace root
├── Cargo.lock
└── crates/
    ├── api/                # Provider clients + streaming
    ├── commands/           # Slash-command registry + help
    ├── compat-harness/     # Parity harness utilities
    ├── claw-analog/        # Lean agent (suprai-analog)
    ├── claw-rag-service/    # RAG HTTP service
    ├── mock-anthropic-service/
    ├── plugins/
    ├── runtime/            # Sessions, config, permissions, MCP
    ├── rusty-claude-cli/   # Main CLI → binary `suprai`
    ├── telemetry/
    └── tools/              # Built-in tool implementations
```

## Crate responsibilities

| Crate | Responsibility |
|-------|----------------|
| **api** | Provider clients, SSE streaming, auth, request preflight |
| **commands** | Slash commands, parsing, help text, JSON rendering |
| **compat-harness** | Parity comparison helpers |
| **claw-analog** | Minimal tool-agent loop for CI / NDJSON |
| **claw-rag-service** | Ingest, HTTP query API, optional web UI |
| **mock-anthropic-service** | Deterministic `/v1/messages` mock |
| **plugins** | Plugin install, hooks, bundled plugins |
| **runtime** | `ConversationRuntime`, sessions, permissions, MCP, prompts |
| **rusty-claude-cli** | REPL, CLI parsing, streaming display |
| **telemetry** | Trace events and usage payloads |
| **tools** | Bash, read/write/edit, grep, glob, web, agents, skills |

## Model aliases

| Alias | Resolves to |
|-------|-------------|
| `opus` | `claude-opus-4-7` |
| `sonnet` | `claude-sonnet-4-6` |
| `haiku` | `claude-haiku-4-5-20251213` |

## Mock parity harness

Deterministic end-to-end tests use `mock-anthropic-service` and `tests/mock_parity_harness.rs`. See [Mock parity harness](mock-parity.md).

## Related

- [Building & testing](building.md)
- [CLI usage](../guide/cli-usage.md)
