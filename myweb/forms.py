from.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class BannerForm(forms.ModelForm):
	class Meta:
		model = banner
		fields = ['banner1','banner2','banner3','banner4','banner5']