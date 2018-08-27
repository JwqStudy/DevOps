from django.contrib import admin
from saltstack.models import AppList, IpList


# Register your models here.

#设置相应的数据库添加到admin内管理


class AppAdmin(admin.ModelAdmin):
    list_display = ['id', 'priority', 'appname']


class IpAdmin(admin.ModelAdmin):
    list_display = ['id', 'ipnum']


admin.site.register(AppList, AppAdmin)
admin.site.register(IpList, IpAdmin)