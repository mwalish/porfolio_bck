from rest_framework import viewsets, permissions, generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Project, PersonalInfo, CodeSnippet
from .serializers import ProjectSerializer, PersonalInfoSerializer, CodeSnippetSerializer


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
