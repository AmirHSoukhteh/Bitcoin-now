import requests
import json

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

data = json.loads(r.text)

print(data['bpi']['USD']['rate'])
