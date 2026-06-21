#!/usr/bin/env bash
# Build or serve the MkDocs documentation site.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v mkdocs >/dev/null 2>&1; then
  echo "mkdocs not found. Install with: pip install -r requirements-docs.txt" >&2
  exit 1
fi

case "${1:-serve}" in
  serve)
    mkdocs serve -a 127.0.0.1:8000
    ;;
  build)
    mkdocs build --strict
    echo "Site written to ${ROOT}/site/"
    ;;
  *)
    echo "Usage: $0 [serve|build]" >&2
    exit 2
    ;;
esac
