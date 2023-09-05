import pandas as pd
import os
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(os.getcwd(), base_dir, f"{symbol}.csv")

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)

    # Iterate through the symbol list being passed in
    for symbol in symbols:
        # Read the data for each symbol into a temp dataframe
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates=True, usecols=["Date","Adj Close"], na_values=['nan'])
        df_temp = df_temp.rename(columns = {"Adj Close": symbol})
        # Join the temp data with the main data frame
        df = df.join(df_temp)
        # Drop Dates that SPY did not trade
        if symbol == "SPY":
                df = df.dropna(subset=["SPY"])

    return df

def plot_data(df, title="Stock prices"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def plot_selected(df, symbols, start_date, end_date):
    temp_df = df.loc[start_date:end_date, symbols]
    plot_data(temp_df, "Plot")

def normalize_data(df):
     return df/df.iloc[0,:]

def get_rolling_mean(values, window):
     return values.rolling(window).mean()

def get_rolling_std(values, window):
     return values.rolling(window).std()

def get_bollinger_bands(rm, rstd):
     upper_band = rm + 2*rstd
     lower_band = rm - 2*rstd
     return upper_band, lower_band

def compute_daily_returns(df):
     daily_returns = df.copy()

     #compute daily returns for row 1 onwards
     #daily_returns[1:] = (df[1:] / df[:-1].values) - 1
     daily_returns = (df/df.shift(1))-1
     daily_returns.iloc[0, :] = 0
     return daily_returns

def test_run():
    # Define Date Range
    start_date = '2012-01-01'
    end_date = '2012-12-31'
    dates = pd.date_range(start_date, end_date)

    # Choose stock symbols to read
    symbols = ["SPY"]

    # Get stock data
    df = get_data(symbols, dates)

    # Plot Spy Data, Retain Matplotlib axis object
    ax = df['SPY'].plot(title="SPY Rolling Mean", label="SPY")

    # Compute Rolling mean,std & bollinger bands using a 20 day window
    rm_SPY = get_rolling_mean(df["SPY"], 20)
    rsd_SPY = get_rolling_std(df["SPY"], 20)
    bollinger_upper, bollinger_lower = get_bollinger_bands(rm_SPY, rsd_SPY)

    # Add rolling mean to same plot
    rm_SPY.plot(label="Rolling Mean", ax=ax)
    #rsd_SPY.plot(label="Rolling Std Dev", ax=ax)
    bollinger_upper.plot(label="Bollinger Upper", ax=ax)
    bollinger_lower.plot(label="Bollinger Lower", ax=ax)
    
    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")
    plt.show()

    daily_returns = compute_daily_returns(df)
    plot_data(df)
    plot_data(daily_returns, title="Daily Returns")

if __name__ == "__main__":
    test_run()