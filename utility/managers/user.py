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

from django.contrib.auth.base_user import BaseUserManager


class ManagerUser(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, last_name, password,
                     **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password,
                    **extra_fields):
        return self._create_user(email,
                                 first_name,
                                 last_name,
                                 password,
                                 **extra_fields)

    def create_superuser(self, email, first_name, last_name, password,
                         **extra_fields):
        user = self._create_user(email,
                                 first_name,
                                 last_name,
                                 password,
                                 **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
