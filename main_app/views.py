from django.shortcuts import render
from .models import Teacher


# Create your views here.
def home(request):
  return render(request, 'home.html')

def teachers_index(request):
  teachers = Teacher.objects.all()
  print(teachers)
  return render(request, 'teachers/index.html', {'teachers': teachers})
