# Generated by Django 4.0.4 on 2022-06-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0023_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='extras',
            field=models.ManyToManyField(blank=True, to='workhours.extra', verbose_name='Extras'),
        ),
    ]