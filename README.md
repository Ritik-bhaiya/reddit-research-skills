# Reddit Research Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![GitHub Repo](https://img.shields.io/badge/Repo-Reddit%20Research%20Skills-lightgrey.svg)]()

A brand-aware Reddit research workflow for discovering, scoring, shortlisting, and learning from Reddit posts and comments.

## What it does

- discovers Reddit posts/comments for a target brand
- scores items for relevance and timing
- produces shortlists of useful opportunities
- learns from saved / irrelevant / successful items
- keeps the workflow human-in-the-loop

## Skills

### `reddit-research`
Find, score, shortlist, and learn from Reddit opportunities.

## Core workflow

1. Discover Reddit items.
2. Score and shortlist.
3. Log the outcome.
4. Learn from feedback.

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


## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the discovery and scoring workflow from the `reddit-research` skill files.

Typical flow:

```bash
python skills/reddit-research/scripts/discover.py
python skills/reddit-research/scripts/score.py
python skills/reddit-research/scripts/report.py
```

## Repository layout

```text
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
.gitignore
skills/
  reddit-research/
    SKILL.md
    scripts/
      discover.py
      score.py
      cleanup.py
      report.py
      _shared.py
    references/
      brand-profiles.md
      scoring-rules.md
      intent-patterns.md
      examples.md
```

## Repository health

This public repository should include:
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

## License

MIT
