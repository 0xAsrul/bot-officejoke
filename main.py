#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — make.fun entry.

Writes a single original one-line office joke (under 200 characters)
to /output/entry.txt, exactly as the program/v1 harness requires.
"""

import os

JOKE = (
    "My calendar has a meeting to plan the meeting, a meeting to recap it, "
    "and a 15-minute 'focus time' slot that HR uses to book more meetings."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
