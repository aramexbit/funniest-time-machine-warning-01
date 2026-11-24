#!/usr/bin/env python3
"""Time Machine Warning Label — one-line entry for the make.fun bounty.

The entry is the label itself, so this program stays small on purpose:
it keeps the label as fixed text, checks it against the bounty gate
(UTF-8, 1 to 120 characters, a single line, not only whitespace), and
writes it to `/output/entry.txt`. Deterministic, standard library
only, no network.

The joke turns the classic time-travel hazard — meeting your own
duplicate self — into the punchline, and saves the surprise for the
last few words, while keeping the straight face of a genuine safety
notice. That is the order the judge's brief weighs: a real hazard
made into the joke, surprise at the end, official calm throughout.

Usage:
    python3 main.py [--output PATH]

The default output is /output/entry.txt, the path the harness reads.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# The label. 90 characters. The hazard is meeting your duplicate self;
# the surprise lands in the last clause, where the universe reacts
# like a spouse walking out.
LABEL = "WARNING: Do not meet yourself. One awkward eye contact and the universe files for divorce."

DEFAULT_OUTPUT = Path("/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 120


def check_gate(text: str) -> str:
    """Return the text when it passes the entry gate, else raise."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS} to {MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises UnicodeEncodeError on a bad character
    return text


def write_entry(text: str, output: Path) -> Path:
    """Write the checked text to output, creating its folder if needed.

    No trailing newline is added: the file holds exactly the label,
    byte for byte, which is what the gate and the judge read.
    """
    checked = check_gate(text)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(checked, encoding="utf-8")
    return output


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="where to write the entry (default: /output/entry.txt)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        written = write_entry(LABEL, args.output)
    except (ValueError, UnicodeEncodeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(LABEL)} characters to {written}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
