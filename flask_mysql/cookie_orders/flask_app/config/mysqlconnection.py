# Importing cursors for quering data from a database
import pymysql.cursors
# Creating configuration class for establishing MySQL connections
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

    # Query database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                # Commits the query automatically, no matter the query
                cursor.execute(query, data)
                # INSERT queries will return the row id of the record inserted
                if query.lower().find('insert') >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                if query.lower().find('select') >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing~
                    self.connection.commit()

            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            
            finally:
                # Always close the connection at the end of a query
                self.connection.close()

# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

