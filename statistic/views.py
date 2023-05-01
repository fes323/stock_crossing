import json
from os import truncate
from django.shortcuts import render
from datetime import datetime, timedelta
from django.views.generic import TemplateView, DetailView, ListView
from discount.models import BugsInDiscount, DiscountData, ActiveDiscount
from shops.models import Shop
from django.db.models import Count, F, Q, Sum
from django.db.models.functions import TruncDay
from django.utils.timezone import now, timedelta


class Statistic(TemplateView):
    template_name = 'statistics.html'
    
    now = datetime.now()

    discountData = DiscountData.objects.all()
    allShops = Shop.objects.all()
    bug = BugsInDiscount.objects.all()
    activeDiscount = ActiveDiscount.objects.all()
    
    def get_context_data(self, **kwargs):
        
        # Блок "Общая статистика"
        allDiscountCounter = self.discountData.count()
        allCurrentDiscountCounter = self.discountData.filter(startDate__lte=self.now).filter(endDate__gte=self.now).count()
        allPastDiscountCounter = self.discountData.filter(startDate__lte=self.now).filter(endDate__lte=self.now).count()
        
        # Блок "Топ по количеству действующих акций"
        topByNumberOfDiscount = self.allShops.annotate(num_discount=Count('shop')).order_by('-countCurrentDiscount')
        
        # Блоки счетчиков багов
        totalBugCounter = self.bug.count()
        fixBugCounter = self.bug.filter(status='D').count()
        todayBugCounter = self.bug.filter(createDate=self.now).count()
        
        # Блок графика
        # Получаем список всех магазинов
        shops = Shop.objects.all()

        # Формируем список с данными для каждого магазина
        data = []
        for shop in shops:
            # Получаем список акций для текущего магазина на последние 30 дней
            discounts = ActiveDiscount.objects.filter(
                shop=shop, date__gte=now().date() - timedelta(days=30)
            )

            # Группируем акции по дате и считаем их количество
            counts = discounts.annotate(
                date_trunc_day=TruncDay("date")
            ).values("date_trunc_day").annotate(
                total=Sum("count")
            ).values_list("date_trunc_day", "total")

            # Добавляем данные магазина в общий список данных
            data.append(
                {
                    "name": shop.title,
                    "data": counts,
                }
            )
        
        # Блок "последнии акции"
        lastDiscount = self.discountData.order_by('-createDate')[:10]
        
        # Блок "последний баг"
        lastBug = self.bug.latest('createDate')

        context = {
            'allDiscountCounter' : allDiscountCounter,
            'allCurrentDiscountCounter' : allCurrentDiscountCounter,
            'allPastDiscountCounter' : allPastDiscountCounter,
            
            'topByNumberOfDiscount' : topByNumberOfDiscount,
            
            'totalBugCounter' : totalBugCounter,
            'fixBugCounter' : fixBugCounter,
            'todayBugCounter' : todayBugCounter,
            
            'data': data,
            
            'lastDiscount' : lastDiscount,
            
            'lastBug' : lastBug,
        }
        
        return context
    