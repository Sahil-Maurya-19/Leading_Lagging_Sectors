import yfinance as yf
import pandas as pd

def fetch_sector_data(start_date, end_date):
    """
    Fetches daily closing prices for the Nifty 50 and key sectoral indices.
    """
    # Yahoo Finance tickers for Indian Indices
    tickers = {
        'Nifty_50': '^NSEI',
        'Bank_Nifty': '^NSEBANK',
        'Nifty_IT': '^CNXIT',
        'Nifty_Pharma': '^CNXPHARMA',
        'Nifty_Auto': '^CNXAUTO'
    }
    
    # Initialize an empty DataFrame to hold all our closing prices
    df = pd.DataFrame()
    
    print("Fetching data from Yahoo Finance...")
    
    for name, ticker in tickers.items():
        # Download the historical data for each ticker
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
        
        # We only need the 'Close' price for this macro analysis
        # Using squeeze() handles the MultiIndex structure yfinance sometimes returns
        df[name] = data['Close'].squeeze()
        
    # FIX: Use the dedicated ffill() method for newer versions of pandas
    df.ffill(inplace=True)
    
    # Drop any rows that are entirely NaN (usually at the very beginning if start dates mismatch)
    df.dropna(inplace=True)
    
    print(f"Data successfully loaded. Total trading days: {len(df)}")
    return df

# --- Execution ---
# We will pull data from January 1st, 2021 to today
data = fetch_sector_data(start_date='2021-01-01', end_date='2026-04-27')
print(data.head())


def calculate_relative_performance(df):
    """
    Normalizes the data to a base of 100 for true percentage comparison
    and calculates the Relative Strength (RS) ratio against the benchmark (Nifty 50).
    """
    # 1. Normalize the Data (Base 100)
    # Divide every row by the first row (iloc[0]) and multiply by 100
    normalized_df = (df / df.iloc[0]) * 100
    
    # 2. Calculate Relative Strength (Sector / Benchmark)
    rs_df = pd.DataFrame(index=df.index)
    sectors = ['Bank_Nifty', 'Nifty_IT', 'Nifty_Pharma', 'Nifty_Auto']
    
    for sector in sectors:
        # A rising RS line means the sector is outperforming the Nifty 50
        # A falling RS line means it is underperforming
        rs_df[f'{sector}_RS'] = df[sector] / df['Nifty_50']
        
    return normalized_df, rs_df

# --- Execution ---
# Keep your existing code, and add these execution lines at the very bottom:
normalized_data, relative_strength = calculate_relative_performance(data)

print("\n--- Normalized Data (Base 100) ---")
print(normalized_data.tail())

print("\n--- Relative Strength vs Nifty 50 ---")
print(relative_strength.tail())


import matplotlib.pyplot as plt

def visualize_rotation(normalized_df, rs_df):
    """
    Plots a two-panel chart showing absolute normalized growth
    and the smoothed relative strength against the benchmark.
    """
    # Normalize the RS dataframe so all lines start at 100. 
    # If a line goes above 100, it is outperforming Nifty 50.
    rs_normalized = (rs_df / rs_df.iloc[0]) * 100

    # Apply a 50-day moving average to smooth out the daily volatility
    rs_smoothed = rs_normalized.rolling(window=50).mean()

    # Create a figure with 2 subplots (Top for Absolute, Bottom for Relative)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

    # Dictionary to keep line colors consistent across both charts
    colors = {
        'Nifty_50': 'black', 
        'Bank_Nifty': '#1f77b4',  # Blue
        'Nifty_IT': '#ff7f0e',    # Orange
        'Nifty_Pharma': '#2ca02c',# Green
        'Nifty_Auto': '#d62728'   # Red
    }
    
    # --- TOP CHART: Absolute Normalized Growth ---
    for col in normalized_df.columns:
        # Make the Nifty 50 benchmark line thicker and black for contrast
        linewidth = 3.5 if col == 'Nifty_50' else 1.5
        ax1.plot(normalized_df.index, normalized_df[col], label=col, color=colors.get(col), linewidth=linewidth)
    
    ax1.set_title('Absolute Sector Growth (Base 100 = Jan 2021)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Index Value (Normalized)')
    ax1.legend(loc='upper left')
    ax1.grid(True, linestyle='--', alpha=0.6)

    # --- BOTTOM CHART: Relative Strength vs Nifty 50 ---
    for col in rs_smoothed.columns:
        sector_name = col.replace('_RS', '')
        ax2.plot(rs_smoothed.index, rs_smoothed[col], label=f'{sector_name} RS (50d MA)', color=colors.get(sector_name), linewidth=2.5)
    
    # Add a flat baseline at 100 (representing the Nifty 50's exact performance)
    ax2.axhline(100, color='black', linestyle='-', linewidth=3.5, label='Nifty 50 Baseline')
    
    ax2.set_title('Relative Strength vs Nifty 50 (50-Day Smoothed)', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Relative Strength (Base 100)')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.legend(loc='upper left')
    ax2.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()

# --- Execution ---
# Add this single line at the very end of your script:
visualize_rotation(normalized_data, relative_strength)