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

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import pgettext_lazy

from utility.managers import ManagerIsActive
from utility.models import BaseModel, BaseModelAdmin


class Team(BaseModel):
    """
    Teams
    """
    name = models.CharField(max_length=255,
                            blank=False,
                            null=False)
    description = models.TextField(blank=True,
                                   null=False)
    is_active = models.BooleanField(null=False,
                                    default=True)
    employees = models.ManyToManyField(to='Employee')
    managers = models.ManyToManyField(to=get_user_model(),
                                      blank=True)

    # Automatically filter on the enabled only records
    objects = models.Manager()
    objects_active = ManagerIsActive()

    class Meta:
        ordering = ['name']
        verbose_name = pgettext_lazy('Team',
                                     'Team')
        verbose_name_plural = pgettext_lazy('Team',
                                            'Teams')

    def __str__(self):
        return self.name


class TeamAdmin(BaseModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active', )
