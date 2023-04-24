from django.db import models


class CurrentDiscountPerDay(models.Model):
    discountCounter = models.IntegerField(default=0, verbose_name='Количество акций')
    day = models.DateField(unique=True, verbose_name='День')