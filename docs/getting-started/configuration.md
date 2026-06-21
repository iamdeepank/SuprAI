# Configuration

SuprAI reads configuration from environment variables, a project `.env` file, `.suprai/settings.json`, and optional `.suprai.json` at the repo root.

## API credentials

Copy the example env file at the **repository root**:

```bash
cp .env.example .env
```

### OpenAI-compatible (OpenAI, gateways, many local servers)

```env
OPENAI_API_KEY=sk-your-key-here
OPENAI_BASE_URL=https://api.openai.com/v1
```

### Anthropic

```env
ANTHROPIC_API_KEY=sk-ant-...
# or bearer token:
# ANTHROPIC_AUTH_TOKEN=...
# optional proxy:
# ANTHROPIC_BASE_URL=https://your-proxy.example/v1
```

### Ollama (local, often no key)

```env
OLLAMA_HOST=http://127.0.0.1:11434
```

Run `suprai` from the directory that contains `.env` (typically the repo root).

!!! warning "Secrets"
    Never commit `.env`. Use placeholders in docs and issues (`sk-ant-...`, `local-dev-token`).

## Default model

Edit `.suprai/settings.json` in your project:

```json
{
  "model": "openai/gpt-4.1-mini",
  "aliases": {
    "fast": "openai/gpt-4.1-mini",
    "smart": "openai/gpt-5.4"
  }
}
```

Use provider prefixes (`openai/`, `anthropic/`, `local/`) so routing picks the correct backend. See [Model compatibility](../MODEL_COMPATIBILITY.md).

## User-level config directory

| Variable | Default | Purpose |
|----------|---------|---------|
| `SUPRAI_CONFIG_HOME` | `~/.suprai` | User plugins, agents, skills, OAuth state |
| `SUPRAI_OUTPUT_FORMAT` | `text` | Default `text` or `json` for CLI output |
| `SUPRAI_LOG` | unset | Log level for SuprAI crates |
| `RUST_LOG` | unset | Standard Rust logging |

## Project artifacts

| Path | Purpose |
|------|---------|
| `.suprai/settings.json` | Project model defaults and merged settings |
| `.suprai/settings.local.json` | Machine-local overrides (gitignored) |
| `.suprai/sessions/` | Session JSONL files (partitioned by workspace fingerprint) |
| `.suprai.json` | Project-level JSON overrides |
| `CLAUDE.md`, `SUPRAI.md`, `AGENTS.md` | Project memory / instructions |

Initialize a new repo:

```bash
suprai init
```

## Permission modes

Set via CLI flag or config:

| Mode | Behavior |
|------|----------|
| `read-only` | No writes without approval |
| `workspace-write` | Writes inside workspace with policy |
| `danger-full-access` | Elevated — use only in trusted environments |

```bash
suprai --permission-mode workspace-write
```

## Preflight check

```bash
suprai doctor
suprai doctor --output-format json
```

Doctor reports auth, config parse health, sandbox posture, MCP validation, and memory file discovery.

## Related

- [Local OpenAI-compatible providers](../local-openai-compatible-providers.md)
- [Windows guide](windows.md)
