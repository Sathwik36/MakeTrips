from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Feedback(models.Model):

    name=models.CharField( max_length=50)
    phone=models.CharField( max_length=10)
    email=models.CharField( max_length=50)
    desc=models.TextField()
    def __str__(self):
        return self.name
    
class Place(models.Model):
    placename=models.CharField(max_length=20,primary_key=True)
    placedescription=models.TextField()
    placeimage=models.ImageField(upload_to="places")
    placeimage2=models.ImageField(upload_to="places")
    placeimage3=models.ImageField(upload_to="places")
    placeimage4=models.ImageField(upload_to="places")
    def __str__(self):
        return self.placename
    
class Myreviews(models.Model):
    username=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    review_place=models.CharField( max_length=50)
    rating_no=models.IntegerField()
    review_desc=models.TextField()
    # def __str__(self) :
    #     return self.username

class Hotels(models.Model):
    hotel_name=models.CharField( max_length=50)
    hotel_addresss=models.TextField()
    hotel_rating=models.IntegerField()
    hotel_price=models.IntegerField()
    hotel_location=models.CharField( max_length=50)
    hotel_desc=models.TextField()
    hotel_Mainimage=models.ImageField(upload_to="hotels")
    hotel_image1=models.ImageField(upload_to="hotels")
    hotel_image2=models.ImageField(upload_to="hotels")
    hotel_image3=models.ImageField(upload_to="hotels")
    def __str__(self):
        return self.hotel_name
    
class TravellerDetail(models.Model):
    username=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    booking_id=models.IntegerField()
    h_name=models.CharField( max_length=60)
    T_FirstName=models.CharField(max_length=50)
    T_LastName=models.CharField(max_length=50)
    T_email=models.EmailField(max_length=254)
    T_contactNo=models.CharField(max_length=20)
    T_address=models.CharField(max_length=70)
    room_type=models.CharField( max_length=100)
    days=models.IntegerField()
    T_pincode=models.IntegerField()
    T_country=models.CharField( max_length=50)
    special_req=models.TextField()
    def __str__(self):
        return self.T_FirstName
    



# class trip(models.Model):
#     user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
#     place_name=models;models.CharField( max_length=50)
#     place_description=models.TextField()
#     place_image=models.ImageField(upload_to="places", height_field=None, width_field=None, max_length=None)
