from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Base home page
from django.shortcuts import redirect

def home_view(request):
    if request.user.is_authenticated:
        return redirect("logs")  # or "dashboard" later
    return redirect("login")
