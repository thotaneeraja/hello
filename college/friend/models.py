from django.db import models
class func1(models.Model):
    text=models.TextField()
    age=models.IntegerField(max_length=10)
    lastname=models.CharField(max_length=10)
    phonenumber=models.IntegerField(max_length=15)

# Create your models here.
