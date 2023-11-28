from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Feedback(models.Model):
    username=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField( max_length=50)
    phone=models.CharField( max_length=10)
    email=models.CharField( max_length=50)
    desc=models.TextField()
    def __str__(self):
        return self.name
    
class Place(models.Model):
    placename=models.CharField(max_length=20,primary_key=True)
    placedescription=models.TextField()
    splace1=models.CharField( max_length=50)
    splace1description=models.TextField()
    splace2=models.CharField( max_length=50)
    splace2description=models.TextField()
    splace3=models.CharField( max_length=50)
    splace3description=models.TextField()
    splace4=models.CharField( max_length=50)
    splace4description=models.TextField()
    splace5=models.CharField( max_length=50)
    splace5description=models.TextField()

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

class Gallery(models.Model):
    Gallery_place=models.CharField(max_length=50,null=True)
    Gallery_img=models.CharField(max_length=100,null=True)
    Gallery_place_desc=models.TextField(null=True)
    def __str__(self):
        return self.Gallery_place

class Gallery_2(models.Model):
    G_place=models.CharField(max_length=50)
    Gallery_img=models.CharField(max_length=150)
    def __str__(self):
        return self.G_place
    
class TravellerDetail(models.Model):
    username=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    booking_id=models.IntegerField()
    h_name=models.CharField( max_length=60)
    T_FirstName=models.CharField(max_length=50)
    T_LastName=models.CharField(max_length=50)
    T_email=models.EmailField(max_length=254)
    T_contactNo=models.CharField(max_length=20,unique=True)
    T_address=models.CharField(max_length=70)
    room_type=models.CharField( max_length=100)
    days=models.IntegerField()
    T_pincode=models.IntegerField()
    T_country=models.CharField( max_length=50)
    special_req=models.TextField()
    def __str__(self):
        return self.T_FirstName

class vacations(models.Model):
    v_place=models.CharField(max_length=70)
    v_desc=models.TextField()
    img_link=models.CharField(max_length=150)
    def __str__(self):
        return self.v_place   

class package(models.Model):
    p_title=models.CharField(max_length=70)
    p_cname=models.CharField(max_length=70)
    p_img=models.CharField( max_length=150)
    No_D=models.IntegerField()
    No_N=models.IntegerField()
    No_F=models.IntegerField()
    No_H=models.IntegerField()
    p_price=models.IntegerField()
    Offer_type=models.CharField(max_length=50)
    p_item1=models.CharField(max_length=50)
    p_item2=models.CharField(max_length=50)
    p_item3=models.CharField(max_length=50)
    p_item4=models.CharField(max_length=50)
    p_item5=models.CharField(max_length=50,null=True)
    def __str__(self):
            return self.p_cname
    


# class trip(models.Model):
#     user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
#     place_name=models;models.CharField( max_length=50)
#     place_description=models.TextField()
#     place_image=models.ImageField(upload_to="places", height_field=None, width_field=None, max_length=None)
