from django.db import models

class Syain(models.Model):
    phone = models.CharField(max_length=13,default='000-0000-0000')
    name = models.CharField(max_length=30,default='sei-mei')
    corporation_name = models.CharField(max_length=30,default='corpration-name')
# expire_date = models.DateField(max_length=10,default='0000-00-00')
    job_start = models.IntegerField(default=0)
    job_end = models.IntegerField(default=0)
    status = models.CharField(max_length=2,default='休暇')
    min = models.IntegerField(default=14000)
    max = models.IntegerField(default=18000)
    overtime = models.IntegerField(default=0)
    