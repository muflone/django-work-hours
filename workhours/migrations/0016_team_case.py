# Generated by Django 4.0.2 on 2022-02-19 19:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workhours', '0015_shift_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='team',
            name='employees',
            field=models.ManyToManyField(to='workhours.Employee', verbose_name='Employees'),
        ),
        migrations.AlterField(
            model_name='team',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
        ),
        migrations.AlterField(
            model_name='team',
            name='managers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Managers'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]
