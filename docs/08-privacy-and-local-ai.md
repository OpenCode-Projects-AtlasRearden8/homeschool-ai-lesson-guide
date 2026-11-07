# Privacy and Local AI

*Summary: what never goes into a cloud prompt, plus a realistic look at
running AI on your own machine. Time to do: 10 minutes reading; local setup
optional and its own evening project.*

## The rule that keeps showing up

A chat message sent to a cloud AI service is, from a privacy standpoint, a
message sent to a company you don't control, possibly retained, possibly
reviewed. Whether that's fine depends on what's in it. So here's the
household rule this guide builds everything else on:

**Kid names, health details, diagnoses, custody, finances, addresses — none
of that goes into a prompt.** Not for state paperwork questions (chapter 07),
not for "why is my kid melting down over math" — none of it.

You don't need any of it to get good planning help. The model honestly
teaches better when you *don't* dump family drama into the prompt: describe
the *teaching situation*, not the child's identity.

## "But I use initials" and similar comfort

Describing your kid by pseudonym works fine for planning prompts, and it's
what this guide's prompt library models. Two cautions:

1. **Details combine.** "9-year-old girl, county fair chess champion, hates
   handwriting" is a recognizable child to anyone who knows her. Ask
   yourself whether each detail actually serves the planning at all. Usually
   three details are enough, and usually the most distinctive one is the one
   you don't need.
2. **Health and diagnosis details.** For accommodations help, describe the
   *accommodation need*, not the condition or evaluation history: "needs
   extended time and low-pressure output" is privacy-safe, plenty for
   worksheet generation, and yours to decide how to explain to AI.

## Local AI: the honest version

Running a model on your own machine removes the "sent to a company" concern
entirely. It's a real option in 2026 and worth considering if privacy matters
to you a lot — but it has costs, and this page prefers honesty over hype:

| | Cloud AI (free or paid) | Local AI on your machine |
|---|---|---|
| Setup | none | an evening (download a 4–8 GB model, an app, GUI) |
| Quality | usually top-tier | good for planning/rewriting; weaker on the hardest reasoning |
| Speed | fast | depends on your hardware; slow on old laptops |
| Privacy | the company's policy applies | stays on the machine, essentially |
| Cost | free tiers exist; paid tier for heavy use | free after hardware you may already own |

**Practical guidance:** start on cloud with the privacy rules above. If
you find yourself carefully pre-redacting every prompt — that's a sign
local AI is worth one evening. Tools in this space change fast; the current
leading free apps run models like the small Llama/Mistral/others family —
search "run a local LLM on Windows/Mac 2026" rather than trusting this page's
year-old links. The manual's sibling projects cover local setup in detail.

Great local-uses for this workflow: rewriting worksheets at reading levels
(chapter 04), brainstorming quiet-day variants, drafting portfolio summaries
from your own log files, anything you'd paste kid detail into.

Bad fits: heavy fact-check pipeline (local models hallucinate at *least* as
often as cloud ones), anything requiring up-to-the-minute info.

## Files and folders: keep them, back them up

Whole-family school records are some of the most important data you own.
Two cheap habits:

- **Back up `records/` to a second medium** (external drive, or a private
  cloud folder you control). Once a month is plenty.
- **Keep photos of kid work out of the AI** unless they're truly anonymous
  (a math worksheet is fine; a photo of your kid's face with their name
  visible is a "not to cloud" item).

## A word on accounts

Prefer a dedicated account email you don't tie to your main identity if the
tool allows it; turn off "improve the model for everyone"/chat-training
toggles if the service offers the setting; and never paste documents
containing other people's kids (co-op rosters, co-op emails, other families'
IEPs) into any AI, cloud or not. The consent you'd want for your kid's data
is the consent you extend to theirs.

---

Next: [Chapter 09 — Low Energy and Accommodations](09-low-energy-and-accommodations.md)
