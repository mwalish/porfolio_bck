from rest_framework import serializers
from .models import Project, Profile


class ProfileSerializer(serializers.ModelSerializer):
    skill_list = serializers.SerializerMethodField()
    avatar_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'name', 'title', 'bio', 'location', 'avatar', 'avatar_image',
            'github', 'linkedin', 'twitter', 'email', 'skills',
            'skill_list', 'updated_at',
        ]

    def get_skill_list(self, obj):
        return obj.skill_list()


class ProjectSerializer(serializers.ModelSerializer):
    tech_list = serializers.SerializerMethodField()
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'image', 'image_url',
            'tech_stack', 'tech_list', 'live_url', 'github_url',
            'featured', 'created_at', 'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_tech_list(self, obj):
        return obj.tech_list()
