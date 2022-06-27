from abc import ABC, abstractmethod


class TransportFactory(ABC):
    __transport_type = None

    @abstractmethod
    def get_transport(self):
        pass
