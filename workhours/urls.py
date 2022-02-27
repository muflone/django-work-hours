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

from django.urls import path

from .views import (DashboardView,
                    HomeView,
                    ReportsView,
                    ShiftUpdateView,
                    TeamView,
                    WeekCloseView,
                    WeekOpenView,
                    WeekView)
from .views.auth import LoginView, LogoutView


urlpatterns = []
# Home page
urlpatterns.append(path(route='',
                        view=HomeView.as_view(),
                        name='workhours.home'))
# Login page
urlpatterns.append(path(route='login',
                        view=LoginView.as_view(),
                        name='workhours.auth.login'))
# Logout page
urlpatterns.append(path(route='logout',
                        view=LogoutView.as_view(),
                        name='workhours.auth.logout'))
# Dashboard page
urlpatterns.append(path(route='dashboard',
                        view=DashboardView.as_view(),
                        name='workhours.dashboard'))
# Team page
urlpatterns.append(path(route='team/'
                              '<int:pk>',
                        view=TeamView.as_view(),
                        name='workhours.team'))
# Week page
urlpatterns.append(path(route='week/'
                              '<int:pk>',
                        view=WeekView.as_view(),
                        name='workhours.week'))
# Shift update page
urlpatterns.append(path(route='shift_update',
                        view=ShiftUpdateView.as_view(),
                        name='workhours.shift_update'))
# Week close page
urlpatterns.append(path(route='week/'
                              '<int:pk>/'
                              'close',
                        view=WeekCloseView.as_view(),
                        name='workhours.week.close'))
# Week open page
urlpatterns.append(path(route='week/'
                              '<int:pk>/'
                              'open',
                        view=WeekOpenView.as_view(),
                        name='workhours.week.open'))
# Report page
urlpatterns.append(path(route='reports',
                        view=ReportsView.as_view(),
                        name='workhours.reports'))
