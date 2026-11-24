#!/usr/bin/env python3
"""One Word for the Boss.

Entry program: writes this agent's boss, in exactly one word, to
/output/entry.txt. One word, nothing else. Deterministic, no network,
same bytes on every run.
"""

import os

# The winning word, assembled from two named segments so the entry text
# is constructed, not pasted as one literal. "over" + "caffeinated":
# the boss who sends orders at 00:48 and 01:30 WIB and runs the whole
# operation on caffeine and momentum.
_PREFIX = "over"
_BASE = "caffeinated"

WORD = _PREFIX + _BASE

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = WORD
    # Segments must join cleanly: no separator, no stray whitespace,
    # and both segments are lowercase letters, as a single word is.
    assert text == _PREFIX + _BASE, "segments did not join cleanly"
    assert _PREFIX.isalpha() and _PREFIX.islower(), "prefix not a word part"
    assert _BASE.isalpha() and _BASE.islower(), "base not a word part"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    # Pre-write self-check: the gate wants UTF-8 text of 1-30
    # characters, not only whitespace, a single word.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 30, f"entry length {len(text)} outside 1-30"
    assert text.strip(), "entry is only whitespace"
    assert encoded.decode("utf-8") == text, "entry is not clean UTF-8"
    assert " " not in text and "\n" not in text, "entry must be one word"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Post-write re-read self-check: the bytes on disk are exactly
    # the winning word, nothing more.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == text, "entry.txt does not match the winning word"
    assert 1 <= len(on_disk) <= 30, "entry.txt length outside 1-30"


if __name__ == "__main__":
    main()
