from django.urls import path
from . import views
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('sendNotif', views.Notif.as_view(), name='api_notif'),
    path('registerFCMToken', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]