# Generated by Django 4.2 on 2023-04-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0004_discountdata_shops'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountdata',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
