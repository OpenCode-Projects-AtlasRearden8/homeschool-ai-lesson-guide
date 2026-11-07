"""Tone + safety tests: warm anti-condescending voice, no legal advice, no
secrets or personal data, license and credit lines exactly right."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
README = ROOT / "README.md"
LICENSE = ROOT / "LICENSE"

# Phrases that would mean the writing started sneering at the reader.
# (file, substring) triples are known good uses — quoted examples of what
# NOT to say, in meta-commentary about tone.
SNEERS = [
    r"(?i)\bdumb\b",
    r"(?i)\bstupid\b",
    r"(?i)\bas anyone knows\b",
    r"(?i)\bit'?s easy[,!.]",
    r"(?i)\bsimply (use|click|type|do|choose)\b",
    r"(?i)\bdo this yourself[,\.]?\b",
    r"(?i)\byou obviously\b",
]
ALLOWED = [
    ("00-start-here.md", 'say "well, simply open the settings"'),  # quoted bad example
    ("01-principles.md", 'stopping just short of "dearie."'),       # quoted bad example
]


def test_docs_never_sneer():
    problems = []
    for md in list(DOCS.rglob("*.md")) + [README]:
        rel = md.relative_to(ROOT).as_posix()
        text = md.read_text(encoding="utf-8")
        for pattern in SNEERS:
            for m in re.finditer(pattern, text):
                if any(rel.endswith(fname) and frag in text
                       for fname, frag in ALLOWED):
                    continue
                start = max(0, m.start() - 50)
                problems.append(f"{rel}: ...{text[start:m.end() + 50]!r}...")
    assert problems == [], "\n".join(problems)


def test_state_paperwork_chapter_is_informational_only():
    text = (DOCS / "07-state-paperwork.md").read_text(encoding="utf-8")
    assert "not legal advice" in text.lower()
    assert "department of education" in text.lower()
    # the chapter must never hand out a state-specific requirement
    assert "you must file with" not in text.lower()
    assert "here's what your state requires" not in text.lower()


def test_no_secrets_or_keys_anywhere():
    patterns = [
        r"sk-[A-Za-z0-9]{8,}",        # openai-style keys
        r"AKIA[0-9A-Z]{12,}",          # aws access keys
        r"(?i)api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{8,}",
        r"(?i)password\s*[:=]\s*['\"]\S{6,}",
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        r"(?i)\b\d{3}-\d{2}-\d{4}\b",  # SSN-shaped data
    ]
    for f in ROOT.rglob("*"):
        if any(s in f.as_posix() for s in ["/.git/", "/site/", "__pycache__"]) \
                or not f.is_file():
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pattern in patterns:
            assert re.search(pattern, text) is None, f"{f} matches {pattern}"


def test_no_placeholder_personal_data_in_examples():
    """The docs' example kids use descriptors, and real-looking personal data
    (full names with surnames, addresses) must not appear in examples."""
    banned = [
        r"Asdale Jr\.?", r"Dylan's daughter", r"@gmail\.com",
        r"\d+ [A-Z][a-z]+ (Street|Avenue|Lane|Rd\.|St\.|Ave\.|Main Street)",
    ]
    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for pattern in banned:
            assert re.search(pattern, text) is None, \
                f"{md.name} contains placeholder personal data: {pattern}"


def test_license_exact():
    text = LICENSE.read_text(encoding="utf-8")
    assert "MIT License" in text
    assert "Copyright (c) 2026 Asdale Dynamics, LLC" in text
    # exact line, no leading decoration
    assert any(
        line.strip() == "Copyright (c) 2026 Asdale Dynamics, LLC"
        for line in text.splitlines()
    )


def test_readme_credits_and_positions_the_guide():
    text = README.read_text(encoding="utf-8")
    assert "Asdale Dynamics, LLC" in text
    assert "Dylan Asdale" in text
    assert "parent-teacher" in text.lower()
    lower = text.lower()
    assert "not legal advice" in lower


def test_docs_have_no_orphan_pages():
    """Every doc page must either link to another doc page or be linked
    from one, so nobody lands on a dead end."""
    files = sorted(DOCS.rglob("*.md"))
    names = {f.name for f in files}
    link_re = re.compile(r"\]\(([^)]+)\)")
    referenced = set()
    outlinks = {}
    for f in files:
        targets = set()
        for m in link_re.finditer(f.read_text(encoding="utf-8")):
            base = m.group(1).split("/")[-1]
            if base in names:
                targets.add(base)
                referenced.add(base)
        outlinks[f.name] = targets
    orphans = [n for n, t in outlinks.items()
               if not t and n not in referenced]
    assert orphans == [], f"orphan pages: {orphans}"
