import configparser


class PropertyUtil:
    @staticmethod
    def getPropertyString():
        """
        Reads database properties from a configuration file and returns the connection string.
        """
        config = configparser.ConfigParser()
        config.read('db.properties')

        # Extract the necessary properties
        host = config.get('database', 'hostname')  # e.g., localhost\\SQLEXPRESS
        dbname = config.get('database', 'dbname')  # e.g., HospitalDataBase

        # Build the connection string using the desired format
        return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={host};Database={dbname};Trusted_Connection=yes;"
