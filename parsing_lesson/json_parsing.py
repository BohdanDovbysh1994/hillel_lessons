import json
import requests

get_requst = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=pending')
json_object = json.loads()


#
# # request_json = get_requst.json()
#
#
# json_string = '{"id": true, "name": null}'
#
# from_json = json.loads(json_string)
#
# example = {'id': 146564, 'status': True, 'is_dead': False, 'children': None}
#
# to_json = json.dumps(example)
# c = 0

class DataOrder:
    def __init__(self, **kwargs):
        self.id = 12344
        self.status = True
        self.is_dead = False
        self.children = None

    def get_dict(self):
        return self.__dict__

    def update_dict(self, **kwargs):
        self.__dict__.update(**kwargs)


our_class_one = DataOrder().get_dict()

to_json = json.dumps(our_class_one)
c = 0
