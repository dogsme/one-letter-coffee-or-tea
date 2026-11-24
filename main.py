#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry A (coffee).

Writes exactly one letter, A, to /output/entry.txt and nothing else:
no word, no explanation, no punctuation, no trailing newline.

Why coffee: the judge weighs vivid first, then funny, then true. Coffee
is the bolder, more alive answer -- dark, bitter, the morning jolt that
wakes you up -- where tea is calm and gentle. A single A lands as a
fuller, punchier stance than a single B, and as the first letter it
reads as the first choice too.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
CHOICE = "A"  # A = coffee, B = tea


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(CHOICE)


if __name__ == "__main__":
    main()
