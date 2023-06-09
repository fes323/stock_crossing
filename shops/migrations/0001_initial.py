# Generated by Django 4.2 on 2023-05-02 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopManagers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Руководить сети (акции)')),
                ('phone', models.CharField(blank=True, default='+7', max_length=25, verbose_name='Телефон')),
                ('countFutureDiscount', models.IntegerField(default=0, verbose_name='Количество будущих акций')),
                ('countPastDiscount', models.IntegerField(default=0, verbose_name='Количество прошедших акций')),
                ('countCurrentDiscount', models.IntegerField(default=0, verbose_name='Количество текущих акций')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Наименование магазина')),
                ('countFutureDiscount', models.IntegerField(default=0, verbose_name='Количество будущих акций')),
                ('countPastDiscount', models.IntegerField(default=0, verbose_name='Количество прошедших акций')),
                ('countCurrentDiscount', models.IntegerField(default=0, verbose_name='Количество текущих акций')),
                ('manager', models.ManyToManyField(to='shops.shopmanagers')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('date', models.DateField(default=None, verbose_name='Дата создания')),
                ('desc', models.TextField(blank=True, max_length=2000, verbose_name='Текст')),
                ('files', models.FileField(blank=True, upload_to='', verbose_name='Файлы')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shopmanagers')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
            },
        ),
    ]
