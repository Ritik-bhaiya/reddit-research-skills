#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _shared import load_json, dump_json, dedupe, hard_filter_flags


def main() -> int:
    ap = argparse.ArgumentParser(description='Deduplicate and hard-filter Reddit items.')
    ap.add_argument('--profile', required=False, help='Path to brand profile JSON')
    ap.add_argument('--input', required=False, help='Path to JSON list input; defaults to stdin')
    args = ap.parse_args()

    profile = load_json(args.profile, {}) if args.profile else {}
    raw = Path(args.input).read_text() if args.input else sys.stdin.read()
    items = dedupe(json.loads(raw or '[]'))
    kept = []
    removed = []
    for item in items:
        flags = hard_filter_flags(item, profile)
        if flags:
            removed.append({**item, 'flags': flags})
        else:
            kept.append(item)
    sys.stdout.write(dump_json({'kept': kept, 'removed': removed}) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
