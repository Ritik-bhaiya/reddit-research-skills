#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _shared import load_json, dump_json


def main() -> int:
    ap = argparse.ArgumentParser(description='Filter a Reddit candidate feed by target subreddits and freshness.')
    ap.add_argument('--profile', required=False, help='Path to brand profile JSON')
    ap.add_argument('--input', required=False, help='Path to JSON list input; defaults to stdin')
    args = ap.parse_args()

    profile = load_json(args.profile, {}) if args.profile else {}
    raw = Path(args.input).read_text() if args.input else sys.stdin.read()
    items = json.loads(raw or '[]')
    target = set(profile.get('target_subreddits', []))
    freshness = int(profile.get('freshness_window_hours', 48))

    out = []
    for item in items:
        if target and item.get('subreddit') not in target:
            continue
        if freshness and int(item.get('age_hours', 0)) > freshness:
            continue
        out.append(item)
    sys.stdout.write(dump_json(out) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
