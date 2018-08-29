from django.contrib import admin
from cmdb.models import Host, HostGroup


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


class HostGroupAdmin(admin.ModelAdmin):
    list_display = ['groupname']   #这里只能写groupname，组成员的数据类型不能显示


admin.site.register(Host, HostAdmin)    #添加到admin管理界面上
admin.site.register(HostGroup, HostGroupAdmin)