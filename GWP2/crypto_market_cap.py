import pandas as pd
def convert_to_float(s):
    multiplier = 1
    if s[-1] == 'B':
        multiplier = 1e9
    elif s[-1] == 'M':
        multiplier = 1e6
    elif s[-1] == 'K':
        multiplier = 1e3
    number_part = s[1:-1]
    return float(number_part) * multiplier

def get_crypto_market_cap_weights ():
    with open("marketdata.txt") as f:
        lines = [x.split("\n") for x in f.read().split("\n\n")]
    market_cap = pd.DataFrame(lines[1:])[[1, 5, 6]]
    market_cap.columns = ["Symbol", "Cap", "Type"]
    market_cap["Cap"] = market_cap["Cap"].apply(convert_to_float)
    market_cap["Weight"] = market_cap["Cap"] / market_cap["Cap"].sum()
    return market_cap