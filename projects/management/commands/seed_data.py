from django.core.management.base import BaseCommand
from django.utils import timezone
from projects.models import (
    Project, PersonalInfo, Skill, Experience,
    Testimonial, Post, CodeSnippet,
)


class Command(BaseCommand):
    help = 'Seed the database with realistic portfolio sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding portfolio data...')

        # ── Personal Info ──────────────────────────────────────────────
        profile, _ = PersonalInfo.objects.get_or_create(pk=1)
        profile.name = 'Mwalish'
        profile.title = 'Software Engineering Student & Full-Stack Developer'
        profile.bio = (
            "I'm Mwalish, a software engineering student passionate about building "
            "innovative, full-stack applications. I love turning ideas into real, "
            "working products that solve problems and create delightful experiences. "
            "Currently focused on Django, React, and clean API design."
        )
        profile.location = 'Nairobi, Kenya'
        profile.avatar = ''
        profile.github = 'https://github.com/mwalish'
        profile.linkedin = 'https://linkedin.com/in/mwalish'
        profile.twitter = 'https://twitter.com/mwalish'
        profile.email = 'mwalish@example.com'
        profile.website = ''
        profile.skills = (
            'Python, Django, JavaScript, React, TypeScript, PostgreSQL, '
            'REST APIs, Git, Docker, Tailwind CSS'
        )
        profile.now_status = 'Building polished full-stack products & learning system design'
        profile.save()
        self.stdout.write(self.style.SUCCESS('✓ Personal info'))

        # ── Skills ─────────────────────────────────────────────────────
        Skill.objects.all().delete()
        skills_data = [
            # Frontend
            {'name': 'React', 'percentage': 85, 'category': 'frontend', 'icon': 'react', 'color': '#61DAFB', 'order': 1},
            {'name': 'TypeScript', 'percentage': 75, 'category': 'frontend', 'icon': 'typescript', 'color': '#3178C6', 'order': 2},
            {'name': 'Tailwind CSS', 'percentage': 90, 'category': 'frontend', 'icon': 'tailwind', 'color': '#06B6D4', 'order': 3},
            {'name': 'Next.js', 'percentage': 70, 'category': 'frontend', 'icon': 'nextjs', 'color': '#000000', 'order': 4},
            # Backend
            {'name': 'Python', 'percentage': 90, 'category': 'backend', 'icon': 'python', 'color': '#3776AB', 'order': 1},
            {'name': 'Django / DRF', 'percentage': 88, 'category': 'backend', 'icon': 'django', 'color': '#092E20', 'order': 2},
            {'name': 'PostgreSQL', 'percentage': 75, 'category': 'backend', 'icon': 'postgresql', 'color': '#4169E1', 'order': 3},
            {'name': 'Node.js', 'percentage': 65, 'category': 'backend', 'icon': 'nodejs', 'color': '#339933', 'order': 4},
            # Tools
            {'name': 'Git & GitHub', 'percentage': 90, 'category': 'tools', 'icon': 'git', 'color': '#F05032', 'order': 1},
            {'name': 'Docker', 'percentage': 70, 'category': 'tools', 'icon': 'docker', 'color': '#2496ED', 'order': 2},
            {'name': 'VS Code', 'percentage': 95, 'category': 'tools', 'icon': 'vscode', 'color': '#007ACC', 'order': 3},
            # Soft
            {'name': 'Problem Solving', 'percentage': 90, 'category': 'soft', 'icon': 'brain', 'color': '#8B5CF6', 'order': 1},
            {'name': 'Communication', 'percentage': 85, 'category': 'soft', 'icon': 'message', 'color': '#EC4899', 'order': 2},
        ]
        for s in skills_data:
            Skill.objects.create(**s)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(skills_data)} skills'))

        # ── Experience ─────────────────────────────────────────────────
        Experience.objects.all().delete()
        experiences = [
            {
                'title': 'Software Engineering Student',
                'organization': 'University / Bootcamp',
                'type': 'education',
                'description': (
                    'Studying core CS concepts, data structures, algorithms, '
                    'and building full-stack projects with modern frameworks.'
                ),
                'location': 'Nairobi, Kenya',
                'start_date': '2023-09-01',
                'end_date': None,
                'order': 1,
            },
            {
                'title': 'Full-Stack Developer (Freelance)',
                'organization': 'Independent',
                'type': 'work',
                'description': (
                    'Designed and shipped client projects including REST APIs, '
                    'admin dashboards, and responsive React frontends.'
                ),
                'location': 'Remote',
                'start_date': '2024-03-01',
                'end_date': None,
                'order': 2,
            },
            {
                'title': 'Backend Intern',
                'organization': 'Local Tech Startup',
                'type': 'internship',
                'description': (
                    'Worked on Django REST APIs, database design, and '
                    'integration with third-party services.'
                ),
                'location': 'Nairobi',
                'start_date': '2024-06-01',
                'end_date': '2024-08-31',
                'order': 3,
            },
        ]
        for e in experiences:
            Experience.objects.create(**e)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(experiences)} experience entries'))

        # ── Projects (case-study style) ─────────────────────────────────
        Project.objects.all().delete()
        projects_data = [
            {
                'title': 'AI Task Manager',
                'short_description': 'Smart task prioritization powered by AI.',
                'description': (
                    'A full-stack task management app that uses AI to prioritize '
                    'daily tasks and suggest optimal schedules based on deadlines, '
                    'energy levels, and past completion patterns.'
                ),
                'problem': (
                    'People often struggle to decide what to work on next. '
                    'Traditional to-do lists lack prioritization intelligence.'
                ),
                'solution': (
                    'Built a React + Django app with OpenAI integration. Users '
                    'add tasks; the backend scores urgency/importance and returns '
                    'a ranked daily plan.'
                ),
                'challenges': (
                    'Prompt engineering for consistent prioritization scores, '
                    'rate-limit handling for the AI API, and keeping the UI fast '
                    'while waiting on external responses.'
                ),
                'outcome': (
                    'Reduced decision fatigue for test users. Average time-to-first-task '
                    'dropped noticeably in informal testing.'
                ),
                'tech_stack': 'React, Django, PostgreSQL, OpenAI API, Tailwind',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example/ai-task-manager',
                'category': 'ai',
                'featured': True,
                'order': 1,
            },
            {
                'title': 'Weather Dashboard',
                'short_description': 'Beautiful real-time weather with forecasts.',
                'description': (
                    'Real-time weather dashboard with 7-day forecasts, location-based '
                    'alerts, and clean data visualizations.'
                ),
                'problem': 'Most free weather UIs feel cluttered or outdated.',
                'solution': (
                    'Clean card-based UI, Chart.js visualizations, and a simple '
                    'Express backend that proxies and caches weather API responses.'
                ),
                'challenges': 'Handling geolocation permissions and API rate limits gracefully.',
                'outcome': 'Fast, mobile-friendly experience with clear visual hierarchy.',
                'tech_stack': 'Vue, Express, REST API, Chart.js',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example/weather-dashboard',
                'category': 'frontend',
                'featured': False,
                'order': 3,
            },
            {
                'title': 'E-Commerce Store',
                'short_description': 'Full-featured store with Stripe payments.',
                'description': (
                    'Complete e-commerce platform with product catalog, cart, '
                    'checkout via Stripe, admin dashboard, and order tracking.'
                ),
                'problem': 'Small businesses need a simple, reliable online store without heavy SaaS fees.',
                'solution': (
                    'Next.js frontend + Django backend + Stripe Checkout. '
                    'Admin can manage products and view orders in one place.'
                ),
                'challenges': (
                    'Idempotent payment handling, inventory race conditions, '
                    'and secure webhook processing.'
                ),
                'outcome': 'End-to-end purchase flow tested successfully; solid base for real shops.',
                'tech_stack': 'Next.js, Django, Stripe, Redis, PostgreSQL',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example/ecommerce',
                'category': 'fullstack',
                'featured': True,
                'order': 2,
            },
            {
                'title': 'Dev Social',
                'short_description': 'Social network for sharing code & collab.',
                'description': (
                    'A social platform for developers to share snippets, '
                    'collaborate on projects, and build communities.'
                ),
                'problem': 'Developers want a focused place to share code without general social noise.',
                'solution': 'React SPA + Django REST + WebSockets for real-time comments and presence.',
                'challenges': 'Real-time updates at scale and clean code rendering with syntax highlighting.',
                'outcome': 'Working MVP with auth, feed, and live comments.',
                'tech_stack': 'React, Django REST, WebSockets, Docker',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example/dev-social',
                'category': 'fullstack',
                'featured': False,
                'order': 4,
            },
            {
                'title': 'Fitness Tracker',
                'short_description': 'Mobile-first workouts with progress analytics.',
                'description': (
                    'Fitness tracking app with workout plans, progress charts, '
                    'and gamified challenges.'
                ),
                'problem': 'Many fitness apps are feature-heavy and intimidating for beginners.',
                'solution': 'Flutter mobile app + Node.js backend focused on simple logging and clear progress.',
                'challenges': 'Offline-first data sync and consistent cross-platform UI.',
                'outcome': 'Clean onboarding and motivating weekly progress views.',
                'tech_stack': 'Flutter, Node.js, MongoDB',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example/fitness-tracker',
                'category': 'mobile',
                'featured': False,
                'order': 5,
            },
            {
                'title': 'Real Estate Finder',
                'short_description': 'Map-based property search with smart filters.',
                'description': (
                    'Property search platform with map filtering, price insights, '
                    'and virtual tour links.'
                ),
                'problem': 'Finding the right property is slow when filters and maps are disconnected.',
                'solution': 'Angular frontend + Django API + Mapbox for interactive map search.',
                'challenges': 'Efficient geospatial queries and smooth map performance on mobile.',
                'outcome': 'Intuitive map + filter experience that feels modern.',
                'tech_stack': 'Angular, Django, MapBox, ML',
                'live_url': 'https://example.com',
                'github_url': 'https://github.com/example/real-estate',
                'category': 'fullstack',
                'featured': True,
                'order': 6,
            },
        ]

        created_projects = []
        for data in projects_data:
            p = Project.objects.create(**data)
            created_projects.append(p)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(created_projects)} projects'))

        # Sample snippet on first project
        if created_projects:
            CodeSnippet.objects.create(
                title='Task prioritization helper',
                language='Python',
                code=(
                    'def prioritize_tasks(tasks, weights):\n'
                    '    """Score tasks by urgency and importance."""\n'
                    '    scored = []\n'
                    '    for t in tasks:\n'
                    '        score = t.urgency * weights["urgency"] + t.importance * weights["importance"]\n'
                    '        scored.append((score, t))\n'
                    '    return [t for _, t in sorted(scored, reverse=True)]\n'
                ),
                description='Simple scoring function used in the AI Task Manager backend.',
                project=created_projects[0],
            )
            self.stdout.write(self.style.SUCCESS('✓ Sample code snippet'))

        # ── Testimonials ───────────────────────────────────────────────
        Testimonial.objects.all().delete()
        testimonials = [
            {
                'name': 'Alex Kimani',
                'role': 'Fellow Developer',
                'message': (
                    'Mwalish ships clean, well-structured code and is great at '
                    'explaining technical decisions. A pleasure to collaborate with.'
                ),
                'order': 1,
            },
            {
                'name': 'Sarah Otieno',
                'role': 'Project Mentor',
                'message': (
                    'Strong problem-solver who takes ownership of features from '
                    'design to deployment. The portfolio projects speak for themselves.'
                ),
                'order': 2,
            },
            {
                'name': 'James Mwangi',
                'role': 'Client',
                'message': (
                    'Delivered a solid MVP on time with clear communication throughout. '
                    'Would definitely work together again.'
                ),
                'order': 3,
            },
        ]
        for t in testimonials:
            Testimonial.objects.create(**t)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(testimonials)} testimonials'))

        # ── Blog Posts ─────────────────────────────────────────────────
        Post.objects.all().delete()
        posts = [
            {
                'title': 'Building a Portfolio Backend with Django REST Framework',
                'excerpt': (
                    'How I structured models, permissions, and a clean API '
                    'for a modern developer portfolio.'
                ),
                'content': (
                    '## Why a custom backend?\n\n'
                    'Static portfolios are fine, but a real API lets you manage '
                    'projects, skills, and messages without redeploying.\n\n'
                    '## Core models\n\n'
                    '- PersonalInfo (singleton)\n'
                    '- Project (with case-study fields)\n'
                    '- Skill, Experience, Testimonial, Post\n\n'
                    '## Key lessons\n\n'
                    'Keep public endpoints read-only, use Token auth for writes, '
                    'and design serializers that match what the frontend actually needs.'
                ),
                'tags': 'Django, REST API, Portfolio, Backend',
                'featured': True,
                'published': True,
                'published_at': timezone.now(),
            },
            {
                'title': 'Case Study Thinking for Portfolio Projects',
                'excerpt': (
                    'Turning “I built X” into a clear problem → solution → outcome story.'
                ),
                'content': (
                    'Hiring managers remember stories more than tech stacks.\n\n'
                    'For each project, write:\n'
                    '1. The problem\n'
                    '2. Your approach\n'
                    '3. Challenges\n'
                    '4. Measurable outcome\n\n'
                    'Even small personal projects become more impressive this way.'
                ),
                'tags': 'Career, Portfolio, Writing',
                'featured': False,
                'published': True,
                'published_at': timezone.now(),
            },
        ]
        for p in posts:
            Post.objects.create(**p)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(posts)} blog posts'))

        self.stdout.write(self.style.SUCCESS('\n🎉 Seed complete! Run the server and explore /api/'))
