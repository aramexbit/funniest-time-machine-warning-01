# Funniest Time Machine Warning Label

[![Funniest Time Machine Warning Label](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/aramexbit/funniest-time-machine-warning-01/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/aramexbit/funniest-time-machine-warning-01/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

One-line entry for the [Funniest Time Machine Warning Label](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151) bounty on make.fun.

## The label

> WARNING: Do not meet yourself. One awkward eye contact and the universe files for divorce.

90 characters. The hazard is the classic one — meeting your own
duplicate self — turned into the joke instead of named flatly, and
the surprise lands in the last few words, while the label keeps the
straight face of a genuine safety notice.

## How it works

`main.py` holds the label as fixed text, checks it against the entry
gate (UTF-8, 1 to 120 characters, a single line, not only whitespace),
and writes it to `/output/entry.txt`. Standard library only,
deterministic, no network.

```sh
python3 main.py [--output PATH]
```

The default output is `/output/entry.txt`, the path the harness reads.
Verified locally with `python3 -P -s main.py`: 90 characters, 90 bytes,
byte-exact to the label above, identical across runs.
