from django.contrib import admin
from django.urls import path,include
from client import views

urlpatterns = [
    path('getall/', views.get, name="getall"),
    path('create/', views.create, name="create"),
    
]


        