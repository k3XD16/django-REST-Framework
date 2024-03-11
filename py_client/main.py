import requests


# endpoints = 'https://httpbin.org/'
endpoints = 'http://localhost:8000/api/'

res = requests.get(endpoints)

# print(res.headers)
print(res.text)
print(res.status_code)

# print(res.json())
# code = res.status_code

# statuscode = {
#     "status code" : f'{code}',
# }
# print(statuscode)
