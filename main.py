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

Before writing, the word is validated against the competition gate
(UTF-8 text of 1 to 30 characters, not only white space, and a single
word with no internal white space), so a bad constant can never
silently produce an invalid entry.

Usage (as the grader runs it):
    python3 main.py            # writes /output/entry.txt
    python3 main.py <path>     # optional: write to <path> instead (testing)
"""

import sys
from pathlib import Path

WORD = "doohickey"
DEFAULT_OUTPUT = Path("/output/entry.txt")

# The competition gate: 1 to 30 characters, not only white space.
MIN_WORD_CHARS = 1
MAX_WORD_CHARS = 30


def validate_word(word: str) -> str:
    """Check the word against the competition gate and return it.

    Raises ValueError if the word is empty, only white space, longer
    than 30 characters, contains internal white space (i.e. more
    than one word), or contains a control character that could never
    appear in a grandma's text message.
    """
    if not word:
        raise ValueError("word must not be empty")
    if len(word) < MIN_WORD_CHARS or len(word) > MAX_WORD_CHARS:
        raise ValueError(
            f"word must be {MIN_WORD_CHARS}-{MAX_WORD_CHARS} characters, "
            f"got {len(word)}"
        )
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no white space")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("word must not contain control characters")
    return word


def main() -> int:
    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    word = validate_word(WORD)
    if out_path.parent != Path("."):
        out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(word, encoding="utf-8", newline="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
