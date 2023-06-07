from django.db import models, IntegrityError, transaction
from datetime import datetime, timedelta
from django.db.models.functions import Coalesce
from django.db.models import Count, F, Q, Max

from shops.models import *


def update_bug_counters():
    discounts = DiscountData.objects.annotate(
        bug_counter=Count('bugsindiscount')
    )
    
    # Извлекаем только записи, в которых количество багов изменилось
    updated_discounts = []
    for discount in discounts:
        if discount.bugCounter != discount.bug_counter:
            discount.bugCounter = F('bugCounter')
            updated_discounts.append(discount)
            
    DiscountData.objects.bulk_update(updated_discounts, ['bugCounter'])
    
            
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
                
class DiscountData(models.Model):
    
    STATUS = [
        ('N', 'Новая'),
        ('W', 'В работе'),  
        ('T', 'Тестирование'),
        ('D', 'Релиз'),
    ]
    
    SUMMATION = [
        ('N', 'Не суммируется с ПЛ'),
        ('S', 'Суммируется с ПЛ на строку'),
        ('P', 'Суммируется с ПЛ на документ'),
        ('B', 'Суммируется с ДК, но не суммируется с ДР'),
    ]
    
    THRESHOLDTYPE = [
        ('P', 'Порог с учетом ПЛ'),
        ('F', 'Порог без учета ПЛ'),
        ('N', 'Без порога'),
    ]
    
    DISCOUNT_TUPE = [
        ('P', 'Скидка процентом'),
        ('S', 'Скидка суммой'),
        ('B', 'Бонусные баллы'),
        ('L', 'Потеряшки'),
        ('C', 'Кэшбек'),
        ('G', 'Подарок'),
        ('W', 'Лотерея'),
        ('v', 'Установка цены'),
    ]
    
    #Основные поля
    title = models.CharField(max_length=250, null=True, db_index=True, verbose_name='Название скидки')
    id_DO = models.IntegerField(db_index=True, verbose_name='ID акции в ДО')
    startDate = models.DateTimeField(verbose_name='Дата начала акции')
    endDate = models.DateTimeField(verbose_name='Дата окончания окончания')
    description = models.TextField(max_length=1500, blank=True, null=True, verbose_name='Описание')
    discountSum = models.CharField(max_length=250, blank=True, null=True, verbose_name='Значение скидки (процент/сумма/баллы)')
    summation = models.CharField(max_length=1, choices=SUMMATION, default='N')
    discountThreshold = models.PositiveIntegerField(null=True, blank=True, verbose_name='Порог скидки')
    discountThresholdType = models.CharField(max_length=1, choices=THRESHOLDTYPE, default='N')
    type = models.CharField(max_length=1, choices=DISCOUNT_TUPE, default='P', verbose_name='Тип акции')
    promocode = models.ManyToManyField(Promocode, blank=True, null=True, )
    manager = models.ManyToManyField(ShopManagers, verbose_name='менеджер', related_name='manager')
    shops = models.ManyToManyField(Shop, verbose_name='магазины', related_name='shop')
    segment = models.BooleanField(default=False, verbose_name='Формирование сегмента')
    
    #Служебные поля
    status = models.CharField(max_length=1, choices=STATUS, default='N')
    createDate = models.DateTimeField(auto_now_add=True)     
    isDoneDate = models.DateField(blank=True, null=True)
    slug = models.SlugField(db_index=True, verbose_name='slug')
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
        
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
           
        
class DiscountFiles(models.Model):
    file = models.FileField(verbose_name='Файлы')
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
    discount = models.ManyToManyField(DiscountData, blank=True, null=True)
    description = models.TextField(max_length=1500, verbose_name='Описание')
    bugDateTime = models.DateTimeField(default=None, verbose_name='Дата и время инцидента')
    createDate = models.DateTimeField(auto_now_add=True, editable=False)
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
    file = models.FileField(verbose_name='Файлы')
    bug = models.ForeignKey(BugsInDiscount, on_delete=models.CASCADE, verbose_name='баг')


class ActiveDiscount(models.Model):
    date = models.DateField(unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date}: {self.count} акций"

    class Meta:
        verbose_name = 'Действующая акция'
        verbose_name_plural = 'Действующие акции'
