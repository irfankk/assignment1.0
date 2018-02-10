from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.conf import settings

class Activation(PasswordResetTokenGenerator):
	def make(self, user):
		last_login = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
		return (
			six.text_type(timestamp) +
			six.text_type(user.activate)
			)


activation_token = Activation()