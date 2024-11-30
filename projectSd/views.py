from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, "hello.html")

def someS(request):
    return render(request, "base.html")

def Home(request):
    prj = {
        "prjseed": "PROJECT BIBEK"
    }
    return render(request, "index.html", prj)