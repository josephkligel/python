from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    # Get all dojos from database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        # Connect to database by creating a MySQLConnection 
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query)

        dojos = []
        # Iterate through results and creat a Dojo instances of each iteration
        for dojo in results:
            dojos.append(cls(dojo))
        # Return list of dojos
        return dojos

    # Save new data to table
    @classmethod
    def save(cls, data):
        # Create query
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(dname)s, NOW(), NOW());"
        # Return connection to mysql database and query answer
        return connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)

    # Get dojo record by id number
    @classmethod
    def get_dojo_by_id(cls, data):
        # Create query
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        # Get and return result
        return connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)

    # Get ninjas from dojo using left join
    @classmethod
    def get_one(cls, id):
        # Query to get ninjas using a dojo's id
        query = """
            SELECT
                *
            FROM dojos
                LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(id)s;
        """
        # Assigning ninjas to a list
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query, {'id': id})
        # Break out of function early if there are no ninjas
        if not results:
            return None
        # Create dojo instance from first result of ninjas
        dojo = cls(results[0])

        for row in results:
            if row['ninjas.id']:
                dojo.ninjas.append(Ninja(
                    {
                        'id': row['ninjas.id'],
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'age': row['age'],
                        'created_at': row['ninjas.created_at']
                    }
                ))
        
        return dojo