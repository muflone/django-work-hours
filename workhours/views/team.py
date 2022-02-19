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
from django.utils.translation import pgettext_lazy
from django.views.generic import DetailView

from utility.extras import get_configuration_int
from utility.mixins import RequireLoginMixin

from workhours.constants import WEEKS_TO_LIST
from workhours.mixins import IsInTeamUserMixin, TeamMixin
from workhours.models import Team, Week


class TeamView(RequireLoginMixin,
               TeamMixin,
               IsInTeamUserMixin,
               DetailView):
    model = Team
    template_name = 'workhours/team.html'
    page_title_1 = pgettext_lazy('Team', 'Team')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title_1'] = self.object.name
        # Get the previous weeks
        weeks = []
        weeks_to_list = get_configuration_int(name=WEEKS_TO_LIST,
                                              default=5)
        today = datetime.date.today()
        for week_number in range(weeks_to_list):
            starting_date = (today -
                             datetime.timedelta(days=today.weekday(),
                                                weeks=week_number))
            ending_date = starting_date + datetime.timedelta(days=6)
            if week_number > 0:
                # Get a previous week if it exists
                week = Week.objects.filter(team_id=self.object.pk,
                                           starting_date=starting_date,
                                           ending_date=ending_date).first()
            else:
                # Create the current week if it's missing
                week, _ = Week.objects.get_or_create(
                    team_id=self.object.pk,
                    starting_date=starting_date,
                    ending_date=ending_date,
                    defaults={'is_closed': False})
            # Add a week if it was created or found
            if week:
                week_title = pgettext_lazy(
                    'Week',
                    'Week from {STARTING_DATE} to {ENDING_DATE}').format(
                    STARTING_DATE=format_date(
                        value=week.starting_date,
                        format_string=context['date_format_short']),
                    ENDING_DATE=format_date(
                        value=week.ending_date,
                        format_string=context['date_format_short']))
                weeks.append((week_number, week, week_title))
        context['weeks'] = weeks
        return context
