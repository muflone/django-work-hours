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
from typing import Generator


def iter_dates(starting_date: datetime.date,
               ending_date: datetime.date) -> Generator[datetime.date,
                                                        None,
                                                        None]:
    """
    Iterate over two dates
    :param starting_date: initial date
    :param ending_date: ending date
    :return: each date between the two dates
    """
    for day in iter_days(starting_date=starting_date, ending_date=ending_date):
        yield starting_date + datetime.timedelta(days=day)


def iter_days(starting_date: datetime.date,
              ending_date: datetime.date) -> Generator[int, None, None]:
    """
    Iterate the days over two dates
    :param starting_date: initial date
    :param ending_date: ending date
    :return: relative day numbers between the two dates
    """
    for day in range(int((ending_date - starting_date).days) + 1):
        yield day
