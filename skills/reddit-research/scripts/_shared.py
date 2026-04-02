#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable

JOB_PATTERNS = [r"\bhiring\b", r"\bjob(s)?\b", r"\brecruit(ing|er|ment)\b", r"\bcareers?\b"]
DEFAULT_AVOID_PATTERNS = [r"\bNSFW\b", r"\bcrypto\b", r"\bgiveaway\b"]


def normalize_text(text: str) -> str:
    text = text or ""
    text = text.lower()
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[^a-z0-9\s]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def contains_any(text: str, patterns: Iterable[str]) -> bool:
    return any(re.search(p, text, re.I) for p in patterns)


def hard_filter_flags(item: dict[str, Any], profile: dict[str, Any] | None = None) -> list[str]:
    profile = profile or {}
    text = normalize_text(" ".join(str(item.get(k, "")) for k in ("title", "body", "text", "subreddit")))
    flags: list[str] = []
    if contains_any(text, JOB_PATTERNS):
        flags.append("job_post")
    for topic in profile.get("avoid_topics", []):
        if topic and topic.lower() in text:
            flags.append(f"avoid_topic:{topic}")
    if contains_any(text, profile.get("avoid_patterns", DEFAULT_AVOID_PATTERNS)):
        flags.append("avoid_pattern")
    if profile.get("target_subreddits") and item.get("subreddit") and item["subreddit"] not in profile["target_subreddits"]:
        flags.append("off_target_subreddit")
    return flags


def load_json(path: str | Path, default: Any = None) -> Any:
    p = Path(path)
    if not p.exists():
        return default
    return json.loads(p.read_text())


def dump_json(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True)


def score_item(item: dict[str, Any], profile: dict[str, Any] | None = None) -> dict[str, Any]:
    profile = profile or {}
    text = normalize_text(" ".join(str(item.get(k, "")) for k in ("title", "body", "text")))
    flags = hard_filter_flags(item, profile)
    if flags:
        return {"id": item.get("id"), "score": 0, "flags": flags, "reasons": ["filtered"]}

    weights = profile.get("weights", {})
    reasons: list[str] = []
    score = 0.0
    for topic in profile.get("target_topics", []):
        if topic and topic.lower() in text:
            score += float(weights.get("target_topic", 10))
            reasons.append(f"target_topic:{topic}")
    for intent in profile.get("intent_patterns", []):
        if intent and intent.lower() in text:
            score += float(weights.get("intent", 8))
            reasons.append(f"intent:{intent}")
    if "?" in item.get("title", "") or "how" in text or "which" in text:
        score += float(weights.get("question", 4))
        reasons.append("question")
    if len(reasons) == 0:
        score += float(weights.get("baseline", 1))
        reasons.append("baseline")
    return {"id": item.get("id"), "score": round(score, 2), "flags": flags, "reasons": reasons}


def dedupe(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen = set()
    out = []
    for item in items:
        key = item.get("url") or item.get("id") or item.get("title")
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out
