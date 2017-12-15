from flask import Flask #, render_template, request
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig

import json
import scipy
import plotly
import plotly.figure_factory as ff
import plotly.graph_objs as go

import pandas as pd
import numpy as np

from .frontend import frontend
from .nav import nav

def create_app(configfile=None):
    # We are using the "Application Factory"-pattern here, which is described
    # in detail inside the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/

    app = Flask(__name__)

    # We use Flask-Appconfig here, but this is not a requirement
    AppConfig(app)

    # Install our Bootstrap extension
    Bootstrap(app)

    # Our application uses blueprints as well; these go well with the
    # application factory. We already imported the blueprint, now we just need
    # to register it:
    app.register_blueprint(frontend)

    # Because we're security-conscious developers, we also hard-code disabling
    # the CDN support (this might become a default in later versions):
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    # We initialize the navigation as well
    nav.init_app(app)

    return app



# Commenting out for attempt to swith to application factory format

# app = Flask(__name__)

# @app.route('/wordclouds', methods=['GET', 'POST'])
# def wordclouds():
#     return render_template('wordclouds.html')
#
#
# @app.route('/dendro', methods=['GET', 'POST'])
# def dendro():
#     return render_template('dendro.html')
#
#
# @app.route('/')
# def home():
#     name = request.args.get('name')
#     if name == None:
#         name = 'World'
#     return render_template('home.html', name = name)
#
#
# # Run the app!
# if __name__ == '__main__':
#     app.debug = True
#     app.run()
