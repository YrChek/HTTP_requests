import requests
import time

files_url = 'https://api.stackexchange.com/2.3/search'
todate = int(time.time())
fromdate = todate - 172800
params = {"fromdate": str(fromdate), "todate": str(todate), "order": "desc", "sort": "creation", "tagged": "Python",
          "site": "stackoverflow"}
response = requests.get(files_url, params=params)
for titles in response.json()['items']:
    print(titles['title'])
