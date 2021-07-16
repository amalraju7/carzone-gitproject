from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Feedback(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    subject  = models.CharField(max_length=255,default="")
    feedback = RichTextField()
    date = models.DateField(default=datetime.now, blank=True)
