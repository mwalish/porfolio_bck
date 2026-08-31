from rest_framework import serializers
from .models import (
    Project, ProjectImage, PersonalInfo, CodeSnippet,
    Skill, Experience, Testimonial, ContactMessage, Post,
)


class PersonalInfoSerializer(serializers.ModelSerializer):
    skill_list = serializers.SerializerMethodField()
    profile_image = serializers.ImageField(required=False, allow_null=True)
    resume = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = PersonalInfo
        fields = [
            'id', 'name', 'title', 'bio', 'location', 'avatar', 'profile_image',
            'github', 'linkedin', 'twitter', 'email', 'website',
            'skills', 'skill_list', 'resume', 'now_status', 'updated_at',
        ]

    def get_skill_list(self, obj):
        return obj.skill_list()


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'percentage', 'category', 'icon', 'color', 'order']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id', 'title', 'organization', 'type', 'description',
            'location', 'start_date', 'end_date', 'order',
        ]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id', 'name', 'role', 'message', 'avatar',
            'linkedin', 'order', 'created',
        ]
        read_only_fields = ['created']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'created']
        read_only_fields = ['id', 'created']


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'caption', 'order']


class CodeSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSnippet
        fields = [
            'id', 'title', 'language', 'code',
            'description', 'project', 'created',
        ]
        read_only_fields = ['created']


class ProjectSerializer(serializers.ModelSerializer):
    tech_list = serializers.SerializerMethodField()
    image = serializers.ImageField(required=False, allow_null=True)
    snippets = CodeSnippetSerializer(many=True, read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'short_description', 'description',
            'problem', 'solution', 'challenges', 'outcome',
            'image', 'image_url', 'demo_video',
            'tech_stack', 'tech_list', 'live_url', 'github_url',
            'category', 'featured', 'order',
            'created', 'updated_at', 'snippets', 'images',
        ]
        read_only_fields = ['slug', 'created', 'updated_at']

    def get_tech_list(self, obj):
        return obj.tech_list()


class ProjectListSerializer(serializers.ModelSerializer):
    """Lighter serializer for list views (faster cards)."""
    tech_list = serializers.SerializerMethodField()
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'short_description', 'description',
            'image', 'image_url', 'tech_stack', 'tech_list',
            'live_url', 'github_url', 'category', 'featured',
            'order', 'created',
        ]

    def get_tech_list(self, obj):
        return obj.tech_list()


class PostSerializer(serializers.ModelSerializer):
    tag_list = serializers.SerializerMethodField()
    cover_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'content',
            'cover_image', 'cover_image_url', 'tags', 'tag_list',
            'featured', 'published', 'published_at',
            'created', 'updated_at',
        ]
        read_only_fields = ['slug', 'published_at', 'created', 'updated_at']

    def get_tag_list(self, obj):
        return obj.tag_list()


class PostListSerializer(serializers.ModelSerializer):
    """Lighter serializer for blog list."""
    tag_list = serializers.SerializerMethodField()
    cover_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt',
            'cover_image', 'cover_image_url', 'tags', 'tag_list',
            'featured', 'published_at', 'created',
        ]

    def get_tag_list(self, obj):
        return obj.tag_list()
