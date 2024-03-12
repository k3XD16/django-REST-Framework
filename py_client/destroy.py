import requests

try:    
    id = int(input("Enter the Product ID: "))
except:
    id = None
    print(f"{id} is not valid")

if id:
    endpoint = f'http://localhost:8000/api/products/{id}/delete/'
    
    res = requests.delete(endpoint)

    # print(res.json())
    # print(res.text)
    print(res.status_code,res.status_code==204)
