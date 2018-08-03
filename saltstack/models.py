from django.db import models

# Create your models here.

class AppList(models.Model):
    priority = models.IntegerField()
    appname = models.CharField(max_length=50)