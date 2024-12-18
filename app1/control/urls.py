from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.control_home,name='control_home'),
    path('addfaculty/', views.add_faculty,name='add_faculty'),
    path('addkafedra/', views.add_kafedra,name='add_kafedra'),
    path('educational-programs-create-or-update/', include('educational_programs.urls')),
    path('group-create-or-update/', include('group.urls')),
    path('robochiy-navchalnuy-plan/', include('robochiy_navchalnuy_plan.urls')),
    path('vukladach/', include('vukladach.urls')),
    path('rozklad/', include('rozklad.urls')),
    path('grafik-navchannya/', include('grafik_navchannya.urls')),
    path('korustyvach/', include('korustyvach.urls')),
]