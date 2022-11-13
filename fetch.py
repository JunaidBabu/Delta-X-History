"""
Fetch data from DeltaX periodically and store as file

"""

import json
import time
import requests


url = "https://p-api.delta.exchange/v2/tickers?contract_types=put_options,call_options"
data = requests.get(url).json()

with open("data/" + str(int(time.time())) + ".json", "w") as f:
    f.write(json.dumps(data))