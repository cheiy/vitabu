# home/views.py

from flask import Flask, abort, render_template, request, redirect, flash, url_for, request
#from flask_login import current_user, login_required
#from .forms import BookSearchForm, AddListingForm
#from ..models import Book

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome to Vitabu.ke")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
