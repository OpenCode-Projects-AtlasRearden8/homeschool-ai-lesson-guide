# Fact-Check Everything

*Summary: AI-generated text is confident even when wrong. Here's a 5-minute
per-lesson verification routine that catches almost everything, without
turning you into a full-time editor. Time to do: 5 minutes per lesson.*

## Why this chapter exists

A model will write "Harriet Tubman developed over 300 varieties of peanuts"
with the same calm sentence rhythm it uses for true things. Trusting prose
rhythm is the number-one way AI errors leak into homeschool materials —
because an unverified, confidently-written fact *looks* like every verified
fact. And once it's on a worksheet, it becomes "what my mom taught me."

Two facts about the error pattern worth knowing up front:

1. Models are **worse at specifics** (dates, numbers, names, quotes, statistics)
   than at processes and general concepts. "Why rain forms" reasoning is
   usually solid; the year the Kansas-Nebraska Act passed is a coin flip.
2. Errors **compound in generated material.** If the model hallucinates early
   ("Tubman, born in 1720..."), everything after is built on it. Catch errors
   at generation time, not at dinner when your kid repeats them at Grammy's.

## The triage table: what must be verified

Not everything needs the same care.

| Content type | Verify? | How fast |
|---|---|---|
| Math arithmetic, steps ("how to regroup in column addition") | Do the problems yourself | 30 sec |
| Names, dates, inventions ("who invented the printing press") | **Always** | Book or 2 trusted sites, 2 min |
| Quotes ("Einstein said ...") | **Always** — misquotes are rampant | Quote is real or delete, 2 min |
| Statistics ("60% of farms in 1800s...") | **Always**, and cite a source on the sheet | 2 min |
| Definitions ("what's a serif?") | Usually fine; spot-check if unusual | 1 min |
| Step-by-step how-tos (experiment setup, craft) | Check safety + physics | 2 min |
| Discussion prompts, opinions, essay structure | No — no facts to check | 0 min |

## Two ways to verify — pick your speed

**Fast path (most days).** For each factual claim on the sheet:
open a *known* reference — a real encyclopedia, your curriculum's own text,
.gov or museum sites. Search "claim + correction?" doesn't work; search the
claim itself, then read what a real source says. If names/dates disagree,
**the real source wins**, every time. Then log it in your `fact-checks.md`
(six words: "week 4, Rome dates — fixed"). Done.

**Thorough path (new topic weeks).** When you're teaching something well
outside your own comfort zone, do the fact-check *before* generating
materials, using the verification prompt
([prompts/verification-pass.md](prompts/verification-pass.md)):

1. Ask the model to **list** every factual claim it used, with a source it
   thinks it got each from. (Models sometimes invent sources; if it can't
   name one, treat the claim as unsourced.)
2. Verify *each named source is real* — this catches a surprisingly large
   share of hallucinations, since fake sources are easier to spot than fake
   facts.
3. Then, and only then, generate worksheets and reading passages.

## Verification helpers the model can give you

Useful, verified-safe asks:

- "List every named entity in this text — person, place, date, number — so I
  can check them." (Cheap; makes the check mechanical.)
- "What's a common misconception people have here, and is anything in this
  text at risk of repeating it?"
- "Which claims here would change the lesson if they were wrong?" (Priorities
  your checking time.)

Not useful, and a trap:

- "Is everything you wrote correct?" — models nearly always say yes.
- "Search and tell me." — early tools sometimes invented search results;
  newer ones do real searches but grab random pages. Trust the *page you
  open yourself*, not the model's summary of a page you haven't seen.

## The sheet-level habit

For anything that stays on a worksheet, keep one line of provenance on the
page itself. A footer like: *"Fact-checked against [source], [date]."*
Chapter 06 suggests logging these in a `fact-checks.md` file per unit. It
takes seconds, and it's exactly the kind of habit that makes a portfolio
durable if anyone ever looks closely.

## Failure modes to know

- **Plausible-audio trap.** A generated science explanation *sounds* right
  because it's fluent. Fluency is not evidence. Check the concept, not the vibe.
- **Outdated by design.** Generated text may reflect a world that ended
  years ago ("free resources, current as of ..." with years you didn't
  mention). State laws, websites, and prices age badly.
- **Mixing up similar entities.** Two people with the same fields, two
  treaties, two wars... this is the model's most common deep error and easy
  to miss because everything around it is right.

The one-line culture of this chapter: **fluent text is a rumor until you've
seen a source.** After your first month, checking quarterly is fine — but
keep the footer habit.

---

Next: [Chapter 06 — Portfolios and Logs](06-portfolios-and-logs.md)
