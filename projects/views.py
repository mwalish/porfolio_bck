from rest_framework import viewsets, permissions, generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Project, PersonalInfo, CodeSnippet, Skill, Experience, Testimonial, ContactMessage
from .serializers import (
    ProjectSerializer, PersonalInfoSerializer, CodeSnippetSerializer,
    SkillSerializer, ExperienceSerializer, TestimonialSerializer, ContactMessageSerializer,
)


class PersonalInfoView(generics.RetrieveUpdateAPIView):
    """Return and update the single personal-info record."""
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        obj, _ = PersonalInfo.objects.get_or_create(pk=1)
        return obj

    def get_permissions(self):
        # Allow anyone to read, but require auth to update
        if self.request.method in ['GET']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class ProjectViewSet(viewsets.ModelViewSet):
    """Full CRUD API for projects."""
    queryset = Project.objects.all().prefetch_related('snippets')
    serializer_class = ProjectSerializer

    def get_permissions(self):
        # Allow anyone to read (list/retrieve), but require auth for write operations
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class CodeSnippetViewSet(viewsets.ModelViewSet):
    """Full CRUD API for code snippets. Optionally filter by ?project=<id>."""
    serializer_class = CodeSnippetSerializer

    def get_queryset(self):
        queryset = CodeSnippet.objects.all().select_related('project')
        project_id = self.request.query_params.get('project')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class SkillListView(generics.ListAPIView):
    """Public read-only list of skills, managed via Django admin."""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]


class ExperienceListView(generics.ListAPIView):
    """Public read-only timeline of education/work entries, managed via Django admin."""
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


class TestimonialListView(generics.ListAPIView):
    """Public read-only list of testimonials, managed via Django admin."""
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]


class ContactMessageCreateView(generics.CreateAPIView):
    """Public endpoint the contact form POSTs to. No read access — messages
    are only viewable via Django admin, never exposed over the API."""
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]
