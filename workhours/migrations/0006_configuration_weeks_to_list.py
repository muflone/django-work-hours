from django.db import migrations

from workhours.constants import WEEKS_TO_LIST


def add_configuration_values(apps, schema_editor) -> None:
    """
    Insert some default settings
    """
    Configuration = apps.get_model('utility', 'Configuration')
    Configuration.objects.get_or_create(
        name=WEEKS_TO_LIST,
        defaults={'group': 'Teams',
                  'value': '5',
                  'description': 'Weeks to list in the team page'}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0005_shift_holiday'),
    ]

    operations = [
        migrations.RunPython(code=add_configuration_values,
                             reverse_code=migrations.RunPython.noop),
    ]
