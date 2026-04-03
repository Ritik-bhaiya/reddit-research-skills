#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus
from urllib.request import Request, urlopen

from _shared import load_json, score_item, dedupe

USER_AGENT = "reddit-research-skills/1.0"


def fetch_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    delays = [1.5, 3.0, 6.0]
    last_err = None
    for d in delays:
        try:
            with urlopen(req, timeout=20) as resp:
                return json.loads(resp.read().decode("utf-8", errors="replace"))
        except HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(d)
                continue
            break
        except (URLError, TimeoutError, json.JSONDecodeError) as e:
            last_err = e
            time.sleep(d)
    return {"data": {"children": []}, "error": str(last_err) if last_err else "fetch_failed"}


def to_item(child: dict) -> dict:
    d = child.get("data", {})
    created = int(d.get("created_utc", 0) or 0)
    age_hours = round((time.time() - created) / 3600, 2) if created else None
    permalink = d.get("permalink", "")
    return {
        "id": d.get("id"),
        "subreddit": d.get("subreddit"),
        "title": (d.get("title") or "").strip(),
        "body": (d.get("selftext") or "").strip(),
        "author": d.get("author"),
        "url": f"https://www.reddit.com{permalink}" if permalink else d.get("url", ""),
        "permalink": permalink,
        "num_comments": int(d.get("num_comments", 0) or 0),
        "score": int(d.get("score", 0) or 0),
        "created_utc": created,
        "age_hours": age_hours,
        "is_locked": bool(d.get("locked", False)),
        "over_18": bool(d.get("over_18", False)),
    }


def query_search(query: str, limit: int) -> list[dict]:
    url = f"https://www.reddit.com/search.json?q={quote_plus(query)}&sort=new&limit={limit}"
    data = fetch_json(url)
    return [to_item(c) for c in data.get("data", {}).get("children", [])]


def query_subreddit(subreddit: str, limit: int) -> list[dict]:
    sub = subreddit.strip().lstrip("r/")
    url = f"https://www.reddit.com/r/{sub}/new.json?limit={limit}"
    data = fetch_json(url)
    return [to_item(c) for c in data.get("data", {}).get("children", [])]


def main() -> int:
    ap = argparse.ArgumentParser(description="Live Reddit discovery using a public-safe brand profile.")
    ap.add_argument("--profile", required=True, help="Path to brand profile JSON")
    ap.add_argument("--freshness-hours", type=float, default=48)
    ap.add_argument("--max-candidates", type=int, default=20)
    ap.add_argument("--search-limit", type=int, default=10)
    args = ap.parse_args()

    profile = load_json(args.profile, {})
    target_subreddits = profile.get("target_subreddits", []) or []
    keywords = profile.get("keywords", []) or []
    intent_terms = profile.get("intent_terms", []) or []

    items = []

    # 1) subreddit scan
    for sub in target_subreddits[:10]:
        items.extend(query_subreddit(sub, limit=10))

    # 2) keyword search
    search_terms = (keywords[:8] if keywords else []) + (intent_terms[:8] if intent_terms else [])
    for term in search_terms[:12]:
        items.extend(query_search(term, limit=args.search_limit))

    # 3) cleanup + freshness filter
    items = dedupe(items)
    if args.freshness_hours:
        filtered = []
        for item in items:
            age = item.get("age_hours")
            if age is None or age <= args.freshness_hours:
                filtered.append(item)
        items = filtered

    # 4) score
    scored = [score_item(item, profile) | {"title": item.get("title"), "subreddit": item.get("subreddit"), "url": item.get("url"), "author": item.get("author"), "age_hours": item.get("age_hours") } for item in items]
    scored.sort(key=lambda x: x.get("score", 0), reverse=True)

    # 5) shortlist
    shortlist = scored[: args.max_candidates]
    print(json.dumps({"brand": profile.get("brand_name", profile.get("brand_id", "unknown")), "shortlist": shortlist}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
