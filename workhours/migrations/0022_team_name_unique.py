# Generated by Django 4.0.4 on 2022-06-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0021_configuration_delay_before_save_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
    ]
