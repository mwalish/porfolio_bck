from django.db import models
from django.utils.text import slugify


class PersonalInfo(models.Model):
    """
    Personal profile information for the portfolio owner.
    Enforced single-instance: save() always writes to pk=1, so there can
    never be more than one row no matter how it's created.
    """
    name = models.CharField(max_length=100, default='Mwalish')
    title = models.CharField(max_length=200, default='Software Engineering Student')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    avatar = models.URLField(blank=True, help_text='Fallback external avatar URL (used if no profile_image is uploaded)')
    profile_image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    skills = models.CharField(max_length=500, blank=True, help_text='Comma separated skills')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Personal Info'
        verbose_name_plural = 'Personal Info'

    def __str__(self):
        return self.name

    def skill_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]

    def save(self, *args, **kwargs):
        # Single-instance enforcement: every save writes to pk=1, so a
        # second "create" just overwrites the same row instead of adding
        # a new one. This holds regardless of which code path saves it
        # (admin, API, shell), not just the get_or_create() convention
        # used in the view.
        self.pk = 1
        super().save(*args, **kwargs)


class Project(models.Model):
    """A project showcased on the portfolio platform."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=500, help_text='Comma separated, e.g. React, Django, PostgreSQL')
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def tech_list(self):
        """Return tech stack as a list."""
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f'{base_slug}-{counter}'
            self.slug = slug
        super().save(*args, **kwargs)


class CodeSnippet(models.Model):
    """A reusable code snippet, optionally tied to a project."""
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=50, help_text='e.g. Python, JavaScript, SQL')
    code = models.TextField()
    description = models.TextField(blank=True)
    project = models.ForeignKey(
        Project, related_name='snippets', on_delete=models.CASCADE,
        null=True, blank=True,
        help_text='Optional — leave blank for a standalone snippet',
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
