# Generated by Django 4.2 on 2023-05-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0007_alter_discountdata_discountthreshold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugsindiscount',
            name='discount',
            field=models.ManyToManyField(blank=True, null=True, to='discount.discountdata'),
        ),
    ]
