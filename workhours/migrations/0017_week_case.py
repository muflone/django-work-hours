# Generated by Django 4.0.2 on 2022-02-19 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0016_team_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='ending_date',
            field=models.DateField(verbose_name='Ending date'),
        ),
        migrations.AlterField(
            model_name='week',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='Is closed'),
        ),
        migrations.AlterField(
            model_name='week',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='week',
            name='starting_date',
            field=models.DateField(verbose_name='Starting date'),
        ),
        migrations.AlterField(
            model_name='week',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workhours.team', verbose_name='Team'),
        ),
    ]
