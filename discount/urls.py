from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.mainPage, name='home'),
    path('discountList', views.discountList, name='discountList'),
    path('OldDiscountList', views.discountList, name='OldDiscountList'),
    path('CurrentDiscountList', views.discountList, name='CurrentDiscountList'),
    path('search/', views.searchDiscount, name='search_results'),
    path('filter/discountList/<shop_id>/', views.discountListFilter, name='discountListFilterOnShop'),
    path('filter/OldDiscountList/<shop_id>/', views.discountListFilter, name='discountListFilterOnShop'),
    path('filter/CurrentDiscountList/<shop_id>/', views.discountListFilter, name='discountListFilterOnShop'),
    path('discountList/<discount_slug>/', views.discountDetail, name='discountDetail'),
    path('discountList/delete/<discount_slug>/', views.deleteDiscount, name='deleteDiscount'),
    path('statistics', views.statistics, name='statistics'),
]