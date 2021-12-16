from django.urls import path,include
from . import views

urlpatterns =[
    path('employer/create/',views.Registration,name='employercreate'),
    path('employer/list/',views.Registration,name='employerlist'),
    path('employer/edit/<uuid:pk>',views.Mentainanace,name='employeredit'),
    path('login',views.Login,name='login'),
    path('user',views.AuthenticateUser,name='user'),
]