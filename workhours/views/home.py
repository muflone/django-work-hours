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

from django.urls import reverse_lazy
from django.views.generic import RedirectView


class HomeView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs) -> str:
        """
        Redirect page to the destination URL
        :param args:
        :param kwargs: captured arguments
        :return: destination URL
        """
        if not self.request.user.is_authenticated:
            url = reverse_lazy('workhours.auth.login',
                               kwargs=kwargs)
        else:
            page = self.request.user.login_redirect_page
            args = None
            query = None
            if page:
                if (page.startswith('/') or
                        page.startswith('http:') or
                        page.startswith('https:')):
                    # Use complete URL
                    url = page
                else:
                    # Use route with arguments and parameters
                    # Redirect page present, split page and arguments
                    if '?' in page:
                        page, query = page.split('?', 1)
                    if '/' in page:
                        page, *args = page.split('/')
                    querystring = query or ''
                    url = '{PAGE}{QUERYSTRING}'.format(
                        PAGE=reverse_lazy(page, args=args),
                        QUERYSTRING=f'?{querystring}' if querystring else '')
            else:
                url = reverse_lazy('workhours.dashboard')
        return url
