from django.db import migrations

from project import PRODUCT_NAME

from utility.constants import SITE_TITLE


def add_configuration_values(apps, schema_editor) -> None:
    """
    Insert some default settings
    """
    Configuration = apps.get_model('utility', 'Configuration')
    Configuration.objects.get_or_create(
        name=SITE_TITLE,
        defaults={'group': 'Site',
                  'value': PRODUCT_NAME,
                  'description': 'Site pages title'}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0005_configuration_admin'),
    ]

    operations = [
        migrations.RunPython(code=add_configuration_values,
                             reverse_code=migrations.RunPython.noop),
    ]
