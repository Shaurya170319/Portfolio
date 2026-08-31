# Django Portfolio - Setup Guide

Your portfolio has been successfully converted to a full Django application!

## Project Structure

```
portfolio_django/
├── venv/                          # Virtual environment
├── portfolio_config/              # Django project settings
│   ├── settings.py               # Project configuration
│   ├── urls.py                   # Main URL routing
│   └── wsgi.py                   # WSGI application
├── portfolio/                     # Main Django app
│   ├── models.py                 # Database models
│   ├── views.py                  # View logic
│   ├── admin.py                  # Admin interface
│   ├── urls.py                   # App URL routing
│   ├── management/
│   │   └── commands/
│   │       └── populate_portfolio.py  # Data population script
│   ├── templates/
│   │   └── portfolio/
│   │       └── index.html        # Main template
│   └── static/
│       └── portfolio/
│           ├── css/styles.css
│           ├── js/script.js
│           └── images/profile.jpg
├── manage.py                      # Django management script
└── db.sqlite3                     # Database (auto-created)
```

## Quick Start

### 1. Navigate to the project directory
```bash
cd ~/portfolio_django
```

### 2. Activate the virtual environment
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Populate portfolio data
```bash
python manage.py populate_portfolio
```

This will add all your portfolio information (experience, projects, skills, certificates, social links) to the database.

### 4. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account. Example:
- Username: admin
- Email: your@email.com
- Password: (enter a secure password)

### 5. Run the development server
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

### 6. Access your portfolio
- **Portfolio**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

## Key Features

### Database Models

**Experience**
- Title, Company Name, Duration
- Description and Bullet Points
- Associated Skills

**Project**
- Title, Description, Images
- GitHub and Live URLs
- Tags and Project Type
- Featured flag for homepage display

**Skill**
- Name and Category (Languages, Web Dev, Databases, AI/ML, Tools, Concepts)
- Organized by category automatically

**Certificate**
- Title, Issuer, Date
- Credential URL and PDF file upload
- Custom icon class

**About**
- Bio text
- Graduation date, internship duration
- Certifications count

**SocialLink**
- Platform, URL, Icon class
- Display in hero section and contact area

## Admin Panel Features

The Django admin panel allows you to:

1. **Manage Experience**: Add/edit/delete your work experiences
2. **Manage Projects**: Create new projects with images, links, and tags
3. **Manage Skills**: Add technical skills and organize by category
4. **Manage Certificates**: Upload certificates and credential links
5. **Manage About Section**: Update your bio and stats
6. **Manage Social Links**: Add/edit your social media profiles

## Customization

### Adding a New Project

1. Go to http://localhost:8000/admin/
2. Click "Projects" in the left sidebar
3. Click "Add Project"
4. Fill in the details:
   - Title: Your project name
   - Description: What the project does
   - Image: Upload a project screenshot (optional)
   - GitHub URL: Link to your repository
   - Live URL: Link to live demo (if available)
   - Tags: Comma-separated technologies used
   - Project Type: e.g., "Academic Project", "Personal Project"
   - Is Featured: Check this to show on homepage

### Updating Your About Section

1. Go to Admin Panel → About
2. Edit the existing About entry
3. Update your bio and statistics
4. Save

### Styling

The CSS file is located at:
```
portfolio/static/portfolio/css/styles.css
```

Modify this file to customize colors, fonts, and layouts. The changes will reflect immediately when you refresh the page.

## Static Files

In production, collect static files using:
```bash
python manage.py collectstatic --noinput
```

## Database

The project uses SQLite by default (db.sqlite3). For production, consider switching to PostgreSQL or MySQL.

## Environment Variables (Production)

For production deployment, set:
```
DEBUG=False
SECRET_KEY=your-secure-secret-key
ALLOWED_HOSTS=yourdomain.com
```

## Deployment

To deploy to PythonAnywhere or Heroku:

1. Create a `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

2. Configure `DEBUG = False` in settings.py

3. Update `ALLOWED_HOSTS` with your domain

4. Follow platform-specific deployment guides

## Useful Commands

```bash
# Create a new migration after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell
python manage.py shell

# Run tests
python manage.py test

# Create superuser
python manage.py createsuperuser

# Populate data
python manage.py populate_portfolio
```

## Troubleshooting

**Static files not showing:**
- Run `python manage.py collectstatic --noinput`
- Check `STATIC_URL` in settings.py

**Template not found:**
- Ensure templates are in `portfolio/templates/portfolio/`
- Check `APP_DIRS = True` in settings.py

**Database errors:**
- Run `python manage.py migrate`
- Check your models for syntax errors

## Next Steps

1. ✅ Portfolio is running locally
2. Add more projects and experiences via the admin panel
3. Customize styling in `styles.css`
4. Update social links
5. Deploy to production (PythonAnywhere, Heroku, or your own server)

Enjoy your Django portfolio! 🚀
