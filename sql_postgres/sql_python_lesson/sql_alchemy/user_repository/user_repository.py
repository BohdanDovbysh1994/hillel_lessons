from sql_python_lesson.sql_alchemy.session import session
from sql_python_lesson.sql_alchemy.models.user import User
from sqlalchemy import select, delete


class UserRepository:
    def __init__(self):
        self.__session = session

    def get_by_id(self, id_value: int):
        user = self.__session.get(User, {'id': id_value})
        return user

    def get_all(self):
        all_users = self.__session.query(User).all()
        for user in all_users:
            print(f'\n{user}')
        return all_users

    def insert_one(self, user: User):
        self.__session.add(user)
        self.__session.commit()

    # def delete_one_by_email(self, user: User):
    #     self.__session.delete(user)
    #     self.__session.commit()
    #
    # def delete_by_email(self, user, email):
    #     addresses = session.query(user).filter(user.email == email)
    #     addresses.delete(synchronize_session=False)

    def delete_user(self, user: User):
        self.__session.delete(user)
        self.__session.commit()

    def get_by_name(self, name):
        stmt = select(User).where(User.name == f"{name}")
        user = self.__session.scalars(stmt).one()
        return user

    def delete_by_id(self, user_id):
        stmt = delete(User).where(User.id == int(f'{user_id}'))
        print(stmt)
        self.__session.execute(stmt)
        self.__session.commit()
