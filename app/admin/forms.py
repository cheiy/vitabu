# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from ..models import  Grade
from app import db
# Add Publisher Form
class PublisherForm(FlaskForm):
    """
    Form for admin to add or edit a publisher
    """
    shortname = StringField('ShortName', validators=[DataRequired()])
    longname = StringField('LongName', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Add Book Form
class AddBookForm(FlaskForm):
    """
    Form for admin to add or edit a book
    """
    isbn_code = StringField('ISBNCode', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    publisher_id = SelectField(u'Publisher', coerce=int)
    #publisher_id = StringField('Publisher', validators=[DataRequired()])
    grade_id = SelectField(u'Grade', coerce=int)
   # grade_id = SelectField(u'Grade', coerce=int)
   # subject_id = StringField('Subject', validators=[DataRequired()])
    subject_id = SelectField(u'Subject', coerce=int)
    submit = SubmitField('Submit')
   


# Add Grade Form
class AddGradeForm(FlaskForm):
    """
    Form for admin to add or edit a Grade/Class
    """
    grade_num = StringField('grade_num', validators=[DataRequired()])
    grade_name = StringField('grade_name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Add Subject Form
class AddSubjectForm(FlaskForm):
    """
    Form for admin to add or edit a Subject/Learning Area
    """
    subject_name = StringField('subject_name', validators=[DataRequired()])
    submit = SubmitField('Submit')
