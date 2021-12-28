from django.urls import path
from . import views
urlpatterns  = [
    path("create",views.LeaveRequestGP,name="leavecreate"),
    path("list",views.LeaveRequestGP,name="leavelist"),
    path("get/<uuid:pk>",views.LeaveRequest_pk,name="leaveget"),
    path("edit/<uuid:pk>",views.LeaveRequest_pk,name="leaveedit"),
    path("delete/<uuid:pk>",views.LeaveRequest_pk,name="leavedelete"),
    path("filter",views.GetUserLeaveRequest,name="leavedelete"),
]