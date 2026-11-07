# Differentiated Worksheets

*Summary: turn one lesson into three worksheets — below level, on level,
above level — in about 10 minutes with a structured prompt. Time to do:
10 minutes per lesson per subject per level.*

## The idea in one sentence

The same material, rendered at different reading levels, so a 7-year-old and a
12-year-old — or one confident reader and one dyslexic reader — can sit at one
table and work on one topic, each with a sheet that doesn't talk down to them
and doesn't overwhelm them.

## Reading levels, briefly

Grade levels are a shorthand, not a diagnosis. When you tell a model "3rd
grade reading level," it doesn't mean the label matches your kid. So the
prompt below works in **descriptors**, not grades — read these and pick by
word count and vocabulary complexity:

| Band you might say | Looks like | Typical features |
|---|---|---|
| Emerging reader | read-aloud, big font, short lines | 6–10 word sentences; one idea per line; no defining-vocabulary homework |
| Decoding comfortably | short instructions, familiar words | 10–14 word sentences; one style of question per section |
| Confident reader | full sentences, richer vocab | 14–20 word sentences; sequencing, why-questions |
| Advanced | dense text, inferential work | primary-source quotes, "compare," "evaluate" |

The rewrite model is *good* at this — better than most teachers have time
for — and *bad* at judging which band your kid is at, so that judgment stays
yours.

## The worksheet workflow

**Step 1.** Pick the lesson and the *same content* for all levels. If the
sheet is about why leaves change color, every kid answers questions about
leaves changing color — not different topics.

**Step 2.** Use the prompt in
[prompts/worksheet-three-levels.md](prompts/worksheet-three-levels.md). It
takes your lesson text, the number of questions, and the level descriptors,
and emits three worksheets plus a short note on *what changed* between them.
The note matters: you should be able to glance at it and know they're the
same lesson.

**Step 3.** Sanity-check each sheet:

- **Emerging reader sheet:** Is the vocabulary actually simple? Wrong-answer
  section still correct? (No "ambiguously right" answers.)
- **On level:** Does it ask real questions, not fill-in-the-blank trivia?
- **Above level:** Does it have an inferential question (why/compare), not
  just harder vocabulary with the same recall answer?

**Step 4.** Good worksheets need good **answer keys**. Ask the AI for one
simultaneously — it's the easiest add-on, and it's what your tired 5 p.m.
self will thank you for.

**Step 5 (single passages).** For one-off text — a paragraph from your
spine book, an explanation that landed badly, a letter for co-op adults
with mixed reading levels — use the rewrite prompt instead:
[prompts/rewrite-reading-level.md](prompts/rewrite-reading-level.md).
Same rules, one passage, plus a what-changed note you check against your
original.

## Formatting choices that matter more than they sound like they might

- **Font.** Larger font w/ sans-serif (Arial or Verdana or APHont) helps a
  lot for emerging and dyslexic readers. Sites have templates; print styles
  matter for worksheets you'll reuse.
- **White space.** Ask for "generous line spacing, no more than 5 questions
  per page" for the emerging band — the model tends to overpack.
- **Answer format variety.** Kids hate 12 blanks in a row. Ask for one
  drawing task, one matching, one short sentence — variety keeps attention.
- **Avoid handwriting-heavy tasks in the emerging band** unless writing IS
  the lesson goal. Oral answers, circling, matching, drawing.

## Ethics of AI-generated kid materials

Your kid's time is your kid's real cost. Every AI worksheet that reaches them
should have been either fact-checked (chapter 05) or been about opinion-free
process work (math operations with correct answers you've spot-checked,
handwriting, summarizing their own reading). This sounds heavy but is a quick
glance — and it protects against things like the wrong kinetic-molecular
explanation quietly becoming your false history of ice melting.

## Sibling-proofing

One trap: generated sheets sometimes reveal the answer in a sibling's sheet
level's wording. Ask, "check these three worksheets so no easy sheet contains
the exact phrasing that would be an answer on the harder sheet." Cheap to
request; the models catch most of it.

---

Next: [Chapter 05 — Fact-Check Everything](05-fact-check-everything.md)
