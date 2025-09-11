# ECB Project – Simulation of Monetary Policy Impacts on Financial Markets  

## Introduction and Purpose  

The European Central Bank (ECB) regularly announces monetary policy decisions, especially regarding interest rates.  
These announcements have direct and indirect effects on financial markets:  

- **Equity indices** (such as EuroStoxx50)  
- **Sensitive sectors** (banks, utilities)  
- **Currencies** (EUR/USD)  
- **Sovereign yields** (e.g., German Bund 10Y)  

The aim of this project is to build a **Python simulator** that can:  
- Download **real market data** (via Yahoo Finance)  
- Compute **daily returns**  
- Estimate **sensitivities (betas)** of assets to one or several factors (FX, rates)  
- Build **ECB policy scenarios** (cut, hold, hike)  
- Visualize the expected impacts with **charts and tables**  

**Final Objective**: create an **educational and analytical tool** to illustrate, share, and discuss on LinkedIn (with this GitHub repo as support).  

---

## Data Used  

- **Source**: Yahoo Finance (`yfinance`)  
- **Selected tickers**:  
  - `^STOXX50E` → EuroStoxx50 (European equity index)  
  - `EUFN` → European banking sector ETF  
  - `XLU` → Utilities sector ETF (rate-sensitive)  
  - `EURUSD=X` → EUR/USD exchange rate  
  - `DE10Y` (if available) → German Bund 10Y yield  

These provide **adjusted daily closing prices**, which are the basis for all calculations.  


---

