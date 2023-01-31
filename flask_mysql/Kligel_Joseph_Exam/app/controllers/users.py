from app import app
from app.models import user
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt

# Setup bcrypt object
bcrypt = Bcrypt(app)

# Table of Contents: users' app routes and functions
# Route index
# Route login
# Route logout
# Route register

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Get user in database by email field
    user_in_db = user.User.get_by_email({'email': request.form['email']})
    # Validate login information. Password checking with bcrypt is users.py
    if not user.User.validate_login(request.form):
        # If user information is invalid redirect to home page and display flash messages
        return redirect('/')
    # If user is valid and in the database, save user's id to session and redirect to dashboard
    session['user_id'] = user_in_db.id

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    # When logout link is clicked, session is deleted
    session.clear()

    return redirect('/')

@app.route('/register', methods=['POST'])
def register(): 
    # Validate registration form data. If data is not valid, return to home page
    if not user.User.validate_registration(request.form):
        return redirect('/')
    # If valid hash password from registration form
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # Put the registration form and hashed password data into a dictionary
    data = {k: v for k,v in request.form.items()}
    # Add hashed password to dictionary
    data['password'] = pw_hash
    # Save dictionary data
    user_id = user.User.save(data)
    # Save session to detect user's id
    session['user_id'] = user_id

    return redirect('/dashboard')