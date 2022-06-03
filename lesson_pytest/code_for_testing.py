class Human:
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name
        self.__age = age
        self._gender = gender

    @property
    def age(self) -> int:
        return self.__age

    def grow(self):
        self.__age += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name[0].isupper():
            raise SyntaxError('Name should starts with capital letter')
        self.__name = new_name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        if new_gender not in ['male', 'female']:
            raise Exception('Gender is not as expected')
        self._gender = new_gender
