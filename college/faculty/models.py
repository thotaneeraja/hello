from django.db import models
class add(models.Model):
    eid=models.CharField(max_length=10)
    firstname=models.CharField(max_length=10)
    email=models.CharField(max_length=20)

# Create your models here.
