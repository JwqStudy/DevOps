from django.contrib import admin
from saltstack.models import AppList

# Register your models here.

class AppAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'priority', 'appname']

admin.site.register(AppList, AppAdmin)