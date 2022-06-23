from restapi_lesson.base_api import BaseAPI


class PeopleApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.people_url = "/api/people/"

    def get_people(self, people_id, headers=None):
        print('GET PEOPLE')
        return self.get(url=f"{self.people_url}{people_id}", headers=headers)
