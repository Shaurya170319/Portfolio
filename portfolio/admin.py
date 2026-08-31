from django.contrib import admin
from .models import Experience, Project, Skill, Certificate, About, SocialLink


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'duration')
    search_fields = ('title', 'company_name')
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'company_name', 'duration')
        }),
        ('Content', {
            'fields': ('description', 'points', 'skills')
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'project_type', 'is_featured')
        }),
        ('Content', {
            'fields': ('description', 'image', 'tags')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date')
    search_fields = ('title', 'issuer')
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'issuer', 'date', 'icon_class')
        }),
        ('Files & Links', {
            'fields': ('certificate_file', 'credential_url')
        }),
    )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fieldsets = (
        ('About Section', {
            'fields': ('bio', 'graduation_date', 'internship_duration', 'certifications_count')
        }),
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url')
    search_fields = ('platform',)
