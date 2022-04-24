# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import enum,  os
from sqlalchemy.sql import func

from app import db, login_manager

class User(UserMixin, db.Model):

      __tablename__ = 'users' 
    
      user_id = db.Column(db.Integer, primary_key=True)
      email_address = db.Column(db.String(255),  index=True, unique=True)
      username = db.Column(db.String(50), index=True)
      first_name = db.Column(db.String(100), index=True)
      last_name = db.Column(db.String(100), index=True)
      password_hash = db.Column(db.String(512), default=False)
      phone_number = db.Column(db.Integer)
      gender = db.Column(db.String(50))
      is_admin = db.Column(db.Boolean, default=False)

      def get_id(self):
        #Return the email address to satisfy Flask-Login's requirements
        return self.user_id

      

      @property
      def password(self):
         """
         Prevent password from being accessed
         """
         raise AttributeError('password is not a readable attribute.')


      @password.setter
      def password(self, password):
         """
         Set password to a hashed value
         """
         self.password_hash = generate_password_hash(password)

      def verify_password(self, password):
         """
         Check if hashed password matches actual password
         """
         return check_password_hash(self.password_hash, password)

      def __repr__(self):
         return '<User: {}>'.format(self.username)

"""class Subject(UserMixin, db.Model):
        Create an Subjects table 
    

    __tablename__ = 'subjects'
   
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(128), index=True, unique=True)
"""
# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Publisher(db.Model):
 
  # Publishers table

   __tablename__ = 'publishers'

   publisher_id = db.Column(db.Integer, primary_key=True)
   shortname = db.Column(db.String(50), unique=True)
   longname = db.Column(db.String(100), unique=True) 
   ISBN = db.Column(db.Integer, unique=True)

   #Return the publisher_id satisfy Flask-Login's requirements
   
   def get_id(self):
        return self.publisher_id
   


   def __repr__(self):
        return '<Publisher: {}>'.format(self.name) 

# Books Model
class Book(db.Model):
   """
   Class Table
   """
   __tablename__ = 'books'


   book_id = db.Column(db.Integer, primary_key = True)
   isbn_code = db.Column(db.Integer(), unique=True) 
   title = db.Column(db.String(255), unique=True)
   publisher_id = db.Column(db.Integer)
   grade_id = db.Column(db.Integer)
   subject_id = db.Column(db.Integer)



   def get_id(self):
       return self.book_id


   def __repr__(self):
       return '<Books: {}>'.format(self.name)

# Grades Model
class Grade(db.Model):
   """
   Class Table
   """
   __tablename__ = 'grades'

   grade_id = db.Column(db.Integer, primary_key = True)
   grade_num = db.Column(db.Integer, unique = True)
   grade_name = db.Column(db.String(100), unique = True)


   def get_id(self):
       return self.grade_id

   def __repr__(self):
       return '<Grades: {}>'.format(self.name)

# Subjects Model
class Subject(db.Model):
   """
   Subject Table
   """
   __tablename__ = 'subjects'

   id = db.Column(db.Integer, primary_key = True)
   subject_name = db.Column(db.String(128), unique = True)

# Enum for sell, exchange or willing to do both
class ListOptions(enum.Enum):
      SELL = "sell"
      EXCHANGE = "exchange"
      BOTH = "sell or exchange"


# Listed Books Model
class ListedBook(db.Model):
   __tablename__ = 'listed_books'

   listing_id = db.Column(db.Integer, primary_key = True)
   listed_by = db.Column(db.BigInteger(), db.ForeignKey('users.user_id'))
   book_title = db.Column(db.String(255), nullable = False)
   options = db.Column(db.Enum(ListOptions), nullable = False)
   price = db.Column(db.Integer)
   book_condition = db.Column(db.String(255), nullable = False)
   publisher_id = db.Column(db.BigInteger(), db.ForeignKey('publishers.publisher_id'))
   grade_id = db.Column(db.Integer(), db.ForeignKey('grades.grade_id'))
   quantity = db.Column(db.Integer, nullable = False)
   listing_date = db.Column(db.DateTime(), server_default=func.now())

   def __repr__(self):
       return f'<Listed Book {self.listed_by}>'



# Uploaded Images Model
class UploadedImage(db.Model):
   __tablename__ = 'book_images'

   image_id = db.Column(db.Integer, primary_key = True)
   listing_id = db.Column(db.Integer(), db.ForeignKey('listed_books.listing_id'))
   image_path = db.Column(db.String(255), unique = True)
   image_size = db.Column(db.Integer)
   uploaded_by = db.Column(db.BigInteger(), db.ForeignKey('users.user_id'))

   def __repr__(self):
       return f'<Image Path {self.image_path}>'
