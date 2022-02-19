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


class Week(BaseModel):
    """
    Weeks
    """
    team = models.ForeignKey(
        to='Team',
        on_delete=models.PROTECT,
        verbose_name=pgettext_lazy('Week', 'team'))
    starting_date = models.DateField(
        null=False,
        verbose_name=pgettext_lazy('Week', 'starting date'))
    ending_date = models.DateField(
        null=False,
        verbose_name=pgettext_lazy('Week', 'ending date'))
    notes = models.TextField(
        blank=True,
        verbose_name=pgettext_lazy('Week', 'notes'))
    is_closed = models.BooleanField(
        default=False,
        verbose_name=pgettext_lazy('Week', 'is closed'))

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['team', 'starting_date'],
                                    name='week_unique_team_starting_date')
        ]
        ordering = ['-starting_date', '-ending_date', 'team']
        verbose_name = pgettext_lazy('Week',
                                     'Week')
        verbose_name_plural = pgettext_lazy('Week',
                                            'Weeks')

    def __str__(self):
        return '{TEAM} - {START} - {END}'.format(
            TEAM=self.team,
            START=self.starting_date.strftime('%Y-%m-%d'),
            END=self.ending_date.strftime('%Y-%m-%d'))


class WeekAdmin(BaseModelAdmin):
    list_display = ('starting_date', 'ending_date', 'team', 'is_closed')
    list_filter = ('team', 'is_closed')
