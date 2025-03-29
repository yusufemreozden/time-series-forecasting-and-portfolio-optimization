# 📈 Stock Forecasting and Portfolio Optimization

This project combines **time series forecasting** and **portfolio optimization** techniques to analyze and construct a risk-minimized stock portfolio based on selected BIST-listed stocks such as:


---

## 🚀 Technologies Used

- `yfinance` – To fetch historical stock data  
- `Prophet` – For time series forecasting (developed by Meta/Facebook)  
- `cvxpy` – For convex optimization (portfolio allocation)  
- `numpy`, `pandas`, `matplotlib` – Data wrangling and visualization

---

## 🔍 Project Workflow

### 1. Fetch Historical Data  
Downloads historical price data for selected stocks starting from a given date (`2022-01-01`).

### 2. Forecast Future Prices  
Uses **Prophet** to predict the next 30 days of closing prices for each stock. The forecasts are visualized with confidence intervals.

### 3. Calculate Returns  
Daily percentage returns are calculated from the closing prices.

### 4. Portfolio Optimization  
A **minimum variance portfolio** is constructed using `cvxpy`, subject to:

- Full investment constraint: ∑weights = 1  
- No short-selling: weights ≥ 0  

The optimal weights are printed for each stock.

---

## 📈 Example Output

Optimal Portfolio Weights:
FROTO.IS: 0.35  
EGEEN.IS: 0.28  
THYAO.IS: 0.22  
KUTPO.IS: 0.15

---

## 🧩 Potential Improvements

- Add Sharpe Ratio optimization (risk-adjusted return)
- Apply rolling windows for dynamic portfolio updates
- Add forecast accuracy evaluation (MAPE, RMSE)
- Extend to include bonds, currencies, or crypto assets
- Wrap the pipeline into a Streamlit dashboard for interactivity

---

## ⚠️ Disclaimer

This is a research project intended for educational purposes only. The forecasts and portfolio outputs are not financial advice. Always consult with a professional before making investment decisions.
