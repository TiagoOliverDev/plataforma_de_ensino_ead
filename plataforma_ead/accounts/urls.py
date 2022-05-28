from django import urls
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    
    path('register/', views.SignUp.as_view(), name="signup"),
    
]

