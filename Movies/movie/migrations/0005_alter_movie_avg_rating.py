# Generated by Django 3.2.6 on 2021-08-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_artist_award'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='avg_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
