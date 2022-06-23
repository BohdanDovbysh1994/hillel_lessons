from restapi_lesson.base_api import BaseAPI


class PlanetAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.people_url = "/api/planets/"

    def get_people(self, planet_id):
        print('GET PLANET')
        return self.get(url=f"{self.people_url}{planet_id}")

    def post_planet(self, planet_body):
        pass
