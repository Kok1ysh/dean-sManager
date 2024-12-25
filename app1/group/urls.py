from django.urls import path
from .views import GroupsList, GroupsCreate, GroupsUpdate, GroupsDelete

urlpatterns = [
    path('', GroupsList.as_view(), name='group_list'),
    path('create/', GroupsCreate.as_view(), name='group_create'),
    path('update/<int:pk>/', GroupsUpdate.as_view(), name='group_update'),
    path('<int:pk>/delete/', GroupsDelete.as_view(), name='delete_group'),
]
