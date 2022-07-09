import psycopg2


# TODO add singleton
class UsersRepository:
    def __init__(self):
        self.__connection = psycopg2.connect(
            user='postgres',
            password="123",
            host="127.0.0.1",
            port='5432',
            database='testdb'
        )
        self.__cursor = self.__connection.cursor()
        self.db_name = 'users'

    def get_all(self):
        self.__cursor.execute('select * from users;')
        return self.__cursor.fetchall()

    def get_email(self):
        pass

    def update_one_by_email(self, email: str, name: str) -> None:
        self.__cursor.execute(f"update users set name = '{name}' where users.email = '{email}';")
        # self.__cursor.commit()
        self.__connection.commit()
