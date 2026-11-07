# The Homeschool AI Lesson Guide

*A plain-English manual for parent-teachers who want to plan a full year of lessons
with AI as their co-planner — and keep their own judgment in the driver's seat.*

**By Asdale Dynamics, LLC** · Dylan Asdale's book *The Massive AI Manual* and the hub
at dylanasdale.github.io explain AI "like a friend would": plain English, step by
step, never condescending. This guide keeps that promise.

---

## What this is

This project is two things at once:

1. **A substantive manual** (`docs/`, written in Markdown) covering the whole
   homeschooling-with-AI workflow:
   - planning a **year of lessons** with AI as co-planner
   - generating **differentiated worksheets** at different reading levels
   - **fact-checking** everything the model tells you
   - keeping **portfolios and logs** (for you, and for any state requirement)
   - checking your **state's paperwork requirements** — *informationally, never legal advice*
2. **A static HTML site** generated from those same docs by a tiny, dependency-free
   Python script — open it from disk, no server, no accounts, no telemetry.

Nothing here requires an account, an API key, or an internet connection beyond
whatever AI tool you already use. Local-first by design.

## Who this is for

**Parent-teachers** — the person wearing both hats in your kitchen on a Tuesday
morning. It is deliberately *not* the same product as its sibling guides:

| Guide | Audience | Shape |
|---|---|---|
| `free-teacher-ai-classroom-guide-pack` | Classroom teachers (25–30 students, standards, admin) | Pack of classroom tools |
| `teach-a-friend-ai-guide` | Anyone tutoring one person, one subject, casually | Short single-topic guide |
| **this project** | **Homeschool parent-teachers running a full year at home** | **Year-shaped manual + worksheets + records + state paperwork checklist** |

If you've been handed lesson-plan formats written for a public-school classroom,
this is the guide that finally uses your words: **year plan, week loop, portfolio,
reading levels, annual assessment** — not bell schedules and seating charts.

## How to use it

```bash
# read the manual (any order, but start with Start Here)
open docs/00-start-here.md

# build the static site into site/
python3 tools/build_site.py

# then open the generated site from disk
open site/index.html            # or xdg-open / double-click it

# run the test suite (pytest)
python3 -m pytest -q
```

Requirements: **Python 3.9+** and nothing else. `pytest` only if you want to
run the tests. No installs into your machine's Python config beyond that.

## What's inside

```
docs/
  00-start-here.md              start here, seriously
  01-principles.md              the philosophy: you're the teacher, AI's the aide
  02-plan-your-year.md          building a 36-week year plan with a model
  03-the-weekly-loop.md         the repeatable Sunday-evening routine
  04-differentiated-worksheets.md  same lesson, three reading levels
  05-fact-check-everything.md       verifying AI content without burning out
  06-portfolios-and-logs.md     records that survive a skeptical audit
  07-state-paperwork.md         finding your state's rules (not legal advice)
  08-privacy-and-local-ai.md    keeping your family's data yours, offline options
  09-low-energy-and-accommodations.md ADHD-friendly, low-spoons schooling
  10-troubleshooting.md         when it's generating nonsense at you
  prompts/                      copy-paste prompt library (8 tested prompts)
  templates/                    fill-in templates (year plan, logs, portfolio, …)
site/                           generated static site (from docs/)
tests/                          pytest suite that keeps all of it honest
tools/build_site.py             one-file stdlib docs→HTML renderer
```

## What this is not

- **Not legal advice.** Chapter 07 shows you *how to look up* your own state's
  requirements on official sources. It never states your requirements for you.
- **Not a curriculum.** It's a planning system. You pick the curriculum; this makes
  the year around it manageable.
- **Not a product with servers.** No API, no logins, no analytics. Your records
  stay in your own files, and the fact-checking chapter treats that as a feature.
- **Not a lecture.** The tone stays warm and anti-condescending — the test suite
  literally checks the docs for sneering phrases so the voice never drifts into
  talking down to you.

## Verification

```bash
python3 -m pytest -q           # structure, links, templates, prompts, site build
python3 tools/build_site.py    # regenerate site/; exits non-zero on bad links
```

## License & credit

MIT — see `LICENSE`. **Copyright (c) 2026 Asdale Dynamics, LLC.**
Written by Dylan Asdale for parent-teachers. Companion to *The Massive AI Manual*
and the sibling guides named above.
