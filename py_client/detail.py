import requests

id = int(input("Enter the Product ID: "))

endpoint = f'http://localhost:8000/api/products/{id}/'

res = requests.get(endpoint)

print(res.json())
