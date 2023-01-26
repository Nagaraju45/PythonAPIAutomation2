import jsonpath
import requests
import json

def test_add_new_student():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/APIAutomation2/files/st_details.json", 'r')
    json_request = json.loads(f.read())
    response = requests.post(url, json_request)
    print(1)
    print(response.text)

def test_get_student_data():
    url = "https://thetestingworldapi.com/api/studentsDetails/4179136"
    response = requests.get(url)
    json_response = json.loads(response.text)
    print(2)
    print(json_response)

def test_update_student_data():
    url = "https://thetestingworldapi.com/api/studentsDetails/4179136"
    f = open("C:/APIAutomation2/files/st_details.json", 'r')
    json_request = json.loads(f.read())
    response = requests.put(url, json_request)
    print(3)
    print(response.text)

# def test_delete_studen():
#     url = "https://thetestingworldapi.com/api/studentsDetails/4179136"
#     response = requests.delete(url)
#     print(4)
#     print(response.text)

def test_get_student_data1():
    url = "https://thetestingworldapi.com/api/studentsDetails/4180500"
    response = requests.get(url)
    json_response = json.loads(response.text)
    print(5)
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 4180500

