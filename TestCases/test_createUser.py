import jsonpath
import requests
import json
import pytest
url = "https://reqres.in/api/users"
# a = 11
# @pytest.mark.skipif(a == 10, reason = "This is not ready for build")
@pytest.fixture
def start_exec():
    global file
    file = open("C:\\APIAutomation2\\files\\CreateUser.json", "r")
@pytest.mark.Smoke
def test_create_new_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201
    print(response.headers)

@pytest.mark.Sanity
def test_create_other_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])
