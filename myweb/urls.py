from django.contrib import admin
from django.urls import path, include
from . import views as auth_views


urlpatterns = [


     path('',auth_views.main,name='home'),
     path('<int:banner_id>/pu/',auth_views.up,name='h'),
     
]