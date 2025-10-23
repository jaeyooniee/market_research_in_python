"""
Compare rolling win rates of S&P 100 vs S&P 500 (Custom Day Window and Step)
"""

"""
1995-01-01 -> 1999-12-31 (window_days=365, step_days=7): win_rate=34/52 (65.38%) - Dotcom Bubble
2000-01-01 -> 2004-12-31 (window_days=365, step_days=7): win_rate=17/52 (32.69%)
2005-01-01 -> 2009-12-31 (window_days=365, step_days=7): win_rate=17/52 (32.69%)
2010-01-01 -> 2014-12-31 (window_days=365, step_days=7): win_rate=23/52 (44.23%)
2015-01-01 -> 2019-12-31 (window_days=365, step_days=7): win_rate=28/52 (53.85%)
2020-01-01 -> 2024-12-31 (window_days=365, step_days=7): win_rate=34/52 (65.38%) - AI bubble(?)

What kind of companies led S&P100 to outperform S&P500? What was the difference between 100 and 500?
Why did this happen? What's the similarity between 1995-2000 and 2020-2025?
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from data_analysis import load_data, simple_return
import matplotlib.dates as mdates

def main():
    print("Welcome all! Let's figure out when and how many times S&P100 outperformed S&P500!")
    print("**********************************************************************************\n")

    start_input = input("Enter start date (YYYY-MM-DD): ")
    end_input = input("Enter end date (YYYY-MM-DD): ")

    window_days = int(input("Enter window size in DAYS: "))
    step_days = int(input("Enter step size in DAYS: "))

    start_date_obj = datetime.strptime(start_input, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_input, "%Y-%m-%d")

    results = []

    prices = load_data(start_input, end_input)

    current_start = start_date_obj

    while current_start + timedelta(days=window_days) <= end_date_obj:
        start_date = current_start.strftime("%Y-%m-%d")
        end_date = (current_start + timedelta(days=window_days)).strftime("%Y-%m-%d")

        print(start_date + "->" + end_date)

        delta = timedelta(days=step_days)
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end_limit = datetime.strptime(end_date, "%Y-%m-%d")

        step_results = []

        while start + delta <= end_limit:
            s = start.strftime("%Y-%m-%d")
            e = (start + delta).strftime("%Y-%m-%d")

            returns = simple_return(prices, s, e)

            if returns is None or len(returns) == 0:
                start += timedelta(days=step_days)
                continue

            if "S&P100" in returns.index and "S&P500" in returns.index:
                snp100 = returns["S&P100"]
                snp500 = returns["S&P500"]
                winner = "S&P100" if snp100 > snp500 else "S&P500"
                step_results.append(winner)

            start += timedelta(days=step_days)

        total = len(step_results)
        wins = step_results.count("S&P100")
        win_rate = (wins/total * 100) if total > 0 else 0

        results.append({
            "Start Date": current_start,
            "End Date": datetime.strptime(end_date, "%Y-%m-%d"),
            "Total Windows": total,
            "S&P100 Wins": wins,
            "Win Rate (%)": round(win_rate, 2)
        })

        current_start += timedelta(days=step_days)

    df = pd.DataFrame(results)
    print("\n===============================")
    print(f"{window_days}-Day Rolling Comparison Results ({step_days}-Day Steps)")
    print(df.to_string(index=False))
    print("===============================")

    print(f"S&P100 wins: {wins}/{total} ({win_rate:.2f}%)")

    plt.figure(figsize=(12, 6))
    plt.plot(
        df["Start Date"],
        df["Win Rate (%)"],
        linewidth=1.0,
        color="blue",   
        alpha=0.9
    )

    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.YearLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    plt.title(f"S&P 100 Win Rate ({window_days}-Day Window, {step_days}-Day Step)", fontsize=15, pad=20)
    plt.xlabel("Year", fontsize=13)
    plt.ylabel("Win Rate (%)", fontsize=13)

    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()

    plt.style.use("seaborn-v0_8-whitegrid")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.show()


if __name__ == "__main__":
    main()
