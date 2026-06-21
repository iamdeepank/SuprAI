# Releasing SuprAI

This project uses [Semantic Versioning](https://semver.org/). The canonical version lives in:

- `VERSION` (release marker)
- `rust/Cargo.toml` workspace `version = "..."` (crate versions)

Keep these aligned when cutting a release.

## Prerequisites

- Clean `main` branch (or your release branch merged to `main`)
- [GitHub Pages](https://github.com/iamdeepank/SuprAI/settings/pages) source set to **GitHub Actions**
- Release workflow enabled (`.github/workflows/release.yml`)

## Cut release v0.1.0 (initial public version)

```bash
# 1. Verify locally
cd rust
cargo build -p rusty-claude-cli --release
cargo test -p rusty-claude-cli --test cli_flags_and_config_defaults
cd ..
pip install -r requirements-docs.txt
mkdocs build --strict

# 2. Update CHANGELOG.md and VERSION if needed, commit to main

# 3. Tag and push
git tag -a v0.1.0 -m "SuprAI v0.1.0 — initial public release"
git push origin main
git push origin v0.1.0
```

GitHub Actions will:

1. **Documentation** — build and deploy MkDocs to GitHub Pages (on push to `main`)
2. **Release** — on tag `v*`, build Linux/macOS/Windows binaries and attach them to a GitHub Release

## Release artifacts

| Asset | Platform |
|-------|----------|
| `suprai-linux-x64` | Linux x86_64 |
| `suprai-macos-x64` | macOS Intel |
| `suprai-macos-arm64` | macOS Apple Silicon |
| `suprai-windows-x64.exe` | Windows x64 |

Each asset includes a `.sha256` checksum file.

## After release

- Verify **Actions** → **Release** job succeeded
- Verify **Settings → Pages** shows the docs URL: `https://iamdeepank.github.io/SuprAI/`
- Update release notes on GitHub if needed

## Docs-only deploy

Docs deploy automatically on every push to `main` via `.github/workflows/docs.yml`.

## Version bump checklist

1. Update `VERSION`
2. Update `version` in `rust/Cargo.toml` (`[workspace.package]`)
3. Add section to `CHANGELOG.md`
4. Tag `vX.Y.Z` and push
