import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name':'sugiyan',
    'roll':101,
    'city':'calicut'
}

json_data = json.dumps(data)
print('json_data',json_data)

response = requests.post(url=URL,data=json_data)
print('response',response.content)

data = response.json()
print(data)