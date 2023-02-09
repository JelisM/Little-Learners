from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
  name = models.CharField(max_length=100)