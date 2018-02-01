from django.shortcuts import render
from django.http import HttpResponse
from .backends import *
from .forms import *
from .models import *




def home(request):
	return render(request, 'students/index.html')


def studentReg(request):
	if request.method =='POST':
		print('post')
		form = StudentReg(request.POST)
		print('object')
		if form.is_valid():
			print('validate')
			password = form.cleaned_data.get('password')
			username = form.cleaned_data.get('username')
			print(username, password)

			new_student = student.objects.create_student(username, password)
			print('created')
			return redirect('studentLog')
	return render(request, 'students/studentReg.html')

def studentLog(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		print('object')
		if form.is_valid():
			print('validate')
			password = form.cleaned_data.get('password')
			username = form.cleaned_data.get('username')
			print(password, password)

			user = StudentaAuth.authenticate(request, username =username, password= password)
			print(user)
			if user is not None:
				return HttpResponse("studentis loged in")
			else:
				render(request, 'students/studentLog.html')


		
		
		
	return render(request, 'students/studentLog.html')