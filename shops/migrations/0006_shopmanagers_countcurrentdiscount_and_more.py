# Generated by Django 4.2 on 2023-04-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_shop_countcurrentdiscount_shop_countfuturediscount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopmanagers',
            name='CountCurrentDiscount',
            field=models.IntegerField(default=0, verbose_name='Количество текущих акций'),
        ),
        migrations.AddField(
            model_name='shopmanagers',
            name='countFutureDiscount',
            field=models.IntegerField(default=0, verbose_name='Количество будущих акций'),
        ),
        migrations.AddField(
            model_name='shopmanagers',
            name='countPastDiscount',
            field=models.IntegerField(default=0, verbose_name='Количество прошедших акций'),
        ),
    ]