from django.db import migrations

from utility.constants import DATE_FORMAT_FULL, DATE_FORMAT_SHORT


def add_configuration_values(apps, schema_editor) -> None:
    """
    Insert some default settings
    """
    Configuration = apps.get_model('utility', 'Configuration')
    Configuration.objects.get_or_create(
        name=DATE_FORMAT_SHORT,
        defaults={'group': 'Dates',
                  'value': 'Y/m/d',
                  'description': 'Short format for dates'}
    )
    Configuration.objects.get_or_create(
        name=DATE_FORMAT_FULL,
        defaults={'group': 'Dates',
                  'value': 'l Y/m/d',
                  'description': 'Full format for dates'}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0003_alter_configuration_table'),
    ]

    operations = [
        migrations.RunPython(code=add_configuration_values,
                             reverse_code=migrations.RunPython.noop),
    ]
