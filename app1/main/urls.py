from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('groups/', views.groups, name='groups'),
    path('predmet/', views.predmet, name='predmet'),
    path('profil/', views.profil,name='profil'),
]
