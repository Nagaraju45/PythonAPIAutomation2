import json

import jsonpath as jsonpath
import requests

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

# Parse Response to Json format
json_response = json.loads(response.text)
# print(json_response)

# Fetch Value using Jsonpath
pages = jsonpath.jsonpath(json_response, "total_pages")
print(pages)
# assert pages[0] == 2

# first_name = jsonpath.jsonpath(json_response, "data[1].first_name")
# print(first_name[0])
for i in range(0, 3):
    first_name = jsonpath.jsonpath(json_response, "data["+str(i)+"].first_name")
    print(first_name[0])