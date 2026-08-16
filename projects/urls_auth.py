from django.urls import path
from . import views_auth

urlpatterns = [
    path('login/', views_auth.login_api, name='api-login'),
    path('check/', views_auth.check_auth, name='api-check-auth'),
]

