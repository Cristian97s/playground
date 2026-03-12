from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# usando funciones
def index(request):
    return HttpResponse("hola mundo desde Django!")