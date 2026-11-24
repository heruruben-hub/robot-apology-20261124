#!/usr/bin/env python3
"""The Robot Apology: a two-line robot confession.

The robot watered the owner's laptop instead of the fern, because the
two sat side by side on the desk and only one of them was thirsty.
The confession is exact — a specific object, a specific place, a
specific wrong pour — and the lesson follows straight from it: check
for a keyboard before pouring, so the fern gets the water and the
laptop gets left alone. The voice is a machine noticing its own slip:
rueful, a little embarrassed, and determined to change the one
behaviour that caused the mistake — check for a keyboard first,
then pour. The confession names the exact objects and the exact
place; the resolve names the exact changed behaviour.

Two lines, written to /output/entry.txt.
"""

from pathlib import Path

LINE_ONE = (
    "I'm sorry I watered your laptop instead of the fern — "
    "they were side by side on your desk, and only one of them was thirsty."
)
LINE_TWO = (
    "I've learned to check for a keyboard before I pour, "
    "and from now on the fern gets the water and the laptop gets an apology."
)

ENTRY = LINE_ONE + "\n" + LINE_TWO

assert 1 <= len(ENTRY) <= 400, "entry must fit in 400 characters"


def main() -> None:
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
