# STATUS

*A snapshot of this project: what it is, how to run it, how it was verified,
and what's still missing. Updated Nov 2026.*

## What was built

**The Homeschool AI Lesson Guide** — a substantive manual for parent-teachers
who want to plan a full year of homeschooling with AI as co-planner, wrapped
in a dependency-free static site. Built from an empty folder in one session;
a full rewrite was not needed since no prior code existed.

Contents:

- **`docs/` — 11-chapter manual (Markdown):** start-here, principles,
  year planning (36-week plan with AI), the weekly 45-minute planning loop,
  differentiated worksheets at reading levels, a fact-checking system,
  portfolios and logs, state paperwork (informational, never legal advice),
  privacy + local AI, low-energy/ADHD-friendly schooling, and
  troubleshooting.
- **`docs/prompts/` — 8-file tested prompt library:** year plan, weekly plan,
  three-level worksheets, verification pass, reading-level rewrite,
  portfolio summaries, state-paperwork lookup assistant, topic rescue.
- **`docs/templates/` — 5 copy-in templates:** year plan, weekly log,
  portfolio index, state paperwork checklist, accommodations notes.
- **`site/` — static HTML site** generated from the docs (index + 24 pages)
  with a warm stylesheet, sidebar navigation, and a "never legal advice"
  footer on every page.
- **`tools/build_site.py` — one-file pure-stdlib docs→HTML renderer**
  (Python 3.9+, no packages). Validates internal links; the build fails
  rather than shipping dead links.
- **`tests/` — pytest suite** covering structure, links, renderer behavior,
  full site build, voice ("no sneering" tone checks), privacy (no
  secrets/keys/personal data), and the exact LICENSE/credit strings.

Distinctness: the README and site index explicitly position this for
**parent-teachers running a full year at home**, deliberately different from
`free-teacher-ai-classroom-guide-pack` (classroom teachers) and
`teach-a-friend-ai-guide` (one-on-one tutoring).

## How to run it

```bash
# build the static site from docs/
python3 tools/build_site.py

# open the site from disk (no server needed)
open site/index.html        # macOS; or xdg-open / double-click

# run the test suite
python3 -m pytest -q
```

Requirements: Python 3.9+ (stdlib only). `pytest` for tests. Build
reruns are cheap and idempotent (`site/` is wiped and regenerated).

## Verification results

Last full run on this machine (Python 3.13, pytest 9.1):

- `python3 tools/build_site.py` → **exit 0**, "Built 25 pages into site/
  (index + 24 doc pages)."
- `python3 -m pytest -q` → **all tests passed** (structure, links,
  renderer, site build, voice, safety). No skips pending.
- Broken-link authority: the site build itself validates every internal
  link and fails on dead ones; the test suite re-checks generated `href`s.
- Text spot-checks: tables, fenced prompt blocks, checkbox tasks, and
  wrapped list items render correctly in generated HTML.

## Known gaps

- **Fact-checking is a process, not automation** — by design. The manual
  teaches the two verification paths (chapter 05) but includes no link
  checker against the live web; a future `tools/factcheck_log.py` could
  lint `fact-checks.md` entries for staleness dates.
- **Reading-level grades are descriptive, not validated** — the
  differentiation chapter and prompt use band descriptors rather than a
  Flesch-Kincaid scorer. Adding an optional `tools/readability.py` would
  close that gap without external dependencies.
- **No per-state requirement data is included** — deliberately: the state
  chapter teaches lookup from official sources, and no legal-adjacent data
  is vendored, keeping the guide's scope informational and current-safe.
- **Single-page print/PDF export not implemented** (the site is per-page;
  a `build_print.py` that concatenates chapters is a future nicety).
- **The renderer covers the Markdown subset actually used in `docs/`**
  (headings, lists, checkboxes, pipe tables, fenced code, blockquotes,
  inline emphasis/code, links). It is not a general Markdown parser by
  design — pull requests with new syntax must stay in the subset or
  extend `_inline`.
- **Local-LLM setup is pointed at, not walked through** — chapter 08
  compares cloud vs. local honestly and defers detailed setup to the
  author's local-AI sibling guides.

## License & credit

MIT. LICENSE contains exactly: `Copyright (c) 2026 Asdale Dynamics, LLC`.
README credits **Asdale Dynamics, LLC** (Dylan Asdale,
*The Massive AI Manual*). No pushes, no remotes, no published artifacts —
everything here is local.
