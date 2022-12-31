# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
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

