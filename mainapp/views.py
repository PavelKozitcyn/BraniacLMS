from django.http import HttpResponse
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'index.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class CoursesPageView(TemplateView):
    template_name = 'courses_list.html'


class DocSitePageView(TemplateView):
    template_name = 'doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class NewsPageView(TemplateView):
    template_name = 'news.html'
