from datetime import date
from django.db import models
from email.mime import image
from turtle import title
from django.forms import URLField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)

def __str__(self):
    return self.title 