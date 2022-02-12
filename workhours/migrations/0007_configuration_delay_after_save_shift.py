from django.db import migrations

from workhours.constants import DELAY_AFTER_SAVE_SHIFT


def add_configuration_values(apps, schema_editor) -> None:
    """
    Insert some default settings
    """
    Configuration = apps.get_model('utility', 'Configuration')
    Configuration.objects.get_or_create(
        name=DELAY_AFTER_SAVE_SHIFT,
        defaults={'group': 'Week',
                  'value': '0',
                  'description': 'Delay in ms after saving a shift'}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0006_configuration_weeks_to_list'),
    ]

    operations = [
        migrations.RunPython(code=add_configuration_values,
                             reverse_code=migrations.RunPython.noop),
    ]
