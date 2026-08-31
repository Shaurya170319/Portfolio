from django.db import models
from django.utils import timezone


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    points = models.TextField(help_text="Bullet points separated by newlines")
    skills = models.CharField(max_length=500, help_text="Comma-separated skills")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} at {self.company_name}"

    @property
    def points_list(self):
        return [point.strip() for point in self.points.split('\n') if point.strip()]

    @property
    def skills_list(self):
        return [skill.strip() for skill in self.skills.split(',') if skill.strip()]


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    github_url = models.URLField(max_length=500, blank=True)
    live_url = models.URLField(max_length=500, blank=True)
    tags = models.CharField(max_length=500, help_text="Comma-separated tags")
    project_type = models.CharField(max_length=100, default="Project")
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('languages', 'Programming Languages'),
        ('web', 'Web Development'),
        ('database', 'Databases'),
        ('ml', 'AI/ML & Data'),
        ('tools', 'Tools & Technologies'),
        ('concepts', 'Concepts & Methodologies'),
    ]

    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='intermediate')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']
        unique_together = ['name', 'category']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()}) - {self.get_proficiency_display()}"


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(max_length=500, blank=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True)
    icon_class = models.CharField(max_length=100, default="fas fa-trophy")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class About(models.Model):
    bio = models.TextField()
    graduation_date = models.CharField(max_length=100)
    internship_duration = models.CharField(max_length=100)
    certifications_count = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return "Portfolio About Section"

    @property
    def bio_paragraphs(self):
        return [p.strip() for p in self.bio.split('\n\n') if p.strip()]


class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return self.platform
