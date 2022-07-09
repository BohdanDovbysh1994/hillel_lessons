from sql_python_lesson.sql_alchemy.models.user import User
from sql_python_lesson.sql_alchemy.user_repository.user_repository import UserRepository

user_repo = UserRepository()

# print(user_repo.get_by_id(3))

# user_repo.get_all()

# user_repo.insert_one(User(name='Newrrrr_user_arc', age=45, email='arrrrc@gmail.com'))
# user_repo.get_all()
# user_repo.delete_by_email(User(email='arc@gmail.com'), 'arc@gmail.com')

# user = user_repo.get_by_id(12)
# user_repo.delete_user(user)

print(user_repo.get_by_name('Homer'))

user_repo.delete_by_id(3)
