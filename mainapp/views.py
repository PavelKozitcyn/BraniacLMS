from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime
from django.core.paginator import Paginator

from .models import News

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
    paginated_by = 3

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get(
            'page',
            1
        )
        paginator = Paginator(News.object.all(), self.paginated_by)
        page = paginator.get_page(page_number)

        context = super().get_context_data(**kwargs)

        context['page'] = page

        return context