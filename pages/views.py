from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hellooo</h1>")

def logs_view(*args, **kwargs):
    return HttpResponse("<h1>da log</h1>")