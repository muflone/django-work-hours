# Generated by Django 4.0.2 on 2022-02-06 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0004_shift'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shift',
            old_name='is_holyday',
            new_name='is_holiday',
        ),
    ]