from . models import *
from django.conf import settings


class StudentaAuth:
	def authenticate(request, username=None, password=None):
		user = student.objects.get(username = username)
		if user.check_password(password):
			return user
		else:
			return None
		
		
	def get_user(self, user_id):
		try:
			user = student.objects.get(pk=user_id)
			return user
		except student.DoesnotExist:
			return None	
