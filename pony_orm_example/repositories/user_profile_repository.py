from pony.orm import db_session

from models.base_model import User


class UserProfileRepository:

    def __init__(self):
        self.__model = User

    @db_session
    def get_user_with_profile(self):
        users = self.__model.select()[:]
        for user in users:
            user_temp = user
            print(user.to_dict())

        return users


if __name__ == '__main__':
    users = UserProfileRepository().get_user_with_profile()

