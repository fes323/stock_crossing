# Generated by Django 4.2 on 2023-04-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentdiscountperday',
            name='day',
            field=models.DateField(unique=True, verbose_name='День'),
        ),
    ]
