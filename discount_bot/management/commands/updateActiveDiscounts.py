from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime

from shops.models import *
from discount.models import *

class Command(BaseCommand):
    help = 'Recomplice Active Discount Counters'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        print('Запускаю перерасчет счетчиков')
        
        start_date = DiscountData.objects.earliest('startDate').startDate.date()
        end_date = DiscountData.objects.latest('endDate').endDate.date()

        date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

        for date in date_list:
            active_discounts = DiscountData.objects.filter(startDate__lte=date, endDate__gte=date)
            count = active_discounts.count()

            active_discount, created = ActiveDiscount.objects.get_or_create(date=date)
            active_discount.count = count
            active_discount.save()
        
        print('Перерасчет окончен!')
    