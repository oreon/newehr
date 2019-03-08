from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login.as_view(), name='api_login'),
    path('logout', views.Login.as_view(), name='measurement_list'),
    path('register', views.Login.as_view(), name='measurement_list'),
]