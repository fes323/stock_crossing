# Generated by Django 4.2 on 2023-04-24 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0006_shopmanagers_countcurrentdiscount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='CountCurrentDiscount',
            new_name='countCurrentDiscount',
        ),
        migrations.RenameField(
            model_name='shopmanagers',
            old_name='CountCurrentDiscount',
            new_name='countCurrentDiscount',
        ),
    ]
