from django.urls import path
from mainapp import views
from .views import *

from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('contacts/', views.ContactsPageView.as_view(), name='contacts'),
    path('courses_list/', views.CoursesPageView.as_view(), name='courses'),
    path('doc_site/', views.DocSitePageView.as_view(), name='docs'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('news/', views.NewsPageView.as_view(), name='news'),
]
