import requests

endpoint = f'http://localhost:8000/api/products/'

data = {
    "brand" : "Nothing",
    "model" : "Phone (1)",
    "price" : "38900"   
}
res = requests.post(endpoint, json=data)

print(res.json())
