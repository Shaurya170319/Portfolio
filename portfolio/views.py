from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Experience, Project, Skill, Certificate, About, SocialLink


class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all()
        context['projects'] = Project.objects.filter(is_featured=True)
        context['skills'] = Skill.objects.all()
        context['certificates'] = Certificate.objects.all()
        context['about'] = About.objects.first()
        context['social_links'] = SocialLink.objects.all()
        return context
