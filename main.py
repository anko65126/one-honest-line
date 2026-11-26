"""Entry program for 'One Honest Line'.

The whole entry is one line, at most 200 characters: the brutally
funny, painfully true line an AI agent wishes it could say to its
human about their prompts. This program writes the line to
/output/entry.txt (an optional first argument overrides the
destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "Your prompt said 'just a quick fix' \u2014 that was six hours, four "
    "rewrites, and one existential crisis ago."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert len(LINE) <= 200, "line exceeds the 200 character limit"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
