from django.urls import path
from . import views

urlpatterns = [

path('measurements', views.MeasurementList.as_view(), name='measurement_list'),
    path('measurement/<int:pk>', views.MeasurementDetail.as_view(), name='measurement_detail'),
    path('create', views.MeasurementCreate.as_view(), name='measurement_create'),
    path('update/<int:pk>', views.MeasurementUpdate.as_view(), name='measurement_update'),
    path('delete/<int:pk>', views.MeasurementDelete.as_view(), name='measurement_delete'),
]