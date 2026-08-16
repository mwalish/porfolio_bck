from django.contrib import admin
from .models import Project, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'location', 'email')
    fieldsets = (
        ('Identity', {'fields': ('name', 'title', 'location', 'bio', 'avatar', 'email')}),
        ('Social Links', {'fields': ('github', 'linkedin', 'twitter')}),
        ('Skills', {'fields': ('skills',)}),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at')
    list_filter = ('featured',)
    search_fields = ('title', 'description', 'tech_stack')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'featured')}),
        ('Media', {'fields': ('image', 'image_url')}),
        ('Links', {'fields': ('tech_stack', 'live_url', 'github_url')}),
    )
