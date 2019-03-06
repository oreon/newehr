from django.urls import path, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # path(r'^$', 'prototype.views.home', name='home'),
    # path(r'^blog/', include('blog.paths')),
    path('', include('healthnet.urls')),
    
    path('admin/', admin.site.urls),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)