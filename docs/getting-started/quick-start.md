# Quick start

Get from zero to a working `suprai` prompt in a few minutes.

## 1. Install

=== "Windows"

    ```powershell
    git clone https://github.com/iamdeepank/SuprAI.git
    cd SuprAI
  ```

    Download a release binary from [GitHub Releases](https://github.com/iamdeepank/SuprAI/releases) **or** build:

    ```powershell
    cd rust
    cargo build -p rusty-claude-cli --release
    ```

=== "macOS / Linux"

    ```bash
    git clone https://github.com/iamdeepank/SuprAI.git
    cd SuprAI
    ./install.sh --release
    ```

See [Installation](installation.md) for PATH setup and all platforms.

## 2. Configure

```bash
cp .env.example .env
# Edit .env — set OPENAI_API_KEY + OPENAI_BASE_URL, or OLLAMA_HOST for local models
```

Optional model defaults in `.suprai/settings.json`:

```json
{
  "model": "openai/gpt-4.1-mini"
}
```

Details: [Configuration](configuration.md).

## 3. Verify

From the **repo root** (where `.env` lives):

```bash
suprai doctor
suprai prompt "Say hello in one sentence"
```

## 4. Interactive mode

```bash
suprai
```

Inside the REPL:

```text
/help
/doctor
/status
```

## Next steps

- [CLI usage](../guide/cli-usage.md) — full command reference
- [Local models](../local-openai-compatible-providers.md) — Ollama, llama.cpp, vLLM
- [Documentation home](../index.md)
