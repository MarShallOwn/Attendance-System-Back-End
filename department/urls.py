from django.urls import path
from . import views
urlpatterns =[
    path('create',views.Department_List,name='departmentcreate'),
    path('list',views.Department_List,name='departmentlist'),
    path('get/<uuid:pk>',views.Department_pk,name='departmentget'),
    path('edit/<uuid:pk>',views.Department_pk,name='departmentedit'),
    path('delete/<uuid:pk>',views.Department_pk,name='departmentdelete'), 
]