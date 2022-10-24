import mysql.connector as connection
import pandas as pd

# It connects to a database, creates a cursor, and then executes a query.

class Data_Bd:

    def __init__(self):

        # It connects to the database and creates a cursor object

        self.mydb = connection.connect(
            host="localhost",
            database='practica',
            user="root",
            passwd="1234567",
            use_pure=True)

    def get_InfoDb(self):

        query = """
            SELECT
                   *
            FROM
                datos
            """
        result_dataFrame = pd.read_sql(query, self.mydb)
        return result_dataFrame
