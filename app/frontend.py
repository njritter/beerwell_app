# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape

from .nav import nav

frontend = Blueprint('frontend', __name__)

# We're adding a navbar as well through flask-navbar. In our example, the
# navbar has an usual amount of Link-Elements, more commonly you will have a
# lot more View instances.
nav.register_element('frontend_top', Navbar(
    View('BeerWell', '.home'),
    View('Home', '.home'),
    View('Map', '.map'),
    View('Explore', '.explore'),
    View('About', '.about') ))


# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/')
def index():
    return render_template('home.html')

@frontend.route('/home')
def home():
    return render_template('home.html')

@frontend.route('/map')
def map():
    return render_template('map.html')

@frontend.route('/explore')
def explore():
    return render_template('explore.html')

# About page
@frontend.route('/about/')
def about():
    return render_template('about.html')
