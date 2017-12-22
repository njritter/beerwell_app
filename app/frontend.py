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
import pandas as pd
import dill

from .nav import nav

frontend = Blueprint('frontend', __name__)

# We're adding a navbar as well through flask-navbar.
nav.register_element('frontend_top', Navbar(
    View('BeerWell', '.home'),
    View('Home', '.home'),
    View('Map', '.map'),
    View('Explore', '.explore'),
    View('About', '.about') ))


# Pages
@frontend.route('/')
def index():
    return render_template('home.html')

@frontend.route('/home')
def home():
    return render_template('home.html')

@frontend.route('/map')
def map():
    return render_template('map.html')

@frontend.route('/explore/')
@frontend.route('/explore/<ind>')
def explore(ind=0):
    beerPanda = pd.read_pickle('/Users/Drazi/beerwell_app/app/data/beerpanda.pkd')
    all_beers = zip(list(range(250)), beerPanda.Name.tolist()) # index attached
    beer_stats = beerPanda.iloc[int(ind)].tolist() # row from beerPanda
    return render_template('explore.html',
                            all_beers=all_beers,
                            beer='wordclouds/Beer_' + str(ind),
                            beer_stats=beer_stats)

@frontend.route('/about/')
def about():
    return render_template('about.html')
