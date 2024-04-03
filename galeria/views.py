from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> Fancisco Frutuoso da Silva</h1>')