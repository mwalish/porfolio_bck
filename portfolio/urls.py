"""
URL configuration for portfolio project.
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve as static_serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
]

# django.conf.urls.static.static() silently returns NO routes at all when
# DEBUG=False, regardless of any explicit "if DEBUG" wrapper around it —
# that combination is what broke media serving in production before.
# WhiteNoiseMiddleware already serves STATIC_ROOT correctly in all cases,
# but MEDIA_ROOT needs an explicit, always-on route like this one.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
]
