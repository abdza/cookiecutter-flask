from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose

import flask_login as login
from flask import redirect, request, url_for

from .models import User, Role


class UserManagementAdmin(ModelView):

    def is_accessible(self):
        if(login.current_user.is_authenticated):
            return login.current_user.is_admin
        return False

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('public.home', next=request.url))


class UserAdmin(UserManagementAdmin):
    form_excluded_columns = ['password', 'creations', 'order_roles', 'staffs', 'roles']
    column_exclude_list = ['password', ]


class RoleAdmin(UserManagementAdmin):
    pass


def add_views(admin, db):
    admin.add_view(UserAdmin(User, db.session, endpoint='useradmin'))
    admin.add_view(RoleAdmin(Role, db.session, endpoint='roleadmin'))
