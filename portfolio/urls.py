"""
URL configuration for portfolio project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
    path('api/auth/', include('projects.urls_auth')),
]

# Alwaysdata's Python hosting runs your WSGI app directly with no separate
# web server serving /media/ for you — so unlike a typical Django deploy,
# media must be served unconditionally here, not just when DEBUG=True.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
