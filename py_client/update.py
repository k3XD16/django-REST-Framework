import requests

id = int(input("Enter the Product ID: "))

endpoint = f'http://localhost:8000/api/products/{id}/update/'

data = {
    "brand" : "Nothing",
    "model" : "Phone (1)",
    "price" : "29999",
}

res = requests.put(endpoint,json=data)

print(res.json())
# print(res.text)
