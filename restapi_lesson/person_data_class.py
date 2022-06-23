class Person:
    def __init__(self, name, height, mass, hair_color):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color

    def __eq__(self, other):
        object_1 = self.__dict__
        object_2 = other.__dict__
        return self.__dict__ == other.__dict__
