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

from django.db import models
from django.utils.translation import pgettext_lazy

from .base_model import BaseModel, BaseModelAdmin


class Configuration(BaseModel):
    """Configuration item"""
    name = models.CharField(max_length=255,
                            blank=False,
                            null=False)
    group = models.CharField(max_length=255,
                             default='',
                             blank=False,
                             null=False)
    value = models.TextField(blank=True,
                             null=False)
    description = models.TextField(blank=True)

    class Meta:
        # Define the database table
        ordering = ['group', 'name']
        verbose_name = pgettext_lazy('Configuration',
                                     'Configuration')
        verbose_name_plural = pgettext_lazy('Configuration',
                                            'Configurations')

    def __str__(self):
        return self.name


class ConfigurationAdmin(BaseModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group', )
