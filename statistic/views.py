from django.shortcuts import render
from django.views.generic import TemplateView

class Statistic(TemplateView):
    template_name = 'statistics.html'