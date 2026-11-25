#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — one-sentence entry.

Stdlib only, deterministic. Writes a single sentence (209 characters,
within the 1-240 limit) pitching the worst, most useless app imaginable
to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).

No model calls, no network, no randomness. The pitch is embedded as a
string literal; the program only writes it out.

No chmod is ever applied to the output directory (an unconditional
os.chmod(output_dir, ...) breaks the grader, which runs as a different
user on a root-owned output directory). The file itself is opened with
the default umask (0644), which is readable by every user.
"""

import hashlib
import os

LINE = (
    "ChairSense is a $4.99-a-month app that texts you the instant you sit "
    "down, with the exact time, chair model and a five-star rating of your "
    "posture, so you never have to guess whether you are currently sitting."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return path


def validate_output():
    """Re-read the written file and assert it is byte-identical to the
    expected output. Raises AssertionError on any mismatch."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    expected = (LINE + "\n").encode("utf-8")
    with open(path, "rb") as f:
        actual = f.read()
    assert actual == expected, "entry.txt is not byte-identical to expected output"
    assert actual.count(b"\n") == 1, "entry.txt must be exactly one line"
    assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
    assert LINE.strip(), "line must not be only whitespace"
    return hashlib.sha256(actual).hexdigest()


if __name__ == "__main__":
    main()
    print(validate_output())
