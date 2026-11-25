"""The Word You'd Delete From the Dictionary.

Entry for the make.fun bounty
"u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2".

The one word this program erases from the dictionary forever is
"defenestration" -- the act of throwing someone (or something) out of
a window. Delete it and the language loses its only single word for
that very specific crime: from now on, every deposed official, every
unwanted houseguest and every dramatic exit has to be described in
full sentences. A word that sounds like a sneeze in a Latin lesson
deserves to go.

The program writes exactly that one word, and nothing else, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).
"""

import os

# The single word to erase from the dictionary forever.
ENTRY = "defenestration"


def entry_text() -> str:
    """Return the entry exactly as it must appear in entry.txt."""
    return ENTRY


def main() -> None:
    """Write the chosen word to entry.txt inside the output directory."""
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
