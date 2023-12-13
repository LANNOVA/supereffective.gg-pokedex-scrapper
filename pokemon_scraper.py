import requests
import csv
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
API = response.json()
count = 0


with open('pokemon_data.csv', 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile)


    csvwriter.writerow(['Name', 'Color', 'Generation', 'Region', 'Type1', 'Type2'])

    while count < len(API):
        name = API[count]['name']
        color = API[count]['color']
        generation = API[count]['generation']
        region = API[count]['region']
        type1 = API[count]['type1']
        type2 = API[count]['type2']


        csvwriter.writerow([name, color, generation, region, type1, type2])

        count += 1
     
# results at pokemon_data.csv
