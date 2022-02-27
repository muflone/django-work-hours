from django.db import migrations

from workhours.constants import DELAY_BEFORE_SAVE_DAY


def add_configuration_values(apps, schema_editor) -> None:
    """
    Insert some default settings
    """
    Configuration = apps.get_model('utility', 'Configuration')
    Configuration.objects.get_or_create(
        name=DELAY_BEFORE_SAVE_DAY,
        defaults={'group': 'Week',
                  'value': '0',
                  'description': 'Delay in ms before saving the daily data'}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0019_alter_week_options'),
    ]

    operations = [
        migrations.RunPython(code=add_configuration_values,
                             reverse_code=migrations.RunPython.noop),
    ]
