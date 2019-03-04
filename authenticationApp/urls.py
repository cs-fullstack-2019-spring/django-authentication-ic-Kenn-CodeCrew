from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name ='index'),
    path('newUser/', views.newUser, name ='newUser'),
    path('welcomeNewUser/', views.welcomeNewUser, name ='welcomeNewUser'),
]