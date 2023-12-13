

from django.urls import path
from .views import property_list, property_detail

urlpatterns = [
    path('property_list/', property_list, name='property_list'),
    path('property_detail/<int:property_id>/', property_detail, name='property_detail'),

]
