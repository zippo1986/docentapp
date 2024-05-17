from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path("index/", views.index),
    path("about/", views.about)
    
]