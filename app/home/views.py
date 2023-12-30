# app/home/views.py

from flask import abort, render_template, request, redirect, flash, url_for, request
from flask_login import current_user, login_required
from .forms import BookSearchForm, AddListingForm, AddBooksToList
from ..models import Book, Grade, BookListing, UserPost, PostedBook

from . import home
from .. import db

@home.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/landing.html', title="Welcome to Vitabu.ke")

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
    lists = PostedBook.query.all()
    return render_template('home/dashboard.html', title="Your Dashboard", listed_books=listed_books, lists=lists)

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

@home.route('/add_listing', methods=['GET', 'POST'])
@login_required
def add_listing():
    """
    Add Listing
    """
    form = AddListingForm()
    lists = PostedBook.query.all()
    if form.validate_on_submit():
        listing = UserPost(title=form.title.data, user_id=10)
        
        
        try:
            # Add Listing to the database
            db.session.add(listing)
            db.session.commit()
            flash('Please proceed to add books to your listing')
            return redirect(url_for('home.add_books_to_list'))

        except:
            flash('Error, could not add listing')


    return render_template('home/listings.html', form=form, lists=lists)

@home.route('/add_books_to_list', methods=['GET', 'POST'])
@login_required
def add_books_to_list():
    """
    Add books to our list
    """
    form = AddBooksToList()
    if form.validate_on_submit():
        books = PostedBook(book_title=form.BookTitle.data,
                          book_author=form.BookAuthors.data,
                          book_grade=form.BookGrade.data,
                          book_publisher=form.BookPublisher.data,
                          book_subject=form.BookSubject.data,
                          book_price=form.BookPrice.data,
                          user_id=10,
                          post_id=10
                          )
        try:
            # listing to the database
            db.session.add(books)
            db.session.commit()
            flash('You have successfully listed a book')
            return redirect(url_for('home.show_listing_details'))
        except:
            flash('Error, could not add book to list')
        
        # Take user to their listings page
    return render_template('home/listings.html', form=form)

@home.route('/listings_details/<int:id>', methods=['GET', 'POST'])
@login_required
def show_listing_details(id):
    """
    Show listing
    """
    user_post = UserPost.query.filter_by(user_id=id)

    return render_template('home/list_listings.html', user_post=user_post, title='Listing details')

@home.route('/list_by_grade/<int:id>', methods=['GET', 'POST'])
def list_by_grades(id):
    """
    List all books in selected grade
    """

    #book = Book.query.all()
    book = Book.query.filter_by(grade_id=id)
    listings = BookListing.query.filter_by(grade_id=id)
        
    return render_template('home/books.html', book=book, listings=listings, title='GradeBooks')
