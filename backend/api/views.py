from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def api_home(request, *args, **kwargs):
    
    print(request.GET)
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    print(request.headers)
    # json.dumps(request.headers)
    data['params'] = request.GET
    data['Headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    
    return JsonResponse(data)
    
    # return JsonResponse(
    #     {"greet":"Welcome to Django REST Framework API!!",
    #      "name":"hello",
    #      "age": 25,
    #      "version": "v1.0.1",
    #     })