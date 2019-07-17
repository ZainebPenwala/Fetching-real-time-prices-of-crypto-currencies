# Bitcoin
--Bitcoin usd:

import requests
import json

url= "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
print(url)
ans=requests.get(url)
print(ans,ans.text)
j_ans=json.loads(ans.text)
print(j_ans['bpi']['USD']['rate_float'])


--bitcoin INR:

import requests
import json

url= "https://api.coindesk.com/v1/bpi/currentprice/INR.json"
print(url)
ans=requests.get(url)
print(ans,ans.text)
j_ans=json.loads(ans.text)
print(j_ans['bpi']['INR']['rate_float'])




# Ethereum
--Ethereum to usd:

import requests
import json

url= "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
print(url)
ans=requests.get(url)
print(ans,ans.text)
j_ans=json.loads(ans.text)
print(j_ans)


--Ethereum to INR:

import requests
import json

url= "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=INR"
print(url)
ans=requests.get(url)
print(ans,ans.text)
j_ans=json.loads(ans.text)
print(j_ans)

