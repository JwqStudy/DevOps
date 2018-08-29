from django.contrib import admin
from cmdb.models import Host

# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = [
        'hostname',
        'ip',
        'osver',
        'vendor',
        'product',
        'sn',
        'cpu_model',
        'cpu_num',
        'memory',
    ]

admin.site.register(Host, HostAdmin)