from django.db import models
from datetime import datetime, timedelta
from django.db.models import Count, F, Q

from shops.models import *


def update_active_discounts():
    start_date = DiscountData.objects.earliest('startDate').startDate.date()
    end_date = DiscountData.objects.latest('endDate').endDate.date()
    
    date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    
    for date in date_list:
        active_discounts = DiscountData.objects.filter(startDate__lte=date, endDate__gte=date)
        count = active_discounts.count()

        active_discount, created = ActiveDiscount.objects.get_or_create(date=date)
        active_discount.count = count
        active_discount.save()

def update_discount_counters():
        now = datetime.now()
        for shop in Shop.objects.all():
            future_discounts = DiscountData.objects.filter(shops=shop, startDate__gt=now).count()
            past_discounts = DiscountData.objects.filter(shops=shop, endDate__lt=now).count()
            current_discounts = DiscountData.objects.filter(shops=shop, startDate__lte=now, endDate__gte=now).count()
            shop.countFutureDiscount = future_discounts
            shop.countPastDiscount = past_discounts
            shop.CountCurrentDiscount = current_discounts
            shop.save()
        for manager in ShopManagers.objects.all():
            future_discounts = DiscountData.objects.filter(manager=manager, startDate__gt=now).count()
            past_discounts = DiscountData.objects.filter(manager=manager, endDate__lt=now).count()
            current_discounts = DiscountData.objects.filter(manager=manager, startDate__lte=now, endDate__gte=now).count()
            manager.countFutureDiscount = future_discounts
            manager.countPastDiscount = past_discounts
            manager.CountCurrentDiscount = current_discounts
            manager.save()

def update_bug_counters():
    for discount in DiscountData.objects.filter(discount=discount):
            counter = BugsInDiscount.objects.filter(discount=discount).count()
            discount.bugCounter = counter
            discount.save()
    
            
class PromocodeType(models.Model):
    
    title = models.CharField(max_length=250, verbose_name='Тип промокода')
    description = models.TextField(max_length=1500, blank=True, verbose_name='Описание')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип промокода'
        verbose_name_plural = 'Тип промокодов'


class Promocode(models.Model):
    
    promocode = models.CharField(max_length=250, verbose_name='Промокод')
    promocodeType = models.ManyToManyField(PromocodeType)
    
    def __str__(self):
        return self.promocode

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'


class DiscountType(models.Model):
    
    title = models.CharField(max_length=250, verbose_name='Тип скидки')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип акции'
        verbose_name_plural = 'Тип акций'
    
                
class DiscountData(models.Model):
    
    STATUS = [
        ('N', 'Новая'),
        ('W', 'В работе'),  
        ('T', 'Тестирование'),
        ('D', 'Релиз'),
    ]
    
    #Основные поля
    title = models.CharField(max_length=250, null=True, db_index=True, verbose_name='Название скидки')
    id_DO = models.IntegerField(blank=True, default=None, db_index=True, verbose_name='ID акции в ДО')
    startDate = models.DateTimeField(blank=True, default=None, verbose_name='Дата начала акции')
    endDate = models.DateTimeField(blank=True, default=None, verbose_name='Дата окончания окончания')
    description = models.TextField(max_length=1500, default='', blank=True, verbose_name='Описание')
    type = models.ManyToManyField(DiscountType)
    promocode = models.ManyToManyField(Promocode)
    manager = models.ManyToManyField(ShopManagers)
    shops = models.ManyToManyField(Shop, verbose_name='магазины', related_name='shop')
    
    #Служебные поля
    status = models.CharField(max_length=1, choices=STATUS, default='N')
    createDate = models.DateTimeField(null=True, auto_now_add=True)     
    isDoneDate = models.DateField(default='2000-01-01')
    slug = models.SlugField(blank=True, db_index=True, verbose_name='slug')
    bugCounter = models.IntegerField(default=0, verbose_name='Количество текущих акций')
    isDone = models.BooleanField(default=False, verbose_name='Подготовлена')
    
    #Поля для проверки запуска счетчиков (обновление)
    addDiscountCounters = models.BooleanField(default=False)
    addActiveDiscountCounter = models.BooleanField(default=False)
      
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        
        if self.status == 'D':
            self.isDone = True
            self.isDoneDate = datetime.now()
        else:
            print('Поле "isDoneDate" равно значению по умолчанию')
            
        super().save(*args, **kwargs)
        
        if self.addDiscountCounters == False:
            update_discount_counters()
            self.addDiscountCounters = True
        if self.addActiveDiscountCounter == False:
            update_active_discounts()
            self.addActiveDiscountCounter = True
        else:
            update_active_discounts()
            update_discount_counters()
        

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
           
        
class DiscountFiles(models.Model):
    file = models.FileField(blank=True, verbose_name='Файлы', )
    discount = models.ForeignKey(DiscountData, on_delete=models.CASCADE)
        
        
class BugsInDiscount(models.Model):
    
    STATUS = [
        ('N', 'Новый'),
        ('O', 'Ознакомлен'),
        ('W', 'В работе'),
        ('U', 'Требуется разработка'),
        ('I', 'Нужна информация'),
        ('D', 'Исправлено'),
    ]
    
    title = models.CharField(max_length=250, null=True, verbose_name='Название бага')
    discount = models.ManyToManyField(DiscountData)
    description = models.TextField(max_length=1500, default='', blank=True, verbose_name='Описание')
    bugDateTime = models.DateTimeField(blank=True, default=None, verbose_name='Дата и время инцидента')
    createDate = models.DateTimeField(null=True, auto_now_add=True, editable=False)
    status = models.CharField(max_length=1, choices=STATUS, default='N')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        update_bug_counters()

    class Meta:
        verbose_name = 'Баг'
        verbose_name_plural = 'Баги'


class GalleryFilesWhithErrors(models.Model):
    file = models.FileField(blank=True, verbose_name='Файлы', )
    bug = models.ForeignKey(BugsInDiscount, on_delete=models.CASCADE, verbose_name='баг')


class ActiveDiscount(models.Model):
    
    date = models.DateField(unique=True)
    count = models.IntegerField(default=0)
    discount = models.ManyToManyField(DiscountData)
    
    def __str__(self):
        return f"{self.date}: {self.count} акций"
    
    class Meta:
        verbose_name = 'Действующая акция'
        verbose_name_plural = 'Действующие акции'