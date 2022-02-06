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

from workhours.models import Shift


class ShiftUpdateForm(forms.ModelForm):
    pk = forms.IntegerField(required=True)
    present = forms.BooleanField(required=False)
    holiday = forms.BooleanField(required=False)
    permit = forms.IntegerField(required=False)

    class Meta:
        model = Shift
        fields = ('pk', 'present', 'holiday', 'permit')


class ShiftUpdateView(RequireLoginMixin,
                      UpdateView):
    model = Shift
    form_class = ShiftUpdateForm

    def post(self, request, *args, **kwargs):
        form = super().get_form(form_class=self.form_class)
        if form.is_valid():
            shift = Shift.objects.get(pk=form.cleaned_data['pk'])
            if not shift.week.is_closed:
                shift.is_present = form.cleaned_data.get('present', False)
                shift.is_holiday = form.cleaned_data.get('holiday', False)
                shift.permit_hours = form.cleaned_data.get('permit', 0)
                shift.save()
                return JsonResponse({'code': 200})
            else:
                # The week is closed, unable to update
                return HttpResponseForbidden()
        else:
            return HttpResponseServerError()
