from django.urls import path, include

from django.contrib import admin
from healthnet.api import router
#admin.autodiscover()

urlpatterns = [
    path('', include('healthnet.urls')),
    path('msmt/', include('hnet.urls'), ),
    path('api/', include('api.urls'), ),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)