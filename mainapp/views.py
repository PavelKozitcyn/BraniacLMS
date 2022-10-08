from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from mainapp import forms as mainapp_forms
from mainapp import models as mainapp_models
from datetime import datetime
from django.core.paginator import Paginator

from .models import News

class MainPageView(TemplateView):
    template_name = 'index.html'

class NewsPageView(ListView):
    model = mainapp_models.News
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

class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)


class NewsDetailView(DetailView):
    model = mainapp_models.News


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = mainapp_models.News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)

class CoursesPageView(TemplateView):
    template_name = 'courses_list.html'

    def get_context_data(self, **kwargs):
        context = super(CoursesPageView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context

class CoursesDetailView(TemplateView):
    template_name = "courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lesson.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.CourseTeachers.objects.filter(course=context["course_object"])
        if not self.request.user.is_anonymous:
            if not mainapp_models.CourseFeedback.objects.filter(
                    course=context["course_object"], user=self.request.user
            ).count():
                context["feedback_form"] = mainapp_forms.CourseFeedbackForm(
                    course=context["course_object"], user=self.request.user
                )
        context["feedback_list"] = mainapp_models.CourseFeedback.objects.filter(
            course=context["course_object"]
        ).order_by("-created", "-rating")[:5]
        return context

class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = mainapp_models.CourseFeedback
    form_class = mainapp_forms.CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string("mainapp/includes/feedback_card.html", context={"item": self.object})
        return JsonResponse({"card": rendered_card})


class LoginPageView(TemplateView):
    template_name = 'login.html'

class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class DocSitePageView(TemplateView):
    template_name = 'doc_site.html'