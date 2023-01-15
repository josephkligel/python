from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.object import Object

class Author(Object):

    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
