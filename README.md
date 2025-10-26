# S&P 100 vs S&P 500 Performance Analysis in Python

This project analyses and visualises the relative performance of the **S&P 100** and **S&P 500** indices across custom time windows using Python.  
This calculates how often the S&P 100 outperformed the S&P 500 within a defined rolling period and visualises the win rate over time.
The interpretation of the results is inside the file named "Result Explanation"

---

## Features
1. Custom date range
2. Flexible rolling window and step interval
3. Calculates **S&P100 win rate (%)** for each rolling window  
4. Produces a **time-series visualisation** of performance dominance
5. Efficient data handling using `pandas` and clean plotting with `matplotlib`

---

## How The Program Works
1. Loads adjusted price data for both **S&P 100 (OEX)** and **S&P 500 (GSPC)** via `load_data()`  
2. Iteratively compares returns over each rolling window:
   - Computes daily or annual returns using `simple_return()`
   - Counts how many sub-periods the S&P 100 outperformed the S&P 500
3. Aggregates results into a `pandas.DataFrame`
4. Plots the rolling win rate trend with yearly x-axis ticks

