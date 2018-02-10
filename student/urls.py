from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns  = [
	url  (r'^$',views.HomePage.as_view()),
	url (r'^studentReg$', views.StudentRegistr.as_view()),
	url (r'^studentLog$', views.StudentLog.as_view()),
	url (r'^studentHome$', login_required(views.StudentHome.as_view()),name = 'studenthome'),
	# url (r'^studentLogout$', views.StudentLogout.as_view(),name = 'studentlogout'),
	url (r'^home$', views.HomePage.as_view()),
	path('studentLogout', views.out, name = 'logout'),
	url(r'^book$', views.CrudOperations.as_view(),name = 'book'),
	url(r'^set/(?P<username>[A-Za-z]+)/(?P<token>[0-9A-Za-z]{1,15}-[0-9A-Za-z]{1,30})$', views.set, name = 'set')
	# re_path(r'^activate/(?P<uid>\d+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name = 'activate'),
	# url(r'^activate$', views.activate.as_view(), name= 'activate')

	]
