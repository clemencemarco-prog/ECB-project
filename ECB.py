import pandas as pd

try:
    import yfinance as yf
    HAS_YF = True
except Exception:
    HAS_YF = False
    
TICKERS = {
    "EUROSTOXX50": "^STOXX50E",
    "EUFN": "EUFN",
    "XLU": "XLU",
    "EURUSD": "EURUSD=X",
   # "DE02Y": "DE02Y-DE",# 
   # "DE10Y": "DE10Y-DE",#
}

def load_prices(days: int = 260) -> pd.DataFrame:
    """Télécharge les clôtures quotidiennes. Si yfinance indispo, renvoie DataFrame vide."""
    if not HAS_YF:
        return pd.DataFrame()
    data = {}
    for name, ticker in TICKERS.items():
        try:
            df = yf.download(
                ticker, period=f"{days}d", interval="1d", 
                auto_adjust=True, progress=False
                )
            if df is not None and not df.empty and "Close" in df:
                data[name] = df["Close"]
            else:
                print(f"[warn] Pas de données pour {name} ({ticker})")
        except Exception as e:
            print(f"[warn] Échec téléchargement {name} ({ticker}) -> {e}")

    if len(data) == 0:
        return pd.DataFrame(data)

if __name__ == "__main__":
    df = load_prices(30)
    print(df.head())
