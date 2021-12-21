from django.urls import path
from . import views
urlpatterns =[
    path('create',views.role_List,name='rolecreate'),
    path('list',views.role_List,name='rolelist'),
    path('get',views.role_pk,name='roleget'),
    path('edit',views.role_pk,name='roleedit'),
    path('delete',views.role_pk,name='roledelete'), 
]