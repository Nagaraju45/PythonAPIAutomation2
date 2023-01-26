import requests

param = {'name':'Rohit', 'email':'rohit123@gmail.com', 'number':'123'}
response = requests.get("https://httpbin.org/get", params = param)
print(response.text)