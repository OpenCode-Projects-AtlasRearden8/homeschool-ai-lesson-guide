# Troubleshooting

*Summary: the ten failure patterns you'll actually hit, and the fastest
honest fix for each. Bookmark this one.*

## 1. "Everything it generates sounds the same"

Generic output is a context problem, not a model problem. Your prompt needs
three more specifics it doesn't have: your kid's actual interests, the
materials you own, and a length constraint. "Use my kids' current obsession
(nail polish/forestry/Bluey) as an example in at least one item" works
shockingly well.

## 2. "It keeps giving me classroom-seat-time plans"

Because most of its training data is classroom. Correct it once, explicitly:
"In our home school we do 3 hours a day, mixed ages at one table, no
transitions, no 25-student group work." The model adapts immediately — this
is a one-paragraph fix per prompt, or saved as a "preamble" you reuse (the
prompt library files in [prompts/](prompts/) each contain one ready-made).

## 3. "A fact on today's worksheet is wrong"

Good catch — that's chapter 05 doing its job. Fix the sheet, and *write the
correction in your `fact-checks.md` with the correct date/name*, so the
fixed version gets used next time you regenerate the unit.

## 4. "The reading level came out wrong — too hard"

Two reliable moves: (1) ask for shorter sentences and 100 fewer unique
words; (2) ask it to "explain the same content to someone reading it aloud
to a listener who can stop and ask questions." Reading level is measurable;
ask the model to report its sentence-length average if it can, and compare
against your kid's real tolerance.

## 5. "My kid names it 'Siri-for-school' and refuses"

Rebrand. The AI is your planning tool, not an in-lesson presence. If your
kid does interact with it (asking questions), set rules like "AI is for
finding sources, then we check them" — that habit *is* chapter 05, taught
early, and it's a genuinely good life skill.

## 6. "I fell a whole unit behind"

Chapter 03's slide-the-plan move, done once, is fifteen minutes and fixes
the vibe immediately. Do *not* try to double-up lessons to "catch up" —
doubling is how plans die in winter. If behind by a lot, use the AI to
compress: "here's the rest of this unit's plan and my honest remaining
weeks; propose what to cut and what to keep."

## 7. "It wrote a worksheet whose answer key is wrong"

This happens with generated math word problems more than anyone admits.
Spot-check keys before Monday when the topic is arithmetic; if the key is
wrong, fix it yourself, log it in fact-checks.md, and consider regenerating
the whole sheet — broken keys mean the model was confused the whole way
through.

## 8. "My records folder is chaos"

One-time triage day (30 min): archive everything not current into an
`archive-YYYY/` subfolder; keep this year's `records/2026-2027/` clean. Then
make the ritual stricter: Move 4 of the weekly loop exists precisely so
chaos can't re-form. If paperwork from the state is mixed in, chapter 06's
correspondence folder is its home.

## 9. "I'm drowning in open browser tabs with lesson ideas"

Give tabs to the AI: "for each link I paste, summarize in one sentence and
file under subject." Then close the tabs. Lessons don't need to live in
tabs; they need to live in your weekly loop's queue. Ten pasted links,
ten sentences, one organized note, tabs closed, sleep.

## 10. "I don't trust any of it anymore"

Totally normal, and chapter 05's triage table is built exactly for the
aftermath of discovering an error. The trust calibration to aim for: use
generated material freely for *structure* (outlines, instructions, formats,
prompts-for-self) and treat every *fact* as a rumor until you've seen a
source. That calibration is what the whole guide teaches — and after a
month it's as automatic as checking a receipt.

## Still stuck?

- Re-read the chapter for the area that's failing — each one ends with its
  failure *and* its fix built in.
- Check the prompt you actually pasted. Most "the AI can't do this"
  moments are "the prompt had no context" moments.
- The issues page of this project's repository exists for guide bugs;
  real classroom additions are welcome.

---

Back to [Start Here](00-start-here.md)
