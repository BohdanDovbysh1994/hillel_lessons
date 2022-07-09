from home_ex.arch.data_models.user_data import UserDataClass
from home_ex.arch.models.users_model import Users
from home_ex.arch.session import session


class UsersRepository:
    def __init__(self):
        self.__session = session

    def get_by_id(self):
        user = self.__session.get(Users, {'id': 1})
        print(user)
        return user

    def get_all(self):
        all_users = self.__session.query(Users).all()
        for users in all_users:
            print(f"\n{users}")

    def insert_one(self, user: UserDataClass):
        self.__session.add(user)
        self.__session.commit()

    def get_one_by_email(self):
        all_users = self.__session.query(Users).filter_by(email='test_email').first()
        print(all_users)
        return all_users
