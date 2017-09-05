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
from flask_mail import Mail, Message
from flask_babelex import Babel
from celery import Celery
from flask_chartjs import ChartJs
from flask_babelex import lazy_gettext as _
from .settings import Config
import os
if os.environ.get('{{cookiecutter.app_name | upper}}_ENV')!='prod':
    from flask_debugtoolbar import DebugToolbarExtension

bcrypt = Bcrypt()
csrf_protect = CsrfProtect()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
admin = Admin(
    template_mode='bootstrap3',
    index_view=AdminIndexView(
        name=str(_('Main Site')),
        url='/{{cookiecutter.app_name | lower }}',
        menu_icon_type='fa',
        menu_icon_value='fa fa-home'
    ),
    category_icon_classes={
        'User Management': 'fa fa-user',
    }
)
api = Api()
mail = Mail()
babel = Babel()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

if os.environ.get('{{cookiecutter.app_name | upper}}_ENV')!='prod':
    debug_toolbar = DebugToolbarExtension()
