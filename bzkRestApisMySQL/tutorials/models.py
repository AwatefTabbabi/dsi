
from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
class User(models.Model):
    login = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    