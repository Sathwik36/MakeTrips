from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class feedback(models.Model):

    name=models.CharField( max_length=50)
    phone=models.CharField( max_length=10)
    email=models.CharField( max_length=50)
    desc=models.TextField()
    def __str__(self):
        return self.name

class trip(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    place_name=models;models.CharField( max_length=50)
    place_description=models.TextField()
    place_image=models.ImageField(upload_to="places", height_field=None, width_field=None, max_length=None)
