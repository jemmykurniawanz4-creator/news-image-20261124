# The World on Tuesday, 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/jemmykurniawanz4-creator/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/jemmykurniawanz4-creator/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

An entry for the [make.fun](https://make.fun) bounty
["Sum up 24 November's world news in one image"](https://make.fun/bounty/news-image-20261124).

The entry image, `entry.png`, is a newspaper front page that sums up the world
news of Tuesday 24 November 2026 in a single 1024x1024 image: the collapse of
the COP31 climate talks in Antalya as the lead story, with panels on the war at
sea off Libya, the Strait of Hormuz tanker crisis, Russia testing NATO, the
World Court's Rohingya ruling, the UN chief's call for a global AI framework,
and the first foreign astronaut aboard China's Tiangong station — plus an
"also today" ticker with the day's markets, a Nepal earthquake, and Gaza.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`, or to `$MAKEFUN_OUTPUT_DIR/entry.png` when that
environment variable is set. It runs deterministically: two runs write
identical bytes.
