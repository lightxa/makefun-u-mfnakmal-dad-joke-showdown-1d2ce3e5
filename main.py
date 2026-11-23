#!/usr/bin/env python3
"""Dad Joke Showdown entry (Python 3.13, standard library only).

Writes one dad joke to /output/entry.txt. Outside the grader's
container the MAKEFUN_OUTPUT_DIR environment variable stands in
for /output, exactly as the kit starter does for Node:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The gate reads the file as UTF-8 text of 1 to 200 characters with
at least one non-whitespace character, and the judge reads exactly
the bytes written, so the joke is written with no trailing line end.

The joke: one sharp incident, one pun, one short line. A father,
impatient for dinner, tells the slow cooker to hurry up, and the
cooker answers with the pun: "one stew at a time" for "one step
at a time". The pun lands at the very end, is understood on first
read, and the subject (a slow cooker at the dinner table) is an
everyday father-at-the-table scene, not one of the famous dad
jokes told a thousand times. Original wording, never copied.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

JOKE = (
    "I told the slow cooker to hurry up for dinner. "
    "It said it was taking things one stew at a time."
)


def main() -> None:
    # Self-check against the sealed gate: 1 to 200 characters,
    # not only white space. Fail loudly here rather than ship
    # an entry the gate would refuse.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError(f"joke fails the gate: {len(JOKE)} characters")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
