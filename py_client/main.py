import requests


# endpoints = 'https://httpbin.org/'
endpoints = 'http://localhost:8000/api/'

res = requests.get(endpoints)

print(res.json())
print("") 
print(res.status_code)
print("")
print(res.json()['greet'])
