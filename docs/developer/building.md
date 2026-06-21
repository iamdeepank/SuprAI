# Building & testing

## Formatting

From repository root (preferred):

```bash
scripts/fmt.sh
scripts/fmt.sh --check   # CI style
```

From `rust/`:

```bash
../scripts/fmt.sh
```

## Build

```bash
cd rust
cargo build --workspace
cargo build -p rusty-claude-cli --release
```

From repo root:

```bash
cargo build --manifest-path rust/Cargo.toml --workspace
```

## Test

```bash
cd rust
cargo test --workspace
cargo test -p rusty-claude-cli
```

## Clippy

```bash
cd rust
cargo clippy --workspace --all-targets -- -D warnings
```

## Documentation site

Build the MkDocs site locally:

```bash
pip install -r requirements-docs.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build          # output in site/
```

Or use the helper script:

```bash
./scripts/build-docs.sh serve
```

## Release binary

```bash
cd rust
cargo build -p rusty-claude-cli --release
# rust/target/release/suprai (or suprai.exe on Windows)
```

## Install script (Unix)

```bash
./install.sh --release
```

## Pre-push hook

```bash
git config core.hooksPath .github/hooks
```

Docs-only bypass: `SKIP_SUPRAI_PRE_PUSH_BUILD=1`

## Doc source-of-truth checks (maintainers)

```bash
python .github/scripts/check_doc_source_of_truth.py
python .github/scripts/check_release_readiness.py
```
