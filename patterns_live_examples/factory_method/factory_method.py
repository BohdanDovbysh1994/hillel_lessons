from patterns_live_examples.factory_method.Car import Car
from patterns_live_examples.factory_method.Bus import Bus


def create_transport(transport_type):
    if transport_type == 'Car':
        print('Create car')
        return Car('BMV', '100')
    elif transport_type == 'Bus':
        print('Create Bus')
        return Bus('Electron', '700')


create_transport('Car')
create_transport('Bus')
