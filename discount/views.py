from datetime import *
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import DiscountData
from shops.models import Shop
from datetime import datetime


def discountList(request, shop_id=None):
    now = datetime.now()
    shopsList = Shop.objects.all().order_by('title')
    
    discountCurrent = DiscountData.objects.filter(startDate__lte=now).filter(endDate__gte=timezone.now()).order_by('-startDate')
    discountsOld = DiscountData.objects.filter(startDate__lte=now).filter(endDate__lte=timezone.now()).order_by('-startDate')
    discountsFuture = DiscountData.objects.filter(startDate__gte=now).order_by('startDate')
    
    discountCounter = discountsFuture.count()
    discountCounterOld = discountsOld.count()
    discountCounterCurrent = discountCurrent.count()
    
    if request.path == '/discountList':
        discounts = discountsFuture
        
    elif request.path == '/OldDiscountList':
        discounts = discountsOld
        
    elif request.path == '/CurrentDiscountList':
        discounts = discountCurrent
        
    context = {
        'discounts' : discounts,
        'counter' : discountCounter,
        'counterOLd' : discountCounterOld,
        'counterCurrent' : discountCounterCurrent,
        'shopListItem' : shopsList,
    }
    
    return render(request, template_name='discount_list.html', context=context)


def discountListFilter(request, shop_id):
    now = datetime.now()
    shopsList = Shop.objects.all().order_by('title')
    
    currentShop = Shop.objects.get(id=shop_id)

    discountCurrent = DiscountData.objects.filter(startDate__lte=timezone.now()).filter(shops__exact=shop_id).filter(endDate__gte=timezone.now()).order_by('-startDate')
    discountsOld = DiscountData.objects.filter(startDate__lte=timezone.now()).filter(shops__exact=shop_id).filter(endDate__lte=timezone.now()).order_by('-startDate')
    discountsFuture = DiscountData.objects.filter(startDate__gte=timezone.now()).filter(shops__exact=shop_id).order_by('startDate')
    
    discountCounter = discountsFuture.count()
    discountCounterOld = discountsOld.count()
    discountCounterCurrent = discountCurrent.count()
    
    if '/discountList' in request.path:
        discounts = discountsFuture
        
    elif '/OldDiscountList' in request.path:
        discounts = discountsOld
        
    elif '/CurrentDiscountList' in request.path:
        discounts = discountCurrent
    
    id_shop = shop_id
    
    context = {
        'discounts' : discounts,
        'counter' : discountCounter,
        'counterOLd' : discountCounterOld,
        'counterCurrent' : discountCounterCurrent,
        'shopListItem' : shopsList,
        'shop_id' : id_shop,
        'currentShop' : currentShop,
    }
    
    return render(request, template_name='filter_discount_list.html', context=context)


def discountDetail(request, discount_slug):
    context = {
        'discount' : DiscountData.objects.get(slug=discount_slug)
    }
    return render(request, template_name='discount_card.html', context=context)


def deleteDiscount(request, discount_slug):
    try:
        discount = DiscountData.objects.get(slug=discount_slug)
        discount.delete()
        context = {
            'discounts' : DiscountData.objects.filter(startDate__gte=timezone.now()).order_by('startDate')
        }
        return render(request, template_name='discount_list.html', context=context)
    except DiscountData.DoesNotExist:
        return redirect('discountList')
    

def mainPage(request):
    context = {
        
    }
    return render(request, template_name='main_page.html', context=context)


def statistics(request):
    discountCounter = DiscountData.objects.all().count()
    futureDiscount = DiscountData.objects.filter(startDate__gte=timezone.now()).order_by('startDate').count()
    oldDiscount = DiscountData.objects.filter(startDate__lte=timezone.now()).order_by('-startDate').count()
    
    context = {
        "discountCounter" : discountCounter,
        'futureDiscount' : futureDiscount,
        'oldDiscount' : oldDiscount,
    }
    return render(request, 'statistics.html', context=context)