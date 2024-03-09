from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    return JsonResponse(
        {"greet":"Welcome to Django REST Framework API!!",
         "name":"hello",
         "age": 25,
         "version": "v1.0.1",
        })