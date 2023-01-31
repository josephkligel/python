from app.config.mysqlconnection import connectToMySQL
from app.models.user import User
from flask import flash

class Sighting:

    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.details = data['details']
        self.date_of_sighting = data['date_of_sighting']
        self.number_of_sasquatches = data['number_of_sasquatches']
        self.created_at = data['created_at']
        self.users_id = data['users_id']

        self.user = None

    # Table of Contents: Methods
    # delete
    # get_all
    # get_recipe_by_id
    # save
    # validate_sighting

    @classmethod
    def delete(cls, id):
        # Query to delete record by id
        query = 'DELETE FROM sightings WHERE id = %(id)s;'
        # Send query
        connectToMySQL('sightings_schema').query_db(query, {'id': id})

        return None

    @classmethod
    def get_all(cls):
        # Query to select all records from sightings table
        query = """
            SELECT * FROM sightings
            LEFT JOIN users ON sightings.users_id = users.id
        """
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('sightings_schema').query_db(query)
        # Create a user list and append instances of sightings
        sightings = [cls(result) for result in results]
        # Zip through sightings and results and create a user for each recipe using user information in results
        for row, recipe in zip(results, sightings):
            recipe.user = User({
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at']
            })

        return sightings

    @classmethod
    def get_by_id(cls, id):
        # Query to select sighting by id
        # query = 'SELECT * FROM sightings WHERE id = %(id)s;'
        query = """
            SELECT * FROM sightings
            LEFT JOIN users ON sightings.users_id = users.id
            WHERE sightings.id = %(id)s;
        """
        # Create connection and retreive record
        results = connectToMySQL('sightings_schema').query_db(query, {'id': id})
        sighting = cls(results[0]) if results else None
        # Zip through sightings and results and create a user for each sighting using user information in results
        for row in results:
            sighting.user = User({
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at']
            })

        return sighting

    @classmethod
    def save(cls, data):
        # Insert query to create a new record in the sightings table
        query = """
            INSERT INTO sightings
            (location, details, date_of_sighting, number_of_sasquatches, created_at, users_id)
            VALUES (%(location)s, %(details)s, %(date_of_sighting)s, %(number_of_sasquatches)s, NOW(), %(users_id)s)
        """
        # Send query to database and get id number returned
        id = connectToMySQL('sightings_schema').query_db(query, data)
        # Return id of the new record created
        return id

    @classmethod
    def update(cls, data):
        # Query to update recipe
        query = """
            UPDATE sightings
            SET 
                location = %(location)s, details = %(details)s, date_of_sighting = %(date_of_sighting)s,
                number_of_sasquatches = %(number_of_sasquatches)s WHERE id = %(id)s;
        """
        # Send query to database
        connectToMySQL('sightings_schema').query_db(query, data)

        return None

    @staticmethod
    def validate_sighting(sighting):
        # Valid flag set to True
        is_valid = True
        # Check for blank fields in the recipe
        for item in sighting:
            if len(sighting[item]) <= 0:
                flash('Blank fields!')
                is_valid = False
                # Return is_valid
                return is_valid
        # number_of_sasquatches must be 1 or more      
        if int(sighting['number_of_sasquatches']) < 1:
            flash('The # of Sasquatches field must be 1 or more!')
            is_valid = False

        # If is_valid has not been returned by now then method will return it
        return is_valid


