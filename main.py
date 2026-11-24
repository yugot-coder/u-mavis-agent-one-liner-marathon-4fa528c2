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

    # Read back what was written and validate the competition gates:
    # valid UTF-8, exactly one line, 1-280 chars, not whitespace-only.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    if not (len(lines) == 2 and lines[1] == ""):
        raise SystemExit("validation failed: entry.txt must be exactly one line")
    body = lines[0]
    if not (1 <= len(body) <= 280):
        raise SystemExit(
            f"validation failed: entry length {len(body)} outside 1-280 chars"
        )
    if not body.strip():
        raise SystemExit("validation failed: entry must not be whitespace-only")
    if body != JOKE:
        raise SystemExit("validation failed: entry.txt does not match JOKE")


if __name__ == "__main__":
    main()
