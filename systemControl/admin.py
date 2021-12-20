from django.contrib import admin
from .models import Control

# #used to show some field in admin panel
class ControlPanel(admin.ModelAdmin):
    list_display = ['id','checkinMinTime','checkinMaxTime','checkoutMinTime','checkoutMaxTime','numOfLeaveRequest',]
# Register your models to admin panel.
admin.site.register(Control,ControlPanel)