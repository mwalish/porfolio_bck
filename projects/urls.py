# projects/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # ✅ ADD THIS
from .views import ProjectViewSet, CodeSnippetViewSet, PersonalInfoView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'snippets', CodeSnippetViewSet)

urlpatterns = [
    path('login/', obtain_auth_token, name='api-login'),  # ✅ /api/login/
    path('profile/', PersonalInfoView.as_view(), name='profile'),
    path('', include(router.urls)),
]