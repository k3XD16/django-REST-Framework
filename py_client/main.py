import requests


# endpoints = 'https://httpbin.org/'
endpoints = 'http://localhost:8000/api/'

res = requests.get(endpoints , params={"abc": 212},json={"hi": "Hello world"})

# print(res.headers)
# print(res.text)
# print(res.status_code)
print(res.json())
