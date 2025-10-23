import matplotlib.pyplot as plt

# matplotlib.pyploy is one of the basic visualisation libraries in python

def graph_index(prices, start_date, end_date):
    past_prices = prices.loc[start_date:end_date]
    # loc = label location, name
    indexed = (past_prices / past_prices.iloc[0]) * 100
    # iloc = integer location, index
    plt.figure(figsize=(6, 4))
    indexed.plot(ax=plt.gca())
    plt.title(f"S&P 500 vs S&P 100 (Indexed to 100, {start_date}-{end_date})")
    plt.xlabel("Date")
    plt.ylabel("Index (Start = 100)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show() 



