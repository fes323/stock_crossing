# Generated by Django 4.2 on 2023-04-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0014_bugsindiscount_status_alter_bugsindiscount_isfix'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Тип скидки')),
            ],
        ),
        migrations.CreateModel(
            name='PromocodeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Тип промокода')),
                ('description', models.TextField(blank=True, max_length=1500, verbose_name='Описание')),
            ],
        ),
        migrations.RemoveField(
            model_name='bugsindiscount',
            name='isFix',
        ),
        migrations.AddField(
            model_name='discountdata',
            name='status',
            field=models.CharField(choices=[('N', 'Новая'), ('W', 'В работе'), ('T', 'Тестирование'), ('D', 'Релиз')], default='N', max_length=1),
        ),
        migrations.CreateModel(
            name='Promocode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promocode', models.CharField(max_length=250, verbose_name='Промокод')),
                ('promocodeType', models.ManyToManyField(to='discount.promocodetype')),
            ],
        ),
        migrations.AddField(
            model_name='discountdata',
            name='type',
            field=models.ManyToManyField(to='discount.discounttype'),
        ),
    ]
