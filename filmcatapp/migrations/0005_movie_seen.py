# Generated by Django 3.1.5 on 2021-01-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmcatapp', '0004_auto_20210124_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='seen',
            field=models.CharField(choices=[('BT', 'obydwojgoro'), ('NB', 'nikt'), ('JK', 'Julka'), ('PK', 'Piotrek')], default='NB', max_length=2),
        ),
    ]
