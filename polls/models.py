from django.db import models

# Create your models here.

class SyainData(models.Model):
    phone = models.CharField(max_length=13,default='000-0000-0000')
    date = models.DateField(max_length=10,default='0000-00-00')
    password = models.CharField(max_length=30,default='sei-mei')
    name = models.CharField(max_length=30,default='sei-mei')
    job_start = models.TimeField()
    job_end = models.TimeField()
    status = models.CharField(max_length=2,default='休暇')
   