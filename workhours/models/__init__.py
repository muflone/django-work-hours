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

from .employee import Employee, EmployeeAdmin                      # noqa: F401
from .extra import Extra, ExtraAdmin                               # noqa: F401
from .shift import Shift, ShiftAdmin                               # noqa: F401
from .shift_extra import ShiftExtra, ShiftExtraAdmin               # noqa: F401
from .team import Team, TeamAdmin                                  # noqa: F401
from .week import Week, WeekAdmin                                  # noqa: F401
