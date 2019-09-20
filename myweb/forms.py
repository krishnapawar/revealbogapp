from.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class BannerForm(forms.Form):
	banner1 = forms.ImageField()
	banner2 = forms.ImageField()
	banner3 = forms.ImageField()
	banner4 = forms.ImageField()
	banner5 = forms.ImageField()
	class Meta:
		fields = ['banner1','banner2','banner3','banner4','banner5']