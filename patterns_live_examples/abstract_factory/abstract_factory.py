from patterns_live_examples.abstract_factory.bus_factory import BusFactory
from patterns_live_examples.abstract_factory.car_factory import CarFactory


class AbstractFactory:
    @staticmethod
    def get_factory(transport_type):
        if transport_type == 'Car':
            return CarFactory()
        elif transport_type == 'Bus':
            return BusFactory()


if __name__ == '__main__':
    factory_car = AbstractFactory.get_factory('Car')
    factory_bus = AbstractFactory.get_factory('Bus').create_bus_900_model()
    # print(factory_car.get_transport())
    # print(factory_bus.get_transport())
    c = 0
