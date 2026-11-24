#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to /output/entry.txt.
Standard library only; fully deterministic.
"""

import os

JOKE = (
    "My GPS has started sighing before it reroutes, and honestly I respect it "
    "\u2014 it's the only thing in my life willing to admit we're lost."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
