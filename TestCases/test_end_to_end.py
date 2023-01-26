import requests
import json
import jsonpath

def test_add_student():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/APIAutomation2/files/RequestJson.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(url, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_url = "https://thetestingworldapi.com/api/technicalskills"
    f = open("C:/APIAutomation2/files/tech_details.json", 'r')
    request_json = json.loads(f.read())
    request_json['id'] = id[0]
    request_json['st_id'] = id[0]
    response = requests.post(tech_url, request_json)
    print(response.text)

    address_url = "https://thetestingworldapi.com/api/addresses"
    f = open("C:/APIAutomation2/files/address_details.json", 'r')
    request_json = json.loads(f.read())
    request_json['stId'] = id[0]
    response = requests.post(address_url, request_json)
    print(response.text)

    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(final_details)
    print(response.text)
