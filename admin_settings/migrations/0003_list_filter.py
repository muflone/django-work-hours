# Generated by Django 4.0.4 on 2022-05-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_settings', '0002_list_display_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('ConfigurationAdmin', 'ConfigurationAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('ListDisplayAdmin', 'ListDisplayAdmin'), ('ListDisplayLinkAdmin', 'ListDisplayLinkAdmin'), ('ShiftAdmin', 'ShiftAdmin'), ('TeamAdmin', 'TeamAdmin'), ('WeekAdmin', 'WeekAdmin')], max_length=255, verbose_name='model')),
                ('field', models.CharField(max_length=255, verbose_name='field')),
                ('order', models.PositiveIntegerField(verbose_name='order')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
            options={
                'verbose_name': 'List Filter',
                'verbose_name_plural': 'List Filters',
                'ordering': ['model', 'order', 'field'],
                'unique_together': {('model', 'order'), ('model', 'field')},
            },
        ),
    ]
