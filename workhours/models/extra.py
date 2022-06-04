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

from utility.managers import ManagerIsActive
from utility.models import BaseModel, BaseModelAdmin


class Extra(BaseModel):
    """
    Extras
    """
    EXTRA_TYPE_TEXT = 0
    EXTRA_TYPE_NUMERIC = 1
    EXTRA_TYPE_CHECK_LEFT = 2
    EXTRA_TYPE_CHECK_RIGHT = 3
    EXTRA_TYPE_SELECT = 4

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        verbose_name=pgettext_lazy('Extra', 'Name'))
    description = models.TextField(
        blank=True,
        verbose_name=pgettext_lazy('Extra', 'Description'))
    type = models.PositiveSmallIntegerField(
        null=False,
        choices=((EXTRA_TYPE_TEXT, pgettext_lazy('Extra', 'Text')),
                 (EXTRA_TYPE_NUMERIC, pgettext_lazy('Extra', 'Numeric')),
                 (EXTRA_TYPE_CHECK_LEFT, pgettext_lazy('Extra',
                                                       'Checkbox on left')),
                 (EXTRA_TYPE_CHECK_RIGHT, pgettext_lazy('Extra',
                                                        'Checkbox on right')),
                 (EXTRA_TYPE_SELECT, pgettext_lazy('Extra', 'Select'))),
        default=True,
        verbose_name=pgettext_lazy('Extra', 'Type'))
    minimum = models.PositiveIntegerField(
        null=False,
        default=0,
        verbose_name=pgettext_lazy('Extra', 'Minimum value'))
    maximum = models.PositiveIntegerField(
        null=False,
        default=0,
        verbose_name=pgettext_lazy('Extra', 'Maximum value'))
    values = models.TextField(
        blank=True,
        verbose_name=pgettext_lazy('Extra', 'Values'))
    order = models.PositiveIntegerField(
        verbose_name=pgettext_lazy('Extra', 'order'))
    is_active = models.BooleanField(
        null=False,
        default=True,
        verbose_name=pgettext_lazy('Extra', 'Is active'))

    objects = models.Manager()
    objects_active = ManagerIsActive()

    class Meta:
        ordering = ['order', 'name']
        verbose_name = pgettext_lazy('Extra', 'Extra')
        verbose_name_plural = pgettext_lazy('Extra', 'Extras')

    def __str__(self):
        return self.name


class ExtraAdmin(BaseModelAdmin):
    list_display = ('__str__', 'is_active')
    list_filter = ('is_active', )
