from django.urls import path
from statistic.views import Statistic


urlpatterns = [
    path('statistic', Statistic.as_view(), name='statistic'),
]