from django.urls import path
from . import views
urlpatterns =[
    path('create',views.holiday_List,name='holidaycreate'),
    path('list',views.holiday_List,name='holidaylist'),
    path('<uuid:id>',views.holiday_pk,name='holidayget'),
    path('edit/<uuid:id>',views.holiday_pk,name='holidayedit'),
    path('delete/<uuid:id>',views.holiday_pk,name='holidaydelete'), 
]