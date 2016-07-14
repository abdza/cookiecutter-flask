# -*- coding: utf-8 -*-
"""Flask Admin admins."""
import flask_login as login
from flask import redirect, request, url_for
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView

from .models import Role, User


class UserManagementAdmin(ModelView):
    """Base Model for user management."""

    def is_accessible(self):
        """Need to make sure user is an admin to allow user management."""
        if(login.current_user.is_authenticated):
            return login.current_user.is_admin
        return False

    def inaccessible_callback(self, name, **kwargs):
        """What to do if user is not allowed to user manage."""
        return redirect(url_for('public.home', next=request.url))


class UserAdmin(UserManagementAdmin):
    """User admin."""

    form_excluded_columns = ['password', 'creations', 'order_roles', 'staffs', 'roles']
    column_exclude_list = ['password', ]


class RoleAdmin(UserManagementAdmin):
    """Role admin. Currently use default."""

    pass


def add_views(admin, db):
    """Add user admin views into views."""
    admin.add_view(UserAdmin(User, db.session, endpoint='useradmin'))
    admin.add_view(RoleAdmin(Role, db.session, endpoint='roleadmin'))
