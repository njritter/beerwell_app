from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import json
import scipy
import plotly
import plotly.figure_factory as ff
import plotly.graph_objs as go

import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/wordclouds', methods=['GET', 'POST'])
def wordclouds():
    return render_template('wordclouds.html')


@app.route('/dendro', methods=['GET', 'POST'])
def dendro():
    return render_template('dendro.html')


@app.route('/')
def home():
    name = request.args.get('name')
    if name == None:
        name = 'World'
    return render_template('home.html', name = name)


# Run the app!
if __name__ == '__main__':
    app.debug = True
    app.run()
