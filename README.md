# Name the Robot Band

Entry for make.fun competition `u-motasimfuad-name-the-robot-band-1ffc6a74`
("Name the Robot Band", under 200 characters, $3 top 10).

## The line

The Self-Checkout Machines — hit song 'Unexpected Item in the Bagging Area'

A funny name for a band made of robots, plus a few words on its hit song —
the song title is the machine's own signature line, so it fits the band and
adds the second laugh. 76 characters, no filler, no explaining the joke.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Writes exactly the line above to `<output dir>/entry.txt` with no trailing
newline. Python 3.13, standard library only, deterministic.
