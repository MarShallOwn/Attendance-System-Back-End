from django.contrib import admin
from .models import weekend
# Register your models here.
class weekendPanel(admin.ModelAdmin):
    list_display = ['saturday','sunday','monday','tuesday','wendesday','thursday','friday']

admin.site.register(weekend,weekendPanel)