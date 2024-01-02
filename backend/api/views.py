import json

from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def api01_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hello World"})

def api02_home(request, *args, **kwargs):
    # print(dir(request))
    body = request.body
    # print(body)

    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data.keys())
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)