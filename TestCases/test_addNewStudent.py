import requests
import json
import jsonpath

def test_add_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/APIAutomation2/files/RequestJson.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(API_URL, request_json)
    print(response.text)

def test_get_student_data2():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/4180500"
    response = requests.get(API_URL)
    # print(response.text)
    json_response = json.loads(response.text)
        # or
    # json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    # print(id)
    assert id[0] == 4180500

def test_update_student_data():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/4180500"
    f = open("C:/APIAutomation2/files/RequestJson.json", 'r')
    json_request = json.loads(f.read())
    response = requests.put(API_URL, json_request)
    print(response.text)

def test_delete_student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/4180482"
    response = requests.delete(API_URL)
    print(response.text)
# After deleting fetch the data it's an error occurred
def test_get_student_data1():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/4180500"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 4180500




