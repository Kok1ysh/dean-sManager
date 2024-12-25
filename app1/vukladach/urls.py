from django.urls import path
from .views import VukladachList, VukladachCreate, VukladachUpdate, VukladachDelete

urlpatterns = [
    path('', VukladachList.as_view(), name='vukladach_list'),
    path('create/', VukladachCreate.as_view(), name='vukladach_create'),
    path('update/<int:pk>/', VukladachUpdate.as_view(), name='vukladach_update'),
    path('<int:pk>/delete/', VukladachDelete.as_view(), name='delete_vukladach'),
]
