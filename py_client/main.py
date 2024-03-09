import requests


# endpoints = 'https://httpbin.org/'
endpoints = 'http://localhost:8000'

res = requests.get(endpoints, json= {"hi":"hello"})

print(res.text) 
print(res.status_code)
