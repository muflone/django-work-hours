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

from django.db import models
from django.contrib.auth.models import AbstractUser

from utility.managers import ManagerIsActive, ManagerUser
from utility.models import BaseModel


class User(BaseModel,
           AbstractUser):
    """User"""
    email = models.EmailField(unique=True,
                              blank=False,
                              null=False)
    first_name = models.CharField(max_length=255,
                                  blank=False,
                                  null=False)
    last_name = models.CharField(max_length=255,
                                 blank=False,
                                 null=False)
    login_redirect_page = models.CharField(max_length=255,
                                           blank=True,
                                           null=False)
    # Remove the username field with unique constraint
    username = None
    # Set the user manager
    objects = ManagerUser()
    objects_active = ManagerIsActive()
    # Set properties
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        # Define the database table
        db_table = 'auth_users'
        ordering = ['id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.get_full_name()} <{self.email}>'

    def get_initials(self):
        """User initials"""
        return f'{self.first_name[0]} {self.last_name[0]}'

    def get_full_name(self):
        """User full name"""
        return f'{self.first_name} {self.last_name}'
