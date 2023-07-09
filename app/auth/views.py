# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add a user to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email_address=form.email_address.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                phone_number=form.phone_number.data,
                password=form.password.data,
                username=form.email_address.data,
                gender=form.gender.data)

        # ADd user to the database
        db.session.add(user)
        db.session.commit()
        flash('You  have signed up successfully! Please login now.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load the registration template
    return render_template('auth/register.html', form=form, title='Register')

                
