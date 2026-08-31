#!/usr/bin/env python3
"""Refresh the sha256sum fields in metadata.yaml and report drift.

Rewrites each `sha256sum:` line in place rather than re-serialising the file, so
comments, key order and block-scalar formatting survive untouched. Run after adding
or changing anything under data/.

    python3 update_hashes.py            # rewrite metadata.yaml
    python3 update_hashes.py --check    # report only; exit 1 if anything is stale

Reports two kinds of problem, both of which should be fixed before committing:
  - a data file with no metadata block
  - a metadata block naming a file that no longer exists
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
METADATA = ROOT / "metadata.yaml"

# Files that are not sample data and get no metadata block.
IGNORED_NAMES = {".DS_Store", ".gitkeep"}

KEY_RE = re.compile(r"^(?P<key>[^#\s].*?):\s*$")
HASH_RE = re.compile(r"^(?P<indent>\s*)sha256sum:\s*(?P<value>\S*)\s*$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def data_files() -> dict[str, Path]:
    """Every data file, keyed by its path relative to data/."""
    return {
        str(path.relative_to(DATA_DIR)): path
        for path in sorted(DATA_DIR.rglob("*"))
        if path.is_file() and path.name not in IGNORED_NAMES
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report stale hashes without rewriting metadata.yaml",
    )
    args = parser.parse_args()

    if not METADATA.is_file():
        print(f"error: {METADATA.name} not found", file=sys.stderr)
        return 1

    files = data_files()
    lines = METADATA.read_text(encoding="utf-8").splitlines(keepends=True)

    current_key: str | None = None
    documented: set[str] = set()
    updated: list[str] = []
    orphaned: list[str] = []
    out: list[str] = []

    for line in lines:
        key_match = KEY_RE.match(line)
        if key_match:
            current_key = key_match.group("key")
            documented.add(current_key)
            if current_key not in files:
                orphaned.append(current_key)

        hash_match = HASH_RE.match(line)
        if hash_match and current_key in files:
            actual = sha256(files[current_key])
            if hash_match.group("value") != actual:
                updated.append(current_key)
                line = f"{hash_match.group('indent')}sha256sum: {actual}\n"

        out.append(line)

    undocumented = sorted(set(files) - documented)

    for name in updated:
        print(f"{'stale' if args.check else 'updated'}: {name}")
    for name in undocumented:
        print(f"missing metadata block: {name}", file=sys.stderr)
    for name in orphaned:
        print(f"metadata block for missing file: {name}", file=sys.stderr)

    if args.check:
        problems = bool(updated or undocumented or orphaned)
        if not problems:
            print(f"metadata.yaml is up to date ({len(files)} files)")
        return 1 if problems else 0

    if updated:
        METADATA.write_text("".join(out), encoding="utf-8")
        print(f"\nrewrote {METADATA.name}: {len(updated)} hash(es) updated")
    else:
        print(f"all {len(files)} hashes already correct")

    return 1 if (undocumented or orphaned) else 0


if __name__ == "__main__":
    raise SystemExit(main())
