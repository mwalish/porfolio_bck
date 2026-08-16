from django.db import migrations, models
import django.db.models.deletion
from django.utils.text import slugify


def populate_project_slugs(apps, schema_editor):
    """Backfill a unique slug for every existing project from its title."""
    Project = apps.get_model('projects', 'Project')
    seen = set()
    for project in Project.objects.all():
        base_slug = slugify(project.title) or f'project-{project.pk}'
        slug = base_slug
        counter = 1
        while slug in seen or Project.objects.filter(slug=slug).exclude(pk=project.pk).exists():
            counter += 1
            slug = f'{base_slug}-{counter}'
        seen.add(slug)
        project.slug = slug
        project.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_profile_avatar_image'),
    ]

    operations = [
        # ---- PersonalInfo (renamed from Profile) ----
        migrations.RenameModel(old_name='Profile', new_name='PersonalInfo'),
        migrations.RenameField(model_name='personalinfo', old_name='avatar_image', new_name='profile_image'),
        migrations.AlterModelOptions(
            name='personalinfo',
            options={'verbose_name': 'Personal Info', 'verbose_name_plural': 'Personal Info'},
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='avatar',
            field=models.URLField(blank=True, help_text='Fallback external avatar URL (used if no profile_image is uploaded)'),
        ),

        # ---- Project: rename created_at -> created, add slug ----
        migrations.RenameField(model_name='project', old_name='created_at', new_name='created'),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created']},
        ),
        # Add nullable first so the migration works against existing rows,
        # then backfill, then tighten to match the final model definition.
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=220, blank=True, null=True, unique=True),
        ),
        migrations.RunPython(populate_project_slugs, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=220, blank=True, unique=True),
        ),

        # ---- CodeSnippet (new) ----
        migrations.CreateModel(
            name='CodeSnippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(help_text='e.g. Python, JavaScript, SQL', max_length=50)),
                ('code', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(
                    blank=True, null=True,
                    help_text='Optional — leave blank for a standalone snippet',
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='snippets', to='projects.project',
                )),
            ],
            options={'ordering': ['-created']},
        ),
    ]
