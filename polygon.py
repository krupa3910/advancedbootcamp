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