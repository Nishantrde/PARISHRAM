from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Workers(models.Model):
    name = models.CharField(max_length=50, default="")
    occupation = models.CharField(max_length=50, default="")
    charge_per_hr = models.IntegerField(default=0)
    ratings = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=1000, default="")
    accept = models.BooleanField(default = False)
    on_work = models.BooleanField(default = False)
    work_done = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class User_profile(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(null=True, blank=True)
    history = ArrayField(models.CharField(max_length=50), default=list, blank=True)
    def __str__(self):
        return self.email
    

