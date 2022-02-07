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

from django.views.generic import DetailView

from utility.extras import get_configuration_value
from utility.mixins import RequireLoginMixin

from workhours.constants import WEEKS_TO_LIST
from workhours.mixins import TeamMixin
from workhours.models import Team, Week


class TeamView(RequireLoginMixin,
               TeamMixin,
               DetailView):
    model = Team
    template_name = 'workhours/team.html'
    page_title = 'Team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.name
        # Get the previous weeks
        weeks = []
        weeks_to_list = int(get_configuration_value(name=WEEKS_TO_LIST,
                                                    default='5'))
        today = datetime.date.today()
        for week_number in range(weeks_to_list):
            starting_date = (today -
                             datetime.timedelta(days=today.weekday(),
                                                weeks=week_number))
            ending_date = starting_date + datetime.timedelta(days=6)
            week, _ = Week.objects.get_or_create(team_id=self.object.pk,
                                                 starting_date=starting_date,
                                                 ending_date=ending_date,
                                                 defaults={'is_closed': True})
            weeks.append((week_number, week))
        context['weeks'] = weeks
        return context
