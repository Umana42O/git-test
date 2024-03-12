from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    nombre = "Tuma"
    data = {'nombre': nombre}
    return render(request,"./home/index.html", data)

