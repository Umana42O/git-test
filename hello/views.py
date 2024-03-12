from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request,saludo):
    return HttpResponse(f"Hola, {saludo}")
