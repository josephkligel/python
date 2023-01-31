from app import app
from app.models.user import User
from flask import render_template, request, redirect, session
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
   
    # Validate registration form data. If data is not valid, return to home page
    if not User.validate_registration(request.form):
        return redirect('/')

    # Hash password from registration form if password is valid
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # Else if correct save new user data, save id in session, and redirect to dashboard
    # Put the registration form and hashed password data into a dictionary
    data = {k: v for k,v in request.form.items()}
    data['password'] = pw_hash
    user_id = User.save(data)
    session['users_id'] = user_id
    return redirect('/recipes')
        

@app.route('/login', methods=['post'])
def login():
    user_in_db = User.get_user_by_email({'email': request.form['email']})
    # Validate login information. I put the password checking in user.py instead including it here. Just felt more natural
    if not User.validate_login(request.form):
        # Go user information is invalid redirect to home page
        return redirect('/')
    # If user is valid and in the database, save user's id to session and redirect to dashboard
    session['users_id'] = user_in_db.id
    return redirect('/recipes')

@app.route('/logout')
def logout():
    # When logout link is clicked, session is deleted
    session.clear()
    return redirect('/')
