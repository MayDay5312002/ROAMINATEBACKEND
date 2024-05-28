from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def main(request):
    data = {
        'user' : 'test111',
        'pass' : 'test111'
    }
    return JsonResponse(data)


    