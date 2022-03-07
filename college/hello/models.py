from django.db import models
class next(models.Model):
    gender=models.BooleanField(default=False)
    email=models.CharField(max_length=10)
    phonenumber=models.IntegerField(max_length=20)
    name=models.CharField(max_length=15)


# Create your models here.
