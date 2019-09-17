from django.shortcuts import render,redirect,get_object_or_404
from .models import clients,banner
from django.utils import timezone
from user.models import photfolio
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.edit import UpdateView 


# Create your views here.

def main(request):
	p = photfolio.objects.all()
	b = banner.objects.all()

	if request.method =='POST':
		if  request.POST['name'] and request.POST['email'] and request.POST['subject'] and request.POST['message']:
			clien = clients()
			clien.name = request.POST['name']
			clien.email = request.POST['email']
			clien.subject = request.POST['subject']
			clien.massage = request.POST['message']
			clien.date = timezone.datetime.now()
			clien.save()
			return redirect('home')
		else:
			return render(request,'myweb/index.html',{'p1':p,'w':b,'err':'please fill the block'})
	else:
		return render(request,'myweb/index.html',{'p1':p,'w':b})

# Create your views here.

def updatebanner(request,banner_id):
	b = get_object_or_404(banner, id = banner_id)
	return render(request,'myweb/bannerup.html',{'bb':b})

class Bupdate(UpdateView):
	model = banner
	fields = ['banner1','banner2','banner3','banner4','banner5']
		

