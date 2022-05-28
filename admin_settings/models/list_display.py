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

from utility.extras import get_admin_models
from utility.models.base import BaseModel, BaseModelAdmin
from django.utils.translation import pgettext_lazy


class ListDisplay(BaseModel):
    """List Display"""
    admin_models = get_admin_models()

    model = models.CharField(
        max_length=255,
        choices=((model_name, model_name)
                 for model_name
                 in sorted(admin_models.keys())),
        verbose_name=pgettext_lazy('ListDisplay', 'model'))
    field = models.CharField(
        max_length=255,
        verbose_name=pgettext_lazy('ListDisplay', 'field'))
    order = models.PositiveIntegerField(
        verbose_name=pgettext_lazy('ListDisplay', 'order'))
    enabled = models.BooleanField(
        default=True,
        verbose_name=pgettext_lazy('ListDisplay', 'enabled'))

    class Meta:
        # Define the database table
        ordering = ['model', 'order', 'field']
        unique_together = (('model', 'field'),
                           ('model', 'order'))
        verbose_name = pgettext_lazy('ListDisplay',
                                     'List Display')
        verbose_name_plural = pgettext_lazy('ListDisplay',
                                            'List Display')

    def __str__(self):
        return '{MODEL} - {FIELD}'.format(MODEL=self.model,
                                          FIELD=self.field)


class ListDisplayAdmin(BaseModelAdmin):
    pass
