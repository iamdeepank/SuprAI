#!/usr/bin/env python3
"""Second-pass rebrand: user-facing suprai CLI strings -> suprai."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {"/target/", "/.git/", "/crates/claw-", "/.claw/sessions/", "/.claude/sessions/"}
EXTENSIONS = {
    ".rs", ".md", ".example", ".json", ".sh", ".py", ".html", ".txt", ".yml", ".yaml", ".toml"
}

REPLACEMENTS = [
    ("`suprai`", "`suprai`"),
    ("suprai --", "suprai --"),
    ("suprai prompt", "suprai prompt"),
    ("suprai doctor", "suprai doctor"),
    ("suprai status", "suprai status"),
    ("suprai version", "suprai version"),
    ("suprai help", "suprai help"),
    ("suprai init", "suprai init"),
    ("suprai config", "suprai config"),
    ("suprai mcp", "suprai mcp"),
    ("suprai skills", "suprai skills"),
    ("suprai agents", "suprai agents"),
    ("suprai export", "suprai export"),
    ("suprai diff", "suprai diff"),
    ("suprai state", "suprai state"),
    ("suprai sandbox", "suprai sandbox"),
    ("suprai acp", "suprai acp"),
    ("suprai compact", "suprai compact"),
    ("suprai session", "suprai session"),
    ("suprai cost", "suprai cost"),
    ("suprai clear", "suprai clear"),
    ("suprai permissions", "suprai permissions"),
    ("suprai requires", "suprai requires"),
    ("Run suprai", "Run suprai"),
    ("run suprai", "run suprai"),
    ("Start suprai", "Start suprai"),
    ("start suprai", "start suprai"),
    ("install suprai", "install suprai"),
    ("Install suprai", "Install suprai"),
    ("the SuprAI CLI", "the SuprAI CLI"),
    ("The SuprAI CLI", "The SuprAI CLI"),
    ("SuprAI-specific", "SuprAI-specific"),
    ("SuprAI routing", "SuprAI routing"),
    ("SuprAI selects", "SuprAI selects"),
    ("from SuprAI", "from SuprAI"),
    ("into SuprAI", "into SuprAI"),
    ("only SuprAI", "only SuprAI"),
    ("SuprAI can", "SuprAI can"),
    ("SuprAI currently", "SuprAI currently"),
    ("SuprAI can", "SuprAI can"),
    ("SuprAI ", "SuprAI "),
    ("this SuprAI ", "this SuprAI "),
    ("current SuprAI", "current SuprAI"),
    ("for suprai", "for suprai"),
    ("Usage            suprai ", "Usage            suprai "),
    ("Resume previous  suprai ", "Resume previous  suprai "),
    ("Run:   suprai", "Run:   suprai"),
    ("Or:    suprai", "Or:    suprai"),
    ("Then rerun: suprai", "Then rerun: suprai"),
    ("suprai should", "suprai should"),
    ("~/.config/suprai/", "~/.config/suprai/"),
    ("Binary name:** `suprai`", "Binary name:** `suprai`"),
    ("**Binary name:** `suprai`", "**Binary name:** `suprai`"),
    ("interactive_only: suprai", "interactive_only: suprai"),
    ("suprai -p", "suprai -p"),
    ("suprai -C", "suprai -C"),
    ("suprai -V", "suprai -V"),
    ("| suprai`", "| suprai`"),
    (" | suprai ", " | suprai "),
    ("echo 'task' | suprai`", "echo 'task' | suprai`"),
    ("`echo 'task' | suprai`", "`echo 'task' | suprai`"),
    ("cargo install suprai", "cargo install suprai"),
    ("suprai install", "suprai install"),
    ("suprai output", "suprai output"),
    ("suprai dump", "suprai dump"),
    ("suprai bootstrap", "suprai bootstrap"),
    ("suprai system", "suprai system"),
    ("suprai dump-manifests", "suprai dump-manifests"),
    ("suprai bootstrap-plan", "suprai bootstrap-plan"),
    ("suprai system-prompt", "suprai system-prompt"),
    ("suprai `", "suprai `"),
    ("`suprai ", "`suprai "),
    (" suprai`", " suprai`"),
    (" suprai ", " suprai "),
    (" suprai.", " suprai."),
    (" suprai,", " suprai,"),
    (" claw\n", " suprai\n"),
    (" claw\r", " suprai\r"),
    ("(suprai ", "(suprai "),
    (" suprai)", " suprai)"),
    ("claw\n", "suprai\n"),
    ("claw\r", "suprai\r"),
    ("suprai.", "suprai."),
    ("suprai,", "suprai,"),
    ("suprai;", "suprai;"),
    ("suprai:", "suprai:"),
    ("suprai)", "suprai)"),
    ("(suprai)", "(suprai)"),
    ("suprai`", "suprai`"),
    ("`suprai", "`suprai"),
]


def should_skip(path: Path) -> bool:
    s = path.as_posix()
    return any(part in s for part in SKIP_PARTS)


def main() -> None:
    count = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in EXTENSIONS:
            continue
        if should_skip(path):
            continue
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        text = re.sub(r"(?m)^claw$", "suprai", text)
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            count += 1
    print(f"Updated {count} files")


if __name__ == "__main__":
    main()
