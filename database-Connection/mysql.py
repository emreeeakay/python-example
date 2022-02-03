import pymysql


class mysqlConnector:
    db = ''

    def __init__(self):
        db = pymysql.connect("localhost", "root", "", "deneme")

    def mysqlVersion(self):
        cursor = self.db.cursor()

        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print("Database version : %s " % data)

    def closeConnection(self):
        self.db.close()
