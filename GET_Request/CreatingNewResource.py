import json
import jsonpath
import requests

url = "https://reqres.in/api/users"
# Read json input
file = open("C:\\APIAutomation2\\files\\CreateUser.json", "r")
json_input = file.read()
request_json = json.loads(json_input)
# print(request_json)
# Make POST request with json body
response = requests.post(url, request_json)
# print(response)
# Validating response code
assert response.status_code == 201
# Fetch headers from Response
print(response.headers)
print("----------")
print(response.headers.get('Server'))
# Parse response to json format
response_json = json.loads(response.text)
# Pick id using jsonpath
std_id = jsonpath.jsonpath(response_json, 'id')
print(std_id[0])
