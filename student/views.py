from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import TemplateView, RedirectView, CreateView, View,ListView
from django.views.generic.edit import UpdateView, FormView
from .backends import *
from .forms import StudentReg, LoginForm, BookForm
from .models import student
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .token import activation_token


class HomePage(TemplateView):
	template_name = 'students/index.html'

class StudentRegistr(FormView):
	template_name = 'students/studentReg.html'
	form_class = StudentReg
	model = student
	success_url = '/studentReg'

	def form_invalid(self, form):
		print('hh invalid')
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		
		response = super(StudentRegistr, self).form_invalid(form)
		if self.request.is_ajax():
			print('ajd')
			return JsonResponse(form.errors, status = 400)
		else:
			return response

	def form_valid(self, form):
		print('form valid')
		response = super(StudentRegistr, self).form_valid(form)
		print('fomr is validate')
		if self.request.is_ajax():
			print('ajax')
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			first_name = form.cleaned_data.get('first_name') 
			last_name = form.cleaned_data.get('last_name')
			email = form.cleaned_data.get('email')
			phone_number = form.cleaned_data.get('phone_number')
			location = form.cleaned_data.get('location')
			image = form.cleaned_data.get('file')
			resume = form.cleaned_data.get('file')
			print(username, password)
		
			new_student = student.objects.create_student(username, first_name, last_name, email, phone_number, location, image, resume, password)
			user = student.objects.get(username = username)
			print(user)
			user_id = user.pk
			print(user_id)
			current_site = get_current_site(self.request)
			message = render_to_string('students/mail.html',{'user': username,
				'domain': current_site,
				'token':activation_token.make_token(user),
				 'uid' : user_id
					
				})
			from_email = settings.EMAIL_HOST_USER 
			to_mail = 'irfan.kadavath@gmail.com'
			
			send_mail ('subject', message, from_email , [to_mail,]
				 ,fail_silently=False)
			print('mail send_mail')
			return response
		else:
			return response

			



	

class StudentLog(FormView):
	template_name  = 'students/studentLog.html'
	form_class = LoginForm
	# success_url = '/studentHome'
	
	def form_valid(self, form):
		password = form.cleaned_data.get('password')
		username = form.cleaned_data.get('username')
		print(username, password)
		user = StudentaAuth.authenticate(username =username, password= password)
		print(user)
		if user is not None :
			print('lmm')

			login(self.request, user)	
			
			return HttpResponseRedirect("/studentHome")
		return HttpResponseRedirect("/studentLog")

	



class StudentHome(TemplateView):
	template_name = 'students/studentHome.html'
	

def out(request):
	logout(request)
	return HttpResponseRedirect("/")


def set(request, username, token):
	user  = student.objects.get(username = username)
	if user is not None and activation_token.check_token(user, token):
		user.activate = True
		user.save()
		login(request, user)	
			
		return HttpResponseRedirect("/studentHome")
		# return HttpResponse('Your account is activated please login')
	else:
		return HttpResponse('Activation link is invalid!')



class CrudOperations(FormView):
	model =  student
	template_name = 'students/book.html'
	form_class = BookForm
	success_url = '/book'

	def form_valid(self, form):
		response = super(CrudOperations, self).form_valid(form)
		if self.request.is_ajax():

			print('jjj')
			
			print(form.cleaned_data	)

			return self.render_to_json_response(data)
		else:
			return response
			

	def list(request):
		book = Book.objects.all()
		return book

	class activate(View):
		def activate():
			if user is not None and activation_token.check_token(user, token):
				user.active = True
				user.save()
				login(request, user)
				# return redirect('dashboard')
				return HttpResponse('Your account is activated please login')
			
			else:
				return HttpResponse('Activation link is invalid!')