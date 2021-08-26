# Generated by Django 3.2.6 on 2021-08-25 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_award'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='award',
            field=models.ManyToManyField(to='movie.Award'),
        ),
    ]