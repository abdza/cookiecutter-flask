# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

bcrypt = Bcrypt()
csrf_protect = CsrfProtect()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
admin = Admin(template_mode='bootstrap3')
api = Api(prefix='/api')
