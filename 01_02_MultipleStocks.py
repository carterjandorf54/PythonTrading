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

def test_run():
    # Define Date Range
    start_date = '2010-01-01'
    end_date = '2010-12-31'
    dates = pd.date_range(start_date, end_date)

    # Choose stock symbols to read
    symbols = ["SPY", "GOOG", "IBM", "GLD"]

    # Get stock data
    df = get_data(symbols, dates)

    # Normalize Stock Data
    df = normalize_data(df)
    plot_data(df)

    # Slice and plot
    plot_selected(df, ["SPY", "IBM"], '2010-03-01','2010-04-01')
    

if __name__ == "__main__":
    test_run()