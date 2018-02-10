from . models import *
from django.conf import settings
from .views import *
from django.http import HttpResponse


class StudentaAuth:
	def authenticate(username=None, password=None):
		try:
			user = student.objects.get(username = username)
			if user.check_password(password):
				return user
			
		except student.DoesNotExist:
			return None

	
	def get_user(self, user_id):
			try:
				user = student.objects.get(pk=user_id)
				return user
			except student.DoesNotExist:
				return None

