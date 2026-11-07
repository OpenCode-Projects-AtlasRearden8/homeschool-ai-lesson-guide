# Prompt: Verification Pass

*Category: quality · Use: before printing or teaching anything factual ·
Pairs with: chapter 05.*

## Why this prompt exists

It converts "trust the confident text" into "verify a short list" — which is
a 2-minute job instead of an anxiety spiral. It does NOT verify anything for
you: it *extracts* the claims so you can check them against real sources.

## Paste this prompt (run BEFORE materials generation for new topics)

```text
Here is content I'm considering teaching. Do NOT expand or "fix" it.

[PASTE THE DRAFT TEXT OR YOUR TOPIC OUTLINE]

Your job:
1. List every factual claim contained in or implied by this text: names,
   dates, numbers, quotes, causes, "how X works" mechanisms. Number them.
2. For each, say your confidence: [near-certain] [likely] [uncertain]
   [often-confused-with-something-else].
3. For the often-confused ones, name the thing it's commonly confused with,
   so I know what to check against.
4. List the TWO claims that would most damage this lesson if wrong. Those
   are my priority checks.
5. Name any claim that references something time-sensitive (prices,
   websites, current events, laws) — flag it as [DOES NOT AGE WELL].
6. Do not add new facts. Do not smooth over uncertainty. If you don't
   know, write "I don't know" — that answer is genuinely helpful here.
```

## Then: the two paths (chapter 05 details)

- **Fast path today:** prioritize items from step 4 (two most damaging) plus
  every "often-confused" one. Real source — encyclopedia, your spine book,
  .gov/museum site. Two minutes. Fix, footer the sheet.
- **Thorough path new-topic weeks:** check *sources* named in step 2
  (fake sources are easier to spot than fake facts), then generate
  materials only after that pass.

## Companion mini-prompts

- **Claim harvester re-run:** "New version pasted below — list ONLY claims
  that differ from the last version." (Catches model drift between passes.)
- **Source oracle:** "Name the source you're drawing each claim from. If you
  cannot name one, say so." Unsourced + confident is exactly the pattern
  worth pausing on.

## What NOT to do with this prompt

- Don't ask it "so was everything correct?" — the answer will be yes, every
  time, which is exactly the failure mode this prompt exists to route
  around.
- Don't let it "verify" by summarizing web pages you haven't opened. You are
  the verifier. It is the extractor.
