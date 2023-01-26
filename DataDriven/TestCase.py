import requests
import json
from DataDriven import Library


def test_add_multiple_data():

    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:/APIAutomation2/files/add_new_student.json")
    json_request = json.loads(f.read())

    obj = Library.Common("C:/Users/nagar/OneDrive/Documents/add_students.xlsx", "Sheet1")
    row = obj.fetch_row_count()
    key_lists = obj.fetch_key_names()

    for i in range(2, row + 1):
        updated_json_request = obj.update_request_with_data(i, json_request, key_lists)
        response = requests.post(url, updated_json_request)
        print(response.text)
