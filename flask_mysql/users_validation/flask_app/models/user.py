# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# Importing flash to validate and show requirements for user parameters
from flask import flash
import re
# model the class after the friend table from our database

class User:

    def __init__(self, data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.full_name = self.first_name + ' ' + self.last_name
        self.email = data['email']
        self.created_at = data['created_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances
        for user in results:
            users.append(cls(user))

        return users

    # class method to save our user to the database
    @classmethod
    def save(cls, data):
                query = "INSERT INTO users ( first_name , last_name , email , created_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW());"
                # data is a dictionary that will be passed into the save method from server.py
                return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_record_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('users_schema').query_db(query, data)
        
        return result

    @classmethod
    def update_record(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name= %(lname)s, email = %(email)s, updated_at = NOW(), dojo_id = %(dojo_id)s WHERE id = %(id)s"

        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete_record(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"

        return connectToMySQL('users_schema').query_db(query, data)

    @staticmethod
    def validate_user(user):
        is_valid = True # Set to True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        all_users = User.get_all()
        # Checking all fields for blanks
        for item in user.values():
            if len(item) <= 0:
                flash("There are blank field!")
                is_valid = False
                return is_valid
        # Checking email is valid
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        # Check if email is unique
        for individual_user in all_users:
            if(individual_user.email == user['email']):
                flash(f"Email address {individual_user.email} is already in use")
                is_valid = False
        
        return is_valid
        

