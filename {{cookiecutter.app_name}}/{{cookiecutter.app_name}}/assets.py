# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

css = Bundle(
    'libs/bootstrap/dist/css/bootstrap.css',
    'libs/bootstrap/dist/css/bootstrap-datepicker.css',
    'libs/font-awesome4/css/font-awesome.min.css',
    'libs/material-design/material-icons.css',
    'libs/adminLTE/css/AdminLTE.css',
    'libs/adminLTE/css/skins/skin-yellow.css',
    'css/style.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'libs/jQuery/dist/jquery.js',
    'libs/bootstrap/dist/js/bootstrap.js',
    'libs/bootstrap/dist/js/bootstrap-datepicker.js',
    'libs/adminLTE/js/adminlte.js',
    'libs/adminLTE/js/app.js',
    'js/plugins.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
