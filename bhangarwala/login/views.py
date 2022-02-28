from django.shortcuts import render
from flask import request


# Create your views here.

def register(request):
   return render(request,'login/register.html')

def login(request):
    return render(request,'login/login.html')