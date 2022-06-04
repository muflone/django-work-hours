# Generated by Django 4.0.4 on 2022-05-29 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0011_user_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_last',
            field=models.BooleanField(choices=[(True, 'Show first name + last name'), (False, 'Show last name + first name')], default=True, verbose_name='First and last name order'),
        ),
    ]