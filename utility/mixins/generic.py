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

from utility.extras import get_configuration_value


class GenericMixin(ContextMixin,
                   View):
    """Generic mixin"""
    extra_context = {
        'app_name': PRODUCT_NAME,
        'app_version': VERSION,
        'date_format_short':  get_configuration_value(name='date_format_short',
                                                      default='Y/m/d'),
        'date_format_full': get_configuration_value(name='date_format_full',
                                                    default='Y/m/d h:i:s'),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_path'] = self.request.path
        context['page_title'] = self.page_title
        return context
