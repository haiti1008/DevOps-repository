import requests
import os

access_token = os.environ.get('WEBEX_TOKEN')
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNjU4OTVhMzAtOWYyNi0xMWYxLWExMGUtMzMxOWY3ZjU4ZDhj'

url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id}

res = requests.get(url, headers=headers, params=params)
print(res.json())
