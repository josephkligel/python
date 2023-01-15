from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.object import Object

class Favorite(Object):

        def __init__(self, data, *args, **kwargs):

            super().__init__(*args, **kwargs)

            self.id = data['id']
            self.book_id = data['book_id']
            self.author_id = data['author_id']
