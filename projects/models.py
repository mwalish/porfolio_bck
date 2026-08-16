from django.db import models


class Profile(models.Model):
    """Personal profile information for the portfolio owner."""
    name = models.CharField(max_length=100, default='Mwalish')
    title = models.CharField(max_length=200, default='Software Engineering Student')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    avatar = models.URLField(blank=True)
    avatar_image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    skills = models.CharField(max_length=500, blank=True, help_text='Comma separated skills')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.name

    def skill_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]


class Project(models.Model):
    """A project showcased on the portfolio platform."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=500, help_text='Comma separated, e.g. React, Django, PostgreSQL')
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def tech_list(self):
        """Return tech stack as a list."""
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]
