import pyodbc


class DBConnection:
    @staticmethod
    def getConnection():
        """
        Returns a connection object using the defined connection string.
        """
        # Updated connection string for Hospital Management project
        conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;Database=HospitalDataBase;Trusted_Connection=yes;'

        try:
            connection = pyodbc.connect(conn_string)
            print("Database connection successful.")
            return connection
        except pyodbc.Error as e:
            print("Database connection error:", e)
            return None
