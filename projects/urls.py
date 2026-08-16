from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, PersonalInfoView, CodeSnippetViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register('snippets', CodeSnippetViewSet, basename='codesnippet')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', PersonalInfoView.as_view(), name='personal-info'),
]
