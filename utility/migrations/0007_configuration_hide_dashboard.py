from django.db import migrations

from utility.constants import SITE_HIDE_DASHBOARD


def add_configuration_values(apps, schema_editor) -> None:
    """
    Insert some default settings
    """
    Configuration = apps.get_model('utility', 'Configuration')
    Configuration.objects.get_or_create(
        name=SITE_HIDE_DASHBOARD,
        defaults={'group': 'Site',
                  'value': '0',
                  'description': 'Hide Dashboard page'}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0006_configuration_site'),
    ]

    operations = [
        migrations.RunPython(code=add_configuration_values,
                             reverse_code=migrations.RunPython.noop),
    ]
