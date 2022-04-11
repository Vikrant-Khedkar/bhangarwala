from asyncio.windows_events import NULL
from django import forms
import email
from importlib.metadata import requires
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login ,logout


# Create your views here.
#class userform(forms.Modelform)
from django.shortcuts import redirect

def register(request):
       return render(request,'login/register.html')

   

def signin(request): 
    if request.method == "POST":
       usern = request.POST['username']
       passw = request.POST['password']

       user = authenticate(username= usern, password=passw)
       if user is not  None: 
          print('Working')
          login(request, user)
          fname= user.first_name
          return render(request,"home/index.html",{'fname':fname})
       else:
          print('failed')
          messages.success(request,("Bad credentials"))
          #return redirect('login')

    return render(request,'login/login.html') 