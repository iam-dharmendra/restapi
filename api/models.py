from django.db import models

# Create your models here.


class record(models.Model):
    name=models.CharField(default='',max_length=123)
    email=models.EmailField(default='')
    sem=models.IntegerField(default=1)

