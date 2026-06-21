# Installation

SuprAI ships as a **local CLI binary** named `suprai`. There is no `npm` or `pip` package today — you build from source or download a release artifact.

## Prerequisites

- **Rust** toolchain (`cargo`, `rustc`) via [rustup.rs](https://rustup.rs/) — for building from source
- **API credentials** for at least one provider (Anthropic, OpenAI-compatible, xAI, or local Ollama)
- **Git** — to clone the repository

## Windows

### Option A: Build from source (PowerShell)

```powershell
git clone https://github.com/iamdeepank/SuprAI.git
cd SuprAI
cd rust
cargo build -p rusty-claude-cli --release
```

Binary: `rust\target\release\suprai.exe`

Add to PATH (one time, adjust path if needed):

```powershell
$bin = "C:\path\to\SuprAI\rust\target\release"
[Environment]::SetEnvironmentVariable(
  "Path", "$bin;" + [Environment]::GetEnvironmentVariable("Path", "User"), "User"
)
```

Open a **new** terminal → `suprai --version`

### Option B: Release binary

Download `suprai-windows-x64.exe` from GitHub Releases. See [Windows release binaries](../windows-install-release.md).

### Option C: GNU toolchain (no Visual Studio)

If `link.exe not found`:

```powershell
winget install --id BrechtSanders.WinLibs.POSIX.UCRT.LLVM -e
rustup toolchain install stable-x86_64-pc-windows-gnu
rustup default stable-x86_64-pc-windows-gnu
```

Full walkthrough: [Windows guide](windows.md).

## macOS

```bash
git clone https://github.com/iamdeepank/SuprAI.git
cd SuprAI
./install.sh --release
```

Binary: `rust/target/release/suprai`

Optional PATH symlink:

```bash
ln -sf "$(pwd)/rust/target/release/suprai" ~/.local/bin/suprai
```

## Linux

Same as macOS:

```bash
git clone https://github.com/iamdeepank/SuprAI.git
cd SuprAI
./install.sh --release
```

Requires: `git`, `pkg-config`, OpenSSL headers (`libssl-dev` on Debian/Ubuntu).

## WSL on Windows

Use the Linux instructions inside your WSL distro. The root `install.sh` script is the supported path (native PowerShell without WSL uses the Windows build flow above).

## Install from repo path (all platforms)

After cloning, you can install the binary into your user cargo bin directory:

```bash
cd SuprAI/rust
cargo install --path crates/rusty-claude-cli --force
suprai --version
```

On Windows, the executable is `suprai.exe` in `%USERPROFILE%\.cargo\bin\`.

## Verify installation

From the **repository root** (so `.env` is discovered):

```bash
suprai doctor
suprai --help
suprai prompt "Say hello in one sentence"
```

## What does *not* work

| Command | Why |
|---------|-----|
| `cargo install SuprAI` | Wrong / deprecated crate name on crates.io |
| `cargo build` from repo root | Workspace lives in `rust/` — use `cd rust` or `--manifest-path rust/Cargo.toml` |

## Next steps

- [Configuration](configuration.md) — API keys, models, `.suprai/settings.json`
- [CLI usage](../guide/cli-usage.md) — REPL, slash commands, JSON automation
