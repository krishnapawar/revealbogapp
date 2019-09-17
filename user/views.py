from django.shortcuts import render,redirect
from myweb.models import clients
from.models import photfolio
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
# Create your views here.


class ClientsListView(LoginRequiredMixin,ListView):
	model = clients
	template_name = 'user/messegeshow.html'
	context_object_name = 'q'
	ordering = ['-date']
	paginate_by = 3

'''@login_required(login_url='login')
def messegeshow(request):
	p = clients.objects
	return render(request,'user/messegeshow.html',{'q':p})'''

@login_required(login_url='login')
def enterphotfolio(request):
	if request.method == 'POST':
		if request.FILES['img'] and request.POST['txt']:
			p = photfolio()
			p.popupimg = request.FILES['img']
			p.item = request.POST['txt']
			p.date = timezone.datetime.now()
			p.save()
			messages.success(request,f'your data enter successful')
			return redirect('photfolioadd')
		else:
			return render(request,'user/photfoliadd.html')
	else:
		return render(request,'user/photfoliadd.html')

@login_required(login_url='login')
def useradmin(request):
	return render(request,'user/user_home.html')



def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('userad')
		else:
			return render(request,'user/loginn.html', {'err':'user name or password does not match' })

	else:
		return render(request,'user/loginn.html')


def signup(request):
	if request.method == 'POST':
		if request.POST['p1'] == request.POST['p2']:
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request,'user/signup.html',{'err':'your name is already existed.'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'],password=request.POST['p2'])
				auth.login(request, user)
				return redirect('ulogin')

		else:
			return render(request,'user/signup.html',{'err':'your password does nat match '})

	else:
		return render(request,'user/signup.html')


