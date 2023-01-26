import requests
import jsonpath
import json

def test_oauth_api():
    #  swagger/docs/v1
    token_url = "https://thetestingworldapi.com/Token"
    data = {"grant_type":"password", "username":"admin", "password":"pass123"}
    response = requests.post(token_url, data)
    # print(response.text)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')
    auth = {"Authorization":"Bearer"+token_value[0]}
    API_URL = "https://thetestingworldapi.com/api/StDetails/1105"
    response = requests.get(API_URL, headers=auth)
    print(response.text)
