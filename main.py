#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt (UTF-8, 1-200 chars).
Pure stdlib only: no third-party imports.
"""

import os

JOKE = "I told the houseplant it was growing on me. It said good \u2014 it was really putting down roots here."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print("wrote {} ({} chars)".format(path, len(JOKE)))


if __name__ == "__main__":
    main()
