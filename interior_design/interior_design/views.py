# code is contributed by Yuvraj
import http
from pickle import GET
from django.http import HttpResponse
from requests import request
from django.shortcuts import render


def index(request):
    fimg = request.GET.get('2.jpg', 'default')
    return render(request, 'index.html')


def home(request):
    return HttpResponse(''' <h1> Home </h1> <a href="http://127.0.0.1:8000/capfirst"> Cap_First </a> ''')


def capfirst(request):
    return HttpResponse(''' <h1> Cap First </h1>   ''')


def charcount(request):
    return HttpResponse("charcount")
