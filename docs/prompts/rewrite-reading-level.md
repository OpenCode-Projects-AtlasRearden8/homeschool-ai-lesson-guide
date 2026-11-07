# Prompt: Rewrite at a Reading Level

*Category: materials · Use: any text that needs to move up or down a band ·
Pairs with: chapter 04.*

## When to use instead of the three-worksheets prompt

This one-off version is for single passages: a paragraph from your spine
book, an explanation that landed badly, a letter to a co-op group with
mixed adult reading levels. The full prompt handles whole worksheets.

## Paste this prompt

```text
Rewrite this passage for a [band: emerging / decoding / confident / advanced]
reader. Same facts, nothing added, nothing dropped, no simplification that
changes meaning.

Rules:
- [Band-specific constraints, e.g., for emerging: "sentences of 8 words max,
  one idea per line, every hard word gets a one-clause definition where it
  first appears"]
- Keep the original's key vocabulary words bolded so I can see targets.
- If any claim in the passage is factual and looks shaky, list it at the end
  under "VERIFY" rather than restating it as settled fact.
- End with a two-line note: what you changed and why, so I can check
  you didn't change meaning.

Passage:
[PASTE TEXT]
```

## Reading the output

- **Changed meaning?** The two-line note at the end is where sneaky changes
  announce themselves. Compare it against your original — that's the whole
  value of the note, and it's why the prompt requires it.
- **Typography** matters more than wording for emerging readers: big font,
  short lines. Most formatting is your print dialog, not the model.
- **Too flat?** Lower-band rewrites can read like GLMs reading rules aloud —
  ask for "vary sentence openers" as a one-line follow-up.

## Band constraints cheat sheet

| Band ask | Sentence length | Extras to request |
|---|---|---|
| Emerging | ≤ 8 words | definitions inline; one idea per line |
| Decoding | ≤ 12 words | consistent question patterns; no nested clauses |
| Confident | ≤ 20 words | connective variety; real "why" questions |
| Advanced | natural | primary-source texture; inference prompts |
