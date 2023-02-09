from django.contrib import admin
from .models import Teacher, Guardian, Child

#Register models
admin.site.register(Teacher, Guardian, Child)

# Register your models here.
