from django.urls import path,include
from . import views

urlpatterns =[
    path('employer/create/',views.Registration),
    path('employer/list/',views.Registration),
    path('employer/edit/<uuid:pk>',views.Mentainanace),
]