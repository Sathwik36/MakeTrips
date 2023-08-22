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

# class trip(models.Model):
#     user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
#     place_name=models;models.CharField( max_length=50)
#     place_description=models.TextField()
#     place_image=models.ImageField(upload_to="places", height_field=None, width_field=None, max_length=None)
