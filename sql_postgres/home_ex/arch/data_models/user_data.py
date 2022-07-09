class UserDataClass:
    def __init__(self, id: int = None, name: str = None, age: int = None, email: str = None):
        self.id = id
        self.name = name
        self.age = age
        self.email = email

    @staticmethod
    def convert_from_archenemy_to_data_class(arch_obj):
        return UserDataClass(id=arch_obj.id, name=arch_obj.name, age=arch_obj.age, email=arch_obj.email)
