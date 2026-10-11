#!/usr/bin/env python3
"""Reproducible toy experiment in proportional betting.

Independent even-money bets with a known 55% win chance. No market data,
transaction costs, changing probabilities, or real trades are modeled.
"""

from __future__ import annotations

import csv
import math
import random
from pathlib import Path
from statistics import median


SEED = 20261011
PATHS = 50_000
BET_COUNT = 100
WIN_PROBABILITY = 0.55
FRACTIONS = (0.05, 0.10, 0.25, 0.50)
OUTPUT = Path(__file__).resolve().parent / "results.csv"


def main() -> None:
    random_generator = random.Random(SEED)
    win_counts = [
        sum(random_generator.random() < WIN_PROBABILITY for _ in range(BET_COUNT))
        for _ in range(PATHS)
    ]
    rows = []
    for fraction in FRACTIONS:
        log_wealth = [
            wins * math.log1p(fraction)
            + (BET_COUNT - wins) * math.log1p(-fraction)
            for wins in win_counts
        ]
        sorted_log_wealth = sorted(log_wealth)
        rows.append(
            {
                "stake_fraction": f"{fraction:.2f}",
                "expected_wealth_exact": f"{(1 + (2 * WIN_PROBABILITY - 1) * fraction) ** BET_COUNT:.4f}",
                "median_wealth_simulated": f"{math.exp(median(sorted_log_wealth)):.4f}",
                "p10_wealth_simulated": f"{math.exp(sorted_log_wealth[int(0.10 * PATHS)]):.4f}",
                "p90_wealth_simulated": f"{math.exp(sorted_log_wealth[int(0.90 * PATHS)]):.4f}",
                "share_below_start_simulated": f"{sum(value < 0 for value in log_wealth) / PATHS:.4f}",
                "expected_log_growth_per_bet_exact": f"{WIN_PROBABILITY * math.log1p(fraction) + (1 - WIN_PROBABILITY) * math.log1p(-fraction):.6f}",
            }
        )
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
