from django.contrib import admin
from .models import Project, PersonalInfo, CodeSnippet


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'location', 'email')
    fieldsets = (
        ('Identity', {'fields': ('name', 'title', 'location', 'bio', 'email')}),
        ('Photo', {'fields': ('profile_image', 'avatar')}),
        ('Social Links', {'fields': ('github', 'linkedin', 'twitter')}),
        ('Skills', {'fields': ('skills',)}),
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
