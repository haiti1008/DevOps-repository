import requests
import json
import os

access_token = os.environ.get('WEBEX_TOKEN')

url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# Replace with the email of a contact you added in Webex Teams
params = {
    'email': 'contact@example.com'
}

res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

# Use the 'id' value from the response above to get extra details
person_id = 'plak_hier_de_id_uit_vorige_output'

url = 'https://webexapis.com/v1/people/{}'.format(person_id)
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

