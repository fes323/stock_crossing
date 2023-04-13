from django.db import models


class ShopManagers(models.Model):
    name = models.CharField(max_length=250, null=True, verbose_name='Руководить сети (акции)')
    phone = models.CharField(max_length=25, blank=True, default='+7', verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class Shop(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name='Наименование магазина')
    manager = models.ManyToManyField(ShopManagers)
    countFutureDiscount = models.IntegerField(default=0, verbose_name='Количество будущих акций')
    countPastDiscount = models.IntegerField(default=0, verbose_name='Количество прошедших акций')
    CountCurrentDiscount = models.IntegerField(default=0, verbose_name='Количество текущих акций')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Notes(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name='Название')
    manager = models.ForeignKey(ShopManagers, on_delete=models.CASCADE)
    date = models.DateField(default=None, verbose_name='Дата создания')
    desc = models.TextField(max_length=2000, blank=True, verbose_name='Текст')
    files = models.FileField(blank=True, verbose_name='Файлы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'