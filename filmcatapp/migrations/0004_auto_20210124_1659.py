# Generated by Django 3.1.5 on 2021-01-24 15:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmcatapp', '0003_auto_20210124_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_seen',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)]),
        ),
    ]
