---
name: reddit-research
description: Reddit research workflow for finding, scoring, shortlisting, and learning from subreddit posts and comments for brand or lead discovery. Use when building or operating a Reddit research pipeline, tuning discovery/scoring rules, organizing brand-specific heuristics, or packaging repeatable Reddit research into a reusable skill.
---

# Reddit Research

Use this skill to turn Reddit into a repeatable signal pipeline.

## Workflow

1. **Discover**
   - Pull from target subreddits first.
   - Keep discovery broad enough to capture candidates, but narrow enough to avoid Reddit-wide noise.
   - Apply freshness and subreddit filters early.

2. **Filter**
   - Remove obvious junk before scoring.
   - Apply hard filters for job posts, irrelevant domains, avoid-list topics, and duplicates.

3. **Score**
   - Score candidates by brand fit, intent, capability match, and risk.
   - Keep brand-specific weights separate from shared rules.
   - Emit a reason trail for every score.

4. **Shortlist**
   - Select the best candidates after filtering.
   - Do not let raw top-score ranking bypass hard filters.

5. **Learn**
   - Record what converted, what was ignored, and what was false-positive noise.
   - Update brand profiles and weights from outcomes.
   - Prefer profile updates over ad hoc rule churn.

## Operating rules

- Keep discovery, scoring, and learning separate.
- Prefer brand-specific profiles over global heuristics.
- Explain every shortlist decision.
- Treat filters as safety rails, not the learning system.

## Resources

- `references/brand-profiles.md` — brand-specific behavior, weights, and profile shape
- `references/scoring-rules.md` — scoring dimensions and hard filter order
- `references/intent-patterns.md` — common Reddit intent buckets and signals
- `references/examples.md` — examples of good, bad, and borderline posts
- `scripts/discover.py` — discovery helper
- `scripts/score.py` — scoring and ranking helper
- `scripts/cleanup.py` — dedupe and inbox cleanup helper
- `scripts/report.py` — summary and reason-trail output helper
