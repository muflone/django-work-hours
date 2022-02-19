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


class Employee(BaseModel):
    """
    Employees
    """
    first_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=pgettext_lazy('Employee', 'First name'))
    last_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=pgettext_lazy('Employee', 'Last name'))
    is_active = models.BooleanField(
        null=False,
        default=True,
        verbose_name=pgettext_lazy('Employee', 'Is active'))

    objects = models.Manager()
    objects_active = ManagerIsActive()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'],
                                    name='employee_unique_first_last_name')
        ]
        ordering = ['first_name', 'last_name']
        verbose_name = pgettext_lazy('Employee', 'Employee')
        verbose_name_plural = pgettext_lazy('Employee', 'Employees')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EmployeeAdmin(BaseModelAdmin):
    list_display = ('__str__', 'is_active')
    list_filter = ('is_active', )
