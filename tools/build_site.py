#!/usr/bin/env python3
"""Build the static site from docs/ into site/.

Pure standard library, no dependencies. Converts the manual (Markdown,
restricted subset) into a small static HTML site with navigation, an index
page, and a warm stylesheet. Internal .md links are rewritten to .html links
and validated: the build fails on broken internal links rather than
shipping dead ones.

Usage:
    python3 tools/build_site.py
"""

import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

TITLE = "The Homeschool AI Lesson Guide"
FOOTER = (
    "The Homeschool AI Lesson Guide — by Asdale Dynamics, LLC. "
    "Educational information only; never legal advice. "
    "MIT licensed — see LICENSE."
)


# --------------------------------------------------------------------------
# Markdown -> HTML (restricted subset used by docs/: headings, paragraphs,
# emphasis + inline code, links, lists, checkbox tasks, pipe tables, fenced
# code blocks, blockquotes, horizontal rules).
# --------------------------------------------------------------------------

def _inline(text: str) -> str:
    """Inline markup for a chunk that is already outside another HTML tag."""
    codes = []

    def stash(m: re.Match) -> str:
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = text.replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", stash, text)
    text = re.sub(r"\*\*\*([^*]+)\*\*\*", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*`]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                  lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', text)
    text = re.sub(r"\x00(\d+)\x00",
                  lambda m: f"<code>{codes[int(m.group(1))]}</code>", text)
    return text


def _rewrite_md_links(chunk: str) -> str:
    return re.sub(r'href="([^"#]+?\.md)"', lambda m: f'href="{m.group(1)[:-3]}.html"', chunk)


def render_markdown(text: str) -> str:
    out = []
    lines = text.splitlines()
    i = 0
    list_stack = []
    table_rows = []
    in_table = False
    open_item = None  # index in `out` of an unclosed <li>

    HRR = re.compile(r"^\s*([-*_])\s*\1\s*\1[\s\-_]*$")

    def seal_item():
        nonlocal open_item
        if open_item is not None:
            out.append("</li>")
            open_item = None

    def close_lists():
        nonlocal open_item
        seal_item()
        while list_stack:
            out.append(f"</{list_stack.pop()}>")

    def close_table():
        nonlocal table_rows, in_table
        if not table_rows:
            in_table = False
            return
        seal_item()
        out.append("<table><thead><tr>")
        for cell in table_rows[0].strip().strip("|").split("|"):
            out.append(f"<th>{_inline(cell.strip())}</th>")
        out.append("</tr></thead><tbody>")
        for row in table_rows[2:]:
            out.append("<tr>")
            for cell in row.strip().strip("|").split("|"):
                out.append(f"<td>{_inline(cell.strip())}</td>")
            out.append("</tr>")
        out.append("</tbody></table>")
        table_rows, in_table = [], False

    def push_item(inline_html: str, i: int, cls: str = "") -> int:
        nonlocal open_item
        seal_item()
        out.append(f"<li{cls}>{inline_html}")
        open_item = len(out) - 1
        i += 1
        while i < len(lines) and is_continuation(lines[i]) and not lines[i].startswith("```"):
            out[open_item] += " " + _inline(lines[i].strip())
            i += 1
        return i

    def is_continuation(s: str) -> bool:
        stripped = s.strip()
        if not s.startswith(" ") or not stripped:
            return False
        if re.match(r"^([-*]|\d+[.)])\s", stripped):
            return False
        if stripped[0] in "#>|*":
            return False
        if stripped.startswith("```"):
            return False
        return True

    para_re = re.compile(
        r"^(\s*$|#{1,4}\s|>\s?|```|\s*[-*]\s|\s*\d+[.)]\s|\s*\||\s*([-*_])\s*\2\s*\2)"
    )

    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            close_lists()
            close_table()
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
            continue

        sep_next = i + 1 < len(lines) and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1])
        if line.strip().startswith("|") and sep_next:
            if not in_table:
                close_lists()
                in_table = True
            table_rows.append(line)
            i += 1
            continue
        elif in_table:
            if line.strip().startswith("|"):
                table_rows.append(line)
                i += 1
                continue
            close_table()

        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            close_lists()
            level, content = len(m.group(1)), m.group(2).strip()
            out.append(f"<h{level}>{_inline(content)}</h{level}>")
            i += 1
            continue

        if HRR.match(line):
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        if line.strip().startswith(">"):
            close_lists()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(
                "<blockquote><p>"
                + _inline(" ".join(q for q in quote if q))
                + "</p></blockquote>"
            )
            continue

        m = re.match(r"^\s*-\s+\[([ xX])\]\s+(.*)$", line)
        if m:
            if list_stack and list_stack[-1] != "ul":
                close_lists()
            if not list_stack:
                list_stack.append("ul")
                out.append('<ul class="tasks">')
            i = push_item(_inline(m.group(2)), i, ' class="task"')
            continue

        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            if list_stack and list_stack[-1] != "ul":
                close_lists()
            if not list_stack:
                list_stack.append("ul")
                out.append("<ul>")
            i = push_item(_inline(m.group(1)), i)
            continue

        m = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        if m:
            if list_stack and list_stack[-1] != "ol":
                close_lists()
            if not list_stack:
                list_stack.append("ol")
                out.append("<ol>")
            i = push_item(_inline(m.group(1)), i)
            continue

        if not line.strip():
            close_lists()
            close_table()
            i += 1
            continue

        words = [line.strip()]
        i += 1
        while i < len(lines) and not para_re.match(lines[i]):
            words.append(lines[i].strip())
            i += 1
        close_lists()
        close_table()
        out.append(f"<p>{_inline(' '.join(words))}</p>")

    close_lists()
    close_table()
    return _rewrite_md_links("\n".join(out))


def extract_title_star(md_text: str):
    title, summary = None, None
    lines = md_text.splitlines()
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if title is None and line.startswith("# "):
            title = line[2:].strip()
        if summary is None and len(stripped) > 2 and stripped.startswith("*") \
                and not stripped.startswith("**"):
            buf = [stripped.lstrip("*")]
            j = idx
            while j + 1 < len(lines) and not buf[-1].endswith("*") and j - idx < 6:
                j += 1
                buf.append(lines[j].strip())
            joined = " ".join(buf).rstrip()
            if joined.endswith("*"):
                summary = joined[:-1].strip()
                if summary.startswith("Summary: "):
                    summary = summary[len("Summary: "):]
    return title or "Untitled", summary or ""


GROUPS = [("Manual", "."), ("prompts", "prompts"), ("templates", "templates")]


def collect_pages():
    pages = []
    for group, sub in GROUPS:
        src_dir = DOCS if sub == "." else DOCS / sub
        for md_path in sorted(src_dir.glob("*.md")):
            if md_path.name.lower() == "readme.md":
                continue
            slug = md_path.relative_to(DOCS).with_suffix("").as_posix()
            title, summary = extract_title_star(md_path.read_text(encoding="utf-8"))
            pages.append({
                "src": md_path, "slug": slug, "title": title,
                "summary": summary, "group": group,
            })
    return pages


def nav_links(pages, root_prefix, active_slug):
    parts = []
    current_group = None
    for p in pages:
        if p["group"] != current_group:
            current_group = p["group"]
            label = "The manual" if current_group == "Manual" else current_group.capitalize()
            parts.append(f'<h2 class="navhead">{label}</h2>')
        cls = ' class="active"' if p["slug"] == active_slug else ""
        href = root_prefix + p["slug"] + ".html"
        parts.append(f'<a href="{href}"{cls}>{html.escape(p["title"])}</a>')
    return "\n".join(parts)


def shell(title, body, pages, active_slug, root_prefix):
    href = root_prefix + "index.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — {TITLE}</title>
<link rel="stylesheet" href="{root_prefix}styles.css">
</head>
<body>
<div class="layout">
<nav class="sidebar" aria-label="Chapters">
  <div class="brand"><a href="{href}">{TITLE}</a></div>
  {nav_links(pages, root_prefix, active_slug)}
</nav>
<main class="content">
{body}
<footer class="site-footer">{FOOTER}</footer>
</main>
</div>
</body>
</html>
"""


def listing(pages, heading):
    parts = [f"<h2>{heading}</h2>", '<ul class="toc">']
    for p in pages:
        sub = (
            f'<span class="sub">{html.escape(p["summary"])}</span>' if p["summary"] else ""
        )
        parts.append(f'<li><a href="{p["slug"]}.html">{html.escape(p["title"])}</a>{sub}</li>')
    parts.append("</ul>")
    return "\n".join(parts)


def build() -> int:
    if not DOCS.exists():
        print(f"error: {DOCS} not found", file=sys.stderr)
        return 1
    pages = collect_pages()
    if not pages:
        print("error: no docs pages found", file=sys.stderr)
        return 1

    if SITE.exists():
        shutil.rmtree(SITE)
    for p in pages:
        (SITE / p["slug"]).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "tools" / "site.css", SITE / "styles.css")

    # Pages grouped for the index and the sidebar order (manual first).
    pages.sort(key=lambda p: ({"Manual": 0, "prompts": 1, "templates": 2}[p["group"]], p["src"].name))

    broken = []
    for p in pages:
        text = p["src"].read_text(encoding="utf-8")
        body = render_markdown(text)
        for link in re.findall(r'href="(\.\.?/[^"#]*?\.md)"', body):
            if not (p["src"].parent / link).resolve().exists():
                broken.append(f'{p["slug"]}.md -> {link}')

    if broken:
        print("BROKEN LINKS:", file=sys.stderr)
        for b in sorted(set(broken)):
            print("  " + b, file=sys.stderr)
        return 1

    # Index page
    manual = [p for p in pages if p["group"] == "Manual"]
    prompts = [p for p in pages if p["group"] == "prompts"]
    templates = [p for p in pages if p["group"] == "templates"]
    lead = manual[0]["summary"] if manual else ""
    lead_html = f'<p class="lead">{html.escape(lead)}</p>' if lead else ""
    index_body = (
        "<h1>The Homeschool AI Lesson Guide</h1>"
        + lead_html
        + "<p>A plain-English manual for parent-teachers: plan a year of lessons with "
        "AI as co-planner, generate differentiated worksheets at reading levels, "
        "fact-check everything, keep portfolios and logs, and find your state's "
        "homeschooling paperwork requirements — <strong>without legal advice</strong>. "
        "Warm, never condescending, local-first.</p>"
        "<p>This is the <em>parent-teacher running a full year at home</em> guide, "
        "deliberately distinct from the classroom-teacher pack and the one-on-one "
        "tutoring guide in the same family of AI guides from Asdale Dynamics, LLC.</p>"
        + listing(manual, "The manual")
        + listing(prompts, "Prompt library — copy, paste, edit")
        + listing(templates, "Templates — copy into your records folder")
    )
    (SITE / "index.html").write_text(
        shell("Home", index_body, pages, "__index__", ""), encoding="utf-8"
    )

    # Doc pages
    for p in pages:
        text = p["src"].read_text(encoding="utf-8")
        body = render_markdown(text)
        # Page lives at site/<slug>.html (deeper for subdirs); the prefix
        # climbs back up to site/ for stylesheet, sidebar, and index links.
        root_prefix = "../" * p["slug"].count("/")
        (SITE / (p["slug"] + ".html")).write_text(
            shell(p["title"], body, pages, p["slug"], root_prefix), encoding="utf-8"
        )

    total = len(pages) + 1
    print(f"Built {total} pages into site/ (index + {len(pages)} doc pages).")
    return 0


if __name__ == "__main__":
    sys.exit(build())
