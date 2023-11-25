"""
URL configuration for maketrips project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('maketripsapp.urls')),
    path('Login',include('maketripsapp.urls')),
    path('Logout',include('maketripsapp.urls')),
    path('verify',include('maketripsapp.urls')),
    path('signup',include('maketripsapp.urls')),
    path('home',include('maketripsapp.urls')),
    path('register',include('maketripsapp.urls')),
    path('gallery',include('maketripsapp.urls')),
    path('search',include('maketripsapp.urls')),
    path('addreview',include('maketripsapp.urls')),
    path('bookhotel',include('maketripsapp.urls')),
    path('hotel',include('maketripsapp.urls')),
    path('book',include('maketripsapp.urls')),
    path('view_more_gallery',include('maketripsapp.urls')),
    path('places',include('maketripsapp.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()
