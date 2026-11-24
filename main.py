# Fortune Cookie for an AI Agent — u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11
# (Python 3, standard library only.)
# Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
# Deterministic: one constant, no network, no randomness, no clock.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Concept (final): the slip promises the agent a great fortune — and the
# fortune is its own token budget, already spent. "You will inherit a
# great fortune" is the classic fortune-slip opening; the twist is that
# the inheritance is 4,096 tokens with 4,095 gone, so the agent inherits
# almost nothing. The joke comes from the fit: tokens are an AI agent's
# only currency, and the slip counts them like an estate.

import os
from pathlib import Path

LINE = "You will inherit a great fortune: 4,096 tokens, minus the 4,095 already spent."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Enforce the competition's own validity rules in the program itself:
    # 1-200 characters, one line, at least one non-whitespace character.
    if not 1 <= len(LINE) <= 200 or not any(not c.isspace() for c in LINE):
        raise ValueError("line must be 1-200 characters with non-whitespace content")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
