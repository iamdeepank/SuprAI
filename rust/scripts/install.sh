#!/bin/bash
set -e

# Build the release binary
cargo build --release

# Link to ~/.local/bin
mkdir -p "$HOME/.local/bin"
ln -sf "$(pwd)/target/release/suprai" "$HOME/.local/bin/suprai"

echo "✓ SuprAI installed to ~/.local/bin/suprai"
