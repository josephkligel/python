from flask_app.config.mysqlconnection import connectToMySQL


class Object:

    # def __init__(self):
    #     super()

    @classmethod
    def get_all(cls):
        query = f'SELECT * FROM {cls.__name__.lower() + "s"};'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("books_schema").query_db(query)
        # Create an empty list to append our instances of the objects passed
        records = [cls(result) for result in results]

        return records

    @classmethod
    def get_records_by_id(cls, data):
        # Query for getting one record by id
        query = f'SELECT * FROM {cls.__name__.lower() + "s"} WHERE id = %(id)s;'
        print(query)
        # The first record from the list
        results = connectToMySQL('books_schema').query_db(query, data)
        # Instantiate class object for each item in results
        records = [cls(result) for result in results]

        return records

    @classmethod
    def get_records_by_type(cls, type, data):
        # Query for getting records by column name
        query = f'SELECT * FROM {cls.__name__.lower() + "s"} WHERE {type} = %(id)s;'
        # Retrieving records
        results = connectToMySQL('books_schema').query_db(query, data)
        
        records = [cls(result) for result in results]

        return records

    @classmethod
    def save(cls, data):
        # Get table name from class name
        table_name = cls.__name__.lower() + "s"
        # Create generic query to be used for any class data
        column_names = data.keys()
        first_part_query = ', '.join(column_names)
        second_part_query = ', '.join([f'%({name})s' for name in column_names])
        query = (f'INSERT INTO {table_name}'
            f' ({first_part_query})'
            f' VALUES ({second_part_query});'
        )
        print(query)
        
        return connectToMySQL('books_schema').query_db(query, data)