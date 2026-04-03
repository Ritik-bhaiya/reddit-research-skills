# Reddit Research Skills

A brand-aware Reddit research workflow for finding useful posts and comments, ranking them by relevance, and learning from outcomes in a lightweight feedback loop.

This repo is for people who want a practical way to:
- discover Reddit opportunities for a brand
- score and shortlist useful threads
- track results in a structured way
- improve the system over time from saved and irrelevant items

## What it includes

### `reddit-research`
A workflow for discovering, scoring, shortlisting, and learning from Reddit opportunities.

### Live discovery demo
- `skills/reddit-research/scripts/discover_live.py` — fetches live Reddit posts from target subreddits and search queries, then ranks them.

### Demo profile
- `brands/sample-marketing.json` — a dummy freelancer/agency profile for testing the workflow without exposing real brand data.

## Who this is for

- developers building brand research workflows
- people tracking Reddit leads manually or semi-automatically
- anyone who wants a repeatable Reddit research pipeline
- teams that want a simple, auditable feedback loop

## How it works

1. Discover Reddit items.
2. Score them for relevance and timing.
3. Shortlist the best ones.
4. Log the result.
5. Learn from feedback.

## Why this exists

Reddit can be a strong signal source, but only if you can separate:
- useful opportunities
- irrelevant noise
- low-quality or forced promotion

This project makes that process repeatable.

## Example output

Using the dummy profile `Sample Marketing`:

- **Task**: Comment
- **Task URL**: `https://www.reddit.com/r/example/comments/abc123/sample_post/`
- **User_name**: `u/sample_user`
- **Status**: `live`
- **Feedback**: `strong fit for agency-style outreach`
- **Report**: `useful lead for freelancer/marketing workflow`

This example is fake on purpose so no real brand data is exposed.

## Quick start

### Install

```bash
pip install -r requirements.txt
```

### Run discovery

```bash
python skills/reddit-research/scripts/discover.py
```

### Run scoring

```bash
python skills/reddit-research/scripts/score.py
```

### Read output

```bash
python skills/reddit-research/scripts/report.py
```

### Run the dummy marketing demo

```bash
python skills/reddit-research/scripts/demo_sample.py
```

## Limitations

- This is not a magic bot.
- It is not fully autonomous.
- Results depend on source quality.
- Human judgment still matters.

## Design principles

- **Brand-specific profiles** — each brand gets its own keywords, competitors, subreddits, and scoring rules.
- **Feedback loop** — outcomes improve future runs.
- **Human-in-the-loop** — items are analyzed before they are stored or acted on.
- **Reusable workflow** — the same process can be reused for multiple brands.

## Example use cases

- Track Reddit leads for one brand.
- Compare which subreddits produce useful comments.
- Save successful comment angles for later reuse.
- Separate brand-specific learning histories.
- Use a dummy profile like `Sample Marketing` to test the workflow without exposing real brand data.

## Repository health

This public repository includes:
- a clear README
- a license
- contribution guidelines
- a code of conduct
- security reporting guidance
- a `.gitignore`

Recommended GitHub settings:
- enable Dependabot alerts
- enable secret scanning
- enable push protection
- enable code scanning where applicable

## Public-safe note

This project is published in a privacy-safe form. It intentionally excludes:

- private Google Sheet links
- internal usernames
- credentials or tokens
- raw lead lists
- private brand notes

## Repository layout

```text
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
.gitignore
brands/
  sample-marketing.json
skills/
  reddit-research/
    SKILL.md
    scripts/
      discover.py
      discover_live.py
      score.py
      cleanup.py
      report.py
      demo_sample.py
      _shared.py
    references/
      brand-profiles.md
      scoring-rules.md
      intent-patterns.md
      examples.md
```

## License

MIT
