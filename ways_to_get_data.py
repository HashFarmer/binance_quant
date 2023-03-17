# 1 , using api 

import requests
import json
import pandas as pd

# Set the API endpoint
url = 'https://api.binance.com/api/v3/klines'

# Set the parameters for the API call
symbol = 'BTCUSDT' # The cryptocurrency pair you want to get the historical data for
interval = '1d' # The time interval you want to get the data for (e.g. 1 day, 1 hour, etc.)
limit = 1000 # The maximum number of data points you want to retrieve (maximum is 1000)

# Set the payload for the API call
payload = {
    'symbol': symbol,
    'interval': interval,
    'limit': limit
}

# Make the API call and store the response in a variable
response = requests.get(url, params=payload)

# Convert the response to a JSON object
data = json.loads(response.text)

# Convert the data to a Pandas dataframe
df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])

# Convert the timestamp to a readable date format
df['date'] = pd.to_datetime(df['timestamp']/1000, unit='s')

# Print the dataframe
print(df)

