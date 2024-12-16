from django.urls import path, include

from .views import (
    RozkladList, create, RozkladUpdate, RozkladDelete
)

##app_name = 'educational_programs'

urlpatterns = [
    path('', RozkladList.as_view(), name='list_rozklad'),    
    path('create/', create, name='create_rozklad'),
    path('<int:pk>/update/', RozkladUpdate.as_view(), name='update_rozklad'),    
    path('<int:pk>/delete/', RozkladDelete.as_view(), name='delete_rozklad'),
]