import requests

headersData = {'T1':'First Header', 'T2':'Second Header'}

response = requests.get("https://httpbin.org/get", headers = headersData)
print(response.text)