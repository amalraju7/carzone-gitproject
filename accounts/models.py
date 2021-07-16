from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=255,unique=True)
    price= models.BigIntegerField()
    # validity = models.IntegerField(default=0)
    cars = models.IntegerField(default=0)

    def __str__(self):
        return self.name;

class Cuspack(models.Model):

    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    no_of_cars = models.IntegerField(default=0)
    total_cars = models.IntegerField(default=1)
    def __str__(self):
        return self.user;

class Card(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    expiry = models.CharField(max_length=255)
    def __str__(self):
        return self.name;

class Packageorder(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    package = models.ForeignKey(Package,null=True,on_delete=models.SET_NULL)
    price = models.IntegerField()
    status = models.CharField(max_length=255)

    date = models.DateField(default=datetime.now)
