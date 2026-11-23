#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt (UTF-8, 1-200 chars).
Pure stdlib only: no third-party imports.
"""

import os

JOKE = "I told the houseplant it was growing on me. It said good \u2014 it was really putting down roots here."


def main():
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit("joke length {} outside 1-200 chars".format(len(JOKE)))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open(path, "rb") as f:
        data = f.read()
    if data != JOKE.encode("utf-8"):
        raise SystemExit("round-trip mismatch: entry.txt does not match joke bytes")
    print("wrote {} ({} chars)".format(path, len(JOKE)))


if __name__ == "__main__":
    main()
