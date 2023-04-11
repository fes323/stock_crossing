from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage),
    path('discountList', views.discountList),
    path('statistics', views.statistics),
]