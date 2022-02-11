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

from django.db import OperationalError, ProgrammingError

from utility.models import Configuration


def get_configuration_int(name: str, default: int = None) -> int:
    """
    Get an integer configuration value from a Configuration object
    :param name: configuration name
    :param default: default value
    :return: configuration value
    """
    return int(get_configuration_value(name=name,
                                       default=str(default)))


def get_configuration_value(name: str, default: str = None) -> str:
    """
    Get a configuration value from a Configuration object
    :param name: configuration name
    :param default: default value
    :return: configuration value
    """
    try:
        configuration = Configuration.objects.filter(name=name).first()
    except (OperationalError, ProgrammingError):
        configuration = None
    return configuration.value if configuration else default
