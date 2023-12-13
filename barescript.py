import requests
import time
url = "https://cdn.supeffective.com/dataset/legacy-pokemon.min.json"

payload = {}
headers = {
  'authority': 'cdn.supeffective.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.8',
  'origin': 'https://supereffective.gg',
  'referer': 'https://supereffective.gg/',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'sec-gpc': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)
import json
API = json.loads(response.text)
count = 0



while count < len(API[count]['name']):
    name = API[count]['name']
    color = API[count]['color']
    generation = API[count]['color']
    region = API[count]['region']
    type1 = API[count]['type1']
    type2 = API[count]['type2']
   
    print(name)
    print(color)
    print(generation)
    print(region)
    print(type1)
    print(type2)
    count = count + 1
    time.sleep(0.5)    
