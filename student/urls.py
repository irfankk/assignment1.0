from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [ 

path('', views.home, name = 'home'),
path('studentReg', views.studentReg, name = 'studentreg'),
path('studentLog', views.studentLog, name = 'studentlog'),

]