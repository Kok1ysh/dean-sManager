from django.urls import path, include

from .views import (
    EducationalProgramsList, EducationalProgramsCreate, EducationalProgramsUpdate,
     delete_komponent_educational_programs
)

##app_name = 'educational_programs'

urlpatterns = [
    path('', EducationalProgramsList.as_view(), name='list_educational_programs'),
    path('create/', EducationalProgramsCreate.as_view(), name='create_educational_programs'),
    path('update/<int:pk>/', EducationalProgramsUpdate.as_view(), name='update_educational_programs'),    
    path('delete-komponent-educational-programs/<int:pk>/',
          delete_komponent_educational_programs, name='delete_komponent_educational_programs'),
]