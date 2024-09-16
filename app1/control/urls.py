from django.urls import path
from . import views

urlpatterns = [
    path('', views.control_home,name='control_home'),
    path('addfaculty/', views.add_faculty,name='add_faculty'),
    path('addkafedra/', views.add_kafedra,name='add_kafedra')
]