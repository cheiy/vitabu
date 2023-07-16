# app/home/views.py

from flask import abort, render_template, request, redirect, flash, url_for, request
from flask_login import current_user, login_required
from .forms import BookSearchForm, AddListingForm
from ..models import Book, Grade, BookListing

from . import home

@home.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Render the homepage template on the / route
    """
    terms =''
    form = BookSearchForm()
    if form.validate_on_submit():
       select = form.select.data
       select2 = form.select2.data
       terms = form.search.data
       #flash(select)
       if select == 'Title':
           results =  Book.query.filter(Book.title.contains(terms))
       elif select == 'Subject':
           results = Book.query.filter(Book.subject_id.contains(terms))
       elif select == 'Grade':
           results = Grade.query.filter_by(grade_name=terms)
       else:
           results = Book.query.all()
           flash("Please select search criteria")
       return render_template('home/results.html', title="results", results=results)
    return render_template('home/landing.html', title="Welcome to Vitabu.ke", form=form)

@home.route('/begin')
def begin_here():
    """
    Leave Landing Page
    """
    return render_template('home/index.html', title="Begin")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    listed_books = Book.query.all()
    return render_template('home/dashboard.html', title="Your Dashboard", listed_books=listed_books)

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing this page
    if not current_user.is_admin:
       abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")

@home.route('/search', methods=['GET','POST'])
def search_results(request):
    #books = Book.query.all()
    
    form = BookSearchForm(request.POST)
    if request.method == 'POST':
       results = form.search.data
    """
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
       return render_template('home/results.html', results=books)"""
    return render_response('home/results.html', form=form)

@home.route('/add_listing')
@login_required
def add_listing():
    form = AddListingForm()
    #listed_books = Book.query.all()
    return render_template('home/listings.html', form=form, listed_books=listed_books)

@home.route('/list_by_grade/<int:id>', methods=['GET', 'POST'])
def list_by_grades(id):
    """
    List all books in selected grade
    """

    #book = Book.query.all()
    book = Book.query.filter_by(grade_id=id)
    listings = BookListing.query.filter_by(grade_id=id)
        
    return render_template('home/books.html', book=book, listings=listings, title='GradeBooks')
