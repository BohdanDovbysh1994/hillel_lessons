import psycopg2

try:
    connection = psycopg2.connect(
        user='postgres',
        password="123",
        host="127.0.0.1",
        port='5432',
        database='testdb'
    )

    cursor = connection.cursor()

    cursor.execute('select * from profiles;')

    for row in cursor.fetchall():
        print(row)
except Exception:
    cursor.close()
    if connection:
        connection.close()
from users_repository import UsersRepository

print(UsersRepository().get_all())
