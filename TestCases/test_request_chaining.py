import requests
import json
import jsonpath


def test_add_new_student():
    global std_id
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/APIAutomation2/files/request_data.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(url, request_json)
    std_id = jsonpath.jsonpath(response.json(), 'id')
    print(std_id[0])


def test_get_student_data():
    url = "https://thetestingworldapi.com/api/studentsDetails/" + str(std_id[0])
    response = requests.get(url)
    print(response.text)
