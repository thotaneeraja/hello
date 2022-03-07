from django.db import models
class disp(models.Model):
    name=models.CharField(max_length=20,null='True',default=123)
    branch=models.CharField(max_length=20,null='True')
    address=models.TextField()
    fathername=models.CharField(max_length=15,null='True')
    mothername=models.CharField(max_length=15,null='True')


