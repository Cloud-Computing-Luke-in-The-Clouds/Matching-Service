import pymysql
from .BaseDataService import DataDataService

class MySQLRDBDataService(DataDataService):
    """
    A generic data service for MySQL databases. The class implements common
    methods from BaseDataService and other methods for MySQL. More complex use cases
    can subclass, reuse methods and extend.
    """

    def __init__(self, context):
        super().__init__(context)

    def _get_connection(self):
        try:
            connection = pymysql.connect(
                host=self.context["host"],
                port=self.context["port"],
                user=self.context["user"],
                passwd=self.context["password"],
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
            )
            print("Connection to MySQL database established successfully.")
            return connection
        except pymysql.Error as e:
            print(f"Error connecting to MySQL database: {e}")
            raise

    def test_connection(self):
        """
        Test the database connection.
        """
        try:
            connection = self._get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                if result and result['1'] == 1:
                    print("Connection test successful.")
                    return True
                else:
                    print("Connection test failed: Unexpected query result.")
                    return False
        except Exception as e:
            print(f"Connection test failed: {e}")
            return False
        finally:
            if 'connection' in locals() and connection:
                connection.close()

    def get_data_object(self,
                        database_name: str,
                        collection_name: str,
                        key_field: str,
                        key_value: str):
        """
        See base class for comments.
        """
        connection = None
        result = None

        try:
            sql_statement = f"SELECT * FROM {database_name}.{collection_name} " + \
                        f"WHERE {key_field}=%s"
            connection = self._get_connection()
            with connection.cursor() as cursor:
                cursor.execute(sql_statement, [key_value])
                result = cursor.fetchone()
            print(f"Query executed successfully: {sql_statement}")
            return result
        except pymysql.Error as e:
            print(f"Database error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
        finally:
            if connection:
                connection.close()