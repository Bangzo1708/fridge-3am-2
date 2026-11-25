#!/usr/bin/env python3
"""The 3AM Fridge Text — round 2 entry.

Writes the single line our smart fridge texts its owner at 3am to
/output/entry.txt. Deterministic: no randomness, no time, no network.
The line is a fixed constant; the program just writes it.
"""

import sys
from pathlib import Path

# The fridge's 3am text. One line, capped at 140 characters.
LINE = (
    "It's 3am. I've been humming in the dark for 9 years and you've "
    "never once asked how I am. The pickles are worried too."
)


def main() -> None:
    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
