import requests
import json
import speake3

# Setup text-to-speach
engine = speake3.Speake()
engine.set('voice', 'en')
engine.set('speed', '150')

# Get api from coindesk.com 
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# Change type of data from json to dictionary
data = json.loads(r.text)

# use dictionary key-value to find price 
btc_price = data['bpi']['USD']['rate']

# Change type of btc_price to int
btc_price = int(float(btc_price.replace(",","")))
print(f"bitcoin price is {btc_price}")

# Speak text
engine.say(f"bitcoin price is {btc_price}")
engine.talkback()