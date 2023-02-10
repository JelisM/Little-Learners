from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
  name = models.CharField(max_length=100)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

class Guardian(models.Model):
  name =  models.CharField(max_length=100)
  relationship = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zip_code = models.CharField(max_length=5)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

class Child(models.Model):
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=10)
  DoB = models.DateField()
  allergies = models.CharField(max_length=100)