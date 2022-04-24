# app/home/views.py

from flask import abort, render_template, request, redirect, flash
from flask_login import current_user, login_required
from .forms import BookSearchForm
from ..models import Book

from . import home

@home.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Render the homepage template on the / route
    """
    search = BookSearchForm(request.form)
   
    if request.method == 'POST':
        return search_results(search)

    return render_template('home/index.html', title="Welcome to Vitabu.ke", form=search)

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Your Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing this page
    if not current_user.is_admin:
       abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")


@home.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
       #search_terms = search.data['search']
       results = Book.query.all()
       #results = Book.query.filter_by(grade_id = 4).all()
       #results = Book.query.filter(Book.title.contains(search_string)).all()
    else:
       results = Book.query.filter(Book.title.contains(search_string)).all()
       #return render_template('home/results.html', results=results)
    if not results:
       flash('No results found!')
       return redirect('/')
    else:
       return render_template('home/results.html', results=results)
