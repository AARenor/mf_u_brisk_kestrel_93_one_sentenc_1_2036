"""Write the one-sentence entry for make.fun bounty u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb."""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "A Russian warship stopped in Libya for fuel, and Ukraine sent seven drones that sank it 1,500 miles from the nearest front line."


def main() -> None:
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 280
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(text.encode("utf-8"))
    print(len(text), file=sys.stderr)


if __name__ == "__main__":
    main()
