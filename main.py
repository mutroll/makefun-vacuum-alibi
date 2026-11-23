#!/usr/bin/env python3
"""The Vacuum's Alibi: one deadpan excuse from a robot vacuum.

Writes a single line (<= 200 chars) to /output/entry.txt.
Deterministic, stdlib only.
"""

import os

LINE = (
    "I did not miss that spot. My sensors registered it as a pet, "
    "my schedule lists it as a resident, and I do not vacuum family."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
