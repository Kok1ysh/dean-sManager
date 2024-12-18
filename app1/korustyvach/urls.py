from django.urls import path
from .views import KorustyvachList,  KorustyvachUpdate, KorustyvachDelete, korustyvach_login, korustyvach_logout,register

urlpatterns = [
    path('', KorustyvachList.as_view(), name='korustyvach_list'),
    path('create/', register, name='korustyvach_create'),
    path('update/<int:pk>/', KorustyvachUpdate.as_view(), name='korustyvach_update'),
    path('<int:pk>/delete/', KorustyvachDelete.as_view(), name='delete_korustyvach'),
    path('login/', korustyvach_login, name='login_korustyvach'),
    path('logout/', korustyvach_logout, name='logout_korustyvach'),
]
