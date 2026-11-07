"""Test: every internal link in docs/ resolves to a real file."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def find_problems():
    problems = []
    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            # internal relative links only (anchors to own page are fine)
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path_part = target.split("#")[0]
            if not path_part:
                continue  # same-page anchor like (#section)
            resolved = (md.parent / path_part).resolve()
            if not resolved.exists():
                problems.append(f"{md.relative_to(ROOT)} -> {target}")
    return problems


def test_all_internal_doc_links_resolve():
    assert find_problems() == []
