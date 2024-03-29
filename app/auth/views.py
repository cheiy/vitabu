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
                        gender='unknown')

        # Add user to the database
        db.session.add(user)
        db.session.commit()
        flash('You have signed up sucessfully! Please login now.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

     # load registration template
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log a user in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

      # check whether the user exists in the database and whether
      # the password entered matches the password in the db
        user = User.query.filter_by(email_address=form.email_address.data).first()
        if user is not None and user.verify_password(
             form.password.data):
           # log user in
           login_user(user)

           #redirect to the appropriate dashboard page after login
           if user.is_admin:
               return redirect(url_for('home.admin_dashboard'))
           else:   
               return redirect(url_for('home.dashboard'))

         # when login details are incorrect
        else:
             flash('Invalid email or password.')
      # load login template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log a user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))

