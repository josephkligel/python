from app import app
from app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']

    # Table of Contents: Methods
    # get_all
    # get_user_by_email
    # get_user_by_id
    # save
    # validate_login
    # validater_registration

    @classmethod
    def get_all(cls):
        # Query to select all records from users table
        query = 'SELECT * FROM users;'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('sightings_schema').query_db(query)
        # Create a user list and append instances of users
        users = [cls(result) for result in results]

        return users

    @classmethod
    def get_by_email(cls, data):
        # Query to select records of users by email column
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        # Retreive results using the data parameter passed into the method
        results = connectToMySQL('sightings_schema').query_db(query, data)
        # Return a instance of the first result. Only one record is needed since the email is/should be unique
        record = cls(results[0]) if results else None
        
        return record

    @classmethod
    def get_by_id(cls, id):
        # Query to select record by id
        query = 'SELECT * FROM users WHERE id = %(id)s'
        # Retreive record from database
        results = connectToMySQL('sightings_schema').query_db(query, {'id': id})
        record = cls(results[0]) if results else None

        return record

    @classmethod
    def save(cls, data):
        # Insert query to create a new record in the users table
        query = """
            INSERT INTO users
            (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        # Send query to database and get id number returned
        id = connectToMySQL('sightings_schema').query_db(query, data)
        # Return id of the new record created
        return id

    @staticmethod
    def validate_login(user):
         # Valid flag set to True
        is_valid = True
        # Email regex to check emails on the back-end. Input email will check the email on the front-end
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # Get record of user by email
        record_by_email = User.get_by_email(user)
        # Check for blank fields in the user parameter
        for item in user:
            if len(user[item]) <= 0:
                flash(f'Blank fields!', 'login')
                is_valid = False
                # Return is_valid. User should fill blanks before other errors in form are checked
                return is_valid
        # Check email validity of user's email
        if not EMAIL_REGEX.match(user['email']):
            flash('Email is invalid!', 'login')
            is_valid = False
        # Check user's password length
        if len(user['password']) < 8:
            flash('Password has to be 8 characters or more!', 'login')
            is_valid = False
        # Check if email is present in users table
        if not record_by_email:
            flash('Invalid credentials!', 'login')
            is_valid = False
            return is_valid
        # Check if password is correct
        if not bcrypt.check_password_hash(record_by_email.password, user['password']):
            flash('Invalid credentials!', 'login')
            is_valid = False
            return is_valid
        # If is_valid has not been returned by now then method will return it now
        return is_valid

    @staticmethod
    def validate_registration(user):
        # Valid flag set to True
        is_valid = True
        # Email regex
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # Get user by email. Email comes from the user data passed into this method
        record_by_email = User.get_by_email(user)
        # Check for blank fields
        for key in user:
            if len(user[key]) <= 0:
                flash('Blank fields!', 'registration')
                is_valid = False
                return is_valid
        # Check first name is letters only
        if not user['first_name'].isalpha():
            flash('First Name needs to be letters only!', 'registration')
            is_valid = False
        # Check first name is two characters or more
        if len(user['first_name']) < 2:
            flash('First Name needs to be 2 letters or more!', 'registration')
            is_valid = False
        # Check last name is letters only
        if not user['last_name'].isalpha():
            flash('Last Name needs to be letters only!', 'registration')
            is_valid = False
        # Check last name is two characters or more
        if len(user['last_name']) < 2:
            flash('Last Name needs to be 2 letters or more!', 'registration')
            is_valid = False
        # Check email is valid
        if not EMAIL_REGEX.match(user['email']):
            flash('Email is invalid!', 'registration')
            is_valid = False
        # Check if email already exists in database
        if record_by_email:
            flash('Email address already exists. Please use another email address', 'registration')
            is_valid = False
        # Check password is 8 characters or more
        if len(user['password']) < 8:
            flash('Password must be 8 characters or more!', 'registration')
            is_valid = False
        # Check if password has digits and uppercase letter
        if not any(ch.isdigit() for ch in user['password']):
            flash('Password must contain at least one number!', 'registration')
            is_valid = False
        if not any(ch.isupper() for ch in user['password']):
            flash('Password must contain at least one uppercase letter!', 'registration')
            is_valid = False
        # Check password confirmation
        if user['password-confirm'] != user['password']:
            flash('Passwords do not match!', 'registration')
            is_valid = False

        return is_valid


