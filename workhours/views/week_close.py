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

from django import forms
from django.http import (HttpResponseForbidden,
                         HttpResponseServerError,
                         JsonResponse)
from django.views.generic import UpdateView

from utility.mixins import RequireLoginMixin

from workhours.mixins import IsInTeamUserMixin
from workhours.models import Week


class WeekCloseForm(forms.ModelForm):
    pk = forms.IntegerField(required=True)
    notes = forms.CharField(required=False)

    class Meta:
        model = Week
        fields = ('pk', 'notes')


class WeekCloseView(RequireLoginMixin,
                    IsInTeamUserMixin,
                    UpdateView):
    model = Week
    form_class = WeekCloseForm

    def post(self, request, *args, **kwargs):
        form = super().get_form(form_class=self.form_class)
        if form.is_valid():
            week = Week.objects.get(pk=form.cleaned_data['pk'])
            if not week.is_closed:
                week.notes = form.cleaned_data.get('notes', '')
                week.is_closed = True
                week.save()
                return JsonResponse({'code': 200})
            else:
                # The week is closed, unable to update
                return HttpResponseForbidden()
        else:
            return HttpResponseServerError()
