#!/usr/bin/env python3
"""Convert Lode Runner JSON level packs to the lodeRunner.v.classic.js format.

usage: python3 convert-json-levels-to-js.py big-red-apple-levels.json

JSON boards use:  . empty  G guard  P player  = solid
JS boards use:    space    0 guard  & player  @ solid
Other tiles (# H - $ S X) are unchanged.

Each level is 16 rows of 28 characters.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TILE_MAP = str.maketrans(
    {
        ".": " ",
        "G": "0",
        "P": "&",
        "=": "@",
    }
)

HEADER = """\
//************************************************************
//* All levels extract from:
//* {title}
//* converted from {source_name}
//************************************************************

var {var_name} = [
"""


def parse_boards(text: str) -> tuple[str, list[str]]:
    title_match = re.search(r'"title"\s*:\s*"(.*?)"', text)
    title = title_match.group(1) if title_match else "Unknown levels"
    boards = re.findall(r'\{\s*"board":\s*"(.*?)"\s*\}', text, re.S)
    if not boards:
        raise SystemExit("No boards found in JSON")
    return title, boards


def to_camel_var(stem: str) -> str:
    parts = re.split(r"[-_\s]+", stem)
    if parts and parts[-1].lower() == "levels":
        parts = parts[:-1]
    if not parts:
        parts = ["level"]
    first, *rest = parts
    return first.lower() + "".join(p[:1].upper() + p[1:] for p in rest) + "Data"


def format_level(index: int, board: str, is_last: bool) -> str:
    lines = board.strip("\n").split("\n")
    if len(lines) != 16:
        raise SystemExit(f"level {index} height {len(lines)}, expected 16")
    mapped = []
    for line in lines:
        if len(line) != 28:
            raise SystemExit(f"level {index} width {len(line)}, expected 28: {line!r}")
        mapped.append(line.translate(TILE_MAP))

    chunks = ['//======<<< Level %03d >>>======' % index, ""]
    for i, line in enumerate(mapped):
        if i < 15:
            chunks.append('"%s" +' % line)
        else:
            comma = "" if is_last else ","
            chunks.append('"%s"%s' % (line, comma))
    chunks.append("")
    return "\n".join(chunks)


def convert(src: Path, dst: Path | None = None, var_name: str | None = None) -> Path:
    title, boards = parse_boards(src.read_text())
    if dst is None:
        dst = src.with_suffix(".js")
    if var_name is None:
        var_name = to_camel_var(src.stem)

    parts = [HEADER.format(title=title, source_name=src.name, var_name=var_name)]
    for i, board in enumerate(boards, 1):
        parts.append(format_level(i, board, is_last=(i == len(boards))))
    parts.append("];\n")
    dst.write_text("".join(parts))
    return dst


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", type=Path, help="Source JSON level pack")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output .js path (default: same name as JSON with .js)",
    )
    parser.add_argument(
        "--var-name",
        help="JS array variable name (default: derived from filename)",
    )
    args = parser.parse_args()
    out = convert(args.json_file, args.output, args.var_name)
    print("wrote", out)


if __name__ == "__main__":
    main()
