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

from django.contrib.auth.mixins import UserPassesTestMixin

from workhours.models import Shift, Team, Week


class IsInTeamUserMixin(UserPassesTestMixin):
    """
    Check if the current user belongs to the team
    Applies to Team, Week and Shift objects
    """
    def test_func(self):
        # Get the object ID from arguments
        object_id = self.kwargs.get('pk')
        if not object_id:
            # Check if there's a valid form
            form = super().get_form(form_class=self.form_class)
            if form.is_valid():
                object_id = form.cleaned_data['pk']
        result = False
        if issubclass(self.model, Team):
            # Check team
            object = self.model.objects.get(pk=object_id)
            result = self.request.user in object.managers.all()
        elif issubclass(self.model, Week):
            # Check week
            object = self.model.objects.get(pk=object_id)
            result = self.request.user in object.team.managers.all()
        elif issubclass(self.model, Shift):
            # Check shift
            object = self.model.objects.get(pk=object_id)
            result = self.request.user in object.week.team.managers.all()
        return result
