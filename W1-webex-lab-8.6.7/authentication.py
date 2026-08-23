import requests
import json
import os

# Read token from environment variable instead of hardcoding it
access_token = os.environ.get('WEBEX_TOKEN')

url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

