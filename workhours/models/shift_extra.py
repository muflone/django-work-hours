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

from utility.models import BaseModel, BaseModelAdmin

from workhours.constants import PERMISSION_CAN_ACCESS_REPORTS


class ShiftExtra(BaseModel):
    """
    Shift Extras
    """
    shift = models.ForeignKey(
        to='Shift',
        on_delete=models.PROTECT,
        verbose_name=pgettext_lazy('Shift', 'Shift'))
    extra = models.ForeignKey(
        to='Extra',
        on_delete=models.PROTECT,
        verbose_name=pgettext_lazy('Extra', 'Extra'))
    value = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        verbose_name=pgettext_lazy('ShiftExtra', 'Value'))

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['shift', 'extra'],
                                    name='shiftextra_unique_shift_extra')
        ]
        ordering = ['-shift', 'extra']
        verbose_name = pgettext_lazy('ShiftExtra', 'Shift Extra')
        verbose_name_plural = pgettext_lazy('ShiftExtra', 'Shift Extras')

    def __str__(self):
        return f'{self.shift} {self.extra.name}'

    def employee(self):
        return self.shift.employee

    def team(self):
        return self.shift.week.team


class ShiftExtraAdmin(BaseModelAdmin):
    list_display = ('shift', 'employee', 'extra')
    list_filter = ('shift__week__team', 'shift__employee',
                   'extra', 'extra__type')
