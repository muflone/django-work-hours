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

import datetime

from django.utils.dateformat import format as format_date
from django.views.generic import DetailView

from utility.mixins import RequireLoginMixin

from workhours.mixins import TeamMixin
from workhours.models import Team, Shift, Week


class WeekView(RequireLoginMixin,
               TeamMixin,
               DetailView):
    model = Week
    template_name = 'workhours/week.html'
    page_title = 'Week'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_format = context['date_format_short']
        context['page_title'] = (
            'Week from {STARTING_DATE} to {ENDING_DATE}'.format(
                STARTING_DATE=format_date(value=self.object.starting_date,
                                          format_string=date_format),
                ENDING_DATE=format_date(value=self.object.ending_date,
                                        format_string=date_format)))
        # Get the team employees
        team = Team.objects_active.get(pk=self.object.team_id)
        employees = team.employees.order_by('first_name', 'last_name')
        # Get the days details
        days = []
        for day_number in range(7):
            day = (self.object.starting_date +
                   datetime.timedelta(days=day_number))
            shifts = []
            for employee in employees:
                shift, _ = Shift.objects.get_or_create(week=self.object,
                                                       employee=employee,
                                                       date=day)
                shifts.append(shift)
            days.append((day_number, day, shifts))
        context['days'] = days
        return context