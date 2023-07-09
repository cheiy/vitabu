# /app/home/forms.py
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


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
    search = StringField('Type search terms here', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddListingForm(FlaskForm):
     BookTitle = StringField('Enter Book Title')
     Submit = SubmitField('Submit')
