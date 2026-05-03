# Leading_Lagging_Sectors
An automated Python pipeline that tracks macro-equity capital rotation by calculating normalized growth and relative strength across major market sectors.


# 🌍 Macro-Equity Sector Rotation Tracker

**An automated Python pipeline that visualizes institutional capital rotation by tracking normalized growth and relative strength across major market sectors.**

## 📝 Project Overview
This project is a macroeconomic data analysis tool designed to track how capital flows between the broader market and specific industry sectors over time. By automatically ingesting years of historical index data via the Yahoo Finance API, the pipeline normalizes asset pricing and calculates 50-day smoothed Relative Strength (RS). 

This tool allows equity researchers and portfolio managers to clearly identify which market sectors are acting as market leaders (outperforming) or laggards (underperforming) compared to the benchmark index.

This project demonstrates core competencies in **API integration, financial data normalization, moving average smoothing, and data visualization.**

## 🛠️ Tech Stack
* **Language:** Python
* **Data Ingestion:** `yfinance` (Yahoo Finance API)
* **Data Manipulation:** `pandas`
* **Data Visualization:** `matplotlib`
* **Domain Context:** Macroeconomics, Equity Research, Portfolio Allocation

---

## 🚀 Key Features

* **Automated API Integration:** Programmatically fetches historical daily closing prices for the Nifty 50 benchmark and major sectoral indices (Bank, IT, Pharma, Auto) without relying on static CSVs.
* **Mathematical Normalization:** Re-bases all distinct financial indices to a common mathematical baseline (Base = 100), allowing for accurate, side-by-side percentage growth comparisons across assets with drastically different nominal prices.
* **Relative Strength (RS) Calculation:** Computes the daily ratio of each sector against the broader market to track the true velocity of capital rotation.
* **Volatility Smoothing:** Applies a 50-day Simple Moving Average (SMA) to the Relative Strength data to filter out daily market noise and expose long-term structural trends.
* **Professional Visualization:** Generates a dual-panel financial chart displaying both absolute normalized growth and relative market outperformance.

---

## 🏗️ System Architecture 

1. **Ingestion Engine:** Connects to `yfinance`, downloads historical OHLCV data, and cleans missing trading days using forward-filling methods.
2. **Transformation Layer:** Slices the data to isolate closing prices and applies the Base-100 normalization formula.
3. **Analytics Engine:** Calculates the relative strength ratios and applies rolling window statistical smoothing.
4. **Presentation Layer:** Renders the final macroeconomic dashboard using customized Matplotlib subplots.

---

## 📊 Results & Business Insights

*Analysis of Indian market sectors from 2021 to 2026 revealed a massive divergence in capital allocation. The Auto sector experienced heavy institutional inflows (growing ~170%), while the IT sector severely lagged the broader market.*

### Sector Rotation Dashboard
<img width="1919" height="986" alt="image" src="https://github.com/user-attachments/assets/14ad4baa-42ea-4723-a48f-050970f35a4e" />


**Key Analytical Takeaways:**
* **Market Leaders:** The Auto and Banking sectors consistently remained above the Nifty 50 baseline, indicating strong structural uptrends and capital inflows.
* **Market Laggards:** The IT sector's 50-day RS line crossed below the benchmark, signaling a macro transition into an unfavorable sector for long-term portfolio allocation during this specific period.
