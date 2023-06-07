from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime

from shops.models import *
from discount.models import *

class Command(BaseCommand):
    help = 'Recomplice Discount Counters'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        print('Запускаю перерасчет счетчиков')
        
        now = datetime.now()
        for shop in Shop.objects.all():
            future_discounts = DiscountData.objects.filter(shops=shop, startDate__gt=now).count()
            past_discounts = DiscountData.objects.filter(shops=shop, endDate__lt=now).count()
            current_discounts = DiscountData.objects.filter(shops=shop, startDate__lte=now, endDate__gte=now).count()
            shop.countFutureDiscount = future_discounts
            shop.countPastDiscount = past_discounts
            shop.countCurrentDiscount = current_discounts
            shop.save()
        for manager in ShopManagers.objects.all():
            future_discounts = DiscountData.objects.filter(manager=manager, startDate__gt=now).count()
            past_discounts = DiscountData.objects.filter(manager=manager, endDate__lt=now).count()
            current_discounts = DiscountData.objects.filter(manager=manager, startDate__lte=now, endDate__gte=now).count()
            manager.countFutureDiscount = future_discounts
            manager.countPastDiscount = past_discounts
            manager.countCurrentDiscount = current_discounts
            manager.save()
        
        print('Перерасчет окончен!')
        