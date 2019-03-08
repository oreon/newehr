from django.urls import path, include

from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    path('', include('healthnet.urls')),
    path('msmt/', include('hnet.urls'), ),
    path('api/', include('api.urls'), ),
    path('admin/', admin.site.urls),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)