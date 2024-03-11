import requests


# endpoints = 'https://httpbin.org/'
endpoint = 'http://localhost:8000/api/'

# res = requests.get(endpoints, params={"abc": 212},json={"hi": "Hello world"})

res = requests.post(endpoint, json={ "brand": "Samsung" ,"model": "S24", "price" : 89900})

# print(res.headers)
# print(res.text)
# print(res.status_code)
print(res.json())

# code = res.status_code
# statuscode = {
#     "status code" : f'{code}',
# }
# print(statuscode)
