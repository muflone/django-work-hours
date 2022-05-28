##
#     Project: Django Work Hours
# Description: A Django application to manage the employees work hours
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2022 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

from django.contrib import admin
from django.db.utils import OperationalError

from admin_settings.extras import get_admin_models, get_class_from_module
from utility.constants import (ADMIN_INDEX_TITLE,
                               ADMIN_SITE_HEADER,
                               ADMIN_SITE_TITLE)
from utility.extras import get_configuration_value
from .models import (ListDisplay, ListDisplayAdmin,
                     ListDisplayLink, ListDisplayLinkAdmin,
                     ListFilter, ListFilterAdmin)


# Models registration
admin.site.register(ListDisplay, ListDisplayAdmin)
admin.site.register(ListDisplayLink, ListDisplayLinkAdmin)
admin.site.register(ListFilter, ListFilterAdmin)

# Admin customization
if setting := get_configuration_value(ADMIN_SITE_HEADER):
    admin.site.site_header = setting
if setting := get_configuration_value(ADMIN_SITE_TITLE):
    admin.site.site_title = setting
if setting := get_configuration_value(ADMIN_INDEX_TITLE):
    admin.site.index_title = setting

# Customize Admin models
admin_models = get_admin_models()
for model_name, model in admin_models.items():
    # Customize list_display
    try:
        if records := ListDisplay.objects.filter(
                model=model_name).order_by('order'):
            # Add the fields to model list_display
            model.list_display = []
            for item in records:
                if item.is_active:
                    model.list_display.append(item.field)
    except OperationalError:
        # If the model doesn't yet exist skip the customization
        pass
    # Customize list_display_links
    try:
        if records := ListDisplayLink.objects.filter(
                model=model_name).order_by('order'):
            # Add the fields to model list_display
            model.list_display_links = []
            for item in records:
                if item.is_active:
                    model.list_display_links.append(item.field)
    except OperationalError:
        # If the model doesn't yet exist skip the customization
        pass
    # Customize list_filter
    try:
        if records := ListFilter.objects.filter(
                model=model_name).order_by('order'):
            # Add the fields to model list_display
            model.list_filter = []
            for item in records:
                if item.is_active:
                    if '|' in item.field:
                        # The filter contains multiple fields
                        # e.g. date|rangefilter.filter.DateRangeFilter
                        new_fields = []
                        fields = item.field.split('|')
                        for field in fields:
                            if '.' in field:
                                # The filter contain a module.class field
                                field = get_class_from_module(field)
                            new_fields.append(field)
                    elif '.' in item.field:
                        # The filter contain a module.class field
                        new_fields = get_class_from_module(item.field)
                    else:
                        # The filter is a string filter
                        new_fields = item.field
                    model.list_filter.append(new_fields)
    except OperationalError:
        # If the model doesn't yet exist skip the customization
        pass
