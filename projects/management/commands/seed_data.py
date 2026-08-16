from django.core.management.base import BaseCommand
from projects.models import Project, PersonalInfo


class Command(BaseCommand):
    help = 'Seed the database with sample projects and personal info'

    def handle(self, *args, **options):
        # Seed personal info (single record)
        profile, created = PersonalInfo.objects.get_or_create(pk=1)
        profile.name = 'Mwalish'
        profile.title = 'Software Engineering Student & Developer'
        profile.bio = (
            "I'm Mwalish, a software engineering student passionate about building "
            "innovative, full-stack applications. I love turning ideas into real, "
            "working products that solve problems and create delightful experiences."
        )
        profile.location = 'Nairobi, Kenya'
        profile.avatar = 'https://avatars.githubusercontent.com/u/placeholder'
        profile.github = 'https://github.com/mwalish'
        profile.linkedin = 'https://linkedin.com/in/mwalish'
        profile.twitter = 'https://twitter.com/mwalish'
        profile.email = 'mwalish@example.com'
        profile.skills = 'Python, Django, JavaScript, React, PostgreSQL, REST APIs, Git, Docker'
        profile.save()
        sample_projects = [
            {
                'title': 'AI Task Manager',
                'description': 'A smart task management app that uses AI to prioritize your daily tasks and suggest optimal schedules.',
                'tech_stack': 'React, Django, PostgreSQL, OpenAI API',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example',
                'featured': True,
            },
            {
                'title': 'Weather Dashboard',
                'description': 'Real-time weather dashboard with beautiful visualizations, 7-day forecasts, and location-based alerts.',
                'tech_stack': 'Vue, Express, REST API, Chart.js',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example',
                'featured': False,
            },
            {
                'title': 'E-Commerce Store',
                'description': 'Full-featured e-commerce platform with cart, payments, admin dashboard, and order tracking.',
                'tech_stack': 'Next.js, Django, Stripe, Redis',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example',
                'featured': True,
            },
            {
                'title': 'Dev Social',
                'description': 'A social network for developers to share code snippets, collaborate on projects, and build communities.',
                'tech_stack': 'React, Django REST, WebSockets, Docker',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example',
                'featured': False,
            },
            {
                'title': 'Fitness Tracker',
                'description': 'Mobile-first fitness tracking app with workout plans, progress analytics, and gamified challenges.',
                'tech_stack': 'Flutter, Node.js, MongoDB',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example',
                'featured': False,
            },
            {
                'title': 'Real Estate Finder',
                'description': 'Property search platform with map-based filtering, price predictions, and virtual tours.',
                'tech_stack': 'Angular, Django, MapBox, ML',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example',
                'featured': True,
            },
        ]

        # Clear existing data and reseed
        Project.objects.all().delete()
        for data in sample_projects:
            Project.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(sample_projects)} projects'))
