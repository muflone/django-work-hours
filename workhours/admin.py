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

from django.contrib import admin

from .models import (Employee, EmployeeAdmin,
                     Extra, ExtraAdmin,
                     Shift, ShiftAdmin,
                     ShiftExtra, ShiftExtraAdmin,
                     Team, TeamAdmin,
                     Week, WeekAdmin)


# Models registration
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(ShiftExtra, ShiftExtraAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Week, WeekAdmin)
