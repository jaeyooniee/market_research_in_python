# 📊 S&P 100 vs S&P 500 Performance Analysis in Python

This project analyses and visualises the **relative performance** of the **S&P 100** and **S&P 500** indices across custom time windows, using Python.  
It calculates how often the S&P 100 *outperformed* the S&P 500 within a defined rolling period and visualises the win rate trend over time.

---

## 🚀 Features
- **Custom date range** input (`start_date`, `end_date`)
- **Flexible rolling window** (`window_days`) and **step interval** (`step_days`)
- Calculates **S&P100 win rate (%)** for each rolling window  
- Produces a **time-series visualisation** of performance dominance
- Efficient data handling using `pandas` and clean plotting with `matplotlib`

---

## ⚙️ How It Works
1. Loads adjusted price data for both **S&P 100 (OEX)** and **S&P 500 (GSPC)** via `load_data()`  
2. Iteratively compares returns over each rolling window:
   - Computes daily or annual returns using `simple_return()`
   - Counts how many sub-periods the S&P 100 outperformed the S&P 500
3. Aggregates results into a `pandas.DataFrame`
4. Plots the rolling win rate trend with yearly x-axis ticks

---

## 🧩 Example Usage
Run the main script:
```bash
python main.py
