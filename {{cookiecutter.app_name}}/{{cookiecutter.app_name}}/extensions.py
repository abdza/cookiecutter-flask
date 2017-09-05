# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_rest_jsonapi import Api
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
import os
if os.environ.get('{{cookiecutter.app_name | upper}}_ENV')!='prod':
    from flask_debugtoolbar import DebugToolbarExtension

bcrypt = Bcrypt()
csrf_protect = CsrfProtect()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
admin = Admin(template_mode='bootstrap3')
api = Api()

if os.environ.get('{{cookiecutter.app_name | upper}}_ENV')!='prod':
    debug_toolbar = DebugToolbarExtension()
