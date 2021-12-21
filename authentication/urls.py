from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns =[
    path('employer/create/',views.Registration,name='employercreate'),
    path('employer/list/',views.Registration,name='employerlist'),
    path('employer/edit/<uuid:pk>',views.Mentainanace,name='employeredit'),
    path('employer/delete/<uuid:pk>',views.Mentainanace,name='employerdelete'),
    path('employer/<uuid:pk>',views.Mentainanace,name='employerget'),
    path('empolyer/forgetpassword/',views.ResetPassword,name='resetpassword'),
    path('employer/updatepassword/',views.UpdatePassword,name='updatepassword'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user',views.AuthenticatedUser,name='user'),
]