#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _shared import dump_json


def main() -> int:
    ap = argparse.ArgumentParser(description='Generate a shortlist summary report.')
    ap.add_argument('--input', required=False, help='Path to JSON list input; defaults to stdin')
    args = ap.parse_args()

    raw = Path(args.input).read_text() if args.input else sys.stdin.read()
    items = json.loads(raw or '[]')
    summary = {
        'count': len(items),
        'top': items[:5],
    }
    sys.stdout.write(dump_json(summary) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
