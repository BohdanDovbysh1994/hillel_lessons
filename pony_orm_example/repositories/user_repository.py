from pony.orm import db_session, select, desc, commit, delete, left_join

from models.base_model import User, Profile


class UserRepository:

    def __init__(self):
        self.__model = User

    # DON'T do this never!!!
    # @db_session
    # def get_user_with_age_greater_than(self, age: int):
    #     users = self.__model.select_by_sql(f'select * from users where users.age > {age};')
    #     for user in users:
    #         print(user.to_dict())
    #     return users

    # @db_session
    # def get_user_with_age_greater_than(self, age: int):
    #     users = select(user for user in User if user.age > age)
    #     for user in users:
    #         print(user.to_dict())

    @db_session
    def get_user_with_age_greater_than(self, age: int):
        users = self.__model.select(lambda user: user.age > age)
        for user in users:
            print(user.to_dict())

    @db_session
    def add_user(self, name, age, email):
        self.__model(name=name, age=age, email=email)

    @db_session
    def get_user_by_name(self, name):
        user = self.__model.get(name=name)
        print(user.name)
        print(user.email)
        # print(user.to_dict())

    @db_session
    def select_user_by_name(self, name):
        users = self.__model.select(lambda user: user.name != name).order_by(desc(self.__model.name))
        for user in users:
            print(user.to_dict())

    # @db_session
    # def select_by_age_grater_than(self, age):
    #     users = self.__model.select(lambda user: user.age > age).limit(2)
    #     for user in users:
    #         print(user.to_dict())

    # @db_session
    # def update_user_by_name(self, name):
    #     user = self.__model.get(name=name)
    #     user.age += 1
    #     user.email = 'new_email@gmail.com'
    #     # commit()

    @db_session
    def delete_user(self, name):
        user = self.__model.get(name=name).delete()
        # delete(user)
        print('DELETED')

    @db_session
    def delete_user_by_name(self, name):
        delete(user for user in self.__model if user.name == name)

    @db_session
    def delete_user_by_name_lambda(self, name):
        delete(user for user in self.__model if user.name == name)

    @db_session
    def left_join(self):
        users = left_join((user, profile) for user in self.__model for profile in user.profiles)[:]
        for user in users:
            print('****************')
            print(user)
            print('****************')


if __name__ == '__main__':
    # UserRepository().get_user_with_age_greater_than(47)

    repo = UserRepository()
    # repo.add_user('Liza', 10, 'liza@gmail.com')
    # repo.add_user('Homer', 75, 'homer@gmail.com')
    # repo.add_user('Peter', 94, 'peter@gmail.com')
    # repo.get_user_by_name('Liza')
    print('*******************************************************')
    # repo.select_by_age_grater_than(28)
    # repo.select_user_by_name('Bla')
    # repo.update_user_by_name('Homer')
    # repo.delete_user('Liza')
    # repo.delete_user_by_name('Liza')
    repo.left_join()
