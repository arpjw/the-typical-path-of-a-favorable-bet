# The typical path of a favorable bet

Companion to [The typical path of a favorable bet](https://aryasomu.com/writing/the-typical-path-of-a-favorable-bet.html).

This deliberately small experiment considers 100 independent even-money bets. Each bet wins with probability 0.55, which is known to the bettor. After each outcome, the bettor stakes a fixed fraction of current wealth. A win multiplies wealth by `1 + f`; a loss multiplies it by `1 - f`. Initial wealth is 1.

Run with Python 3 and no third-party packages:

```bash
python3 simulate.py
```

The script uses seed `20261011`, generates 50,000 paths of 100 outcomes, and applies the *same outcome paths* to four stake fractions. It writes `results.csv`. The exact expected terminal wealth and exact expected log growth in that file are calculated from the model; the median, deciles, and share of paths finishing below 1 are Monte Carlo results. Rerunning the script should reproduce the CSV byte for byte with the same Python random number generator behavior.

The experiment was run October 11, 2026. It is a synthetic illustration, not a backtest or evidence of a tradable edge. It excludes changing win probabilities, dependence, odds, fees, market impact, liquidity constraints, and estimation error. It makes no claim about any real asset or betting market.
