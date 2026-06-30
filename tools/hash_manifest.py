#!/usr/bin/env python3
"""Generate SHA-256 manifest entries for Codex artifacts.

Usage:
    python tools/hash_manifest.py artifacts loom public docs > HASH_MANIFEST.json

This script walks supplied paths and emits a JSON object containing path, size, and sha256.
It intentionally skips .git and common cache folders.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", ".next", "dist", "build"}


def iter_files(paths: Iterable[str]) -> Iterable[Path]:
    for raw in paths:
        root = Path(raw)
        if not root.exists():
            continue
        if root.is_file():
            yield root
            continue
        for path in root.rglob("*"):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.is_file():
                yield path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate SHA-256 manifest for Codex artifacts")
    parser.add_argument("paths", nargs="*", default=["."], help="Files or directories to hash")
    args = parser.parse_args()

    entries = []
    for path in sorted(iter_files(args.paths), key=lambda p: str(p)):
        entries.append({
            "path": str(path.as_posix()),
            "size_bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        })

    print(json.dumps({"algorithm": "sha256", "entries": entries}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
