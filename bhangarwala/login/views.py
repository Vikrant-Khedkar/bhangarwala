from asyncio.windows_events import NULL
import re
from django import forms
import email
from importlib.metadata import requires
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,UserManager
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login ,logout


# Create your views here.
#class userform(forms.Modelform)
from django.shortcuts import redirect

def register(request):
   if request.method == 'POST':
      username = request.POST['username']
      first_name = request.POST['fname']
      last_name = request.POST['lname']
      email = request.POST['email']
      password1 = request.POST['pass1']
      password2 = request.POST['pass2']

      myuser = User.objects.create_user(username=username, password=password1 ,email=email ,first_name=first_name ,last_name=last_name )
      myuser.save();
      print("User created")
      return render(request,'login/login.html')
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