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
    path('home',views.home,name="home"),
    path('gallery',views.gallerytemp,name="gallery"),
    path('search',views.search,name="search"),
    path('addreview',views.addreview,name="addreview"),
    path('bookhotel',views.bookhotel,name="bookhotel"),
    path('hotel/<int:hid>',views.hotel,name="hotel"),
    path('book/<HotelName>',views.book,name="book"),
    path('gallery/<galleryplace>',views.gallery,name="gallery"),
    path('places/<place>',views.places,name="places"),
    path('view_more_gallery',views.view_more_gallery,name="view_more_gallery"),
    path('packages',views.package_temp,name="packages")
]