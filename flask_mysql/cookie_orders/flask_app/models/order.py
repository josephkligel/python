from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# Class to create Order objects
class Order:

    # Initialize data from dictionary variable
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        
    # Get all order records
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM orders;'
        # Connect to cookie order database and return the results
        results = connectToMySQL('cookie_orders_schema').query_db(query)
        # List comprehension is used to create a list of order objects
        orders = [cls(order) for order in results]

        return orders

    @classmethod
    def get_record_by_id(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        result = connectToMySQL('cookie_orders_schema').query_db(query, data)[0]

        return result


    # Save order
    @classmethod
    def save(cls, data):
        query = "INSERT INTO orders (customer_name, cookie_type, num_of_boxes) VALUES (%(customer_name)s, %(cookie_type)s, %(num_of_boxes)s);"

        return connectToMySQL('cookie_orders_schema').query_db(query, data)

    # Update Order
    @classmethod
    def update(cls, data):
        query = "UPDATE orders SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, num_of_boxes = %(num_of_boxes)s, updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL('cookie_orders_schema').query_db(query, data)

    # Static validate form method
    @staticmethod
    def validate_user(order):
        # Set to True
        is_valid = True
        message_string = "{} is invalid. {} must be 2 characters or more"
        for k, v in order.items():
            if k != "id" and len(v) <= 0:
                flash("Blank fields!")
                is_valid = False
                return is_valid
        # Check customer name
        if len(order['customer_name']) < 2:
            flash(message_string.format(order['customer_name'], "Customer Name"))
            is_valid = False
        if len(order['cookie_type']) < 2:
            flash(message_string.format(order['cookie_type'], 'Cookie Type'))
            is_valid = False
        if int(order['num_of_boxes']) < 1:
            flash("The Number of Boxes must be a positive number")
            is_valid = False

        return is_valid