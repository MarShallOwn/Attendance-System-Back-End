
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="ATMS",
      default_version='v1',
      description="Attendance Management System",
      terms_of_service="https://www.app.com/policies/terms/",
      contact=openapi.Contact(email="oursite@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[]
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('auth/',include('authentication.urls')),
   path('department/',include('department.urls')),
   path('role/',include('role.urls')),
   path('systemcontrol/',include('systemControl.urls')),
   path('holiday/',include('holiday.urls')),
   path('weekend/',include('weekend.urls')),
   path('leave/',include('LeaveRequest.urls')),
   path('attendence/',include('attendence.urls')),

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#   path('api/', include(router.urls)),
]
