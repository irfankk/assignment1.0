from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [ 


path('teacherReg', views.teacherReg, name = 'techerreg'),
path('teacherLog', views.teacherLog, name = 'teacherlog'),
# path('teacherLog', views.teacherLog, name = 'teacherlog'),
# path('teacherLog', views.teacherLog, name = 'teacherlog'),

]