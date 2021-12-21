from django.urls import path
from . import views
urlpatterns =[
    path('create',views.SystemControl_List,name='systemcontrolcreate'),
    path('list',views.SystemControl_List,name='systemcontrollist'),
    path('get/<uuid:pk>',views.SystemControl_pk,name='systemcontrolget'),
    path('update/<uuid:pk>',views.SystemControl_pk,name='systemcontrolupdate'),
    path('delete/<uuid:pk>',views.SystemControl_pk,name='systemcontroldelete'), 
]