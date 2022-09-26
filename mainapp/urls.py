from django.urls import path
from .views import *

from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('courses_list/', CoursesPageView.as_view(), name='courses'),
    path('doc_site/', DocSitePageView.as_view(), name='docs'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('news/', NewsPageView.as_view(), name='news'),
]
