from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.mainPage, name='home'),
    path('discountList', views.discountList, name='discountList'),
    path('OldDiscountList', views.discountList, name='OldDiscountList'),
    path('CurrentDiscountList', views.discountList, name='CurrentDiscountList'),
    path('search/', views.searchDiscount, name='search_results'),
    path('search/WihinAWeek/', views.startWithinAWeek, name='startWithinAWeek'),
    path('search/startTomorrow/', views.startTomorrow, name='startTomorrow'),
    path('filter/discountList/<shop_id>/', views.discountListFilterByShop, name='discountListFilterOnShop'),
    path('filter/OldDiscountList/<shop_id>/', views.discountListFilterByShop, name='discountListFilterOnShop'),
    path('filter/CurrentDiscountList/<shop_id>/', views.discountListFilterByShop, name='discountListFilterOnShop'),
    path('filter/discountList/manager/<manager_id>/', views.discountListFilterByManager, name='discountListFilterOnShop'),
    path('filter/OldDiscountList/manager/<manager_id>/', views.discountListFilterByManager, name='discountListFilterOnShop'),
    path('filter/CurrentDiscountList/manager/<manager_id>/', views.discountListFilterByManager, name='discountListFilterOnShop'),
    path('discountList/<discount_slug>/', views.discountDetail, name='discountDetail'),
    path('discountList/delete/<discount_slug>/', views.deleteDiscount, name='deleteDiscount'),
    path('statistics', views.statistics, name='statistics'),
]