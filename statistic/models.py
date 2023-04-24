from django.db import models


class ActiveDiscount(models.Model):
    date = models.DateField(unique=True)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.date}: {self.count} акций"
    class Meta:
        verbose_name = 'Действующая акция'
        verbose_name_plural = 'Действующие акции'