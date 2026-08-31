from django.core.management.base import BaseCommand
from portfolio.models import Experience, Project, Skill, Certificate, About, SocialLink


class Command(BaseCommand):
    help = 'Populate portfolio with initial data'

    def handle(self, *args, **options):
        # Create About section
        about, created = About.objects.get_or_create(
            id=1,
            defaults={
                'bio': '''Currently pursuing a Bachelor's degree in Computer Science at Babu Banarasi Das Institute of Technology and Management (BBDITM), with an anticipated graduation date of June 2027.

I recently completed a Virtual Internship at IBM (PBEL Program) where I gained hands-on experience in Artificial Intelligence, Machine Learning, and Data Analytics. During the internship, I built a Fake News Detection System that achieves 96% accuracy using NLP and classification techniques.

My academic focus includes computer science fundamentals, programming, algorithms, and frameworks. I'm motivated to apply theoretical concepts to practical challenges and develop innovative solutions for real-world problems.''',
                'graduation_date': 'June 2027',
                'internship_duration': '2 Months',
                'certifications_count': 4,
            }
        )
        self.stdout.write(self.style.SUCCESS('Created About section'))

        # Create Experience
        exp, created = Experience.objects.get_or_create(
            title='ML Intern - Virtual Internship via FSP',
            defaults={
                'company_name': 'IBM PBEL Program',
                'duration': 'June 2026 - August 2026',
                'description': 'Virtual Internship in AI and Machine Learning',
                'points': '''Developed Fake News Detection System with ~96% accuracy using TF-IDF and Passive Aggressive Classifier
Built Flask backend API for serving ML model with real-time predictions
Integrated news-verification API to cross-check articles against live internet sources
Gained expertise in Python, AI, Machine Learning, and Data Analytics through practical project-based learning''',
                'skills': 'Python, Machine Learning, Flask, Data Analytics, NLP'
            }
        )
        self.stdout.write(self.style.SUCCESS('Created Experience'))

        # Create Projects
        projects_data = [
            {
                'title': 'Fake News Detection System',
                'description': 'ML pipeline for detecting fake news with ~96% accuracy. Integrated Flask backend serving REST API with real-time predictions. Combined model predictions with live news-verification API to cross-check articles.',
                'github_url': 'https://github.com/Shaurya170319/Fake_News_Detection.git',
                'live_url': '',
                'tags': 'Python, Flask, TF-IDF, Scikit-learn, NLP, REST API',
                'project_type': 'IBM Internship Project',
                'is_featured': True,
            },
            {
                'title': 'Django Video Authentication System',
                'description': 'Full-stack video library platform with secure user authentication. Implemented video upload/streaming with multiple format support. Designed RESTful APIs for frontend-backend communication. Deployed on PythonAnywhere for public access.',
                'github_url': 'https://github.com/Shaurya170319/Django-Project.git',
                'live_url': 'https://shaurya170319.pythonanywhere.com/',
                'tags': 'Django, JavaScript, MySQL, REST API, Authentication, PythonAnywhere',
                'project_type': 'Academic Project',
                'is_featured': True,
            }
        ]

        for proj_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=proj_data['title'],
                defaults=proj_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Project: {proj_data["title"]}'))

        # Create Skills
        skills_data = [
            ('Python', 'languages'),
            ('Core Java', 'languages'),
            ('JavaScript', 'languages'),
            ('Django', 'web'),
            ('HTML5', 'web'),
            ('CSS3', 'web'),
            ('REST APIs', 'web'),
            ('MySQL', 'database'),
            ('SQL', 'database'),
            ('Machine Learning', 'ml'),
            ('Data Analytics', 'ml'),
            ('NLP', 'ml'),
            ('TF-IDF', 'ml'),
            ('Git', 'tools'),
            ('GitHub', 'tools'),
            ('VS Code', 'tools'),
            ('PythonAnywhere', 'tools'),
            ('OOP', 'concepts'),
            ('Data Structures', 'concepts'),
            ('API Integration', 'concepts'),
            ('SDLC', 'concepts'),
            ('MVT Architecture', 'concepts'),
        ]

        for skill_name, category in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_name,
                category=category
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Skill: {skill_name}'))

        # Create Certificates with file paths
        certs_data = [
            {
                'title': 'Virtual Internship in AI',
                'issuer': 'IBM PBEL Program',
                'date': 'June 24 - August 27, 2026',
                'credential_url': 'https://courses.ibmmooc.skillsnetwork.site/certificates/540c061d16254077a019d5f886915005',
                'certificate_file': 'IBM PBEL Certificate.pdf',
                'icon_class': 'fab fa-python',
            },
            {
                'title': 'Exploratory Data Analysis',
                'issuer': 'Sector Skill Council Nasscom',
                'date': '',
                'credential_url': 'https://fsp-assessment-certificates.s3.ap-southeast-1.amazonaws.com/%27/s3/buckets/fsp-assessment-certificates%27/Shaurya%2BSrivastava_162483484.pdf',
                'certificate_file': 'EDA Certificate.pdf',
                'icon_class': 'fas fa-chart-bar',
            },
            {
                'title': 'Core Java Certificate',
                'issuer': 'GRAStech',
                'date': '',
                'credential_url': '',
                'certificate_file': 'core java certificate.pdf',
                'icon_class': 'fas fa-coffee',
            },
            {
                'title': 'Reimagine Certificate',
                'issuer': 'BBDITM - Reimagine IT Club',
                'date': 'Participation Certificate',
                'credential_url': '',
                'certificate_file': 'Reimagine certificate.pdf',
                'icon_class': 'fas fa-trophy',
            }
        ]

        for cert_data in certs_data:
            cert_file = cert_data.pop('certificate_file')
            cert, created = Certificate.objects.get_or_create(
                title=cert_data['title'],
                defaults={**cert_data, 'certificate_file': f'portfolio/{cert_file}'}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Certificate: {cert_data["title"]}'))

        # Create Social Links
        social_data = [
            {
                'platform': 'GitHub',
                'url': 'https://github.com/Shaurya170319',
                'icon_class': 'fab fa-github',
            },
            {
                'platform': 'LinkedIn',
                'url': 'https://www.linkedin.com/in/shaurya-srivastava-8a493b241',
                'icon_class': 'fab fa-linkedin',
            },
            {
                'platform': 'Email',
                'url': 'https://mail.google.com/mail/?view=cm&fs=1&to=Shaurya22256@gmail.com',
                'icon_class': 'fa-solid fa-envelope',
            }
        ]

        for social_data_item in social_data:
            social, created = SocialLink.objects.get_or_create(
                platform=social_data_item['platform'],
                defaults=social_data_item
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Social Link: {social_data_item["platform"]}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated portfolio with data'))
