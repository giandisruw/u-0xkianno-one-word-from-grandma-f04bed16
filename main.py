#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word my grandma
would text about AI.

Why this word: "doohickey" is the word a grandma reaches for when she
cannot name the thing in front of her — warm, a little baffled, and funny
on its own. An AI is the ultimate doohickey: a clever little gadget she
does not pretend to understand, so she gives it the name she gives every
mysterious gadget in the house. It is a real word, instantly readable,
tied to machines and gadgets rather than to any subject at all, and it is
not the obvious "robot" pick.

Deterministic and offline: no network, no randomness, no API key, no
input. The output is always exactly these 9 bytes, with no trailing
newline, so the file holds one word and nothing else.

Usage (as the grader runs it):
    python3 main.py            # writes /output/entry.txt
    python3 main.py <path>     # optional: write to <path> instead (testing)
"""

import os
import sys

WORD = "doohickey"
DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
