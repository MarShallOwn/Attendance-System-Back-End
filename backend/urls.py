
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('department/',include('department.urls')),
    path('role/',include('role.urls')),
    path('holiday/',include('holiday.urls')),
    path('weekend/',include('weekend.urls')),
#   path('api/', include(router.urls)),
]
