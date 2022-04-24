# /app/home/forms.py

from wtforms import Form, StringField, SelectField, SubmitField

class BookSearchForm(Form):
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
    search = StringField('')
    #submit = SubmitField('Submit')
