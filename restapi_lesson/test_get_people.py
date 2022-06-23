import json
from http import HTTPStatus

from requests import get

from restapi_lesson.config import config
from restapi_lesson.people_api import PeopleApi
from restapi_lesson.person_data_class import Person


def get_people(person_id):
    return get(f"{config['base_url']}/api/people/{person_id}")


def test_get_people_response():
    response = get(f"{config['base_url']}/api/people/1")
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_not_found_error():
    response = get(f"{config['base_url']}/api/peoplehfsdhsdfkj/1")
    assert response.status_code == HTTPStatus.NOT_FOUND, f'\nStatus code is not as expected' \
                                                         f'\nActual: {response.status_code}' \
                                                         f'\nExpected: {HTTPStatus.NOT_FOUND}'


def test_response_json(create_person):
    response = PeopleApi().get_people(people_id=1)
    json_person = json.loads(response.text)
    expected_person = create_person
    actual_person = Person(json_person['name'], json_person['height'], json_person['mass'], json_person['hair_color'])
    assert actual_person == expected_person, f"\nPerson is not as expected"
