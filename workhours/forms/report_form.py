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

from django import forms
from django.utils.translation import pgettext_lazy

from bootstrap_datepicker_plus.widgets import DatePickerInput

from workhours.constants import REPORT_TEAMS_HTML, REPORT_TEAMS_XLS


class ReportForm(forms.Form):
    report_type = forms.ChoiceField(
        choices=[(REPORT_TEAMS_HTML,
                  pgettext_lazy('Reports', 'Teams in HTML')),
                 (REPORT_TEAMS_XLS,
                  pgettext_lazy('Reports', 'Teams in Excel')),
                 ],
        required=True,
        label=pgettext_lazy('Reports', 'Report type'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    starting_date = forms.DateField(
        required=True,
        label=pgettext_lazy('Reports', 'Starting date'),
        widget=DatePickerInput(format='%Y/%m/%d',
                               options={'showClose': False,
                                        'showClear': False,
                                        'showTodayButton': True
                                        }),
        initial=datetime.date.today().strftime('%Y/%m/%d'))
    ending_date = forms.DateField(
        required=True,
        label=pgettext_lazy('Reports', 'Ending date'),
        widget=DatePickerInput(format='%Y/%m/%d',
                               options={'showClose': False,
                                        'showClear': False,
                                        'showTodayButton': True
                                        }),
        initial=datetime.date.today().strftime('%Y/%m/%d'))
