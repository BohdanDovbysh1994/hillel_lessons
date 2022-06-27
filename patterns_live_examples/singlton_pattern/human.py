from patterns_live_examples.singlton_pattern.singlton_decorator import singleton


# @singleton
from patterns_live_examples.singlton_pattern.singlton_meta import SingletonMeta


class Human(metaclass=SingletonMeta):

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


if __name__ == '__main__':
    h_1 = Human('Peter', 20, 'labour')
    h_2 = Human('Victor', 45, 'driver')
    c = 0
