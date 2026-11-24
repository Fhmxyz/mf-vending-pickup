#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one vending-machine pickup line to /output/entry.txt and echoes
it to stdout. Python 3, stdlib only, fully deterministic.
"""

import os

LINE = (
    "Are you the bag of chips stuck at B4? Because I've rocked this "
    "machine for ten minutes, and you're the one thing I actually "
    "want to drop into my life."
)


def render() -> str:
    """Return the pickup line exactly as the judge will read it."""
    return LINE.strip()


def main() -> None:
    line = render()
    assert 0 < len(line) <= 200, f"line is {len(line)} characters, gate wants 1..200"
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        # Nowhere to write (e.g. a read-only local checkout): the line
        # still goes to stdout so a human can read the entry.
        pass
    print(line)


if __name__ == "__main__":
    main()
