from django.urls import path
from . import views
urlpatterns =[
    path('get',views.weekend_List,name='weekendget'),
    path('edit',views.weekend_pk,name='weekendedit'),
]