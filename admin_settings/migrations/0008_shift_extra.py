# Generated by Django 4.0.4 on 2022-06-05 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_settings', '0007_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listdisplay',
            name='model',
            field=models.CharField(choices=[('ConfigurationAdmin', 'ConfigurationAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('ExtraAdmin', 'ExtraAdmin'), ('ListDisplayAdmin', 'ListDisplayAdmin'), ('ListDisplayLinkAdmin', 'ListDisplayLinkAdmin'), ('ListFilterAdmin', 'ListFilterAdmin'), ('ShiftAdmin', 'ShiftAdmin'), ('ShiftExtraAdmin', 'ShiftExtraAdmin'), ('TeamAdmin', 'TeamAdmin'), ('WeekAdmin', 'WeekAdmin')], max_length=255, verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='listdisplaylink',
            name='model',
            field=models.CharField(choices=[('ConfigurationAdmin', 'ConfigurationAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('ExtraAdmin', 'ExtraAdmin'), ('ListDisplayAdmin', 'ListDisplayAdmin'), ('ListDisplayLinkAdmin', 'ListDisplayLinkAdmin'), ('ListFilterAdmin', 'ListFilterAdmin'), ('ShiftAdmin', 'ShiftAdmin'), ('ShiftExtraAdmin', 'ShiftExtraAdmin'), ('TeamAdmin', 'TeamAdmin'), ('WeekAdmin', 'WeekAdmin')], max_length=255, verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='listfilter',
            name='model',
            field=models.CharField(choices=[('ConfigurationAdmin', 'ConfigurationAdmin'), ('EmployeeAdmin', 'EmployeeAdmin'), ('ExtraAdmin', 'ExtraAdmin'), ('ListDisplayAdmin', 'ListDisplayAdmin'), ('ListDisplayLinkAdmin', 'ListDisplayLinkAdmin'), ('ListFilterAdmin', 'ListFilterAdmin'), ('ShiftAdmin', 'ShiftAdmin'), ('ShiftExtraAdmin', 'ShiftExtraAdmin'), ('TeamAdmin', 'TeamAdmin'), ('WeekAdmin', 'WeekAdmin')], max_length=255, verbose_name='model'),
        ),
    ]
