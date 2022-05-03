from django import urls
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('cursos/', views.index, name='index'),
    #path(r'^(?P<pk>\d+)/$', views.details, name='details'),
    #path('detalhes/<int:id>', views.detalhes, name='detalhes'),
    path('cursos/<int:id>/', views.details, name='details'), #<int:id>/ serve para que o id do objeto seja posto no id que é parêmetro na respectiva view, assim abrindo uma pag somente daquele objeto
    
]


