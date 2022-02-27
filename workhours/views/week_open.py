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

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse
from django.views.generic import DetailView

from utility.mixins import RequireLoginMixin

from workhours.constants import PERMISSION_CAN_REOPEN_WEEKS
from workhours.mixins import IsInTeamUserMixin
from workhours.models import Week


class WeekOpenView(RequireLoginMixin,
                   PermissionRequiredMixin,
                   IsInTeamUserMixin,
                   DetailView):
    model = Week
    permission_required = (f'workhours.{PERMISSION_CAN_REOPEN_WEEKS}', )

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object.is_closed = False
        self.object.save()
        return JsonResponse({'code': 200})
