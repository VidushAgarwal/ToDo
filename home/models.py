from django.db import models

# Create your models here.
class data(models.Model):
    uname=models.CharField(max_length=20)
    passw=models.CharField(max_length=20)
    email=models.CharField(max_length=20)