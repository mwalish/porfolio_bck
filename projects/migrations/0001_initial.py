# Generated manually for the upgraded portfolio backend

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=200)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Role or degree title', max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('education', 'Education'), ('work', 'Work'), ('volunteer', 'Volunteer'), ('internship', 'Internship')], default='work', max_length=20)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, help_text='Leave blank for "Present"', null=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-start_date', 'order'],
            },
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Mwalish', max_length=100)),
                ('title', models.CharField(default='Software Engineering Student', max_length=200)),
                ('bio', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('avatar', models.URLField(blank=True, help_text='Fallback external avatar URL (used if no profile_image is uploaded)')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True, help_text='Personal website or blog')),
                ('skills', models.CharField(blank=True, help_text='Comma separated skills (legacy — prefer the Skill model)', max_length=500)),
                ('resume', models.FileField(blank=True, help_text='CV/resume PDF for the download button', null=True, upload_to='resume/')),
                ('now_status', models.CharField(blank=True, help_text='What you are currently working on / focusing on', max_length=300)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Personal Info',
                'verbose_name_plural': 'Personal Info',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=270, unique=True)),
                ('excerpt', models.CharField(blank=True, help_text='Short summary shown on cards', max_length=400)),
                ('content', models.TextField(help_text='Full post body (Markdown or HTML)')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('cover_image_url', models.URLField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, help_text='Comma-separated tags', max_length=300)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=False, help_text='Only published posts appear on the public API')),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-published_at', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=220, unique=True)),
                ('short_description', models.CharField(blank=True, help_text='One-liner for project cards', max_length=300)),
                ('description', models.TextField(help_text='Full project overview')),
                ('problem', models.TextField(blank=True, help_text='The problem this project solves')),
                ('solution', models.TextField(blank=True, help_text='How you approached / solved it')),
                ('challenges', models.TextField(blank=True, help_text='Key challenges & how you overcame them')),
                ('outcome', models.TextField(blank=True, help_text='Results, metrics, impact (e.g. "40% faster load times")')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('image_url', models.URLField(blank=True, null=True, help_text='External cover image URL')),
                ('demo_video', models.URLField(blank=True, help_text='Loom, YouTube, or other demo video URL')),
                ('tech_stack', models.CharField(help_text='Comma separated, e.g. React, Django, PostgreSQL', max_length=500)),
                ('live_url', models.URLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(choices=[('fullstack', 'Full-Stack'), ('frontend', 'Frontend'), ('backend', 'Backend'), ('mobile', 'Mobile'), ('ai', 'AI / ML'), ('devops', 'DevOps'), ('other', 'Other')], default='fullstack', max_length=20)),
                ('featured', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0, help_text='Manual sort order (lower = higher priority)')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['order', '-featured', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('percentage', models.PositiveSmallIntegerField(default=50, help_text='0-100 proficiency')),
                ('category', models.CharField(choices=[('frontend', 'Frontend'), ('backend', 'Backend'), ('tools', 'Tools'), ('mobile', 'Mobile'), ('devops', 'DevOps'), ('soft', 'Soft Skills'), ('other', 'Other')], default='frontend', max_length=20)),
                ('icon', models.CharField(blank=True, help_text='Icon name (e.g. "react", "python", "figma") for frontend use', max_length=50)),
                ('color', models.CharField(blank=True, help_text='Hex or CSS color for progress bars / badges (e.g. #61DAFB)', max_length=20)),
                ('order', models.PositiveIntegerField(default=0, help_text='Lower numbers show first')),
            ],
            options={
                'ordering': ['order', '-percentage'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('role', models.CharField(blank=True, help_text='e.g. "CTO at Acme" or "Classmate"', max_length=200)),
                ('message', models.TextField()),
                ('avatar', models.URLField(blank=True, help_text='Optional avatar image URL')),
                ('linkedin', models.URLField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['order', '-created'],
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/gallery/')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.project')),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='CodeSnippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(help_text='e.g. Python, JavaScript, SQL', max_length=50)),
                ('code', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, help_text='Optional — leave blank for a standalone snippet', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='projects.project')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
