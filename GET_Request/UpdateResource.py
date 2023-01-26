import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

# Read Json Input
file = open("../files/UpdateUser.json", "r")
json_input = file.read()
request_json = json.loads(json_input)

response = requests.put(url, request_json)
assert response.status_code == 200

print(response.headers)

response_json = json.loads(response.text)

update_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(update_li[0])


