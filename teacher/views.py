from django.shortcuts import render
from django.http import HttpResponse
from .backends import *
from .forms import *
from .models import *

def teacherReg(request):
	if request.method =='POST':
		form = TeacherReg(request.POST)
		if form.is_valid():
			password = form.cleaned_data.get('password')
			username = form.cleaned_data.get('username')
			phone_number = 1234567890
			new_student = Teacher.objects.create_teacher(username, password, phone_number)
			return HttpResponse("Teacher is created")
	return render(request, 'teacher/teacherReg.html')




def teacherLog(request):
	if request.method == 'POST':
		form = TeacherForm(request.POST)
		if form.is_valid():
			password =form.cleaned_data.get('password')
			username = form.cleaned_data.get('username')
			user = TeachertaAuth.authenticate(request, username =username, password= password)
			if user is not None:
				return HttpResponse("Teacher loged in")
			else: 
				return HttpResponse('error for loging')


	return render(request, 'teacher/teacherLog.html')

