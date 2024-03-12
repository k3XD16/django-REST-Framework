import requests

endpoint = 'http://localhost:8000/api/products/list/'

res = requests.get(endpoint)

# print(res.json())
print(res.text)
