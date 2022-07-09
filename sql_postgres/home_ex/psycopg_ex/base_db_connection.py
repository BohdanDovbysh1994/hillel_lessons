import psycopg2


class BaseDbConnection:
    def __init__(self):
        self._connection = psycopg2.connect(
            user='postgres',
            password="123",
            host="127.0.0.1",
            port='5432',
            database='testdb'
        )
        self._cursor = self._connection.cursor()
        # self.db_name = ''

    def __del__(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()

    # def get_all(self):
    #     self._cursor.execute(f'select * from {self.db_name};')
    #     return self._cursor.fetchall()
