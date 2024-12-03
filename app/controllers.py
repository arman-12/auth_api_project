from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import db, User
from .utils import send_verification_email, validate_email_format
from flask_mail import Mail

controllers_blueprint = Blueprint('controllers', __name__)
mail = Mail()

# Show registration form
@controllers_blueprint.route('/register', methods=['GET'])
def show_register_form():
    return render_template('register.html')

# Handle registration form submission
@controllers_blueprint.route('/register', methods=['POST'])
def register_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Validate email format
    if not validate_email_format(email):
        flash('Invalid email format.', 'danger')
        return redirect(url_for('controllers.show_register_form'))

    user_exists = User.query.filter((User.email == email) | (User.username == username)).first()
    if user_exists:
        flash('Registration unsuccessful. Please check your details and try again.', 'danger')
        return redirect(url_for('controllers.show_register_form'))

    hashed_password = User.hash_password(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Send verification email
    send_verification_email(email, mail)

    flash('If this email is valid, a verification mail has been sent.', 'success')
    return redirect(url_for('controllers.show_login_form'))

# Show login form
@controllers_blueprint.route('/login', methods=['GET'])
def show_login_form():
    return render_template('login.html')

# Handle login form submission
@controllers_blueprint.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        session['username'] = user.username
        flash('Logged in successfully!', 'success')
        return redirect(url_for('controllers.dashboard'))
    else:
        flash('Invalid email or password!', 'danger')

    return redirect(url_for('controllers.show_login_form'))

# Show dashboard
@controllers_blueprint.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('controllers.show_login_form'))

    return render_template('dashboard.html', username=session['username'])

# Handle logout
@controllers_blueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('views.home'))
