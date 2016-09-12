from django.db import models

# Create your models here.

class SyainData(models.Model):
    phone = models.CharField(max_length=13,default='000-0000-0000')
    password = models.CharField(max_length=30,default='sei-mei')
    name = models.CharField(max_length=30,default='sei-mei')
    corporation_name = models.CharField(max_length=30,default='corpration-name')
    date = models.DateField()
    job_start = models.TimeField()
    job_end = models.TimeField()
    status = models.CharField(max_length=2,default='休暇')
    min = models.TimeField()
    max = models.TimeField()
    overtime = models.TimeField()