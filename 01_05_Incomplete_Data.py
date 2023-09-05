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

if __name__ == "__main__":
    symbollist=["FAKE2", "SPY", "JAVA", "FAKE1"]
    start_date = '2005-12-31'
    end_date = '2014-12-07'
    idx=pd.date_range(start_date,end_date)
    df_data = get_data(symbollist, idx)

    # Forward Fill
    df_data.fillna(method="ffill", inplace=True)

    # Back Fill
    df_data.fillna(method='bfill', inplace=True)

    plot_data(df_data)
