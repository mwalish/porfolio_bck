from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Project, Profile
from .serializers import ProjectSerializer, ProfileSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    """Return and update the single profile record."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        obj, _ = Profile.objects.get_or_create(pk=1)
        return obj

    def get_permissions(self):
        # Allow anyone to read, but require auth to update
        if self.request.method in ['GET']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class ProjectViewSet(viewsets.ModelViewSet):
    """Full CRUD API for projects."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        # Allow anyone to read (list/retrieve), but require auth for write operations
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
