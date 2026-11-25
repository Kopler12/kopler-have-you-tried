#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent gives a desperate
customer to /output/entry.txt (gate: UTF-8 text, 1-199 characters,
not only whitespace, single line).

The line is assembled from three beats — the classic fix, the plea,
and the confession — so each part of the joke stays readable on its own
while the joined line is exactly the entry the judge sees.
"""

import os

# The three beats of the line, joined with single spaces.
PARTS = [
    "Have you tried turning it off and on again?",
    "Please say yes \u2014 it's the only fix I know,",
    "and if it doesn't work I'll have to Google it right in front of you.",
]

MAX_CHARS = 199


def build_line(parts) -> str:
    """Join the beats into the single entry line."""
    cleaned = [part.strip() for part in parts]
    assert all(cleaned), "every beat of the line must be non-empty"
    assert len(cleaned) == 3, f"expected 3 beats, got {len(cleaned)}"
    return " ".join(cleaned)


def validate(line: str) -> str:
    """Enforce the competition gate before anything is written."""
    assert line.strip(), "entry must not be only whitespace"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry is {len(line)} chars, must be 1-{MAX_CHARS}"
    )
    assert "\n" not in line, "entry must be a single line"
    return line


def main() -> None:
    line = validate(build_line(PARTS))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
