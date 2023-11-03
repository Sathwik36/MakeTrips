from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from maketripsapp.models import *
from .apifunc import Search_image
from django.db.models import Q
from datetime import datetime
import random
from django.conf import settings

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
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
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
    return render(request,'home.html', {'querys':Myreviews.objects.all() , 'galleries':Gallery.objects.all(),"gallery2":Gallery_2.objects.all()})

def gallerytemp(request):
    return render(request,'gallery.html')

def gallery(request,galleryplace):
    data=Search_image(galleryplace)
    image_data = [ images["urls"]["regular"] for images in data["results"]]
    return render(request,'gallery.html',{'images':image_data})

def view_more_gallery(request):
    if request.method=="POST":
        query=request.POST.get('search_gallery')
        data=Search_image(query)
        image_data = [ images["urls"]["regular"] for images in data["results"]]
        return render(request,'gallery.html',{'images':image_data})

def search(request):
    if request.method=="POST":
        searchedb=request.POST['search_box']
        if  Place.objects.filter( Q(placename__icontains=searchedb)).exists() :
            place=Place.objects.filter( Q(placename__icontains=searchedb) )
            return render(request,'search_temp.html',{'searched':place,'placename':searchedb})
        else:
            data=Search_image(searchedb)
            image_data = [ images["urls"]["regular"] for images in data["results"]]
            return render(request,'search_temp.html',{'images':image_data,'placename':searchedb})
    
def addreview(request):
    if request.method=="POST":
        username=request.user
        review_place=request.POST.get('place_visited')
        rating=request.POST.get('rating')
        review=request.POST.get('review')
        myrevw=Myreviews.objects.create(
            username=username,
            review_place=review_place,
            rating_no=rating,
            review_desc=review,            
        )
        myrevw.save()
    return redirect("/")

def bookhotel(request):
    if request.method=="POST":
        splace=request.POST.get('to_place')
        splace_hotels=Hotels.objects.filter(
            Q(hotel_location__icontains=splace)
        )
        return render(request,'hotels.html',{'hotels':splace_hotels})
    
@login_required(login_url='Login')
def hotel(request,hid):
    hotel=Hotels.objects.filter(id=hid)
    return render(request,'hotel.html',{'hotel':hotel})

def book(request,HotelName):
    if request.method=="POST":
        username=request.user
        booking_id=random.randint(111111,999999)
        h_name=HotelName
        fname=request.POST.get('tfname')
        lname=request.POST.get('tlname')
        email=request.POST.get('temail')
        phone=request.POST.get('tphone')
        addr=request.POST.get('taddress')
        room=request.POST['troom']
        tdays=request.POST.get('tdays')
        tpin=request.POST.get('tpin')
        country=request.POST.get('country')
        sreq=request.POST.get('sreq')
        travelinfo=TravellerDetail.objects.create(
            username=username,
            booking_id=booking_id,
            h_name=h_name,
            T_FirstName=fname,
            T_LastName=lname,
            T_email=email,
            T_contactNo=phone,
            T_address=addr,
            room_type=room,
            days=tdays,
            T_pincode=tpin,
            T_country=country,
            special_req=sreq,
        )
        travelinfo.save()
        booking_info=TravellerDetail.objects.filter(T_contactNo=phone)
    return render(request,'book.html',{'booking_info':booking_info})
