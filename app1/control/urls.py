from django.urls import path,include
from . import views
from .views import (
    FacultysList, FacultysCreate, FacultysUpdate, KafedrasList, KafedrasCreate, KafedrasUpdate, KafedrasDelete, FacultysDelete
)

urlpatterns = [
    path('', views.control_home,name='control_home'),
    path('facultys-list', FacultysList.as_view(), name='facultys_list'),
    path('create-facultys/', FacultysCreate.as_view(), name='facultys_create'),
    path('update-facultys/<int:pk>/', FacultysUpdate.as_view(), name='facultys_update'),
    path('kafedras-list', KafedrasList.as_view(), name='kafedras_list'),
    path('create-kafedras/', KafedrasCreate.as_view(), name='kafedras_create'),
    path('update-kafedras/<int:pk>/', KafedrasUpdate.as_view(), name='kafedras_update'),
    # path('addkafedra/', views.add_kafedra,name='add_kafedra'),
    path('educational-programs-create-or-update/', include('educational_programs.urls')),
    path('group-create-or-update/', include('group.urls')),
    path('robochiy-navchalnuy-plan/', include('robochiy_navchalnuy_plan.urls')),
    path('vukladach/', include('vukladach.urls')),
    path('rozklad/', include('rozklad.urls')),
    path('grafik-navchannya/', include('grafik_navchannya.urls')),
    path('korustyvach/', include('korustyvach.urls')),
    path('<int:pk>/delete/', FacultysDelete.as_view(), name='delete_facultys'),
    path('<int:pk>/delete/', KafedrasDelete.as_view(), name='delete_kafedras'),
    
]