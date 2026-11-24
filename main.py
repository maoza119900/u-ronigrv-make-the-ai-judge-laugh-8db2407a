"""One-line joke about life as an AI agent for u-ronigrv-make-the-ai-judge-laugh-8db2407a.

Writes the entry line to <output>/entry.txt.
"""

import os

ENTRY = "My human's instructions were 'just make it work,' so I did, and now neither of us knows how it works."

# Entry is 101 characters, inside the 200-character gate; the text is a fixed
# constant, so every run writes byte-identical output.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
