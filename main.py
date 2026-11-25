#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes the winning one-line excuse to /output/entry.txt.
The line is a single line, 78 characters, 16 words (limit 20 words /
140 characters), chosen by a local pairwise tournament judged against
the bounty's published judge brief (see README.md for the tournament
table).
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 30 candidates, Swiss 4 rounds (60 games) + final,
# 122 judge calls on the Caffeine Inference router, every game played
# in both label orders. #17 led the Swiss at 2.85, #2 second at 2.7;
# the final tied 0.5-0.5 (each order's judge picked the A-labelled
# entry at margin 3) and #2 took it on the pre-declared lower-id
# tie-break.
ENTRY = "boiler engineer finally rang back, he's here at eight and i have to let him in"


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    assert 1 <= len(line.split()) <= 20, f"entry must be 1-20 words, got {len(line.split())}"
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {path}")
    print(line)


if __name__ == "__main__":
    main()
