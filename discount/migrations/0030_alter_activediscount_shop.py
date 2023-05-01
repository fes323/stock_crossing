# Generated by Django 4.2 on 2023-05-01 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0007_rename_countcurrentdiscount_shop_countcurrentdiscount_and_more'),
        ('discount', '0029_alter_activediscount_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activediscount',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop'),
        ),
    ]
