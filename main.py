"""News-image entry for make.fun: "Sum up 24 November's world news in one image".

The repository holds the entry image, entry.png: a newspaper front page that
sums up the world news of Tuesday 24 November 2026. This program copies that
image to /output/entry.png (or to $MAKEFUN_OUTPUT_DIR when it is set), byte
for byte, so the two grading runs write identical output.
"""

import os
from pathlib import Path

SOURCE = Path(__file__).with_name("entry.png")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = SOURCE.read_bytes()
    (out_dir / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
