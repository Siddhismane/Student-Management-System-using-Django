from django.urls import path
from myaccount.views import *
urlpatterns=[

    path('sign_up/',sign_up,name='sign_up'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('singlestudentdetails/<reg_no>/',singlestudentdetails,name='singlestudentdetails'),
    path('delete/<reg_no>/',delete,name='delete'),
    

]