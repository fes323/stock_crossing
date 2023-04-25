from django.shortcuts import render
from datetime import datetime, timedelta
from django.views.generic import TemplateView, DetailView, ListView
from discount.models import BugsInDiscount, DiscountData
from shops.models import Shop
from django.db.models import Count, F, Q


class Statistic(TemplateView):
    template_name = 'statistics.html'
    
    now = datetime.now()

    discountData = DiscountData.objects.all()
    allShops = Shop.objects.all()
    bug = BugsInDiscount.objects.all()
    
    def get_context_data(self, **kwargs):
        
        # Блок "Общая статистика"
        allDiscountCounter = self.discountData.count()
        allCurrentDiscountCounter = self.discountData.filter(startDate__lte=self.now).filter(endDate__gte=self.now).count()
        allPastDiscountCounter = self.discountData.filter(startDate__lte=self.now).filter(endDate__lte=self.now).count()
        
        # Блок "Топ по количеству действующих акций"
        topByNumberOfDiscount = self.allShops.annotate(num_discount=Count('shop')).order_by('-countCurrentDiscount')[:3]
        
        # Блоки счетчиков багов
        totalBugCounter = self.bug.count()
        fixBugCounter = self.bug.filter(status='D').count()
        todayBugCounter = self.bug.filter(createDate=self.now).count()
        
        # Блок "последнии акции"
        lastDiscount = self.discountData.order_by('-isDoneDate')[:6]
        
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
            
            'lastDiscount' : lastDiscount,
            
            'lastBug' : lastBug,
        }
        
        return context
    