from django.urls import path
from . import views
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

urlpatterns = [
    path('login', views.Login.as_view(), name='api_login'),
    path('logout', views.Login.as_view(), name='measurement_list'),
    path('register', views.Login.as_view(), name='measurement_list'),
    path('devices', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
]