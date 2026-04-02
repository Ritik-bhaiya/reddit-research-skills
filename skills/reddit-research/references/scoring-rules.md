# Scoring Rules

## Order of operations
1. Normalize text
2. Apply hard filters
3. Deduplicate
4. Score brand fit
5. Score intent
6. Score capability match
7. Subtract risk penalties
8. Rank and shortlist

## Hard filters
- job posts
- recruitment ads
- explicit avoid-list topics
- irrelevant communities
- duplicates
- stale posts outside freshness window

## Output
Each scored item should include:
- final score
- sub-scores
- reasons
- filter flags
