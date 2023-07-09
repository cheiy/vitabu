# app/home/views.py

from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    """
    Landing page
    """
    return render_template('home/index.html', title="Vitabu! - Buy, Sell, Exchange")

@home.route('/mylisting')
@login_required
def mylisting():
    """
    Render the logged in user's products on the /mylisting route
    """
    return render_template('home/mylisting.html', title="Listings")
