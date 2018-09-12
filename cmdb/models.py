from django.db import models

# Create your models here.


class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    osver = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)  #厂商
    product = models.CharField(max_length=50) #产品
    sn = models.CharField(max_length=50, unique=True) #不可重复
    cpu_model = models.CharField(max_length=50)
    cpu_num = models.PositiveSmallIntegerField(default=1)
    memory = models.CharField(max_length=50)

    def __str__(self):   #改写数据定义，为了在HostGroup里面可以显示相关hostname
        return self.hostname


class HostGroup(models.Model):
    groupname = models.CharField(max_length=50)
    members = models.ManyToManyField(Host)   #类似外键，指定这个表数据出现的是在Host那里有的