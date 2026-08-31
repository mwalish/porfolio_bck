from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    ProjectViewSet, CodeSnippetViewSet, PersonalInfoView,
    SkillListView, ExperienceListView, TestimonialListView,
    ContactMessageCreateView, PostViewSet, HealthCheckView,
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'snippets', CodeSnippetViewSet, basename='codesnippet')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health'),
    path('login/', obtain_auth_token, name='api-login'),
    path('profile/', PersonalInfoView.as_view(), name='profile'),
    path('skills/', SkillListView.as_view(), name='skills'),
    path('experience/', ExperienceListView.as_view(), name='experience'),
    path('testimonials/', TestimonialListView.as_view(), name='testimonials'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact'),
    path('', include(router.urls)),
]
