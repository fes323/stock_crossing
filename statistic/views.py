import json
from os import truncate
import time
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
        today = datetime.now().date()

        # получаем список объектов ActiveDiscount за последние 30 дней
        start_date = today - timedelta(days=15)
        end_date = today + timedelta(days=15)
        discount_dates = ActiveDiscount.objects.filter(date__range=(start_date, end_date)).order_by('date')
        bug_dates = BugsInDiscount.objects.filter(bugDateTime__range=(start_date, end_date)).order_by('bugDateTime')

        # преобразуем даты в миллисекунды и создаем список значений
        discount_data = []
        for discount in discount_dates:
            timestamp = int(time.mktime(discount.date.timetuple())) * 1000
            value = discount.count
            discount_data.append([timestamp, value])
        # преобразуем даты в миллисекунды и создаем список значений
        bug_data = []
        for bug in bug_dates:
            timestamp = int(time.mktime(bug.bugDateTime.timetuple())) * 1000
            value = 1 # Количество багов в день устанавливаем равным 1
            bug_data.append([timestamp, value])
            
        # Блок "последнии акции"
        lastDiscount = self.discountData.order_by('-createDate')[:10]
        
        # Блок "последний баг"
        lastBug = self.bug.latest('createDate')
        
        # Блок "Акции по сетям магазинов"
        shops = Shop.objects.all()
        data = []
        for shop in shops:
            data.append({'name': shop.title, 'y': shop.countCurrentDiscount})
            
        data_json = json.dumps(data)
        print(data)

        context = {
            'allDiscountCounter' : allDiscountCounter,
            'allCurrentDiscountCounter' : allCurrentDiscountCounter,
            'allPastDiscountCounter' : allPastDiscountCounter,
            
            'topByNumberOfDiscount' : topByNumberOfDiscount,
            
            'totalBugCounter' : totalBugCounter,
            'fixBugCounter' : fixBugCounter,
            'todayBugCounter' : todayBugCounter,
            
            'discount_data' : discount_data,
            'bug_data ' : bug_data,
            'data': data_json,
            
            'lastDiscount' : lastDiscount,
            
            'lastBug' : lastBug,
        }
        
        return context
    