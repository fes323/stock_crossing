# Generated by Django 4.2 on 2023-05-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0004_discountdata_discountsum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountdata',
            name='discountThresholdType',
            field=models.CharField(choices=[('P', 'Порог с учетом ПЛ'), ('F', 'Порог без учета ПЛ'), ('N', 'Без порога')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='discountdata',
            name='summation',
            field=models.CharField(choices=[('N', 'Не суммируется с ПЛ'), ('S', 'Суммируется с ПЛ на строку'), ('P', 'Суммируется с ПЛ на документ'), ('B', 'Суммируется с ДК, но не суммируется с ДР')], default='N', max_length=1),
        ),
        migrations.RemoveField(
            model_name='discountdata',
            name='type',
        ),
        migrations.DeleteModel(
            name='DiscountType',
        ),
        migrations.AddField(
            model_name='discountdata',
            name='type',
            field=models.CharField(choices=[('P', 'Скидка процентом'), ('S', 'Скидка суммой'), ('B', 'Бонусные баллы'), ('L', 'Потеряшки'), ('C', 'Кэшбек')], default='P', max_length=1, verbose_name='Тип акции'),
        ),
    ]