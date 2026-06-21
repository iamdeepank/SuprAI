# SuprAI

SuprAI is a Rust CLI agent harness — an interactive coding assistant with tools, sessions, permissions, MCP, plugins, and skills.

**Version:** 0.1.0 · **Binary:** `suprai` · **Docs:** [iamdeepank.github.io/SuprAI](https://iamdeepank.github.io/SuprAI/)

## Install

| Platform | Command |
|----------|---------|
| **Windows** | [Release `.exe`](https://github.com/iamdeepank/SuprAI/releases) or `cd rust && cargo build -p rusty-claude-cli --release` |
| **macOS / Linux** | `./install.sh --release` after clone |
| **All platforms** | See [Installation](https://iamdeepank.github.io/SuprAI/getting-started/installation/) |

```powershell
git clone https://github.com/iamdeepank/SuprAI.git
cd SuprAI
copy .env.example .env
# edit .env with your API key

cd rust
cargo build -p rusty-claude-cli --release
cd ..
.\rust\target\release\suprai.exe doctor
.\rust\target\release\suprai.exe prompt "say hello"
```

Unix: use `rust/target/release/suprai` instead of `suprai.exe`.

Full guides: [Quick start](https://iamdeepank.github.io/SuprAI/getting-started/quick-start/) · [Windows](https://iamdeepank.github.io/SuprAI/getting-started/windows/) · [Run_SuprAI_on_local.md](./Run_SuprAI_on_local.md)

## Features

- Interactive REPL with slash commands and session resume
- Tools: read, write, edit, grep, glob, bash, web search, sub-agents, skills
- Providers: Anthropic, OpenAI-compatible, xAI, local Ollama
- MCP servers and plugin hooks
- `--output-format json` for automation and CI

## Repository layout

| Path | Role |
|------|------|
| **`rust/`** | Rust workspace — builds the `suprai` CLI |
| **`.suprai/`** | Project config (model, sessions, plugins) |
| **`.suprai.json`** | Project-level config overrides |
| **`docs/`** | MkDocs documentation site source |
| **`src/` + `tests/`** | Python reference helpers (not the runtime) |

## Configuration

- **`.env`** — `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `OLLAMA_HOST`, or Anthropic vars
- **`.suprai/settings.json`** — default model and aliases
- **`SUPRAI_CONFIG_HOME`** — user config directory (default: `~/.suprai`)

## Build and test

```bash
cd rust
cargo build --workspace
cargo test --workspace
cargo clippy --workspace --all-targets -- -D warnings
```

## Documentation

- **Website:** `pip install -r requirements-docs.txt && mkdocs serve` → http://127.0.0.1:8000
- **CLI reference:** [USAGE.md](./USAGE.md) or [online CLI guide](https://iamdeepank.github.io/SuprAI/guide/cli-usage/)
- **Releases:** [CHANGELOG.md](./CHANGELOG.md) · [RELEASE.md](./RELEASE.md)

## License

MIT — see [LICENSE](./LICENSE).
