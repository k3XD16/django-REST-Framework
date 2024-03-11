from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse , HttpResponse
import json

from products.models import Product

# Create your views here.
def api_home(request, *args, **kwargs):
    
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
        # print(data)
    return JsonResponse(data)
        
    #     print(data)
    #     data =dict(data)
    #     json_data = json.dumps(data)
    # return HttpResponse(json_data , headers={"content-Type":"application/json"})
    
    
    # print(request.GET)
    # print(request.POST)
    # body = request.body
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # print(request.headers)
    # # json.dumps(request.headers)
    # data['params'] = request.GET
    # data['Headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    
    # return JsonResponse(
    #     {"greet":"Welcome to Django REST Framework API!!",
    #      "name":"hello",
    #      "age": 25,
    #      "version": "v1.0.1",
    #     })
    