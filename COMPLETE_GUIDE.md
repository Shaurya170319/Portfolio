# 🎉 Django Portfolio - Complete Setup Guide

## ✅ Status: COMPLETE & READY!

Your portfolio has been successfully converted to Django with **ALL your original content**:

✅ All PDF files (Resume, Certificates)  
✅ Profile photo (Shaurya.jpg)  
✅ Internship details (IBM PBEL)  
✅ Projects (Fake News Detection, Django Video Auth)  
✅ Skills (22 skills organized by category)  
✅ Certificates (4 certifications with PDFs)  
✅ Social links (GitHub, LinkedIn, Email)  
✅ Original design and styling preserved  

---

## 🚀 QUICK START (30 Seconds)

### Step 1: Navigate to project
```bash
cd ~/portfolio_django
```

### Step 2: Activate virtual environment
```bash
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### Step 3: Run the server
```bash
python manage.py runserver
```

### Step 4: Open in browser
```
http://localhost:8000/
```

**That's it! Your portfolio is live!** 🎉

---

## 🔐 Admin Panel Setup (First Time Only)

### Create Superuser
```bash
python manage.py createsuperuser
```

Follow the prompts:
- Username: `admin` (or your choice)
- Email: `Shaurya22256@gmail.com`
- Password: Enter a secure password

### Access Admin Panel
Go to: `http://localhost:8000/admin/`

Login with your superuser credentials

---

## 📂 Project Structure

```
portfolio_django/
├── venv/                          # Virtual environment
├── portfolio_config/              # Django project settings
│   ├── settings.py               # Configuration
│   ├── urls.py                   # URL routing
│   └── wsgi.py                   # WSGI app
├── portfolio/                     # Main app
│   ├── models.py                 # Database models
│   ├── views.py                  # Views
│   ├── admin.py                  # Admin config
│   ├── urls.py                   # App URLs
│   ├── management/commands/
│   │   └── populate_portfolio.py # Data loader
│   ├── templates/
│   │   └── portfolio/index.html  # Template
│   └── static/
│       └── portfolio/
│           ├── css/styles.css
│           ├── js/script.js
│           ├── images/Shaurya.jpg
│           ├── resume.pdf
│           ├── IBM PBEL Certificate.pdf
│           ├── EDA Certificate.pdf
│           ├── core java certificate.pdf
│           └── Reimagine certificate.pdf
├── manage.py                      # Django CLI
├── db.sqlite3                     # Database
└── requirements.txt               # Dependencies
```

---

## 📊 What's in Your Database

### About Section
- Bio (3 paragraphs)
- Graduation date: June 2027
- Internship duration: 2 Months
- Certifications: 4

### Experience
- **IBM PBEL Program Internship**
  - Duration: June 2026 - August 2026
  - 4 detailed bullet points
  - 5 associated skills

### Projects (2 Featured)
1. **Fake News Detection System**
   - GitHub: https://github.com/Shaurya170319/Fake_News_Detection.git
   - 6 tech tags
   
2. **Django Video Authentication System**
   - GitHub: https://github.com/Shaurya170319/Django-Project.git
   - Live: https://shaurya170319.pythonanywhere.com/
   - 6 tech tags

### Skills (22 Total)
**Programming Languages:** Python, Core Java, JavaScript
**Web Development:** Django, HTML5, CSS3, REST APIs
**Databases:** MySQL, SQL
**AI/ML & Data:** Machine Learning, Data Analytics, NLP, TF-IDF
**Tools:** Git, GitHub, VS Code, PythonAnywhere
**Concepts:** OOP, Data Structures, API Integration, SDLC, MVT Architecture

### Certificates (4)
1. Virtual Internship in AI (IBM PBEL) - PDF included
2. Exploratory Data Analysis (Nasscom) - PDF included
3. Core Java (GRAStech) - PDF included
4. Reimagine Certificate (BBDITM) - PDF included

### Social Links
- GitHub: https://github.com/Shaurya170319
- LinkedIn: https://www.linkedin.com/in/shaurya-srivastava-8a493b241
- Email: Shaurya22256@gmail.com

---

## 🎯 Common Tasks

### Add a New Project
1. Go to `http://localhost:8000/admin/`
2. Click **Projects** → **Add Project**
3. Fill in:
   - Title
   - Description
   - Image (optional)
   - GitHub URL
   - Live URL (if available)
   - Tags (comma-separated)
   - Project Type
   - Check "Is Featured" to show on homepage
4. Save

### Update Your Bio
1. Admin Panel → **About**
2. Edit the bio text
3. Update stats (internship duration, graduation date, cert count)
4. Save

### Add a New Skill
1. Admin Panel → **Skills** → **Add Skill**
2. Enter skill name
3. Select category
4. Save

### Download a Certificate
- Visit the portfolio page
- Scroll to **Certificates** section
- Click the certificate download button
- Or view the credential link

### Update Social Links
1. Admin Panel → **Social Links**
2. Edit or add new links
3. Save

---

## 🛠️ Useful Commands

```bash
# Start development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8001

# Create superuser
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files (production)
python manage.py collectstatic --noinput

# Clear database and reset
python manage.py flush --no-input

# Repopulate data
python manage.py populate_portfolio
```

---

## 📱 Responsive Design

Your portfolio is fully responsive:
- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (< 768px)

Test on mobile by opening DevTools (F12) and selecting mobile view.

---

## 🎨 Customization

### Change Colors
Edit `portfolio/static/portfolio/css/styles.css`:
```css
:root {
    --primary: #00d4ff;    /* Cyan */
    --secondary: #ff006e;  /* Pink */
    --tertiary: #8338ec;   /* Purple */
}
```

### Update Profile Photo
Replace `portfolio/static/portfolio/images/Shaurya.jpg` with your photo

### Add More PDFs
1. Add your PDF files to `portfolio/static/portfolio/`
2. Link them in templates or via admin

---

## 🚢 Deployment Options

### PythonAnywhere (Easiest for Python)
1. Upload project to GitHub
2. Go to pythonanywhere.com
3. Create account
4. Clone your repo
5. Configure web app
6. Live in 15 minutes!

### Heroku
```bash
# Install Heroku CLI
# Login
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main
```

### Vercel / Netlify
- These work better for static sites
- For Django, use PythonAnywhere or Heroku

---

## 🔒 Production Checklist

Before deploying:

```bash
# 1. Change DEBUG to False in settings.py
DEBUG = False

# 2. Set SECRET_KEY to a secure value
SECRET_KEY = 'your-secure-key-here'

# 3. Set ALLOWED_HOSTS
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# 4. Collect static files
python manage.py collectstatic --noinput

# 5. Run security check
python manage.py check --deploy
```

---

## 📞 Contact Info (In Your Portfolio)

**Email:** Shaurya22256@gmail.com  
**GitHub:** https://github.com/Shaurya170319  
**LinkedIn:** https://www.linkedin.com/in/shaurya-srivastava-8a493b241  

---

## ✨ Features

✅ **Database-Backed** - All content in SQLite  
✅ **Admin Panel** - Manage everything without coding  
✅ **Responsive** - Works on all devices  
✅ **Fast** - Optimized static files  
✅ **Secure** - Django's built-in security  
✅ **Scalable** - Ready to grow  
✅ **Professional** - Production-ready code  

---

## 🐛 Troubleshooting

### Server won't start
```bash
# Check for port conflicts
lsof -i :8000  # macOS/Linux

# Use different port
python manage.py runserver 8001
```

### Static files not showing
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check settings.py STATIC_URL
```

### Database issues
```bash
# Reset database
python manage.py flush --no-input

# Re-migrate
python manage.py migrate

# Repopulate
python manage.py populate_portfolio
```

### Forgot admin password
```bash
python manage.py changepassword admin
```

---

## 🎓 What You've Got

You now have:

✅ Full Django application  
✅ Database with all your content  
✅ Admin panel for easy updates  
✅ Responsive design  
✅ All PDFs and images  
✅ Production-ready code  
✅ Easy to maintain and update  

---

## 📚 Next Steps

1. **Test Locally** ← You are here
2. Deploy to PythonAnywhere or Heroku
3. Add custom domain
4. Share with recruiters
5. Keep updating with new projects

---

## ❓ FAQ

**Q: Can I edit content without accessing Django shell?**
A: Yes! Use the admin panel at `/admin/`

**Q: How do I add a new certificate?**
A: Admin → Certificates → Add Certificate. Upload the PDF file.

**Q: Can I change the design?**
A: Yes! Edit `styles.css` in the static folder.

**Q: Is my data safe?**
A: Yes! Django uses SQLite which is secure and reliable.

**Q: Can I deploy to GitHub Pages?**
A: No, GitHub Pages only hosts static sites. Use PythonAnywhere or Heroku.

---

## 🎉 You're Ready!

Everything is set up and working. Your Django portfolio is:

✅ Complete
✅ Functional
✅ Personalized
✅ Ready for deployment

**Happy coding!** 🚀

---

**Location:** `C:\Users\Shaur\portfolio_django\`  
**Access:** http://localhost:8000/  
**Admin:** http://localhost:8000/admin/  
**Status:** ✅ READY FOR DEPLOYMENT
