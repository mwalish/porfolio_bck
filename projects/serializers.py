from rest_framework import serializers
from .models import Project, PersonalInfo, CodeSnippet


class PersonalInfoSerializer(serializers.ModelSerializer):
    skill_list = serializers.SerializerMethodField()
    profile_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = PersonalInfo
        fields = [
            'id', 'name', 'title', 'bio', 'location', 'avatar', 'profile_image',
            'github', 'linkedin', 'twitter', 'email', 'skills',
            'skill_list', 'updated_at',
        ]

    def get_skill_list(self, obj):
        return obj.skill_list()


class CodeSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSnippet
        fields = ['id', 'title', 'language', 'code', 'description', 'project', 'created']
        read_only_fields = ['created']


class ProjectSerializer(serializers.ModelSerializer):
    tech_list = serializers.SerializerMethodField()
    image = serializers.ImageField(required=False, allow_null=True)
    snippets = CodeSnippetSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'description', 'image', 'image_url',
            'tech_stack', 'tech_list', 'live_url', 'github_url',
            'featured', 'created', 'updated_at', 'snippets',
        ]
        read_only_fields = ['slug', 'created', 'updated_at']

    def get_tech_list(self, obj):
        return obj.tech_list()
