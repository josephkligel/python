from app.config.mysqlconnection import connectToMySQL
from app.models.user import User
from flask import flash

class Recipe:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.users_id = data['users_id']

        self.user = None

    # Table of Contents: Methods
    # delete
    # get_all
    # get_recipe_by_id
    # save
    # validate_recipe

    @classmethod
    def delete(cls, id):
        # Query to delete record by id
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        # Send query
        connectToMySQL('recipes_schema').query_db(query, {'id': id})

        return None

    @classmethod
    def get_all(cls):
        # Query to select all records from recipes table
        query = """
            SELECT * FROM recipes
            LEFT JOIN users ON recipes.users_id = users.id
        """
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes_schema').query_db(query)
        # Create a user list and append instances of recipes
        recipes = [cls(result) for result in results]
        # Zip through recipes and results and create a user for each recipe using user information in results
        for row, recipe in zip(results, recipes):
            recipe.user = User({
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at']
            })

        return recipes

    @classmethod
    def get_recipe_by_id(cls, id):
        # Query to select recipe by id
        # query = 'SELECT * FROM recipes WHERE id = %(id)s;'
        query = """
            SELECT * FROM recipes
            LEFT JOIN users ON recipes.users_id = users.id
            WHERE recipes.id = %(id)s;
        """
        # Create connection and retreive record
        results = connectToMySQL('recipes_schema').query_db(query, {'id': id})
        recipe = cls(results[0]) if results else None
        # Zip through recipes and results and create a user for each recipe using user information in results
        for row in results:
            recipe.user = User({
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at']
            })

        return recipe

    @classmethod
    def save(cls, data):
        # Insert query to create a new record in the recipes table
        query = """
            INSERT INTO recipes
            (name, description, instructions, date_cooked, under_thirty, users_id)
            VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_thirty)s, %(users_id)s)
        """
        # Send query to database and get id number returned
        id = connectToMySQL('recipes_schema').query_db(query, data)
        # Return id of the new record created
        return id

    @classmethod
    def update(cls, data):
        # Query to update recipe
        query = """
            UPDATE recipes
            SET 
                name = %(name)s, description = %(description)s, instructions = %(instructions)s,
                date_cooked = %(date_cooked)s, under_thirty = %(under_thirty)s WHERE id = %(id)s;
        """
        # Send query to database
        connectToMySQL('recipes_schema').query_db(query, data)

        return None

    @staticmethod
    def validate_recipe(recipe):
        # Valid flag set to True
        is_valid = True
        # Check for blank fields in the recipe
        for item in recipe:
            if len(recipe[item]) <= 0:
                flash('Blank fields!')
                is_valid = False
                # Return is_valid
                return is_valid
        # Name, description, and instructions must be 3 characters or more
        if len(recipe['name']) < 3:
            flash('Name must be more than 3 characters long!')
            is_valid = False
        
        if len(recipe['description']) < 3:
            flash('Description must be more than 3 characters long!')
            is_valid = False
        
        if len(recipe['instructions']) < 3:
            flash('Instructions must be more than 3 characters long!')
            is_valid = False

        # If is_valid has not been returned by now then method will return it
        return is_valid


