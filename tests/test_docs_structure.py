"""Test: project structure — every promised file exists and is substantive."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

CHAPTERS = [
    "00-start-here.md",
    "01-principles.md",
    "02-plan-your-year.md",
    "03-the-weekly-loop.md",
    "04-differentiated-worksheets.md",
    "05-fact-check-everything.md",
    "06-portfolios-and-logs.md",
    "07-state-paperwork.md",
    "08-privacy-and-local-ai.md",
    "09-low-energy-and-accommodations.md",
    "10-troubleshooting.md",
]

PROMPTS = [
    "year-plan.md",
    "weekly-plan.md",
    "worksheet-three-levels.md",
    "verification-pass.md",
    "rewrite-reading-level.md",
    "portfolio-summaries.md",
    "state-paperwork-assistant.md",
    "topic-rescue.md",
]

TEMPLATES = [
    "year-plan.md",
    "weekly-log.md",
    "portfolio-index.md",
    "state-paperwork-checklist.md",
    "accommodations-notes.md",
]


def test_top_level_files():
    for name in ["README.md", "LICENSE", "STATUS.md"]:
        assert (ROOT / name).is_file(), f"missing top-level file: {name}"


def test_chapters_exist_and_substantive():
    for name in CHAPTERS:
        p = DOCS / name
        assert p.is_file(), f"missing chapter: {name}"
        text = p.read_text(encoding="utf-8")
        # a real chapter is at least ~1500 chars of prose, not a stub
        assert len(text) > 1500, f"chapter too thin: {name}"
        assert text.startswith("# "), f"chapter has no H1 title: {name}"


def test_prompt_library_complete():
    for name in PROMPTS:
        p = DOCS / "prompts" / name
        assert p.is_file(), f"missing prompt: {name}"


def test_templates_complete():
    for name in TEMPLATES:
        p = DOCS / "templates" / name
        assert p.is_file(), f"missing template: {name}"


def test_every_chapter_opens_with_summary_and_scope():
    for name in CHAPTERS:
        text = (DOCS / name).read_text(encoding="utf-8")
        lines = text.splitlines()
        assert any(
            l.strip().startswith("*Summary:") or l.strip().startswith("*(Summary")
            for l in lines[:8]
        ), f"chapter missing one-line summary up top: {name}"


def test_prompts_contain_pasteable_block():
    for name in PROMPTS:
        text = (DOCS / "prompts" / name).read_text(encoding="utf-8")
        assert "Paste this prompt" in text, f"prompt missing paste block intro: {name}"
        assert text.count("```") >= 2, f"prompt missing fenced paste block: {name}"


def test_templates_are_fill_in():
    for name in TEMPLATES:
        text = (DOCS / "templates" / name).read_text(encoding="utf-8")
        assert "[" in text and "]" in text, f"template has no fill-ins: {name}"


def test_covered_goals_match_project_goal():
    """The five goal areas from the project brief each get a chapter that
    actually covers them (keyword-level sanity, not just file existence)."""
    checks = {
        "02-plan-your-year.md": ["36", "year plan"],
        "04-differentiated-worksheets.md": ["reading level"],
        "05-fact-check-everything.md": ["source"],
        "06-portfolios-and-logs.md": ["weekly log"],
        "07-state-paperwork.md": ["not legal advice", "department of education"],
    }
    for fname, words in checks.items():
        text = (DOCS / fname).read_text(encoding="utf-8").lower()
        for w in words:
            assert w in text, f"{fname} does not cover '{w}'"


def test_reader_distinction_documented():
    """README must state who this is for and how it differs from the sibling
    guides (classroom pack and one-on-one tutoring guide)."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    assert "free-teacher-ai-classroom-guide-pack" in readme
    assert "teach-a-friend-ai-guide" in readme

