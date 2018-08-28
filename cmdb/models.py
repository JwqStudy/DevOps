from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    osver = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)  #厂商
    product = models.CharField(max_length=50) #产品
    sn = models.CharField(max_length=50)
    cpu_model = models.CharField(max_length=50)
    cpu_num = models.IntegerField()
    memory = models.CharField(max_length=50)
