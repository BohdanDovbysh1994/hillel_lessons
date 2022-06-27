from patterns_live_examples.abstract_factory.transpot_factory import TransportFactory


class CarFactory(TransportFactory):
    __transport_type = 'Car'

    def __init__(self):
        self.name = 'Mersedes'
        self.cars_model = ['S300', 'S500', 'S700']

    @property
    def model(self):
        return self.cars_model

    def get_transport(self):
        return self.name
