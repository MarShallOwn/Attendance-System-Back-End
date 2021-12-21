from django.urls import path
from . import views
urlpatterns =[
    path('',views.weekend_pk,name='weekendget'),
    path('edit',views.weekend_pk,name='weekendedit'),
]