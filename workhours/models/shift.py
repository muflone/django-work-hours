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


class Shift(BaseModel):
    """
    Shifts
    """
    week = models.ForeignKey(to='Week',
                             on_delete=models.PROTECT)
    employee = models.ForeignKey(to='Employee',
                                 on_delete=models.PROTECT)
    date = models.DateField(null=False)
    is_present = models.BooleanField(default=False)
    is_holyday = models.BooleanField(default=False)
    permit_hours = models.PositiveSmallIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['week', 'employee', 'date'],
                                    name='shift_unique_date_employee_date')
        ]
        ordering = ['-week', '-date', 'employee']
        verbose_name = pgettext_lazy('Shift',
                                     'Shift')
        verbose_name_plural = pgettext_lazy('Shift',
                                            'Shifts')

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')


class ShiftAdmin(BaseModelAdmin):
    list_display = ('date', 'week', 'employee',
                    'is_present', 'is_holyday', 'permit_hours')
    list_filter = ('employee', )