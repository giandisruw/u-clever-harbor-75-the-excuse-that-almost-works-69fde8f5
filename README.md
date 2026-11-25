[![make.fun](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![Rank](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/giandisruw/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
[![Reward](https://make.fun/badge/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/giandisruw/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)

# The Excuse That Almost Works

The one line a gamer texts the boss to skip work on GTA 6 launch week, 78 characters / 16 words (limits: 20 words, 140 characters):

> boiler engineer finally rang back, he's here at eight and i have to let him in

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Thirty original candidate lines were written across varied angles — tradespeople and appointments (plumber, boiler, gas man, broadband engineer), the flat and the building (flood, power cut, lift, fire alarm), the car (garage, MOT, windscreen, towed), admin and obligations (bank, jury service, council, pharmacy, dentist) — deliberately avoiding the clichés the judge brief penalises (dead grandmother, flat tyre, sudden fever). Two candidates carried a quiet GTA wink (a preordered delivery needing a signature; a new console bricking the router); both scored poorly (1.6 and 1.05), confirming the house judge rewards a straight, boring, believable excuse over a nudge at the game.

They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — on-topic excuse first, then almost-believable (a real, specific, boring detail), funny on its own terms, hurried-text voice, and a fresh angle. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 61 games, 122 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 122 calls returned a verdict, none scored 0.5–0.5 by the no-verdict house rule.

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| #17 | Jury service, standby all week, a day's notice | 2.85 |
| **#2** | Boiler engineer finally rang back, here at eight | **2.7** |
| #10 | Bank needs me in branch before eleven, third time | 2.55 |
| #20 | Water company shutting the street off at nine | 2.55 |
| #1 | Plumber, leak under the kitchen sink | 2.5 |
| #14 | Gas man safety check, fifty pound fine if missed | 2.35 |
| #22 | Key snapped in the lock, locked out of my flat | 2.35 |
| #4 | Car in the garage, the brake thing | 2.25 |
| #18 | Smoke alarm since four am, fire brigade said stay | 2.25 |
| #24 | Broadband engineer moved my appointment, third time | 2.25 |
| #5 | Internet down, hotspotting from a dying phone | 2.2 |
| #6 | Landlord's annual inspection, or he charges me | 2.15 |
| #27 | Landlord selling the flat, viewings all day | 2.15 |
| #19 | Windscreen cracked, autoglass only today | 2.1 |
| #26 | Pharmacy messed up my repeat prescription | 2.1 |
| #9 | Prescription ready, pharmacy closes at noon | 2.05 |
| #11 | Lift broken, seventh floor, knee won't do stairs | 2.05 |
| #16 | Kid's class shut for a burst pipe, collect by ten | 2.05 |
| #25 | Car failed its MOT on the brakes | 2.05 |
| #12 | Council resurfaced the road, car towed, can't find it | 2.0 |
| #28 | Train cancelled, replacement bus full | 2.0 |
| #3 | Dentist moved my filling, jaw still numb | 1.85 |
| #23 | Tooth has to come out today, already swelling | 1.8 |
| #8 | Power cut, whole street, laptop dead | 1.7 |
| #29 | Preordered delivery needs a signature, today only | 1.6 |
| #15 | Slept through my alarm, bus crawling | 1.45 |
| #21 | Fire alarm test turned real, all outside | 1.45 |
| #7 | Flat flooded from the washing machine | 1.15 |
| #30 | New console bricked the router, no wifi | 1.05 |
| #13 | Neighbour's dog ate my laptop charger | 0.45 |

Final: #17 led the Swiss at 2.85, #2 was second at 2.7, and the final tied 0.5–0.5 — each order's judge picked the A-labelled entry at margin 3 (jury service's "real, unavoidable obligation" one way, the boiler engineer's "specific, boring, almost-believable reality" the other), so the two calls cancelled exactly. #2 took the entry on the pre-declared tie-break (lower candidate id). #2's line scores on every brief criterion at once: it is unmistakably a hurried text to a boss, it is almost believable (a tradesman who finally rang back is the most boringly specific thing a manager hears all week), the laugh comes from its own logic ("finally rang back" — the wait is the excuse), and it finds a fresh angle no other candidate used.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
