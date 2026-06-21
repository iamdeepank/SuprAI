# Mock parity harness

The workspace includes a **deterministic Anthropic-compatible mock** and a **clean-environment CLI harness** for end-to-end parity checks without live API keys.

## Components

| Artifact | Path |
|----------|------|
| Mock service | `rust/crates/mock-anthropic-service/` |
| CLI harness tests | `rust/crates/rusty-claude-cli/tests/mock_parity_harness.rs` |
| Wrapper script | `rust/scripts/run_mock_parity_harness.sh` |
| Scenario manifest | `rust/mock_parity_scenarios.json` |
| Diff runner | `rust/scripts/run_mock_parity_diff.py` |

## Run the harness

```bash
cd rust
./scripts/run_mock_parity_harness.sh
```

Or start the mock manually:

```bash
cd rust
cargo run -p mock-anthropic-service -- --bind 127.0.0.1:0
```

## Covered scenarios (examples)

- `streaming_text`
- `read_file_roundtrip`, `grep_chunk_assembly`
- `write_file_allowed`, `write_file_denied`
- `multi_tool_turn_roundtrip`
- `bash_stdout_roundtrip`
- `bash_permission_prompt_approved` / `denied`
- `plugin_tool_roundtrip`
- `auto_compact_triggered`, `token_cost_reporting`

## Parity document

Behavioral checklist and lane status: [Parity](parity.md).

Full harness notes in the repository: `rust/MOCK_PARITY_HARNESS.md`.
