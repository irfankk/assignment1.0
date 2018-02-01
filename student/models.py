from django.db import models
from django.contrib.auth.models import   BaseUserManager, AbstractBaseUser
import uuid






class StudentManager(BaseUserManager):

	def create_user(self, username, password = None):
		student= self.model(
			username = username)
		student.set_password(password)
		student.save(using=self._db)
		return student

	

	def create_student(self, username, password):
		student = self.create_user(
			username,
			password = password)
		
		student.student = True
		student.save()


class student(AbstractBaseUser):
	username =	models.CharField(max_length=200, unique= True)
	first_name = models.CharField(max_length = 200)
	last_name =models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	phone_number = models.IntegerField()
	student = models.BooleanField(default=False) 
	created = models.DateTimeField(auto_now_add=True)
	location = models.CharField(max_length=300)
	uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	objects= StudentManager()

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	
	@property
	def is_student(self):
		return self.student


