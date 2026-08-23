import requests
import os

access_token = os.environ.get('WEBEX_TOKEN')
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNjU4OTVhMzAtOWYyNi0xMWYxLWExMGUtMzMxOWY3ZjU4ZDhj'
message = 'Hello **DevNet Associates**!!'

url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}

res = requests.post(url, headers=headers, json=params)
print(res.json())
