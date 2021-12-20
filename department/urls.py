from django.urls import path
from . import views
urlpatterns =[
    path('create',views.Department_List,name='departmentcreate'),
    path('list',views.Department_List,name='departmentlist'),
    path('get',views.Department_pk,name='departmentget'),
    path('update',views.Department_pk,name='departmentupdate'),
    path('delete',views.Department_pk,name='departmentdelete'), 
]