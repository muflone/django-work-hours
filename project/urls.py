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

from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include('workhours.urls')),
]

if settings.DEBUG:
    try:
        # Try to add the Django Debug Toolbar path
        import debug_toolbar
        urlpatterns.append(path('__debug__/',
                                include(debug_toolbar.urls)))
    except ImportError:
        # Module not found, don't add the Django Debug Toolbar path
        pass
