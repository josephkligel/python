# A cursor is an object used to interact with a database
import pymysql.cursors
# Pymysql Class to create connection instances
class MySQLConnection:
    
    def __init__(self, db):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            db = db,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True
        )

    # The method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                # INSERT queries will return the ID NUMBER of the row inserted
                cursor.execute(query, data)
                if query.lower().find('insert') >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                elif query.lower().find('select') >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print('Something went wrong', e)
                return False
            finally:
                # Close the connection
                self.connection.close()

# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

