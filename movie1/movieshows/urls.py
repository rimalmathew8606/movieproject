"""
URL configuration for movie1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from movieshows import views
app_name="movieshows"

urlpatterns = [
    path('',views.home,name="home"),
    path('movie/<int:movie_id>/',views.details,name="detail"),
    path('addmovies/',views.addmovies,name="addmovies"),
    path('viewmovie',views.viewmovie,name="viewmovie"),
    path('edit/<int:p>', views.edit, name="edit"),
    path('delete/<int:p>', views.delete, name='delete'),




]
