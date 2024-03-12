import requests

endpoint = 'http://localhost:8000/api/products/list/'

res = requests.post(endpoint)

# print(res.json())
print(res.text)
