from django.urls import path
from . import views
urlpatterns =[
    path('get',views.SystemControl_List,name='systemcontrolget'),
    path('update',views.SystemControl_pk,name='systemcontrolupdate'),
]