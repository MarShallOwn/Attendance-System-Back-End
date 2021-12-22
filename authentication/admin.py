from django.contrib import admin
from .models import User

#used to show some field in admin panel
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email']

# Register your models here.
admin.site.register(User,UserAdmin)
