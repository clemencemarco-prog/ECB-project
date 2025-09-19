# ==========================================================
# MODELS.PY — STEP 3: Estimate betas with statsmodels (OLS)
# Multi-factor model:
#   return_asset = alpha + b1*EURUSD + b2*BUND_BP + B3*UST10Y_BP + error
#   with robust standard errors (HAC/Newey-West)
#   Shows: beta (coef), t-stat, p-value, R2, N
# ==========================================================

import numpy as np
import pandas as pd
import statsmodels.api as sm

# ----------------------------------------------------------
# 1) Build the factor matrix X from the daily changes table
#    (keeps only columns that exist)
# ----------------------------------------------------------

def betas(changes: pd.DataFrame, maxlags: int = 5) -> pd.DataFrame:

    """
    Select factor columns from 'changes' to use in regressions.
    Run the same OLS for several assets against available factors.
    Assets: EUROSTOXX50, EUFN, XLU, SP500
    Factors: EURUSD (in % daily change), BUND_BP (Bund 10Y daily change in basis points), UST10Y_BP (UST 10Y daily change in basis points)
    Return a tidy DataFrame with coef, t, p, r2, nobs.
    """
    # Pick assets
    asset_list = asset_list = [c for c in ["EUROSTOXX50", "EUFN", "XLU", "SP500"] if c in changes.columns]
    if not asset_list:
        raise ValueError("No known asset columns found (EUROSTOXX50, EUFN, XLU, SP500).")

    # Pick factor
    factor_list = [c for c in ["EURUSD", "BUND_BP", "UST10Y_BP"] if c in changes.columns]
    if not factor_list:
        raise ValueError("No factor columns found (EURUSD, BUND_BP, UST10Y_BP).")

    rows = []
    for asset in asset_list:
        # Align y and X on the same dates and drop NaNs
        y = changes[[asset]]
        X = changes[factor_list]

        data = pd.concat([y, X], axis=1).dropna()

        y_clean = data[asset]
        X_clean = data[factor_list]

        # Add constant for alpha
        X_const = sm.add_constant(X_clean, has_constant="raise")


        # Fit OLS with HAC/Newey-West standard errors (robust to heteroskedasticity & autocorr)
        res = sm.OLS(y_clean, X_const).fit(cov_type="HAC", cov_kwds={"maxlags": maxlags})


        # Store results for each parameter
        for param in res.params.index:  # 'const', 'EURUSD', 'BUND_BP', 'UST10Y_BP'
            rows.append({
                "asset": asset,
                "param": param,
                "coef": res.params[param],
                "t": res.tvalues[param],
                "p": res.pvalues[param],
                "r2": res.rsquared,
                "nobs": int(res.nobs),
            })

    out = pd.DataFrame(rows).set_index(["asset", "param"]).sort_index()
    return out

if __name__ == "__main__":
    try:
        from data import load_prices
        from returns import daily_returns
    except ImportError:
        print("Tip: make sure data.py has load_prices() and returns.py has build_daily_changes().")
        raise

    prices = load_prices(days=260)
    changes = daily_returns(prices)

    results = betas(changes, maxlags=5)  # ~ 1 trading week
    print("\n=== OLS betas (coef), t-stats (HAC), p-values (HAC) ===")
    print(results.round(4))
