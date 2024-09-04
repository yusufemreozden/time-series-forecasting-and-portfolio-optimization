import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet  # prophet kullanıyoruz
import cvxpy as cp
import numpy as np

# Hisse senedi verilerini indirme
tickers = ['FROTO.IS', 'EGEEN.IS', 'THYAO.IS', 'KUTPO.IS']
start_date = '2022-01-01'
data = {ticker: yf.download(ticker, start=start_date) for ticker in tickers}

# Zaman serisi tahmini ve portföy optimizasyonu
def forecast_and_optimize(ticker_data, ticker):
    # Veriyi hazırlama
    df = ticker_data[['Close']].reset_index()
    df.columns = ['ds', 'y']
    
    # Modeli oluşturma ve eğitme
    model = Prophet()
    model.fit(df)
    
    # Tahmin için veri oluşturma
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    # Grafikleme
    fig = model.plot(forecast)
    plt.title(f'{ticker} Fiyat Tahmini')
    plt.show()
    
    # Getiri hesaplama
    returns = ticker_data['Close'].pct_change().dropna()
    
    return returns

# Portföy optimizasyonu
def portfolio_optimization(returns_list):
    # Portföy optimizasyonu
    num_assets = len(returns_list)
    weights = cp.Variable(num_assets)
    returns_matrix = np.array([returns.values for returns in returns_list]).T
    expected_returns = returns_matrix.mean(axis=0)
    cov_matrix = np.cov(returns_matrix, rowvar=False)
    
    # Amaç: Portföyün varyansını minimize etmek
    portfolio_variance = cp.quad_form(weights, cov_matrix)
    objective = cp.Minimize(portfolio_variance)
    
    # Kısıtlar
    constraints = [cp.sum(weights) == 1, weights >= 0]
    prob = cp.Problem(objective, constraints)
    prob.solve()

    # Sonuçları yazdırma
    print('Optimum Portföy Ağırlıkları:')
    for i, ticker in enumerate(tickers):
        print(f'{ticker}: {weights.value[i]:.2f}')

# Hisse senedi verilerini işleme
returns_list = []
for ticker, ticker_data in data.items():
    returns = forecast_and_optimize(ticker_data, ticker)
    returns_list.append(returns)

portfolio_optimization(returns_list)
