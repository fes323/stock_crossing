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
    
    path('shop/filter/discountList/<shop_id>/', views.discountListFilterByShop, name='shopFilterDiscountList'),
    path('shop/filter/OldDiscountList/<shop_id>/', views.discountListFilterByShop, name='shopFilterDiscountListOld'),
    path('shop/filter/CurrentDiscountList/<shop_id>/', views.discountListFilterByShop, name='shopFilterDiscountListCurrent'),
    
    path('manager/filter/discountList/<manager_id>/', views.discountListFilterByManager, name='managerFilterDiscountList'),
    path('manager/filter/OldDiscountList/<manager_id>/', views.discountListFilterByManager, name='managerFilterDiscountListOld'),
    path('manager/filter/CurrentDiscountList/<manager_id>/', views.discountListFilterByManager, name='managerFilterDiscountListCurrent'),
    
    path('discountList/<discount_slug>/', views.discountDetail, name='discountDetail'),
    path('discountList/delete/<discount_slug>/', views.deleteDiscount, name='deleteDiscount'),
]