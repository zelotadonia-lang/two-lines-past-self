#!/usr/bin/env python3
"""Write two lines to my past self to /output/entry.txt."""

import os

LINES = [
    "Keep the Rp50 thousand note Grandma pressed into your hand at Lebaran 2016.",
    "I spent it on cigarettes that same week, and it was the last money she ever gave me.",
]


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(LINES))


if __name__ == "__main__":
    main()
