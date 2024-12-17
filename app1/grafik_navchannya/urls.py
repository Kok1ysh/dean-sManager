from django.urls import path
from .views import GrafikNavchannyaList, GrafikNavchannyaCreate, GrafikNavchannyaUpdate, GrafikNavchannyaDelete

urlpatterns = [
    path('', GrafikNavchannyaList.as_view(), name='grafik_navchannya_list'),
    path('create/', GrafikNavchannyaCreate.as_view(), name='grafik_navchannya_create'),
    path('update/<int:pk>/', GrafikNavchannyaUpdate.as_view(), name='grafik_navchannya_update'),
    path('<int:pk>/delete/', GrafikNavchannyaDelete.as_view(), name='delete_grafik_navchannya'),
]
