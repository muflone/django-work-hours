from django.db import migrations

from workhours.constants import DELAY_AFTER_SAVE_DAY


def add_configuration_values(apps, schema_editor) -> None:
    """
    Insert some default settings
    """
    Configuration = apps.get_model('utility', 'Configuration')
    Configuration.objects.get_or_create(
        name=DELAY_AFTER_SAVE_DAY,
        defaults={'group': 'Week',
                  'value': '500',
                  'description': 'Delay in ms after saving the daily data'}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0007_configuration_delay_after_save_shift'),
    ]

    operations = [
        migrations.RunPython(code=add_configuration_values,
                             reverse_code=migrations.RunPython.noop),
    ]
