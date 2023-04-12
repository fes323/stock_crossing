from django.db import models
from shops.models import ShopManagers, Shop

                
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

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
