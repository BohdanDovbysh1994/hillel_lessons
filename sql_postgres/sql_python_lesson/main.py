# import psycopg2
#
# try:
#     connection = psycopg2.connect(
#         user='postgres',
#         password='123',
#         host='127.0.0.1',
#         port='5432',
#         database='testdb'
#     )
#     cursor = connection.cursor()
#
#     cursor.execute("select * from users;")
#
#     for row in cursor.fetchall():
#         c = row
#         print(row)
# except Exception:
#     if connection:
#         cursor.close()
#         connection.close()
from sql_python_lesson.user_repository import UserRepository

user_repository = UserRepository()

# print(user_repository.get_all())
print('\n')
# user_repository.delete_by_email('test_user@gmail.com')
# user_repository.insert_one('Pablo', 88, 'pablo@gmail.com')
print(user_repository.get_all())
# print(user_repository.get_all())
# print(user_repository.get_by_name(name='Homer'))
