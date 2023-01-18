from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session
import hashlib

# Global flag for checking whether or not flash messages are displayed on registration or login form
login_check = False

# Function to hash password with md5 encryption
def hash_password(pw):
    pw = pw.encode()
    hashedpw = hashlib.md5(pw)
    return hashedpw.hexdigest()

@app.route('/')
def index():
    # Create and assign registration variable storing registration form data
    registration = session['registration'] if session.get('registration') else None
    session['registration'] = None
    # Creat and assign login form variable
    login = session['login'] if session.get('login') else None
    session['login'] = None
    # Bringing in global variable
    global login_check
    return render_template('index.html', registration = registration, login = login, login_check = login_check)

@app.route('/register_user', methods=['POST'])
def register_user():
    # Save registration form data in session
    session['registration'] = request.form
    # Validate registration form data
    if User.validate_registration(request.form):
        # Put elements from request.form into a mutable dictionary
        data = {k: v for k,v in request.form.items()}
        # Hash password
        data['password'] = hash_password(data['password'])
        # Save user data
        User.save(data)
        data_dict = {'email': request.form['email']}
        session['user'] = User.get_user_by_email(data_dict)
        print(session['user'])
        # Create logged_in session variable
        session['logged_in'] = True
        # Redirect to success page if information was added to the database successfully
        return redirect('/success')
    else:
        # If form data is not valid redirect to home page
        return redirect('/')

@app.route('/login_user', methods=['post'])
def login():
    # Save login information to session['login']
    session['login'] = request.form
    # Validate login information
    if User.validate_login(request.form):
        # Get data os user from database and save it to session['user']
        session['user'] = User.get_user_by_email({'email': request.form['email']})
        # Create logged_in flag
        session['logged_in'] = True
        # Go to success page if user has been validated
        return redirect('/success')
    else:
        # Bring in global login_check flag
        global login_check
        login_check = True
        return redirect('/')

@app.route('/success')
def success():
    # If logged_in flag exists render success page
    if 'logged_in' in session:
        user = session['user']
        return render_template('success.html', user = user)
    # If logged_in flag does not exist return not logged in message
    else:
        return "You are not logged in"

@app.route('/logout')
def logout():
    # When logout button is pressed, session is deleted
    session.clear()
    return redirect('/')
