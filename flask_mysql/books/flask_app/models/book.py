from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.object import Object


class Book(Object):
     
     def __init__(self, data, *args, **kwargs):
         super().__init__(*args, **kwargs)
         
         self.id = data['id']
         self.title = data['title']
         self.num_of_pages = data['num_of_pages']
         self.created_at = data['created_at']
