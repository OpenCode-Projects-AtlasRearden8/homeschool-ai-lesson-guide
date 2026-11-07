"""Tests for the docs -> HTML renderer and the generated static site."""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
SITE = ROOT / "site"
DOCS = ROOT / "docs"

sys.path.insert(0, str(TOOLS))
import build_site  # noqa: E402


# ---- renderer unit tests ------------------------------------------------

def test_headings_paragraphs_bold_italic_code():
    html = build_site.render_markdown("# Title\n\nSome **bold** and *em* text, `code run`.\n")
    assert "<h1>Title</h1>" in html
    assert "<strong>bold</strong>" in html
    assert "<em>em</em>" in html
    assert "<code>code run</code>" in html


def test_unordered_ordered_and_wrapped_list_items():
    md = "1. First item continues\n   across two lines.\n\n- a bullet\n"
    html = build_site.render_markdown(md)
    assert "<ol>" in html and "<ul>" in html
    m = re.search(r"<li>(.*?)</li>", html, re.S)
    assert m and "across two lines" in m.group(1)


def test_checkbox_tasks_render():
    md = "- [ ] task one\n- [x] task two\n"
    html = build_site.render_markdown(md)
    assert '<ul class="tasks">' in html
    assert html.count("<li") == 2


def test_pipe_table_renders():
    md = "| A | B |\n|---|---|\n| 1 | 2 |\n| 3 | 4 |\n"
    html = build_site.render_markdown(md)
    assert "<tr>" in html and "<td>1</td>" in html
    assert "|---|" not in html
    n_rows = html.count("<tr>")
    assert n_rows == 3  # header + 2 data rows


def test_fenced_code_block_escapes():
    md = "```\n<script>alert(1)</script>\n```\n"
    html = build_site.render_markdown(md)
    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;" in html


def test_internal_md_links_rewritten():
    md = "Read [three levels](04-chapter.md) now.\n"
    html = build_site.render_markdown(md)
    assert 'href="04-chapter.html"' in html
    assert '"' in html


# ---- full build ---------------------------------------------------------

def _run_build():
    result = subprocess.run(
        [sys.executable, str(TOOLS / "build_site.py")],
        capture_output=True, text=True, cwd=ROOT, timeout=120,
    )
    return result


def test_build_succeeds_and_generates_pages():
    result = _run_build()
    assert result.returncode == 0, result.stderr
    assert SITE.is_dir()
    pages = list(SITE.rglob("*.html"))
    assert len(pages) >= 25  # index + 11 chapters + 8 prompts + 5 templates
    assert (SITE / "index.html").is_file()
    assert (SITE / "styles.css").is_file()
    for name in ["prompts/year-plan.html", "templates/weekly-log.html",
                 "07-state-paperwork.html"]:
        assert (SITE / name).is_file(), f"missing generated page: {name}"


def test_site_pages_have_no_markdown_leftovers_or_placeholders():
    result = _run_build()
    assert result.returncode == 0
    for page in SITE.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        # no template placeholders
        assert "{{" not in text
        assert 'href="(' not in text
        # internal doc links must point at .html, not .md
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http:", "https:", "#")):
                continue
            assert not href.endswith(".md"), f"{page}: {href}"


def test_site_links_resolve_to_real_files():
    """Every relative href in generated pages resolves to a real site file."""
    result = _run_build()
    assert result.returncode == 0
    problems = []
    for page in SITE.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        for href in re.findall(r'href="([^"#]+)"', text):
            if href.startswith(("http:", "https:", "mailto:")):
                continue
            resolved = (page.parent / href).resolve()
            if not resolved.exists():
                problems.append(f"{page.relative_to(SITE)} -> {href}")
    assert problems == []


def test_site_carries_credit_and_not_legal_advice_notice():
    result = _run_build()
    assert result.returncode == 0
    index = (SITE / "index.html").read_text(encoding="utf-8")
    footer = (SITE / "07-state-paperwork.html").read_text(encoding="utf-8")
    assert "Asdale Dynamics, LLC" in index
    assert "never legal advice" in index.lower() or "without legal advice" in index.lower()
    assert "Asdale Dynamics, LLC" in footer
