from django.conf import settings
from django.core.mail import send_mail
from rest_framework import viewsets, permissions, generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import (
    Project, PersonalInfo, CodeSnippet, Skill,
    Experience, Testimonial, ContactMessage, Post,
)
from .serializers import (
    ProjectSerializer, ProjectListSerializer, PersonalInfoSerializer,
    CodeSnippetSerializer, SkillSerializer, ExperienceSerializer,
    TestimonialSerializer, ContactMessageSerializer,
    PostSerializer, PostListSerializer,
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
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class ProjectViewSet(viewsets.ModelViewSet):
    """Full CRUD for projects with filtering, search, and ordering."""
    queryset = Project.objects.all().prefetch_related('snippets', 'images')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['featured', 'category']
    search_fields = ['title', 'short_description', 'description', 'tech_stack']
    ordering_fields = ['order', 'created', 'featured', 'title']
    ordering = ['order', '-featured', '-created']
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class CodeSnippetViewSet(viewsets.ModelViewSet):
    """CRUD for code snippets. Filter with ?project=<id>."""
    serializer_class = CodeSnippetSerializer

    def get_queryset(self):
        qs = CodeSnippet.objects.all().select_related('project')
        project_id = self.request.query_params.get('project')
        if project_id:
            qs = qs.filter(project_id=project_id)
        return qs

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category']
    ordering_fields = ['order', 'percentage', 'name']
    ordering = ['order', '-percentage']


class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['type']
    ordering = ['-start_date', 'order']


class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]


class ContactMessageCreateView(generics.CreateAPIView):
    """
    Public contact form endpoint.
    Sends an email notification when CONTACT_NOTIFY_EMAIL is configured.
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        message = serializer.save()
        # Send notification email if configured
        notify_to = getattr(settings, 'CONTACT_NOTIFY_EMAIL', '') or settings.EMAIL_HOST_USER
        if notify_to and settings.EMAIL_HOST_USER:
            subject = f'[Portfolio] New message from {message.name}'
            if message.subject:
                subject = f'[Portfolio] {message.subject} — {message.name}'
            body = (
                f'Name: {message.name}\n'
                f'Email: {message.email}\n'
                f'Subject: {message.subject or "(none)"}\n\n'
                f'Message:\n{message.message}\n'
            )
            try:
                send_mail(
                    subject=subject,
                    message=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[notify_to],
                    fail_silently=True,
                )
            except Exception:
                # Never break the API if email fails
                pass


class PostViewSet(viewsets.ModelViewSet):
    """Blog posts. Public only sees published posts."""
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['featured', 'published']
    search_fields = ['title', 'excerpt', 'content', 'tags']
    ordering_fields = ['published_at', 'created', 'title']
    ordering = ['-published_at', '-created']
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        qs = Post.objects.all()
        # Public users only see published posts
        if not self.request.user.is_authenticated:
            qs = qs.filter(published=True)
        return qs

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class HealthCheckView(APIView):
    """Simple health check for uptime monitors and load balancers."""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({'status': 'ok', 'service': 'portfolio-api'}, status=status.HTTP_200_OK)
