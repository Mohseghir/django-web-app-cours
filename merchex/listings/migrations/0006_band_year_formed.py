# Generated by Django 4.2 on 2023-05-05 16:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_remove_band_year_formed'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=1900, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
        ),
    ]
