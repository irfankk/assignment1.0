from django import forms
from .models import *

class TeacherReg(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ['username', 'password', 'email']


class TeacherForm(forms.Form):
	username = forms.CharField(max_length=200)
	password = forms.CharField(max_length=200)