from django.urls import path, include

from .views import (
    RobochiyNavchalnuyPlanList, RobochiyNavchalnuyPlanCreate, RobochiyNavchalnuyPlanUpdate,
     delete_elementrnp
)

##app_name = 'educational_programs'

urlpatterns = [
    path('', RobochiyNavchalnuyPlanList.as_view(), name='list_robochiy_navchalnuy_plans'),
    path('create/', RobochiyNavchalnuyPlanCreate.as_view(), name='create_robochiy_navchalnuy_plan'),
    path('update/<int:pk>/', RobochiyNavchalnuyPlanUpdate.as_view(), name='update_robochiy_navchalnuy_plan'),    
    path('delete-elementrnp/<int:pk>/', delete_elementrnp, name='delete_elementrnp'),
]