from . models import *
from django.conf import settings


class TeachertaAuth:
	def authenticate(request, username=None, password=None):
		try:
			user = Teacher.objects.get(username = username)
			if user.check_password(password):
				return user
			else:
				return None
		except Teacher.DoesnotExist:
			
			return None

	