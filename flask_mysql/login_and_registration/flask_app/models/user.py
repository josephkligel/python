from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import hashlib

class User:
    def __init__(self, data):
        print(data)
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('login_and_registration_schema').query_db(query)
        # Create a user list to append our instances of friends
        users = [cls(result) for result in results]

        return users

    @classmethod
    def get_user_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('login_and_registration_schema').query_db(query, data)
        return results[0]

    @staticmethod
    def validate_registration(user):
        # Valid flag set to True
        is_valid = True
        # Email regex
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # Users
        all_users = User.get_all()
        # Check for blank fields
        for key in user:
            if len(user[key]) <= 0:
                flash('Blank fields!')
                is_valid = False
                return is_valid
        # Check first name
        if not user['first_name'].isalpha():
            flash('First Name needs to be letters only!')
            is_valid = False
        if len(user['first_name']) < 2:
            flash('First Name needs to be 2 letters or more!')
            is_valid = False
        # Check last name
        if not user['last_name'].isalpha():
            flash('Last Name needs to be letters only!')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last Name needs to be 2 letters or more!')
            is_valid = False
        # Check email
        if not EMAIL_REGEX.match(user['email']):
            flash('Email is invalid!')
            is_valid = False
        # Check if email already exists in database
        for a_user in all_users:
            if user['email'] == a_user.email:
                flash('Email is already in database')
                is_valid = False
        # Check password
        if len(user['password']) < 8:
            flash('Password must be 8 characters or more!')
            is_valid = False
        # Check if password has digits and uppercase letter
        if not any(ch.isdigit() for ch in user['password']):
            flash('Password must contain at least one number!')
            is_valid = False
        if not any(ch.isupper() for ch in user['password']):
            flash('Password must contain at least one uppercase letter!')
            is_valid = False
        # Check password confirmation
        if user['password-confirm'] != user['password']:
            flash('Passwords do not match!')
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(user):
         # Valid flag set to True
        is_valid = True
        # Email regex
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # Users
        all_users = User.get_all()
        # Check for blank fields
        for item in user:
            if len(user[item]) <= 0:
                flash('Blank fields!')
                is_valid = False
                return is_valid
        # Check email validity
        if not EMAIL_REGEX.match(user['email']):
            flash('Email is invalid!')
            is_valid = False
        # Check password length
        if len(user['email']) < 8:
            flash('Password has to be 8 characters or more!')
            is_valid = False
        # Check if user exists and password is correct
        # Hash user data password
        password = user['password'].encode()
        password = hashlib.md5(password).hexdigest()
        # Check all users for provided email and password
        for a_user in all_users:
            if user['email'] == a_user.email and a_user.password == password:
                is_valid = True
                return is_valid
            else:
                is_valid = False
        # Check if is_valid is still false and display flash message accordingly
        if not is_valid:
            flash('Incorrect email and/or password!')

        return is_valid

    @classmethod
    def save(cls, data):
        query = ('INSERT INTO users'
            ' (first_name, last_name, email, password) VALUES' 
            ' (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        )
        # Send query to database
        print(query)
        id = connectToMySQL('login_and_registration_schema').query_db(query, data)

        return id

        