from django.db import models
from django.contrib.auth.models import   BaseUserManager, AbstractBaseUser
import uuid
from django.utils import timezone
from time import time


# def change_name(instance, filename):
# 	return  "	uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class StudentManager(BaseUserManager):

	def create_user(self, username, first_name, last_name, email, phone_number, location , image, resume,  password ):
		student= self.model(
			username = username,
			first_name = first_name, 
			last_name = last_name,
			email= email,
			phone_number = phone_number,
			location=location,
			image = image,
			resume = resume,
			# password  =password
			)
		student.set_password(password)
	
		student.save(using=self._db)
			
		return student

	

	def create_student(self, username, first_name, last_name, email, phone_number, location ,image, resume,password, ):
		student = self.create_user(
			username,
			first_name,
			last_name,
			email,
			phone_number,
			location,
			image,
			resume,
			password = password)
		
		student.student = True
		student.activate = False
		student.save()
	

class student(AbstractBaseUser):
	username =	models.CharField(max_length=200, unique= True)
	first_name = models.CharField(max_length = 200)
	last_name =models.CharField(max_length = 200)
	email = models.EmailField()
	phone_number = models.CharField(max_length=12, unique=True, blank=True)
	student = models.BooleanField(default=False) 
	created = models.DateTimeField(default=timezone.now)
	location = models.CharField(max_length=300)
	uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image = models.FileField(upload_to='student/image/%Y/%m/%d')
	resume = models.FileField(upload_to='student/resuem/%Y/%m/%d')
	activate = models.BooleanField(default=False)



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
	@property
	def is_active(self):
		return self.activate

class Book(models.Model):
	name = models.CharField(max_length=300)
	author_name = models.CharField(max_length=300)
	publication = models.CharField(max_length=300)
