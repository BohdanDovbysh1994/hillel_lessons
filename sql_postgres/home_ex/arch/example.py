from home_ex.arch.repositories.users_repository import UsersRepository

# users_repository = UsersRepository().get_by_id()
# #
# # users_repository_2 = UsersRepository().get_all()
#
# # user_data = UserDataClass.convert_from_archenemy_to_data_class(users_repository)
# # c = 0
#
# new_user = UsersRepository().insert_one(Users(name='TEST', age=25, email='test@test.com'))
# users_repository_2 = UsersRepository().get_all()
print('_________________________________')
users_repository_4 = UsersRepository().get_one_by_email()


