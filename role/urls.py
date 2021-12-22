from django.urls import path
from . import views
urlpatterns =[
    path('create',views.role_List,name='rolecreate'),
    path('list',views.role_List,name='rolelist'),
    path('get/<uuid:pk>',views.role_pk,name='roleget'),
    path('edit/<uuid:pk>',views.role_pk,name='roleedit'),
    path('delete/<uuid:pk>',views.role_pk,name='roledelete'), 
]