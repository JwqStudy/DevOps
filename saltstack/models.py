from django.db import models

# Create your models here.

class AppList(models.Model):
    priority = models.IntegerField()
    appname = models.CharField(max_length=50, unique=True)#unique设置不可重复


class IpList(models.Model):
    ipnum = models.GenericIPAddressField(protocol='ipv4', unique=True)  #字符串类型（ip4和ip6是可选的），只在admin上有用
