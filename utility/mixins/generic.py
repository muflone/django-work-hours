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

from django.views.generic import View
from django.views.generic.base import ContextMixin

from project import PRODUCT_NAME, VERSION

from utility.constants import (DATE_FORMAT_FULL,
                               DATE_FORMAT_SHORT,
                               SITE_HIDE_DASHBOARD,
                               SITE_TITLE)
from utility.extras import get_configuration_bool, get_configuration_value


class GenericMixin(ContextMixin,
                   View):
    """Generic mixin"""
    extra_context = {
        'app_name': PRODUCT_NAME,
        'app_version': VERSION,
        'date_format_short':  get_configuration_value(name=DATE_FORMAT_SHORT,
                                                      default='Y/m/d'),
        'date_format_full': get_configuration_value(name=DATE_FORMAT_FULL,
                                                    default='l Y/m/d'),
        'site_hide_dashboard': get_configuration_bool(name=SITE_HIDE_DASHBOARD,
                                                      default=False),
        'site_title': get_configuration_value(name=SITE_TITLE,
                                              default=PRODUCT_NAME),
    }
    page_title_1 = ''
    page_title_2 = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_path'] = self.request.path
        context['page_title_1'] = self.page_title_1
        context['page_title_2'] = self.page_title_2
        return context
