from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [


     path('',views.main,name='home'),
     path('update/<int:pk>',views.Bupdate.as_view(),name='updatebanner')
]