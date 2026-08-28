from django.contrib import admin
from .models import (
    Project, PersonalInfo, CodeSnippet, Skill, Experience, Testimonial, ContactMessage,
)


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'location', 'email')
    fieldsets = (
        ('Identity', {'fields': ('name', 'title', 'location', 'bio', 'email')}),
        ('Photo', {'fields': ('profile_image', 'avatar')}),
        ('Social Links', {'fields': ('github', 'linkedin', 'twitter')}),
        ('Skills (legacy)', {'fields': ('skills',)}),
        ('Resume', {'fields': ('resume',)}),
    )

    def has_add_permission(self, request):
        # Single-instance only — don't let anyone create a second row from
        # the admin UI. The model's save() also enforces this at the DB
        # level as a second line of defense.
        return not PersonalInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class CodeSnippetInline(admin.TabularInline):
    model = CodeSnippet
    extra = 0
    fields = ('title', 'language', 'created')
    readonly_fields = ('created',)
    show_change_link = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created')
    list_filter = ('featured',)
    search_fields = ('title', 'description', 'tech_stack')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CodeSnippetInline]
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'description', 'featured')}),
        ('Media', {'fields': ('image', 'image_url')}),
        ('Links', {'fields': ('tech_stack', 'live_url', 'github_url')}),
    )


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
    list_display = ('name', 'category', 'percentage', 'order')
    list_filter = ('category',)
    list_editable = ('percentage', 'order')
    ordering = ('order', '-percentage')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'type', 'start_date', 'end_date', 'order')
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
        # Messages only ever come in through the public contact form —
        # nobody should be creating fake ones from the admin UI.
        return False
