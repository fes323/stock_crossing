from datetime import *
from django.shortcuts import render
from django.utils import timezone
from .models import DiscountData
# from shops import ShopManagers, Shop


def discountList(request):
    # discounts = DiscountData.objects.all()
    now = timezone.now()
    discounts = DiscountData.objects.filter(startDate__gte=timezone.now()).order_by('startDate')
    context = {
        'discounts' : discounts
    }
    return render(request, template_name='discount_list.html', context=context)

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