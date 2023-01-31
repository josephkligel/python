# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the ninja table from our database

class Ninja:

    def __init__(self, data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']

 # Get all ninjas from database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        # Connect to database by creating a MySQLConnection 
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query)

        ninjas = []
        # Iterate through results and creat a Dojo instances of each iteration
        for ninja in results:
            ninjas.append(cls(ninja))
        # Return list of dojos
        return ninjas

    # Get Ninja by id
    @classmethod
    def get_ninja_by_id(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"

        result = connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)

        return result[0]

    # Get all ninjas at a certain dojo location
    @classmethod
    def get_ninjas_by_dojo_id(cls, data):
        # Create query
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        # Get results and return them
        return connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)

    # class method to save our ninja to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id, created_at ) VALUES ( %(fname)s , %(lname)s , %(age)s, %(did)s , NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)

    # Update ninja
    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s, updated_at = NOW(), dojo_id = %(dojo_id)s WHERE id = %(id)s;"

        return connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)

    # Delete ninja
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        # Return result of deletion
        return connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)