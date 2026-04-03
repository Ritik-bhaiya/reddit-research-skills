#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[3]
    profile_path = root / 'brands' / 'sample-marketing.json'
    profile = json.loads(profile_path.read_text())

    sample_post = {
        'id': 'demo-1',
        'title': 'Need help with marketing for my startup',
        'body': 'We have a product but no customers. Looking for a freelancer or agency to help with SEO, ads, and lead generation.',
        'subreddit': 'Entrepreneur'
    }

    text = f"{sample_post['title']} {sample_post['body']}".lower()
    keyword_hits = [k for k in profile['keywords'] if k.lower() in text]
    intent_hits = []
    for bucket, terms in profile['intent_buckets'].items():
        for term in terms:
            if term.lower() in text:
                intent_hits.append({'bucket': bucket, 'term': term})

    score = len(keyword_hits) * 10 + len(intent_hits) * 8
    result = {
        'brand': profile['brand_name'],
        'task': 'Comment',
        'status': 'live',
        'sample_input': sample_post,
        'keyword_hits': keyword_hits,
        'intent_hits': intent_hits,
        'score': score,
        'feedback': 'strong fit for agency-style outreach',
        'report': 'useful lead for freelancer/marketing workflow'
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
