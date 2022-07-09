from sql_python_lesson.base_db_connection import BaseDbConnection


class UserRepository(BaseDbConnection):
    def __init__(self):
        super().__init__()
        self.table_name = 'users'

    # def get_all(self):
    #     self._cursor.execute('select * from users;')
    #     return self._cursor.fetchall()

    def get_by_name(self, name):
        self._cursor.execute(f"select * from users where users.name = '{name}';")
        return self._cursor.fetchone()

    def insert_one(self, name: str, age: int, email: str):
        self._cursor.execute("insert into users (name, age, email) values (%s, %s, %s);", (name, age, email))
        self._connection.commit()

    def delete_by_email(self, email):
        self._cursor.execute("delete from users where users.email=%s;", (email,))
        self._connection.commit()

    def __del__(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()
