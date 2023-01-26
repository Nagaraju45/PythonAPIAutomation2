import jsonpath
import requests
import json

def test_get_student_data():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/APIAutomation2/files/RequestJson.json", 'r', encoding='utf-8')
    request_json = json.loads(f.read())
    response = requests.post(url, request_json)
    # print(response.text)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response, 'id')
    # print(id[0])
    assert id[0] != 3345