from django.db import models

# Create your models here.
class student(models.Model):
   name = models.CharField(max_length=20)
   description = models.TextField(default="no description")
   status = models.CharField(max_length=20,default="in progress")