# Prompt: State Paperwork Lookup Assistant

*Category: records/compliance · Use: once per year + on moves · Pairs with:
chapter 07 — READ FIRST.*

## The warning, again, in one line

This prompt is for turning an **official page you already found** into
planner-ready sentences. It never answers "what does my state require" by
itself — chapter 07 explains why that's the dangerous question.

## Step 1 (you, 15 minutes): find the official page

Search, in this order: your state's Department of Education homeschooling
page → your state's compulsory-attendance law → a state homeschool
association. Bookmark the DOE page. You will fill the checklist from it.

## Paste this prompt (after Step 1)

```text
You are helping me make a homeschool paperwork checklist from MY OWN STATE'S
official requirements text, which I am pasting below from
[SOURCE, e.g., "our DOE website page X"]. Do not add requirements from your
training data. If the pasted text doesn't answer a question, say so — write
"NOT STATED IN PROVIDED TEXT."

OFFICIAL TEXT:
[PASTE THE DOE PAGE TEXT OR THE STATUTE SECTION]

Produce:
1. A digest of exactly what is required: notification, who may teach,
   required subjects, days/hours, records, assessments, penalties-shaped
   information, re-enrollment notes — ONLY what appears above.
2. Plain-English explanation of each requirement, one sentence each.
3. A list of things parents commonly worry about that this text does NOT
   mention ("NOT REQUIRED per provided text"). I will double-check these
   against the source before trusting the absence.
4. A short list of exact phrases from the text I should quote in my own
   checklist, so my file has provenance.
```

## Step 3 (you, 10 minutes): reconcile

Fill in your
[templates/state-paperwork-checklist.md](../templates/state-paperwork-checklist.md)
with the digest — but every row gets its source quote pasted next to it.
Anything in the "NOT REQUIRED" section deserves a skeptical look at the
actual page before you relax.

## What this prompt does NOT do

- It does not interpret ambiguity ("does this mean I must...?"). For real
  ambiguity: call your state DOE's homeschool contact. Phone beats guessing.
- It does not settle legality anywhere. Chapter 07's professional list
  covers the situations where it can't help and a human must.
- It does not replace the annual re-check. Laws and pages change; the
  calendar reminder is your friend.
