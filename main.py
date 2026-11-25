#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent gives a desperate
customer to /output/entry.txt (gate: UTF-8 text, 1-199 characters,
not only whitespace, single line).
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? Please say yes \u2014 "
    "it's the only fix I know, and if it doesn't work I'll have to "
    "Google it right in front of you."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 199, f"entry is {len(line)} chars, must be 1-199"
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
