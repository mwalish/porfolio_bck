# Portfolio Backend (Upgraded)

A production-ready **Django + Django REST Framework** backend for a modern developer portfolio.

Built for a stunning frontend experience: case-study projects, skills with icons/colors, experience timeline, testimonials, blog, contact form with email notifications, filtering, search, and more.

---

## Features

| Area | What you get |
|------|----------------|
| **Profile** | Single-instance personal info, avatar, resume, social links, “Now” status |
| **Projects** | Full case-study fields (problem, solution, challenges, outcome), gallery images, demo video, categories, featured flag, manual order |
| **Skills** | Category, proficiency %, icon name, color |
| **Experience** | Education / work / internship / volunteer timeline |
| **Testimonials** | Name, role, message, optional avatar & LinkedIn |
| **Blog** | Posts with excerpt, tags, cover image, published flag |
| **Contact** | Public form → stores message + optional email notification |
| **Code snippets** | Linked to projects or standalone |
| **API** | Filtering, search, ordering, pagination, Token auth for writes |
| **Admin** | Polished Django admin with image previews & inlines |
| **Health** | `/api/health/` for uptime checks |

---

## Quick Start (Local)

```bash
# 1. Create & activate virtualenv
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Environment
cp .env.example .env
# Edit .env if needed (defaults work for local SQLite)

# 4. Migrate & seed
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser

# 5. Run
python manage.py runserver
```

- API root: http://127.0.0.1:8000/api/
- Admin: http://127.0.0.1:8000/admin/
- Health: http://127.0.0.1:8000/api/health/

---

## API Endpoints

All under `/api/`.

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/profile/` | Public | Personal info |
| PUT/PATCH | `/profile/` | Token | Update profile |
| GET | `/projects/` | Public | List projects (filter: `featured`, `category`; search; order) |
| GET | `/projects/{slug}/` | Public | Project detail (includes images & snippets) |
| POST/PUT/PATCH/DELETE | `/projects/...` | Token | Manage projects |
| GET | `/skills/` | Public | Skills (`?category=frontend`) |
| GET | `/experience/` | Public | Timeline (`?type=work`) |
| GET | `/testimonials/` | Public | Testimonials |
| POST | `/contact/` | Public | Submit contact message |
| GET | `/posts/` | Public | Published blog posts |
| GET | `/posts/{slug}/` | Public | Post detail |
| GET | `/snippets/` | Public | Code snippets (`?project=id`) |
| POST | `/login/` | — | Obtain auth token (`username` + `password`) |
| GET | `/health/` | Public | Health check |

### Example: list featured projects

```bash
curl http://127.0.0.1:8000/api/projects/?featured=true
```

### Example: login & update profile

```bash
# Get token
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"yourpassword"}'

# Use token
curl http://127.0.0.1:8000/api/profile/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

---

## Project Model Highlights (Case Study)

Each project supports:

- `short_description` — card one-liner  
- `problem` / `solution` / `challenges` / `outcome` — story sections  
- `demo_video` — Loom / YouTube link  
- `category` — fullstack, frontend, backend, mobile, ai, devops, other  
- `featured` + `order` — control what appears first  
- Related `ProjectImage` gallery + `CodeSnippet`s  

This structure makes it easy to build rich project detail pages on the frontend.

---

## Production Notes

1. Set `DJANGO_DEBUG=False` and a strong `DJANGO_SECRET_KEY`.
2. Configure MySQL (or keep SQLite for small sites) via env vars.
3. Set CORS origins to your real frontend URL(s).
4. Configure SMTP and `CONTACT_NOTIFY_EMAIL` so contact form messages email you.
5. Serve media via WhiteNoise (already included) or move to S3/R2 later.
6. Run with Gunicorn:

```bash
gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000
```

---

## Frontend Tips

- Use the **list** serializers for cards (lighter payload).
- Use **detail** endpoints for case-study pages (includes `problem`, `solution`, `images`, `snippets`).
- Skills come with `icon` + `color` — perfect for animated progress bars or badges.
- Blog posts support Markdown content; render with a Markdown component on the frontend.
- Filter projects by `?category=ai&featured=true` for home-page sections.

---

## Folder Structure

```
portfolio_upgraded/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
├── portfolio/          # project settings & root URLs
├── projects/           # main app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── management/commands/seed_data.py
└── media/              # uploaded images & resume
```

---

## What Was Upgraded From the Original

- Richer **Project** model (case-study fields, category, order, demo video)
- **ProjectImage** gallery model
- **Skill** icons & colors
- **Post** (blog) model with publish workflow
- Better **Experience** types + location
- Contact form **email notifications**
- Filtering, search, ordering on projects & posts
- Health check endpoint
- Cleaner settings with `.env` support
- Improved seed data with realistic case studies
- Polished admin with image previews

---

## License

Use freely for your personal portfolio. Replace sample content with your own projects, bio, and links.

Happy shipping! 🚀
