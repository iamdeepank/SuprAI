# Run SuprAI on Windows

PowerShell commands to build and run **SuprAI** (`suprai` CLI) from this repository. Run from the **repo root** unless noted.

Repo root:

```text
C:\Users\WJCZN\Documents\bayer\personal\SuprAI
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
winget install --id BrechtSanders.WinLibs.POSIX.UCRT.LLVM -e
rustup toolchain install stable-x86_64-pc-windows-gnu
rustup default stable-x86_64-pc-windows-gnu
rustup show
```

---

## 2. Clone and enter the project

```powershell
git clone https://github.com/iamdeepank/SuprAI.git
cd SuprAI
```

---

## 3. Configure credentials and model

### Create `.env` (API keys and base URL)

```powershell
copy .env.example .env
notepad .env
```

Example for **OpenAI official API**:

```env
OPENAI_API_KEY=sk-your-key-here
OPENAI_BASE_URL=https://api.openai.com/v1
```

Example for a **custom OpenAI-compatible gateway**:

```env
OPENAI_API_KEY=your-key-here
OPENAI_BASE_URL=https://your-gateway.example.com/api/v2
```

Example for **Ollama (local, no key)**:

```env
OLLAMA_HOST=http://127.0.0.1:11434
```

`.env` is gitignored. **Run `suprai` from the repo root** so `.env` is found.

### Set default model — `.suprai/settings.json`

```powershell
notepad .suprai\settings.json
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

Use the `openai/` prefix so routing stays on the OpenAI-compatible provider.

---

## 4. Build

```powershell
cd rust
cargo build -p rusty-claude-cli
```

Release binary:

```powershell
cargo build -p rusty-claude-cli --release
# Binary: rust\target\release\suprai.exe
```

---

## 5. Verify (no chat yet)

From **repo root**:

```powershell
.\rust\target\debug\suprai.exe --help
.\rust\target\debug\suprai.exe version
.\rust\target\debug\suprai.exe doctor
.\rust\target\debug\suprai.exe status
```

---

## 6. Run prompts

### One-shot prompt

```powershell
.\rust\target\debug\suprai.exe prompt "Say hello in one sentence"
```

Shorthand:

```powershell
.\rust\target\debug\suprai.exe "Explain what this repo does in two sentences"
```

### Interactive REPL (chat mode)

```powershell
.\rust\target\debug\suprai.exe
```

Inside the REPL:

```text
/help
/doctor
/status
/exit
```

---

## 7. Optional: install `suprai` on PATH

```powershell
cd rust
cargo install --path crates/rusty-claude-cli --force
suprai --help
```

---

## 8. Debugging

```powershell
$env:SUPRAI_API_CONNECT_TIMEOUT = "15"
$env:SUPRAI_API_REQUEST_TIMEOUT = "60"
$env:RUST_LOG = "suprai=debug,api=debug"
.\rust\target\debug\suprai.exe prompt "hello"
```

---

## Quick reference

```powershell
cd C:\Users\WJCZN\Documents\bayer\personal\SuprAI
copy .env.example .env
# edit .env and .suprai\settings.json

cd rust
cargo build -p rusty-claude-cli
cd ..

.\rust\target\debug\suprai.exe doctor
.\rust\target\debug\suprai.exe prompt "Say hello"
.\rust\target\debug\suprai.exe
```

---

## Related docs

- [CLI usage](../guide/cli-usage.md) — full CLI reference
- [Rust workspace](../developer/rust-workspace.md) — crate layout
