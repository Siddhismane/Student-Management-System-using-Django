from django.urls import path
from student.views import *
urlpatterns=[
    path('',home,name='home'),
    path('registration/',registration,name='registration'),
    path('about_us/',about_us,name='about_us'),
    path('python/',python,name='python'),
    path('java/',java,name='java'),
    path('aws/',aws,name='aws'),
    path('placement/',placement,name='placement'),


]