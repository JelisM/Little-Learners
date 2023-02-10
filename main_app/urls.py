from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("teachers/", views.teachers_index, name='teachers_index'),
    path('login/', views.login_view, name='login'),
    path('guardians/',views.guardians_index, name ='guardians_index')

]