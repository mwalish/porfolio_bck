from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Project, ProjectImage, PersonalInfo, CodeSnippet,
    Skill, Experience, Testimonial, ContactMessage, Post,
)


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'location', 'email', 'updated_at')
    fieldsets = (
        ('Identity', {
            'fields': ('name', 'title', 'location', 'bio', 'email', 'website', 'now_status')
        }),
        ('Photo', {'fields': ('profile_image', 'avatar')}),
        ('Social Links', {'fields': ('github', 'linkedin', 'twitter')}),
        ('Skills (legacy)', {'fields': ('skills',)}),
        ('Resume', {'fields': ('resume',)}),
    )

    def has_add_permission(self, request):
        return not PersonalInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'caption', 'order')


class CodeSnippetInline(admin.TabularInline):
    model = CodeSnippet
    extra = 0
    fields = ('title', 'language', 'created')
    readonly_fields = ('created',)
    show_change_link = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'featured', 'order',
        'image_preview', 'created'
    )
    list_filter = ('featured', 'category')
    list_editable = ('featured', 'order')
    search_fields = ('title', 'short_description', 'description', 'tech_stack')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline, CodeSnippetInline]
    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'short_description', 'description',
                'category', 'featured', 'order'
            )
        }),
        ('Case Study', {
            'fields': ('problem', 'solution', 'challenges', 'outcome'),
            'classes': ('collapse',),
        }),
        ('Media', {
            'fields': ('image', 'image_url', 'demo_video'),
        }),
        ('Links & Tech', {
            'fields': ('tech_stack', 'live_url', 'github_url'),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:40px;border-radius:4px;" />',
                obj.image.url
            )
        return '—'
    image_preview.short_description = 'Cover'


@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'project', 'created')
    list_filter = ('language', 'project')
    search_fields = ('title', 'code', 'description')
    fieldsets = (
        (None, {'fields': ('title', 'language', 'project')}),
        ('Content', {'fields': ('code', 'description')}),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'percentage', 'icon', 'color', 'order')
    list_filter = ('category',)
    list_editable = ('percentage', 'order', 'icon', 'color')
    ordering = ('order', '-percentage')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'organization', 'type',
        'start_date', 'end_date', 'order'
    )
    list_filter = ('type',)
    list_editable = ('order',)
    ordering = ('-start_date',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'created')
    list_editable = ('order',)
    search_fields = ('name', 'message')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created', 'is_read')
    list_filter = ('is_read',)
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created')

    def has_add_permission(self, request):
        return False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'featured', 'published',
        'published_at', 'created'
    )
    list_filter = ('published', 'featured')
    list_editable = ('featured', 'published')
    search_fields = ('title', 'excerpt', 'content', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'excerpt', 'content',
                'featured', 'published', 'published_at'
            )
        }),
        ('Media', {
            'fields': ('cover_image', 'cover_image_url', 'tags'),
        }),
    )
