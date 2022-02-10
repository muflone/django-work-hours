from django.db import migrations

from project import PRODUCT_NAME

from utility.constants import (ADMIN_INDEX_TITLE,
                               ADMIN_SITE_HEADER,
                               ADMIN_SITE_TITLE)


def add_configuration_values(apps, schema_editor) -> None:
    """
    Insert some default settings
    """
    Configuration = apps.get_model('utility', 'Configuration')
    Configuration.objects.get_or_create(
        name=ADMIN_INDEX_TITLE,
        defaults={'group': 'Admin',
                  'value': '',
                  'description': 'Administration title prefix'}
    )
    Configuration.objects.get_or_create(
        name=ADMIN_SITE_HEADER,
        defaults={'group': 'Admin',
                  'value': PRODUCT_NAME,
                  'description': 'Administration title suffix'}
    )
    Configuration.objects.get_or_create(
        name=ADMIN_SITE_TITLE,
        defaults={'group': 'Admin',
                  'value': PRODUCT_NAME,
                  'description': 'Administration title'}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0004_configuration_date_format'),
    ]

    operations = [
        migrations.RunPython(code=add_configuration_values,
                             reverse_code=migrations.RunPython.noop),
    ]
