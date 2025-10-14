#!/usr/bin/env python3
"""
Mini utility script with a few demo functions and a tiny CLI.
Used only so we have ~100 lines of code to ingest and chunk.
"""

import sys
from datetime import datetime

def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def mul(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def stats(numbers):
    """Return (count, total, avg) for a sequence of numbers."""
    numbers = list(numbers)
    if not numbers:
        return (0, 0.0, 0.0)
    total = sum(numbers)
    return (len(numbers), total, total / len(numbers))

def timestamp() -> str:
    """Current ISO timestamp."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

def usage():
    print(
        "Usage:\n"
        "  app.py greet <name>\n"
        "  app.py add <a> <b>\n"
        "  app.py mul <a> <b>\n"
        "  app.py stats <n1> <n2> ...\n"
        "  app.py time\n"
    )

def main(argv):
    if len(argv) < 2:
        usage()
        return 1

    cmd = argv[1]
    if cmd == "greet" and len(argv) == 3:
        print(greet(argv[2]))
        return 0
    elif cmd == "add" and len(argv) == 4:
        print(add(float(argv[2]), float(argv[3])))
        return 0
    elif cmd == "mul" and len(argv) == 4:
        print(mul(float(argv[2]), float(argv[3])))
        return 0
    elif cmd == "stats" and len(argv) >= 3:
        nums = [float(x) for x in argv[2:]]
        c, t, avg = stats(nums)
        print({"count": c, "total": t, "avg": avg})
        return 0
    elif cmd == "time":
        print(timestamp())
        return 0
    else:
        usage()
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))

# Extra lines to bring us near ~100 lines, realistic comments/docstrings below.
# In a real codebase, these might be logging, config templates, etc.

"""
Notes:
- This file is deliberately simple but non-trivial.
- We'll ingest this source code as text and chunk every 50 characters.
- Later you can swap the chunker to token-based or sentence-based.
- For embeddings or semantic search, consider pgvector.
- For multiple files, walk the repo and repeat.
- For dedupe, we store a SHA-256 of file content.
- For provenance, store file path + git commit if needed.
- For updates, upsert when sha changes.
- For line-aware chunks, store absolute char offsets.
"""