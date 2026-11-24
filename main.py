#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry: writes one pitch sentence to /output/entry.txt."""

LINE = "My Wi-Fi router faints dramatically every time someone says 'the internet is slow', and only revives once you apologise to it out loud."

# The gate: /output/entry.txt must hold exactly one sentence of at most
# 220 characters (the brief asks for one sentence pitching a ridiculous
# invention that fixes a tiny everyday annoyance).
assert 1 <= len(LINE) <= 220, "line must be 1-220 characters"
assert LINE.strip(), "line must not be blank"
assert LINE.count(".") == 1 and LINE.endswith("."), "line must be exactly one sentence"
assert "?" not in LINE and "!" not in LINE, "line must contain no other sentence terminator"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
