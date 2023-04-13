from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainPage),
    path('discountList', views.discountList, name='discountList'),
    path('discountListOld', views.discountList, name='discountListOld'),
    path('discountListCurrent', views.discountList, name='discountListCurrent'),
    path('discountList/filter/<shop_id>/', views.discountList, name='discountListFilterOnShop'),
    path('discountList/<discount_slug>/', views.discountDetail, name='discountDetail'),
    path('discountList/delete/<discount_slug>/', views.deleteDiscount, name='deleteDiscount'),
    path('statistics', views.statistics, name='statistics'),
]