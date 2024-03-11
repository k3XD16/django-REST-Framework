import requests

endpoint = f'http://localhost:8000/api/products/'

data = {
    "brand" : "test",
    "model" : "null",
    "price" : "0"   
}
res = requests.post(endpoint, json=data)

print(res.json())
