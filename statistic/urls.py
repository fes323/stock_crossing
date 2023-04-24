from django.urls import path
from django.views.generic import TemplateView
from statistic.views import Statistic


urlpatterns = [
    path('statistic', Statistic.as_view(), name='statistic'),
]