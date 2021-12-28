from django.contrib import admin
from .models import holiday
# Register your models here.
class holidayPanel(admin.ModelAdmin):
    readonly_fields = ['headName']
    def headName(self,holy):
        return holy.user.username
    list_display = ['id','name','startDate','endDate']
admin.site.register(holiday,holidayPanel)