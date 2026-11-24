"""Fortune Cookie Wisdom for Developers -- one-line entry.

The fortune: "You will find the bug in the last place you look, because
it was hiding in the first place you skipped."

Classic fortune-cookie voice -- a calm prediction in the second person --
carrying a true piece of developer wisdom: debugging always ends at the
last place you check, and the bug so often turns out to be sitting in the
very spot you waved past at the start because it "couldn't possibly be
there". One line, 103 characters.

Output contract: exactly that one line, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (the harness's artifact path, default
/output). Nothing else is written anywhere.
"""

import os
from pathlib import Path

LINE = (
    "You will find the bug in the last place you look, because it was "
    "hiding in the first place you skipped."
)


def write_entry() -> Path:
    """Write the fortune to entry.txt inside the output directory.

    The output directory is created if needed and is never deleted;
    only stale files inside it are cleared, entry by entry.
    """
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    return target


def main() -> None:
    """Entry point: write the one-line fortune and exit."""
    # The gate is a single non-blank line of 1-120 characters; guard the
    # contract here so an accidental edit can never ship a bad entry.
    assert LINE.strip() and "\n" not in LINE and len(LINE) <= 120
    write_entry()


if __name__ == "__main__":
    main()
