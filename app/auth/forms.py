# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Equalto

from ..models import Employee

class RegistrationForm(FlaskForm):
    """
    Form for registering new accounts
    """

    email_address = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = Submitfield('Register')

    def validate_email(self, field):
        if User.query.filter.filter_by(email_address=field.data).first():
            raise ValidationError('Email is already in use.')


class LoginForm(FlaskForm):
    """
    User Log in form
    """
    email_address = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
