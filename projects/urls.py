from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    ProjectViewSet, CodeSnippetViewSet, PersonalInfoView,
    SkillListView, ExperienceListView, TestimonialListView, ContactMessageCreateView,
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'snippets', CodeSnippetViewSet, basename='codesnippet')  # ✅ ADDED basename

urlpatterns = [
    path('login/', obtain_auth_token, name='api-login'),
    path('profile/', PersonalInfoView.as_view(), name='profile'),
    path('skills/', SkillListView.as_view(), name='skills'),
    path('experience/', ExperienceListView.as_view(), name='experience'),
    path('testimonials/', TestimonialListView.as_view(), name='testimonials'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact'),
    path('', include(router.urls)),
]