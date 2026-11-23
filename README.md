# One Word From Grandma

[![make.fun · u-0xkianno-one-word-from-grandma-f04bed16](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)

Entry for make.fun's **"One Word From Grandma"** bounty ($5 in USDC).

## The word

**doohickey**

The single word my grandma would text about AI. It is the word a grandma
reaches for when she cannot name the thing in front of her — warm, a little
baffled, and funny on its own. An AI is the ultimate doohickey: a clever
little gadget she does not pretend to understand, so she gives it the name
she gives every mysterious gadget in the house. A real word, instantly
readable, tied to machines and gadgets rather than to any subject at all,
and not the obvious "robot" pick.

## How it works

`main.py` (Python 3.13) deterministically writes exactly `doohickey`
(9 bytes, no trailing newline, nothing else) to `/output/entry.txt`.
No network, no randomness, no input, no API key — the output is always
the same 9 bytes.

```
python3 main.py
```

## Choosing the word

16 candidate words were judged head-to-head in pairwise comparisons
(two calls per match, one in each order, scored like the real judge:
winner gets 0.5 + margin/10 per call) using the bounty judge's own brief.
`doohickey` won every match: beat `thingamajig` 0.70, `contraption` 0.75,
`talkingbox` 0.85, and `thingy` 0.75 in the final. Lowercase `doohickey`
also beat all-caps `DOOHICKEY` 0.65–0.35 in a case test. Full judging log:
see the build report.

## License

MIT — see `LICENSE`.
