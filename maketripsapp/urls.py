from django.contrib import admin
from django.urls import path
from maketripsapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('Login',views.Login,name='Login'),
    path('Logout',views.Logout,name='Logout'),
    path('verify',views.verify,name='verify'),
    path('signup',views.signup,name="signup"),
    path('register',views.register,name="register"),
    path('home',views.home,name="home")
]