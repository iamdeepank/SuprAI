# SuprAI

SuprAI is a Rust CLI agent harness — an interactive coding assistant with tools, sessions, permissions, MCP, plugins, and skills.


## Quick start (Windows)

```powershell
git clone https://github.com/iamdeepank/SuprAI.git
cd SuprAI
copy .env.example .env
# Edit .env with your API key and base URL

cd rust
cargo build -p rusty-claude-cli
cd ..

.\rust\target\debug\suprai.exe doctor
.\rust\target\debug\suprai.exe prompt "say hello"
.\rust\target\debug\suprai.exe
```

See [Run_SuprAI_on_local.md](./Run_SuprAI_on_local.md) for the full Windows setup guide.

## Repository layout

| Path | Role |
|------|------|
| **`rust/`** | Rust workspace — builds the `suprai` CLI |
| **`.suprai/`** | Project config (model, sessions, plugins) |
| **`.suprai.json`** | Project-level config overrides |
| **`USAGE.md`** | CLI usage reference |
| **`src/` + `tests/`** | Python reference/audit helpers (not the runtime) |

## Configuration

- **`.env`** — `OPENAI_API_KEY`, `OPENAI_BASE_URL` (or Anthropic/Ollama vars)
- **`.suprai/settings.json`** — default model and aliases
- **`SUPRAI_CONFIG_HOME`** — override user config directory (default: `~/.suprai`)

## Build and test

```powershell
cd rust
cargo build --workspace
cargo test --workspace
cargo clippy --workspace --all-targets -- -D warnings
```

## License

MIT — see [LICENSE](./LICENSE).
