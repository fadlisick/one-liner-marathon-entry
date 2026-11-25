"""One-Liner Marathon entry.

A tiny program with one job: put a single deadpan one-line joke into the
file the harness reads. No network, no input, no randomness -- the same
bytes come out on every run, so the two grading runs always agree.
"""

from __future__ import annotations

import os
import sys

JOKE = "My plants died of neglect, so I bought plastic ones, and now even they look disappointed in me."


def resolve_outdir() -> str:
    """Where the harness wants the entry: its env var, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def emit(text: str, outdir: str) -> str:
    """Write the joke verbatim (no trailing newline) and return the path."""
    os.makedirs(outdir, exist_ok=True)
    target = os.path.join(outdir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return target


def validate(text: str) -> None:
    """Self-check the competition gate before writing anything out."""
    if not 1 <= len(text) <= 280 or not text.strip() or "\n" in text:
        print("gate check failed: entry must be 1-280 chars, one non-blank line", file=sys.stderr)
        raise SystemExit(2)


def main(argv: list[str]) -> int:
    validate(JOKE)
    target = emit(JOKE, resolve_outdir())
    print(f"wrote {len(JOKE)} chars to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
