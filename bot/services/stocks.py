from nsepythonserver import *

# positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
# df = pd.DataFrame(positions['data'])
# print(df)


def print_index_quote(index):
    """
    Prints the latest quote for the given index.
    """
    try:
        return nse_get_index_quote(index)["last"]
    except Exception as e:
        print(e)
        raise Exception(f"Invalid Index Name")


def print_equity(equity):
    """
    Prints the latest quote for the given index.
    """
    try:
        return nse_eq(equity)["priceInfo"]["lastPrice"]
    except Exception as e:
        print(e)
        raise Exception(f"Invalid Equity Name")


# print(nse_get_index_quote("NIFTY 50")["last"])
