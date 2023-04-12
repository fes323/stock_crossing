from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainPage),
    path('discountList', views.discountList, name='discountList'),
    path('discountListOld', views.discountList, name='discountListOld'),
    path('discountList/<discount_slug>/', views.discountDetail, name='discountDetail'),
    path('statistics', views.statistics),
]