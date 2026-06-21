# Architecture & concept

SuprAI is a public Rust implementation of a CLI agent **`suprai`** and companion tools. The canonical runtime lives in the [`rust/`](https://github.com/iamdeepank/SuprAI/tree/main/rust) workspace.

A separate product line — from CLI to personal assistant (channels, memory, proactivity) — is outlined in [Personal assistant roadmap](../personal-assistant-roadmap.md).

## Product components

1. **Main CLI `suprai`** (`rusty-claude-cli`) — full REPL, OAuth, bash, MCP, plugins, streaming; providers Anthropic, OpenAI-compatible, xAI.
2. **`suprai-analog`** (`claw-analog` crate) — lean tool loop on the same `api` layer: filesystem tools, explicit permissions, NDJSON for CI and external agents.
3. **`claw-rag-service`** — separate process: repo indexing (chunks + embeddings in SQLite), HTTP search API, minimal web UI for index inspection.

Goal: a **safe**, **auditable**, **reproducible** way to run LLMs over code and docs, from minimal harness to full `suprai`.

## Audience & scenarios

| Segment | Use case |
|---------|----------|
| Developer | Daily work via full `suprai` REPL, tools, sessions |
| Automation author | One-shot prompts, `--output-format json`, agents without bash |
| Audit / compliance | `suprai-analog` read-only + audit presets |
| Parity / porting | Mock harness vs reference behavior ([Parity](../developer/parity.md)) |
| RAG over monorepo | `ingest` + `serve`; agent uses `retrieve_context` when `RAG_BASE_URL` is set |

## Logical architecture

```text
                    ┌─────────────────────────────────────┐
                    │  Providers (Anthropic / OpenAI / …) │
                    └─────────────────┬───────────────────┘
                                      │
       ┌──────────────────────────────┼──────────────────────────────┐
       │                              │                              │
       ▼                              ▼                              ▼
┌──────────────┐              ┌──────────────┐              ┌──────────────────┐
│ rusty-       │              │ claw-analog  │              │ claw-rag-service │
│ claude-cli   │              │ (lean loop)  │              │ HTTP + SQLite    │
│ (`suprai`)   │              │              │              │ ingest / query   │
└──────┬───────┘              └──────┬───────┘              └────────┬─────────┘
       │                              │                               │
       │          crates/api          │         retrieve_context      │
       │    runtime, tools, …         │         (POST /v1/query)      │
       └──────────────┬───────────────┴───────────────────────────────┘
                      │
                      ▼
               Filesystem / workspace (-w)
```

Heavy indexing stays in **RAG service**; agents call retrieval over HTTP so vector stores and embedding secrets can change independently.

## Design principles

1. **Security by default** — path canonicalization, `..` rejection, `PermissionMode` aligned with full CLI; dangerous modes blocked in non-interactive use without explicit flags.
2. **Explicit limits** — read sizes, turn counts, glob/grep caps, RAG timeouts.
3. **Agent observability** — NDJSON with `schema` / `format_version`, structured `tool_result`.
4. **Modularity** — shared `api` crate; analog does not embed RAG keys, only HTTP client.
5. **Parity & tests** — mock Anthropic service, harness scenarios, CI for critical crates.
6. **Docs beside code** — this site, `USAGE`, container and RAG guides.

## Workspace crates (summary)

| Crate | Role |
|-------|------|
| `rusty-claude-cli` | Binary `suprai` |
| `api` | Provider clients, streaming |
| `runtime` | Sessions, config, permissions, MCP, prompts |
| `tools` | Built-in CLI tools |
| `commands` | Slash command registry |
| `plugins` | Plugin and hook runtime |
| `claw-analog` | Lean agent binary |
| `claw-rag-service` | RAG HTTP service |
| `mock-anthropic-service` | Deterministic test double |
| `compat-harness` | Parity utilities |

Details: [Rust workspace](../developer/rust-workspace.md).

## suprai-analog boundaries

Filesystem tools (`read_file`, `list_dir`, `glob_workspace`, `grep_workspace`, optional `write_file`, optional `retrieve_context`). **No** MCP, plugins, or bash in the minimal design — those belong to full `suprai`.

## RAG service evolution

**Today:** full reindex on `ingest`, vectors in SQLite, linear cosine search — fine for moderate codebases.

**Future:** incremental indexing, ANN (Qdrant in `docker-compose.yml`), embedding rate limits. See [RAG service & web UI](../rag-web-ui.md).

## Repository outside the Rust runtime

`src/` and `tests/` at repo root are auxiliary Python helpers. **Canonical runtime is `rust/`.**

Community docs (`PHILOSOPHY.md`, `ROADMAP.md`, `PARITY.md`) complement this architecture with process and backlog context.
