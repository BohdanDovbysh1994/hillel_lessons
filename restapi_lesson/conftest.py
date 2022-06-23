import pytest

from restapi_lesson.person_data_class import Person


@pytest.fixture
def create_person():
    return Person("Luke Skywalker", "172", "77", "blond")
