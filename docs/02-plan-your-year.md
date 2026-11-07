# Plan Your Year

*Summary: build a 36-week plan from your subject list, your curriculum, and
your real constraints — using the AI as a structuring partner, not an oracle.
Time to do: about 60–90 minutes, once per year.*

## What a year plan is (and isn't)

A year plan is a map at the week level. Not day-by-day — that's the weekly
loop's job (chapter 03). It answers: which topics, roughly which weeks, where
the natural break points are, and where the padding goes when life happens.

It does *not* answer what your state requires. Do that lookup first — chapter
07 — because some states require specific hours, subjects, or assessments, and
your year plan should inherit those constraints from the start.

## Before you prompt: gather five facts

Write these down in a scratch note (or the year plan template). These are the
"constraints" every good prompt in this guide assumes you gather first:

1. **Kids and rough levels.** For each: age/grade-ish level and one thing you
   want them to gain this year. Use ordinal descriptions ("reading
   confidently at 3rd-grade level, resistant writer").
2. **Subject list.** Both required-by-state and chosen-by-you. Separate them;
   some states require certain subjects explicitly.
3. **Curriculum anchors.** What you already own or chose — e.g., "Saxon Math
   4", "Story of the World Vol. 2", library-based science.
4. **Your calendar reality.** Start date, holiday weeks, travel weeks, chairs —
   er, seasons you know are bad (post-illness, family emergencies). Add buffer
   weeks *on purpose*, at the end and mid-year.
5. **Your energy pattern.** When do you plan? When are your kids sharp?
   Morning-deep or afternoon-shallow matters for schedule shape.

## The year-plan prompt

The prompt library has the full version (see
[prompts/year-plan.md](prompts/year-plan.md)). The shape, in one paragraph:

Give the model each of the five facts above, then ask for a **week-by-week
table with 36 rows**: week number, focus topic per subject, milestones, and
buffer/assessment weeks marked. Then — this is the part people skip — ask it
to **identify risks**: "which weeks look unrealistic for a sick day plus a
toddler?" and to **propose two alternative shapes** (front-loaded vs.
spray-across-the-year), so you pick a shape rather than accept the first one.

## What a good result looks like

- 36 rows, one per week, with one focus topic per subject per week
- Real break weeks marked and *honorable* — not crumbs at the end
- Assessment or portfolio weeks marked for those states and for chapter 06
- A short risks section the model actually flagged (e.g., "weeks 18–19 fall
  during winter illness season — consider lighter load")
- Subjects your state requires, present every week they should be

## What to fix by hand, every time

The model doesn't know these things; *you* do, so edit them in:

- **Readers' pace.** If your kid reads slower than a syllabus assumes, stretch
  the reading plan across more weeks. Weeks are cheap to move in the plan.
- **Bad calendar weeks.** You know your family's rhythms; the model knows only
  what you typed.
- **Volume.** If a week has three major lessons in four subjects, something is
  wrong for most real kids. Cut it in half. Cutting is easier than catching up.

## Common failure to sidestep

The classic model answer is "180 days, 4 quarters, evenly split." Evenly split
is *plausible*, not *good*. If you get that shape, ask it to redo it in the
shape you actually picked (front-loaded science, seasonal history units, etc.).
A second pass with explicit constraints is where plans stop looking generated.

## Handoff to the weekly loop

Once the year plan exists in your own folder (Save it as
`year-plan.md` from the template — never only inside a chat browser), each
week's work is small. Open your plan, find next week's row, and pull this
week's *detail* using the weekly loop in chapter 03. The plan never tells you
*how* to teach Wednesday; it just makes sure Wednesday has a purpose.

---

Next: [Chapter 03 — The Weekly Loop](03-the-weekly-loop.md)
