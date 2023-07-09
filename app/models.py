# app/models.py
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Users Table
    """
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255), index = True, unique = True)
    username = db.Column(db.String(50), index=True)
    first_name = db.Column(db.String(100), index=True)
    last_name = db.Column(db.String(100), index=True)
    password_hash = db.Column(db.String(512), default=False)
    phone_number = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False)
    publishers = db.relationship('Publisher', backref='user', lazy='dynamic')
    listings = db.relationship('Listing', backref='user', lazy='dynamic')

    def get_id(self):
        """
        Retun the email address to satisfy Flask-Login's requirements
        """
        return self.user_id


    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('Password is not a readable attribute.')


    @password.setter
    def password(self, password):
        """
        Set password to a hashed value
        """
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        """
        Check if the hashed password matches the actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# user_loader setup
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Books Model
class Book(db.Model):
    """
    Books Table
    """
    __tablename__ = 'books'

    book_id = db.Column(db.BigInteger, primary_key = True)
    isbn_code = db.Column(db.BigInteger, unique=True)
    title = db.Column(db.String(255))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.publisher_id'))
    grade_id = db.Column(db.Integer, db.ForeignKey('grades.grade_id'))


    def get_id(self):
        return self.book_id

    def __repr__(self):
        return '<Book Title: {}>'.format(self.title)


class Publisher(db.Model):
    """
    Publishers Table
    """
    
    __tablename__ = 'publishers'

    publisher_id = db.Column(db.Integer, primary_key = True)
    shortname = db.Column(db.String(50), unique = True)
    longname = db.Column(db.String(100), unique = True)
    ISBN_code = db.Column(db.BigInteger, unique = True)
    added_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date_added = db.Column(db.TIMESTAMP, unique = True)
    books = db.relationship('Book', backref='bookpub', lazy='dynamic')

    def get_id(self):
        return self.publisher_id
    
    def __repr__(self):
        return "<Publisher's Name: {}>".format(self.longname)


class Grade(db.Model):
    """
    Grades Table
    """

    __tablename__ = 'grades'

    grade_id = db.Column(db.Integer, primary_key = True)
    grade_num = db.Column(db.Integer, unique = True)
    grade_name = db.Column(db.String(100), unique = True)
    books = db.relationship('Book', backref='book', lazy='dynamic')

    def get_id(self):
        self.id = self.grade_id
        return self.id

    def __repr__(self):
        return '<Grades: {}>'.format(self.grade_name)


class Subject(db.Model):
    """
    Subjects Table
    """

    __tablename__ = 'subjects'

    subject_id = db.Column(db.Integer, primary_key = True)
    subject_name = db.Column(db.String(128), unique = True)
    books = db.relationship('Book', backref='subjectbook', lazy='dynamic')

    def get_id(self):
        return self.subject_id
    
    def __repr__(self):
        return '<Subject: {}>'.format(self.subject_name)


class Author(db.Model):
    """
    Authors Table
    """

    __tablename__ = 'authors'

    author_id = db.Column(db.Integer, primary_key = True)
    author_name = db.Column(db.String(255))
    book_authors = db.relationship('BookAuthor', backref='author', lazy='dynamic')

    def get_id(self):
        return self.author_id

    def __repr__(self):
        return '<Author: {}'.format(self.author_name)


class Listing(db.Model):
    """
    Listings Table
    """

    __tablename__ = 'listings'

    listing_id = db.Column(db.BigInteger, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def get_id(self):
        return self.listing_id

    def __repr__(self):
        return '<Listing: {}'.format(self.listing_id)

class BookAuthor(db.Model):
    """
    Books to Authors Table
    """

    __tablename__ = 'book_authors'

    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'), primary_key=True)
    book_id = db.Column(db.BigInteger, db.ForeignKey('books.book_id'), primary_key = True)

    def __repr__(self):
        return '<Book_ID: {}  <--> Author_ID {}'.format(self.book_id, self.author_id)


class BookListing(db.Model):
    """
    User to Listings Table
    """

    __tablename__ = 'book_listings'

    book_id = db.Column(db.BigInteger, db.ForeignKey('books.book_id'), primary_key = True)
    listing_id = db.Column(db.BigInteger, db.ForeignKey('listings.listing_id'), primary_key = True)

    def __repr__(self):
        return '<Listing_ID: {} <--> User_ID {}'.format(self.listing_id, self.user_id)
