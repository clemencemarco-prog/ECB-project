# ==========================================================
# DATA.PY — STEP 1 OF THE ECB PROJECT
# GOAL: Download market prices from Yahoo Finance
# ==========================================================


import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt 

# Function to load prices
def load_prices(days=260):

    """
    Download market data for the last X days.
    Returns a DataFrame with the columns: EUROSTOXX50, EUFN, XLU, EURUSD.
    """
    # Yahoo Finance tickers
    tickers = {
        "^STOXX50E": "EUROSTOXX50",  # EuroStoxx 50 index
        "EUFN": "EUFN",              # European banks ETF
        "XLU": "XLU",                # Utilities ETF
        "EURUSD=X": "EURUSD"         # EUR/USD exchange rate
    }

    # Download adjusted close prices
    data = yf.download(list(tickers.keys()), period=f"{days}d")["Close"]

    # Rename columns with clearer names
    data = data.rename(columns=tickers)
    return data

if __name__ == "__main__":

    # Load the data
    df = load_prices(260)

    # Show the first 5 rows
    print(df.head())

    # Plot prices
    df.plot(figsize=(10,5), title="Market prices (levels)")
    plt.show()

    
