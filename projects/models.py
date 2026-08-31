from django.db import models
from django.utils.text import slugify


class PersonalInfo(models.Model):
    """
    Single-instance personal profile for the portfolio owner.
    save() always forces pk=1 so only one row can ever exist.
    """
    name = models.CharField(max_length=100, default='Mwalish')
    title = models.CharField(max_length=200, default='Software Engineering Student')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    avatar = models.URLField(
        blank=True,
        help_text='Fallback external avatar URL (used if no profile_image is uploaded)'
    )
    profile_image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True, help_text='Personal website or blog')
    # Legacy comma-separated skills (prefer Skill model)
    skills = models.CharField(
        max_length=500,
        blank=True,
        help_text='Comma separated skills (legacy — prefer the Skill model)'
    )
    resume = models.FileField(
        upload_to='resume/',
        blank=True,
        null=True,
        help_text='CV/resume PDF for the download button'
    )
    # Optional "Now" / status line (popular on modern portfolios)
    now_status = models.CharField(
        max_length=300,
        blank=True,
        help_text='What you are currently working on / focusing on'
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Personal Info'
        verbose_name_plural = 'Personal Info'

    def __str__(self):
        return self.name

    def skill_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Skill(models.Model):
    """A skill with proficiency, category, and optional visual metadata."""
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools'),
        ('mobile', 'Mobile'),
        ('devops', 'DevOps'),
        ('soft', 'Soft Skills'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    percentage = models.PositiveSmallIntegerField(
        default=50,
        help_text='0-100 proficiency'
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='frontend'
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text='Icon name (e.g. "react", "python", "figma") for frontend use'
    )
    color = models.CharField(
        max_length=20,
        blank=True,
        help_text='Hex or CSS color for progress bars / badges (e.g. #61DAFB)'
    )
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers show first')

    class Meta:
        ordering = ['order', '-percentage']

    def __str__(self):
        return f'{self.name} ({self.percentage}%)'


class Experience(models.Model):
    """Education or work timeline entry."""
    TYPE_CHOICES = [
        ('education', 'Education'),
        ('work', 'Work'),
        ('volunteer', 'Volunteer'),
        ('internship', 'Internship'),
    ]
    title = models.CharField(max_length=200, help_text='Role or degree title')
    organization = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='work')
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True,
        help_text='Leave blank for "Present"'
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date', 'order']

    def __str__(self):
        return f'{self.title} @ {self.organization}'


class Testimonial(models.Model):
    """Recommendation / testimonial shown on the site."""
    name = models.CharField(max_length=150)
    role = models.CharField(
        max_length=200,
        blank=True,
        help_text='e.g. "CTO at Acme" or "Classmate"'
    )
    message = models.TextField()
    avatar = models.URLField(blank=True, help_text='Optional avatar image URL')
    linkedin = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created']

    def __str__(self):
        return f'{self.name} — {self.message[:40]}'


class ContactMessage(models.Model):
    """Message submitted through the public contact form."""
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.name} <{self.email}> — {self.created:%Y-%m-%d}'


class Project(models.Model):
    """
    Showcase project with case-study style fields for a stunning portfolio.
    """
    CATEGORY_CHOICES = [
        ('fullstack', 'Full-Stack'),
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('mobile', 'Mobile'),
        ('ai', 'AI / ML'),
        ('devops', 'DevOps'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    short_description = models.CharField(
        max_length=300,
        blank=True,
        help_text='One-liner for project cards'
    )
    description = models.TextField(help_text='Full project overview')
    # Case-study fields
    problem = models.TextField(blank=True, help_text='The problem this project solves')
    solution = models.TextField(blank=True, help_text='How you approached / solved it')
    challenges = models.TextField(blank=True, help_text='Key challenges & how you overcame them')
    outcome = models.TextField(
        blank=True,
        help_text='Results, metrics, impact (e.g. "40% faster load times")'
    )
    # Media
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text='External cover image URL')
    demo_video = models.URLField(
        blank=True,
        help_text='Loom, YouTube, or other demo video URL'
    )
    # Links & tech
    tech_stack = models.CharField(
        max_length=500,
        help_text='Comma separated, e.g. React, Django, PostgreSQL'
    )
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    # Meta
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='fullstack'
    )
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(
        default=0,
        help_text='Manual sort order (lower = higher priority)'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-featured', '-created']

    def __str__(self):
        return self.title

    def tech_list(self):
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


class ProjectImage(models.Model):
    """Extra screenshots / gallery images for a project."""
    project = models.ForeignKey(
        Project,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.project.title} — image {self.order or self.pk}'


class CodeSnippet(models.Model):
    """Reusable code snippet, optionally tied to a project."""
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=50, help_text='e.g. Python, JavaScript, SQL')
    code = models.TextField()
    description = models.TextField(blank=True)
    project = models.ForeignKey(
        Project,
        related_name='snippets',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='Optional — leave blank for a standalone snippet'
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Simple blog / articles section.
    Supports Markdown content on the frontend.
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=270, unique=True, blank=True)
    excerpt = models.CharField(
        max_length=400,
        blank=True,
        help_text='Short summary shown on cards'
    )
    content = models.TextField(help_text='Full post body (Markdown or HTML)')
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    cover_image_url = models.URLField(blank=True, null=True)
    tags = models.CharField(
        max_length=300,
        blank=True,
        help_text='Comma-separated tags'
    )
    featured = models.BooleanField(default=False)
    published = models.BooleanField(
        default=False,
        help_text='Only published posts appear on the public API'
    )
    published_at = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created']

    def __str__(self):
        return self.title

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f'{base_slug}-{counter}'
            self.slug = slug
        if self.published and not self.published_at:
            from django.utils import timezone
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
