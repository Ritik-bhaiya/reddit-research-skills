#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _shared import load_json, dump_json, score_item, dedupe


def main() -> int:
    ap = argparse.ArgumentParser(description='Score Reddit items using a brand profile.')
    ap.add_argument('--profile', required=False, help='Path to brand profile JSON')
    ap.add_argument('--input', required=False, help='Path to JSON list input; defaults to stdin')
    ap.add_argument('--top', type=int, default=10)
    args = ap.parse_args()

    profile = load_json(args.profile, {}) if args.profile else {}
    raw = Path(args.input).read_text() if args.input else sys.stdin.read()
    items = dedupe(json.loads(raw or '[]'))
    scored = [score_item(item, profile) for item in items]
    scored.sort(key=lambda x: x.get('score', 0), reverse=True)
    sys.stdout.write(dump_json(scored[: args.top]) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
