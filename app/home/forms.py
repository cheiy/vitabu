# app/home/forms.py
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from ..models import Grade, Publisher

class BookSearchForm(FlaskForm):
    choices = [('Title','Title'),
               ('Subject','Subject'),
               ('Publisher','Publisher'),
               ('Grade','Grade/Class'),
               ('Author','Author'),
               ('ISBN','ISBN')]
    buy_exchange_both = [('For sale Only', 'For Sale Only'),
                         ('Exchange Only', 'Exchange Only'),
                         ('For Sall or Exchange', 'For Sale or Exchange')]
    select = SelectField('Search for book by Title, Subject, Publisher, Grade, Author or ISBN Number:', choices=choices)
    select2 = SelectField('For Sale, Exchange or Both Sale and Exchange', choices=buy_exchange_both)
   # search = StringField('',render_kw={"placeholder":"search by Title, Subject, Grade"})
    search = StringField('Enter Search Term')
    submit = SubmitField('Submit')


class AddListingForm(FlaskForm):
    title = StringField('Enter Post Name')
    submit = SubmitField('Add Listing')
    
class AddBooksToList(FlaskForm):
     BookTitle = StringField('Enter Book Title')
     BookAuthors = StringField('Enter Book Author(s), separated by commas')
     BookGrade = StringField("Enter Grade")
     #BookGrade = QuerySelectField(query_factory=lambda: Grade.query.all(), get_label="grade_name")
     BookPublisher = QuerySelectField(query_factory=lambda: Publisher.query.all(), get_label="longname")
     BookSubject = StringField("Enter Book's Subject")
     BookPrice = StringField("Enter Book's Price")
     Submit = SubmitField('Add Book Details')
