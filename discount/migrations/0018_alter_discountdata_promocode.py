# Generated by Django 4.2 on 2023-04-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0017_alter_discountdata_promocode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountdata',
            name='promocode',
            field=models.ManyToManyField(blank=True, null=True, to='discount.promocode'),
        ),
    ]