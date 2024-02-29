from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    condition = models.TextField()
    icon = models.ImageField(upload_to='achievements/')


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='advertisements/')
    link = models.URLField()
    publication_date = models.DateTimeField(auto_now_add=True)
