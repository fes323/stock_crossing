from django.shortcuts import redirect, render
from django.utils import timezone
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import DiscountData
from shops.models import Shop, ShopManagers
from datetime import datetime, timedelta


def startTomorrow(request):
    now = datetime.now().date()
    end_date = now + timedelta(days=1)
    
    discounts = DiscountData.objects.filter(startDate__range=[now, end_date])
    
    page_obj = discounts
    
    context = {
        'discounts' : discounts,
        'page_obj' : page_obj,
    }
    return render(request, template_name='discount_list.html', context=context)

def startWithinAWeek(request):
    now = datetime.now().date() + timedelta(days=1)
    end_date = now + timedelta(days=7)

    discounts = DiscountData.objects.filter(startDate__range=[now, end_date]).order_by('startDate')
    
    page_obj = discounts
    
    context = {
        'discounts' : discounts,
        'page_obj' : page_obj,
    }
    return render(request, template_name='discount_list.html', context=context)

def searchDiscount(request):
    query = request.GET.get('q')
    discounts = DiscountData.objects.filter(
        Q(title__icontains=query) | Q(id_DO__icontains=query)
    )
    print(discounts)
    page_obj = discounts
    
    context = {
        'discounts' : discounts,
        'page_obj' : page_obj,
    }
    return render(request, template_name='discount_list.html', context=context)

def discountList(request, shop_id=None):
    now = datetime.now()
    shopsList = Shop.objects.all().order_by('title')
    managers = ShopManagers.objects.all().order_by('name')
    
    discountCurrent = DiscountData.objects.filter(startDate__lte=now).filter(endDate__gte=now).order_by('-startDate')
    discountsOld = DiscountData.objects.filter(startDate__lte=now).filter(endDate__lte=now).order_by('-startDate')
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
    
    paginator = Paginator(discounts, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'discounts' : discounts,
        'counter' : discountCounter,
        'counterOLd' : discountCounterOld,
        'counterCurrent' : discountCounterCurrent,
        'shopListItem' : shopsList,
        'page_obj' : page_obj,
        'managers' : managers,
    }
    
    return render(request, template_name='discount_list.html', context=context)

def discountListFilterByManager(request, manager_id):
    now = datetime.now()
    shopsList = Shop.objects.all().order_by('title')
    managers = ShopManagers.objects.all().order_by('name')
    
    currentManager = ShopManagers.objects.get(id=manager_id)

    discountCurrent = DiscountData.objects.filter(startDate__lte=now).filter(manager__exact=manager_id).filter(endDate__gte=now).order_by('-startDate')
    discountsOld = DiscountData.objects.filter(startDate__lte=now).filter(manager__exact=manager_id).filter(endDate__lte=now).order_by('-startDate')
    discountsFuture = DiscountData.objects.filter(startDate__gte=now).filter(manager__exact=manager_id).order_by('startDate')
    
    discountCounter = discountsFuture.count()
    discountCounterOld = discountsOld.count()
    discountCounterCurrent = discountCurrent.count()
    
    if '/discountList' in request.path:
        discounts = discountsFuture
    elif '/OldDiscountList' in request.path:
        discounts = discountsOld
    elif '/CurrentDiscountList' in request.path:
        discounts = discountCurrent
    
    id_manager = manager_id
    
    paginator = Paginator(discounts, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'discounts' : discounts,
        'counter' : discountCounter,
        'counterOLd' : discountCounterOld,
        'counterCurrent' : discountCounterCurrent,
        'shopListItem' : shopsList,
        'id_manager' : id_manager,
        'currentManager' : currentManager,
        'page_obj' : page_obj,
        'managers' : managers,
    }
    
    return render(request, template_name='filter_discount_list.html', context=context)



def discountListFilterByShop(request, shop_id):
    now = datetime.now()
    shopsList = Shop.objects.all().order_by('title')
    managers = ShopManagers.objects.all().order_by('name')
    
    currentShop = Shop.objects.get(id=shop_id)

    discountCurrent = DiscountData.objects.filter(startDate__lte=now).filter(shops__exact=shop_id).filter(endDate__gte=now).order_by('-startDate')
    discountsOld = DiscountData.objects.filter(startDate__lte=now).filter(shops__exact=shop_id).filter(endDate__lte=now).order_by('-startDate')
    discountsFuture = DiscountData.objects.filter(startDate__gte=now).filter(shops__exact=shop_id).order_by('startDate')
    
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
    
    paginator = Paginator(discounts, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'discounts' : discounts,
        'counter' : discountCounter,
        'counterOLd' : discountCounterOld,
        'counterCurrent' : discountCounterCurrent,
        'shopListItem' : shopsList,
        'shop_id' : id_shop,
        'currentShop' : currentShop,
        'page_obj' : page_obj,
        'managers' : managers,
    }
    
    return render(request, template_name='filter_discount_list.html', context=context)


def discountDetail(request, discount_slug):
    managers = ShopManagers.objects.all()
    shops = Shop.objects.all()
    context = {
        'discount' : DiscountData.objects.get(slug=discount_slug),
        'managers' : managers,
        'shops' : shops,
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