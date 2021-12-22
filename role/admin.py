from django.contrib import admin
from .models import role
# Register your models here.
class rolePanel(admin.ModelAdmin):
    list_display = ['id','roleName']
admin.site.register(role,rolePanel)