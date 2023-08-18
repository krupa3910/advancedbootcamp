import os
import requests
import sys
import pandas as pd
import copy
import json
os.environ.get("")
polygon_key = os.environ.get("POLYGON_KEY")
company_details = "https://api.polygon.io/v3/reference/tickers/{ticker}?apikey={polygon_key}"

def get_stock_data(ticker):
    r = requests.get(company_details.format(polygon_key=polygon_key, ticker=ticker))
    response_text = r.text
    response_dict = json.loads(response_text)
    results_dict = response_dict["results"]
    interested_keys = ["ticker","name","market_cap","currency_name","homepage_url","phone_number","address","total_employees","market_cap","currency_name"]
    compressed_dict = {}
    for key in interested_keys:
        try:
            if key == "address":
                address_string = ""
                for a_key in results_dict["address"].keys():
                    address_string = address_string + " " + results_dict["address"][a_key]
                compressed_dict[key] = address_string
            else:                                    
                compressed_dict[key] = results_dict[key] 
        except:
            continue
            
    return copy.deepcopy(compressed_dict)       
tickers = ["AAPL","AMZN", "TSLA","GOOGL"]
ticker_data =[]
for ticker in tickers:
    ticker_data.append(get_stock_data(ticker))

companies_df = pd.DataFrame(ticker_data)
ticker_data

#######################################################################################

def get_price_data(ticker, date):
    open_close = "https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={polygon_key}"
    r = requests.get(open_close.format(polygon_key=polygon_key, ticker=ticker, date=date))
    response_text = r.text
    response_dict = json.loads(response_text)
    interested_keys = ["from","symbol","open","high","low","close"]
    compressed_dict = {}
    for key in interested_keys:
        compressed_dict[key] = response_dict[key]    
    return copy.deepcopy(compressed_dict)

import pandas as pd
tickers = ["AAPL", "AMZN", "TSLA", "GOOGL"]
ticker_prices = []   
date = "2023-02-06"
for ticker in tickers:
    ticker_prices.append(get_price_data(ticker, date))
ticker_data_df = pd.DataFrame(ticker_prices)

# ticker = "AMZN"
# ticker_prices = []   
# ticker_dates = ["2023-02-06","2023-02-01","2023-01-17","2023-01-12"]
# for date in ticker_dates:
#    ticker_prices.append(get_price_data(ticker, date))

