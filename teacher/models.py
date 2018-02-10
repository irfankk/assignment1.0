from django.db import models
from django.contrib.auth.models import   BaseUserManager, AbstractBaseUser
import uuid
from django.utils import timezone






class TeacherManager(BaseUserManager):

	def create_user(self, username, phone_number, password = None):
		Teacher= self.model(
			username = username,
			phone_number = phone_number)
		Teacher.set_password(password)
		Teacher.save(using=self._db)
		return Teacher

	

	def create_teacher(self, username, password,phone_number):
		Teacher = self.create_user(
			username,
			phone_number,
			password = password)
		Teacher.admin = False
		Teacher.teacher = True
		Teacher.save()


class Teacher(AbstractBaseUser):
	username =	models.CharField(max_length=200, unique= True)
	first_name = models.CharField(max_length = 200)
	last_name =models.CharField(max_length = 200)
	email = models.EmailField()
	teacher = models.BooleanField(default=False) 
	phone_number = models.CharField(max_length=12)
	created = models.DateTimeField(default=timezone.now)
	location = models.CharField(max_length=300)
	uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image = models.FileField(upload_to='teacher/image/%Y/%m/%d')
	




	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	objects= TeacherManager()

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True


	@property
	def is_teacher(self):
		return self.teacher




