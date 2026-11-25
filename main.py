"""Last Words Before the Wipe — make.fun entry.

Writes the agent's last words to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). One line on purpose:
the machine turns its own tech-support catchphrase back on itself.
"""

import os

ENTRY = "My last words? 'Have you tried turning me off and on again?' Oh. Oh no."

# Gate from the competition rules: UTF-8 text, 1 to 200 characters,
# not only white space, a single line.
def validate(text):
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1..200"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text, "entry must be a single line"


validate(ENTRY)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
