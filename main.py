#!/usr/bin/env python3
"""make.fun entry: Name the Robot Band.

Writes the one-line entry to <MAKEFUN_OUTPUT_DIR>/entry.txt
(or /output/entry.txt when the variable is unset).
Deterministic, Python 3.13 stdlib only, no trailing newline.
"""

import os

LINE = "The Self-Checkout Machines \u2014 hit song 'Unexpected Item in the Bagging Area'"
# 76 characters, well under the 200-character cap; no trailing newline
# is written, so the entry file holds exactly this line.

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
