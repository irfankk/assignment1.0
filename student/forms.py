from django import forms
from .models import *
import re
from django.core.validators import RegexValidator

class StudentReg(forms.ModelForm):
	password1 = forms.CharField(max_length=200, widget=forms.PasswordInput)
	password = forms.CharField(max_length=200, widget=forms.PasswordInput)
	
	class Meta:
		model = student
		fields = ['username' ,'first_name', 'last_name','phone_number' ,'email',  'location', 'image', 'resume' ]

	def clean_password(self):

		password = self.cleaned_data.get('password')
		password1  = self.cleaned_data.get('password1')
		if len(password) < 8:
			raise forms.ValidationError('password should be minimum 8 charecter')
		if len(password) > 16:
			raise forms.ValidationError('password lenght not more than 16 charecter')
		if password != password1:
			raise forms.ValidationError('Password donot match')
		return password
	
	def clean_first_name(self):
		pattern = re.compile(r'^[a-zA-Z]+$')
		first_name = self.cleaned_data.get('first_name')
		if len(first_name) < 2:
			raise forms.ValidationError('first name should be minimun two charecter')
		if pattern.match(first_name):
			return first_name
		else:
			raise forms.ValidationError('first number should be alhabets')
			
	 
	def clean_phone_number(self):
		pattern = re.compile(r'^((?!(0|1|2|3|4|5))[0-9]{10,10})$')
		phone_number = self.cleaned_data.get('phone_number')
		if pattern.match(phone_number):
			return phone_number
		else:
			raise forms.ValidationError('mobile number should be valid')
		

	def clean_username(self):
		username = self.cleaned_data.get('username')
		pattern = re.compile(r'^[a-zA-Z0_9]+$')
		if len(username) < 2:
			raise forms.ValidationError('username should be more than two charecter')
		if pattern.match(username):
			return username
		else:
			return forms.ValidationError('username only number and alphebets')	
	
	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name')
		pattern = re.compile(r'^[a-zA-Z]+$')
		if len(last_name) < 2:
			raise forms.ValidationError('last name should be minimun two charecter')
		if pattern.match(last_name):
			return last_name
		else:
			raise forms.ValidationError('first name should be alphabets')

	def clean_location(self):
		location = self.cleaned_data.get('location')
		pattern = re.compile(r'^[a-zA-z]+$')
		if len(location) < 2:
			raise forms.ValidationError('Location should be more than two charecter')
		if pattern.match(location):
			return location
		else:
			raise forms.ValidationError('location only alphabets')


	

class LoginForm(forms.Form):
	username = forms.CharField(max_length=200)
	password = forms.CharField(max_length=200)


class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['name', 'author_name', 'publication']



		#' ,, 