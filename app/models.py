from django.db import models

# Create your models here.

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=20)
    elast=models.CharField(max_length=20)
    eemail=models.EmailField()
    cname = models.CharField(max_length=20)
    econtact=models.CharField(max_length=10)




