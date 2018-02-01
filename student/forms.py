from django import forms
from .models import *

class StudentReg(forms.ModelForm):
	class Meta:
		model = student
		fields = ['username', 'password', 'email']


class LoginForm(forms.Form):
	username = forms.CharField(max_length=200)
	password = forms.CharField(max_length=200)