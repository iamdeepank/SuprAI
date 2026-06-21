# Run SuprAI — command from scretch








# Run Claw Code — command reference (Windows)

PowerShell commands to build and run **`claw`** from this repository. Run from the **repo root** unless noted.

Repo root example:

```text
C:\Users\WJCZN\Documents\bayer\personal\claw-code
```

---

## 1. One-time prerequisites

### Install Rust

Download and install from [https://rustup.rs/](https://rustup.rs/), then **open a new PowerShell window**.

```powershell
cargo --version
rustc --version
```

### If `link.exe not found` (no Visual Studio Build Tools)

Use the **GNU (MinGW)** toolchain instead of MSVC:

```powershell
# Install MinGW (WinLibs) via winget — one time
winget install --id BrechtSanders.WinLibs.POSIX.UCRT.LLVM -e

# Close and reopen PowerShell, then:
rustup toolchain install stable-x86_64-pc-windows-gnu
rustup default stable-x86_64-pc-windows-gnu
rustup show
```

You should see `stable-x86_64-pc-windows-gnu (active, default)`.

---

## 2. Clone and enter the project

```powershell
git clone https://github.com/ultraworkers/claw-code
cd claw-code
```

If you already have the repo, just:

```powershell
cd C:\Users\WJCZN\Documents\bayer\personal\claw-code
```

---

## 3. Configure credentials and model

### Create `.env` (API keys and base URL)

```powershell
copy .env.example .env
notepad .env
```

Example for a **custom OpenAI-compatible gateway** (e.g. corporate chat API):

```env
OPENAI_API_KEY=your-key-here
OPENAI_BASE_URL=https://your-gateway.example.com/api/v2
```

Example for **OpenAI official API**:

```env
OPENAI_API_KEY=sk-your-key-here
OPENAI_BASE_URL=https://api.openai.com/v1
```

Example for **Ollama (local, no key)**:

```env
OLLAMA_HOST=http://127.0.0.1:11434
```

`.env` is gitignored. **Run `claw` from the repo root** so `.env` is found.

### Set default model — `.claw/settings.json`

Already created in this repo; edit if needed:

```powershell
notepad .claw\settings.json
```

Example:

```json
{
  "model": "openai/gpt-5.4",
  "aliases": {
    "fast": "openai/gpt-4.1-mini",
    "smart": "openai/gpt-5.4"
  }
}
```

Use the `openai/` prefix (or `gpt-`) so routing stays on the OpenAI-compatible provider.

---

## 4. Build

From repo root:

```powershell
cd rust
cargo build -p rusty-claude-cli
```

Full workspace (all crates, slower):

```powershell
cd rust
cargo build --workspace
```

Optimized release binary:

```powershell
cd rust
cargo build -p rusty-claude-cli --release
# Binary: rust\target\release\claw.exe
```

**After changing Rust source** under `rust/crates/`, rebuild before testing:

```powershell
cd rust
cargo build -p rusty-claude-cli
```

---

## 5. Verify (no chat yet)

From **repo root** (not `rust/`):

```powershell
cd C:\Users\WJCZN\Documents\bayer\personal\claw-code

.\rust\target\debug\claw.exe --help
.\rust\target\debug\claw.exe version
.\rust\target\debug\claw.exe doctor
.\rust\target\debug\claw.exe status
.\rust\target\debug\claw.exe status --output-format json
```

---

## 6. Run prompts

### One-shot prompt

```powershell
cd C:\Users\WJCZN\Documents\bayer\personal\claw-code

.\rust\target\debug\claw.exe prompt "Say hello in one sentence"
```

Shorthand (same thing):

```powershell
.\rust\target\debug\claw.exe "Explain what this repo does in two sentences"
```

Override model for one run:

```powershell
.\rust\target\debug\claw.exe --model "openai/gpt-4.1-mini" prompt "hello"
```

JSON output (for scripts):

```powershell
.\rust\target\debug\claw.exe --output-format json prompt "hello"
```

### Interactive REPL (chat mode)

```powershell
.\rust\target\debug\claw.exe
```

Inside the REPL:

```text
/help
/doctor
/status
/exit
```

Exit with `Ctrl+C` if needed.

---

## 7. Provider-specific setup

### OpenAI-compatible gateway (custom URL + key)

`.env`:

```env
OPENAI_API_KEY=your-key
OPENAI_BASE_URL=https://your-gateway.example.com/api/v2
```

`.claw/settings.json`:

```json
{ "model": "openai/gpt-5.4" }
```

Run:

```powershell
.\rust\target\debug\claw.exe prompt "hello"
```

### Anthropic (Claude API)

PowerShell session or `.env`:

```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-your-key"
```

Model:

```powershell
.\rust\target\debug\claw.exe --model sonnet prompt "hello"
```

### Ollama (local)

Terminal 1:

```powershell
ollama pull llama3.2
ollama serve
```

Terminal 2:

```powershell
cd C:\Users\WJCZN\Documents\bayer\personal\claw-code
$env:OLLAMA_HOST = "http://127.0.0.1:11434"
.\rust\target\debug\claw.exe --model "llama3.2" prompt "hello"
```

---

## 8. Optional: install `claw` on PATH

```powershell
cd rust
cargo install --path crates/rusty-claude-cli --force
```

Then (if `~\.cargo\bin` is on PATH):

```powershell
claw --help
claw doctor
```

On Windows the binary is still `claw.exe` when using the full path.

---

## 9. Tests and formatting

```powershell
cd rust

# Run all workspace tests
cargo test --workspace

# Format check (from repo root, if scripts exist)
cd ..
.\scripts\fmt.sh --check
```

---

## 10. Debugging slow or failed prompts

Shorter HTTP timeouts:

```powershell
$env:CLAW_API_CONNECT_TIMEOUT = "15"
$env:CLAW_API_REQUEST_TIMEOUT = "60"
```

Debug logging:

```powershell
$env:RUST_LOG = "claw=debug,api=debug"
.\rust\target\debug\claw.exe prompt "hello"
```

Common checks:

| Symptom | What to check |
|---------|----------------|
| `api.openai.com` in error but you use a custom gateway | Run from repo root; ensure `OPENAI_BASE_URL` is in `.env`; rebuild after code changes |
| `link.exe not found` on build | Use GNU toolchain + WinLibs (section 1) |
| `openai_key=absent` in doctor | Key only in `.env` is OK for prompts; doctor reads shell env unless exported |
| Long “Thinking…” then failure | Wrong URL, VPN, or network; use shorter timeouts above |

---

## 11. Quick reference (copy/paste)

```powershell
# Setup (once)
cd C:\Users\WJCZN\Documents\bayer\personal\claw-code
copy .env.example .env
# edit .env and .claw\settings.json

# Build
cd rust
cargo build -p rusty-claude-cli
cd ..

# Run
.\rust\target\debug\claw.exe doctor
.\rust\target\debug\claw.exe prompt "Say hello"
.\rust\target\debug\claw.exe
```

---

## Related docs

- [USAGE.md](../USAGE.md) — full product usage
- [docs/windows-install-release.md](./windows-install-release.md) — install and release artifacts
- [docs/local-openai-compatible-providers.md](./local-openai-compatible-providers.md) — Ollama, OpenRouter, etc.
- [rust/README.md](../rust/README.md) — crate layout
