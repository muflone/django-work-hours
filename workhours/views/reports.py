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

from django.utils.translation import pgettext_lazy
from django.views.generic import FormView

from utility.extras import iter_dates, iter_days
from utility.mixins import RequireSuperUserMixin

from workhours.constants import REPORT_TEAMS_HTML
from workhours.forms import ReportForm
from workhours.mixins import TeamMixin
from workhours.models import Employee, Shift, Team


class ReportsView(RequireSuperUserMixin,
                  TeamMixin,
                  FormView):
    template_name = 'workhours/reports/base.html'
    page_title_1 = pgettext_lazy('Reports', 'Reports')
    form_class = ReportForm

    def form_valid(self, form):
        report_type = form.cleaned_data['report_type']
        starting_date = form.cleaned_data['starting_date']
        ending_date = form.cleaned_data['ending_date']
        if report_type == REPORT_TEAMS_HTML:
            results = self.report_teams_html(starting_date=starting_date,
                                             ending_date=ending_date)
        else:
            results = {}
        return self.render_to_response(
            self.get_context_data(report_type=report_type,
                                  starting_date=starting_date,
                                  ending_date=ending_date,
                                  **results))

    def get_template_names(self):
        form = self.get_form(self.form_class)
        template_name = self.template_name
        # Change template name based on the report type
        if form.data.get('report_type') == REPORT_TEAMS_HTML:
            template_name = 'workhours/reports/teams_html.html'
        return [template_name]

    def report_teams_html(self,
                          starting_date: datetime.date,
                          ending_date: datetime.date) -> dict:
        results = []
        for team in Team.objects.order_by('name'):
            data = {}
            for employee in team.employees.all():
                data[employee.pk] = [None
                                     for _
                                     in iter_days(starting_date, ending_date)]
            shifts = Shift.objects.filter(week__team=team.pk,
                                          date__gte=starting_date,
                                          date__lte=ending_date)
            for shift in shifts:
                # Get relative day
                day = (shift.date - starting_date).days
                # Save shift data
                data[shift.employee_id][day] = shift
            results.append((team.pk, team.name, data))
        return {'days': [day
                         for day
                         in iter_dates(starting_date, ending_date)],
                'employees': {employee.id: str(employee)
                              for employee
                              in Employee.objects.all()},
                'results': results}
