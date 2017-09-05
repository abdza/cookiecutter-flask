# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, render_template, g, current_app
import os, public, user
from .assets import assets
from .extensions import (admin, api, bcrypt, cache, csrf_protect, db,
                         login_manager, migrate, mail, babel)
from .settings import ProdConfig
if os.environ.get('{{cookiecutter.app_name | upper}}_ENV')!='prod':
    from .extensions import debug_toolbar

@babel.localeselector
def get_locale():
    return g.get('lang_code', current_app.config['BABEL_DEFAULT_LOCALE'])

@babel.timezoneselector
def get_timezone():
    user = g.get('user', None)
    if user is not None:
        return user.timezone


@login_manager.request_loader
def load_user_from_request(request):

    uauth = request.authorization

    if uauth:
        user = User.query.filter_by(username=uauth.username).first()
        if user and user.check_password(uauth.password):
            return user
    elif 'Authorization' in request.headers:
        tokens = request.headers['Authorization'].split(' ')
        user = User.query.filter_by(token = tokens[1]).first()
        if user:
            return user
    # finally, return None if both methods did not login the user
    return None


def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    admin_views(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    api.init_app(app)

    if os.environ.get('{{cookiecutter.app_name | upper}}_ENV')!='prod':
        debug_toolbar.init_app(app)

    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    return None


def admin_views(app):
    """Register admin views."""
    user.admin.add_views(admin, db)
    return None


def api_resources():
    """Link up restful controllers."""
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
