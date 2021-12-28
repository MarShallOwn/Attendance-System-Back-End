from django.contrib import admin
from .models import department
# Register your models here.

class departmentPanel(admin.ModelAdmin):
    readonly_fields = ['headName']
    def headName(self,dept):
        if dept.departmentHeadID != None:
            return dept.departmentHeadID.username
        return ""
    list_display = ['id','departmentName','headName']
admin.site.register(department,departmentPanel)