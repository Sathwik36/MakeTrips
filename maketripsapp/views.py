from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def Login(request):
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect("/home")

def verify(request):
   if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
             # A backend authenticated the credentials
            # return render(request,'home.html')
            login(request, user)
            messages.success(request,"Successfully Logged In")
            return redirect("/home")
        else:
            # No backend authenticated the credentials
            messages.error(request,"Invalid Cresentials")
            return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            return HttpResponse("Username alredy exists")
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()

    return redirect('/')

def home(request):
    return render(request,'home.html')