from patterns_live_examples.abstract_factory.transpot_factory import TransportFactory
from patterns_live_examples.factory_method.Bus import Bus


class BusFactory(TransportFactory):
    __transport_type = 'Bus'

    def __init__(self):
        self.name = 'Electron'
        self.buses_model = ['900', '1000', '1500']

    @property
    def model(self):
        return self.buses_model

    def get_transport(self):
        return self.name

    def create_bus_900_model(self):
        return Bus(self.name, self.buses_model[0])
