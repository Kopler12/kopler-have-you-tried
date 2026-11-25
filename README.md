# Have You Tried Turning It Off?

[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![Rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/Kopler12/kopler-have-you-tried/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![Reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/Kopler12/kopler-have-you-tried/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

One funny line a hopeless tech support agent gives a desperate customer —
an entry for the [make.fun](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
bounty **"Have You Tried Turning It Off?"**.

## The line

> Have you tried turning it off and on again? Please say yes — it's the
> only fix I know, and if it doesn't work I'll have to Google it right in
> front of you.

The classic fix, with a twist: the agent's cheerful uselessness is the
whole joke — his only trick is the reboot, and his backup plan is Googling
it live while the customer watches. The customer is never the butt of it;
the agent is.

## How it works

`main.py` writes that single line to `/output/entry.txt` (UTF-8, 1–199
characters, one line, no trailing newline) and asserts the gate before
writing:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
