# read json from file and print

import json

with open("data/1668308134.json", "r") as f:
    data = json.load(f)

print(data)

