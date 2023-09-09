import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data, plot_data

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    #daily_returns.ix[0, :] = 0
    daily_returns.iloc[0,:] = 0
    return daily_returns

# Plot a Single Histogram
def test_run():
    #Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute Daily Returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily Returns", ylabel="Daily Returns")

    #Plot a Histogram
    daily_returns.hist(bins=20)

    # Get Mean and Std Deviation
    mean = daily_returns['SPY'].mean()
    print(f"mean = {mean}")
    std = daily_returns["SPY"].std()
    print(f"std = {std}")

    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()

    # Compute Kurtosis
    print(daily_returns.kurtosis())

# Plot multiple histograms against each other
def test_run2():

    #Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', "XOM"]
    df = get_data(symbols, dates)
    plot_data(df)

    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily Returns", ylabel="Daily Returns")

    daily_returns["SPY"].hist(bins=20, label="SPY")
    daily_returns["XOM"].hist(bins=20, label="XOM")

    plt.legend(loc='upper right')
    plt.show()

# Plot Scatter Plots
def test_run3():

    #Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', "XOM", "GLD"]
    df = get_data(symbols, dates)
    print(df)
    #plot_data(df)

    daily_returns = compute_daily_returns(df)
    #plot_data(daily_returns, title="Daily Returns", ylabel="Daily Returns")

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter', x="SPY", y='XOM')
    # Fit to a polynomial function with degree 1 (Linear)
    beta_XOM, alpha_XOM = np.polyfit(daily_returns["SPY"], daily_returns["XOM"], 1)
    # y = mx+b
    plt.plot(daily_returns["SPY"], beta_XOM*daily_returns["SPY"] + alpha_XOM, '-', color='r')
    

    # Scatterplot SPY vs GOLD
    daily_returns.plot(kind='scatter', x="SPY", y='GLD')
    beta_GLD, alpha_GLD = np.polyfit(daily_returns["SPY"], daily_returns["GLD"], 1)
    plt.plot(daily_returns["SPY"], beta_GLD*daily_returns["SPY"] + alpha_GLD, '-', color='r')

    plt.show()

    # Calculate correlation coefficient
    print(daily_returns.corr(method='pearson'))

    

if __name__ == "__main__":
    test_run3()