from django.db import models
from shops.models import ShopManagers, Shop
from datetime import datetime
            
     
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

                   
class DiscountData(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name='Название скидки')
    id_DO = models.IntegerField(blank=True, default=None, verbose_name='ID акции в ДО')
    startDate = models.DateTimeField(blank=True, default=None, verbose_name='Дата начала акции')
    endDate = models.DateTimeField(blank=True, default=None, verbose_name='Дата окончания окончания')
    description = models.TextField(max_length=1500, default='', blank=True, verbose_name='Описание')
    manager = models.ManyToManyField(ShopManagers)
    shops = models.ManyToManyField(Shop, verbose_name='магазины', related_name='shop')
    files = models.FileField(blank=True, verbose_name='Файлы', )
    createDate = models.DateTimeField(null=True, auto_now_add=True, editable=False)
    isDone = models.BooleanField(default=False, verbose_name='Подготовлена')
    idDoneDate = models.DateField(default='2000-01-01')
    slug = models.SlugField(blank=True, db_index=True, verbose_name='slug')
      
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        update_discount_counters()

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

