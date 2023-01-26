import requests
# API url
url = "https://reqres.in/api/users?page=2"
# Send Request
response = requests.get(url)
# print(response)
# Display Response Content
# print(response.content)
# Display Response Header
# print(response.headers)
# print(response.status_code)
# Validate status code
assert response.status_code == 200
# assert response.status_code == 201

# Fetch Response Header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))
print(response.headers.get('NEL'))

# Fetch Cookies
print(response.cookies)
# Fetch Encoding
print(response.encoding)
# Fetch Elapsed
print(response.elapsed)
