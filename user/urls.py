from django.urls import path
from.import views
from.views import ClientsListView

urlpatterns = [
            
            path ('massege/',ClientsListView.as_view(), name= 'messegeshow'),
            path('photfolioadd/',views.enterphotfolio,name ='photfolioadd'),
            path('user/',views.useradmin,name='userad'),
            path('userlogin/',views.login,name='ulogin'),
            path('signup/',views.signup,name='signup'),



]