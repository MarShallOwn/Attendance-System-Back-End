from django.contrib import admin
from LeaveRequest.models import LeaveRequest
# Register your models here.
class LeaveRequestPanel(admin.ModelAdmin):
    readonly_fields = ['userName']
    def userName(self,leave):
        return leave.user.username
    list_display = ['userName','typeOfLeave','startDate','endDate','status']

admin.site.register(LeaveRequest,LeaveRequestPanel)