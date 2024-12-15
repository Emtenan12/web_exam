from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('Landing_Page/', views.Landing_Page,name= "books.Landing_Page"),
    path('list_games/', views.list_games,name= "books.list_games"),
    



     
]

